import numpy as np
import pandas as pd
import streamlit as st
import pydeck as pdk
import googlemaps

gm = googlemaps.Client("YOUR_API_KEY")
break_points=[]

# Calculates total distance and duration of route
def calc_tots(route):
    total_dist=0
    total_time=0
    
    for i in route[0]["legs"][0]["steps"]:
        total_dist += int(i["distance"]["value"])
        total_time += int(i['duration']['value'])
        
    total_dist /= 1000
    total_time /= 60
    
    return total_dist,total_time

# Calculates break points in route
def calc_break_points(origin,destination,mileage,fuel_level,max_fuel,query,rating):
    
    route = gm.directions(origin=origin,destination=destination,mode="driving")
    
    total_dist,total_time = calc_tots(route)
    
    travellable_dist = mileage*fuel_level

    travellable_dist *= 1000
    
    cum_dist = 0
    prev_cum = 0
    
    fail = False
    
    count=0
    for i in route[0]["legs"][0]["steps"]:
        prev_cum = cum_dist
        cum_dist+=int(i['distance']['value'])
        if cum_dist>travellable_dist:
            break_coords = i["start_location"]
            backup_coords = route[0]["legs"][0]["steps"][count-1]['start_location']
            remaining_dist = travellable_dist-prev_cum
            fail = True
            break
        count+=1
        
    if not fail:
        return
    
    else:
        
        break_point = gm.reverse_geocode(gm.nearest_roads(break_coords)[0]['location'])[0]['formatted_address']
        # print(f"You need to refill at {break_point}")
        
        results = gm.places_nearby(location=break_coords,keyword=query,radius=remaining_dist-(0.5*remaining_dist))["results"]
        
        count=0
        results_ = []
        for i in results:
            if 'opening_hours' in i and 'open_now' in i['opening_hours']:
                opclose = 'Open' if i["opening_hours"]['open_now']==True else "Closed"
            else:
                opclose = "NA"
            results_+=[{'name':i["name"],'status':opclose,'rating':i["rating"],'coords':i['geometry']['location']}]
            # print(f'{count}\nName: {i["name"]}\nStatus: {opclose}\nRating: {i["rating"]}\n')
            count+=1
            
        dests = [i["coords"] for i in results_]
        
        matrix = gm.distance_matrix(origins=break_coords,destinations=dests,mode="driving")['rows'][0]['elements']
        
        for i in range(len(results)):
            results_[i]['distance'] = matrix[i]["distance"]['text']
            results_[i]['duration'] = matrix[i]["duration"]['text']     
            # print(f"Name: {results_[i]['name']}\nCoords: {results_[i]['coords']}\nDistance: {matrix[i]['distance']['text']}\nDuration: {matrix[i]['duration']['text']}\n")
        results_.sort(key = lambda x: float(x['distance'][:-2]))

        # results_ = [i for i in results_ if i['status']=='Open']

        if rating!=0:
            results_ = [i for i in results_ if i['rating']>rating]
        
        global break_points
        break_coords = [i["coords"] for i in break_points]
        
        while results_[0]['coords'] in break_coords:
            results_ =  results_[1:]
        
        break_points+=[results_[0]]
        
        if (calc_tots(gm.directions(results_[0]['coords'],destination,mode='driving'))[0]/mileage)>max_fuel:
            calc_break_points(results_[0]['coords'], destination, mileage, max_fuel, max_fuel,query,rating)
        else:
            return

# To plot coordinates
def plot_coord(l): 
    df = pd.DataFrame(
    l,columns=['lat', 'lon'])

    st.map(df)

# Plot using pydeck scatterplot 
def plot_coord_new(l):
    start = l[0]
    end = l[-1]
    avg_long = (start[1] + end[1]) / 2
    avg_lat = (start[0] + end[0]) / 2

    view_state = pdk.ViewState(
        longitude = avg_long,
        latitude = avg_lat,
        zoom = 5
    )

    ll = []
    for i in l:
        ll.append([i[1],i[0]])
    df = pd.DataFrame({"coord" : ll})
    df["rad"] = 50

    st.dataframe(df)

    layer = pdk.Layer(
    "ScatterplotLayer",
    df,
    pickable=True,
    opacity=1,
    stroked=True,
    filled=True,
    radius_scale=100,
    radius_min_pixels=1,
    radius_max_pixels=100,
    line_width_min_pixels=1,
    get_position = "coord",
    get_radius = "rad",
    get_fill_color=[255, 140, 0],
    get_line_color=[0, 0, 0],
    )

    r = pdk.Deck(layers=[layer], initial_view_state=view_state)
    st.pydeck_chart(r)

# Plotting Route using pydeck
def plot_route(ll):
    colour = (129,0,189)
    start = -1
    end = -1

    l = []
    col = []
    if(len(ll) != 1):
        for i in ll:
            k = []
            for j in i:
                k.append([j[1],j[0]])
            col.append(colour)
            l.append(k)
        start = l[0][0]
        end = l[-1][-1]
    else:
        for i in ll:
            l.append([i[1],i[0]])
        col.append(colour)
        start = l[0]
        end = l[-1]

    df = pd.DataFrame({"path":l,"color":col})

    avg_long = (start[0] + end[0]) / 2
    avg_lat = (start[1] + end[1]) / 2

    view_state = pdk.ViewState(
        longitude = avg_long,
        latitude = avg_lat,
        zoom = 5
    )

    layer = pdk.Layer(
        type='PathLayer',
        data=df,
        pickable=True,
        get_color='color',
        width_scale=5,
        width_min_pixels=2,
        get_path='path',
        get_width=5
    )

    r = pdk.Deck(layers=[layer], initial_view_state=view_state)

    st.pydeck_chart(r)

# Plotting both Route and Coordinates 
def two_in_one(coords,final,name,rating,status,origin,dest):
    name = [origin] + name + [dest]
    rating = ["NA"] + rating + ["NA"]
    status = ["NA"] + status + ["NA"]

    start = coords[0]
    end = coords[-1]
    avg_long = (start[1] + end[1]) / 2
    avg_lat = (start[0] + end[0]) / 2

    view_state = pdk.ViewState(
        longitude = avg_long,
        latitude = avg_lat,
        zoom = 5
    )

    #Route Map
    colour = (129,0,189)

    ll = final
    l = []
    col = []
    if(len(ll) != 1):
        for i in ll:
            k = []
            for j in i:
                k.append([j[1],j[0]])
            col.append(colour)
            l.append(k)
        start = l[0][0]
        end = l[-1][-1]
    else:
        for i in ll:
            l.append([i[1],i[0]])
        col.append(colour)
        start = l[0]
        end = l[-1]

    df = pd.DataFrame({"path":l,"color":col})

    route = pdk.Layer(
        type='PathLayer',
        data=df,
        pickable=True,
        get_color='color',
        width_scale=5,
        width_min_pixels=2,
        get_path='path',
        get_width=5
    )

    #Points
    ll = []
    for i in coords:
        ll.append([i[1],i[0]])
    df = pd.DataFrame({"coord" : ll,"name" : name})
    df["rad"] = 50

    points = pdk.Layer(
    "ScatterplotLayer",
    df,
    pickable=True,
    opacity=1,
    stroked=True,
    filled=True,
    radius_scale=150,
    radius_min_pixels=1,
    radius_max_pixels=100,
    line_width_min_pixels=1,
    get_position = "coord",
    get_radius = "rad",
    get_fill_color=[255, 61, 81],
    get_line_color=[0, 0, 0],
    )

    # name = np.array(name).reshape(-1,1)

    r = pdk.Deck(layers=[route,points], initial_view_state=view_state,tooltip={"text" : "{name}"})
    st.pydeck_chart(r)

def main():
    st.title("Fuel Planner")

    current_location = st.checkbox("Current Location")
    start_location = -1

    with st.form(key = 'form1'):
        
        if(current_location == False):
            start_location = st.text_input("Start Location")

        destination = st.text_input("Destination")

        vehicle_mileage = st.number_input("Vehicle Mileage [KMPL]",min_value=0.0)
        fuel_level = st.number_input("Current Fuel Level [Liters]",min_value=0.0)
        max_fuel = st.number_input("Fuel Capacity [Liters]",min_value=0.0)

        with st.expander("Filters"):
            col1,col2,col3,col4 = st.columns([1,1,1,1])
            with col1:
                indian_oil = st.checkbox("Indian Oil")
            with col2:
                bharat_petroleum = st.checkbox("Bharat Petroleum")
            with col3:
                shell = st.checkbox("Shell")
            with col4:
                hp = st.checkbox("HP")

            bunk_rating = st.slider(label="Ratings",min_value=0.0,max_value=5.0,step=0.5)


        sumbit_button = st.form_submit_button()
    
    #Results
    if sumbit_button:
        if(start_location and destination):
            if current_location:
                origin = gm.reverse_geocode(gm.geolocate()['location'])[0]["formatted_address"]
            else:
                origin = start_location

            query = "petrol bunk"

            brands = [indian_oil,bharat_petroleum,shell,hp]
            brand_names = ["indian oil ", "bharat petroleum ", "shell ", "hp "]

            for i in range(len(brands)):
                if brands[i]:
                    query = brand_names[i] + query

            calc_break_points(origin,destination,vehicle_mileage,fuel_level,max_fuel,query,bunk_rating)
            
            og = gm.geocode(origin)[0]['geometry']['location']

            og_coords = [og['lat'],og['lng']]

            dt = gm.geocode(destination)[0]['geometry']['location']
            
            dt_coords = [dt['lat'],dt['lng']]

            l = [[i["coords"]["lat"],i['coords']['lng']] for i in break_points]
            
            l = [og_coords] + l + [dt_coords]
            
            routes=[]
            for i in range(1,len(l)):
                routes+=[gm.directions(l[i-1],l[i],mode='driving')]
            routes = [i[0]['legs'][0]['steps'] for i in routes]
            for i in range(len(routes)):
                routes[i] = [j['start_location'] for j in routes[i]]
            for i in range(len(routes)):
                routes[i] = [[j['lat'],j['lng']] for j in routes[i]]
            for i in range(len(routes)):
                routes[i] = gm.snap_to_roads(routes[i])
            for i in range(len(routes)):
                routes[i] = [[j['location']['latitude'],j['location']['longitude']] for j in routes[i]]

            bunk_name = [i["name"] for i in break_points]
            rating = [i["rating"] for i in break_points]
            status = [i["status"] for i in break_points]
            st.write(break_points)
  
            with st.expander("Result"):
                #plot_coord_new(l)
                # plot_route(l)
                final=[]
                for i in routes:
                    # plot_route(i)
                    final+=[i]
                two_in_one(l,final,bunk_name,rating,status,origin,destination) 

if __name__ == "__main__":
    main()