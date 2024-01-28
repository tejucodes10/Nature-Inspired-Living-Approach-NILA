import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title='NILA User Dashboard', page_icon=':bar_chart:')

st.title('Nature Inspired Living Approach(NILA)')
st.title('USER DASHBOARD')
# Load the air quality dataset
df = pd.read_csv(r'D:\Streamlit_Projects\India_Air_Quality\air_quality_data.csv')

# Remove rows with missing values in the date column
df = df.dropna(subset=['Date'])

# Convert the date column to a datetime object
df['Date'] = pd.to_datetime(df['Date'], format='%Y-%m-%d')


# Create a selectbox widget to allow the user to select the city
cities = df['City'].unique()
selected_city = st.selectbox('Select city', cities)

# Filter the data to only include rows for the selected city
df = df[df['City'] == selected_city]


pollutants = st.multiselect('Select pollutants', ['PM2.5','PM10','NO','NO2','NOx','NH3','CO','SO2','O3','Benzene','Toluene','Xylene'])

# Create a scatter plot to display the selected pollutants over time for each city
if pollutants:
    chart_data = df.melt(id_vars=['Date', 'City'], value_vars=pollutants, var_name='pollutant', value_name='level')
    fig = px.scatter(chart_data, x='Date', y='level', color='pollutant')
    
    # Update the title of each subplot
    fig.update_layout({'xaxis1': {'title': {'text': f'Air Quality of {selected_city}'}}})
    
    st.plotly_chart(fig, width=800, height=600)
    
else:
    st.warning('Please select at least one pollutant.')




# Create a DataFrame with the acceptable levels of various air pollutants
data = {'Pollutant': ['PM2.5','PM10','NO','NO2','NOx','NH3','CO','SO2','O3','Benzene','Toluene','Xylene'],
        'Acceptable Level': [12, 50, 53, 100, 100, 100, 9, 75, 70, 5, 7.5, 150]}
acceptable_levels = pd.DataFrame(data)

# Set the index of the acceptable_levels DataFrame to the 'Pollutant' column
acceptable_levels = acceptable_levels.set_index('Pollutant')

# Define a CSS style for centering text in a column
css_style = """
<style>
    td:nth-child(2) {
        text-align: center;
    }
</style>
"""
# Display the acceptable levels as a table without row numbers
st.markdown(f'## Level of Air Pollutants in {selected_city}')

# Group the data by city and year
grouped = df.groupby([df['City'], df['Date'].dt.year])

# Calculate the mean of each pollutant column
annual_averages = grouped[['PM2.5','PM10','NO','NO2','NOx','NH3','CO','SO2','O3','Benzene','Toluene','Xylene']].mean().round(1)

# Reset the index to move the group labels into columns
annual_averages = annual_averages.reset_index()

# Rename the 'Date' column to 'Year'
annual_averages = annual_averages.rename(columns={'Date': 'Year'})

# Melt the annual_averages DataFrame to create a long format table
long_table = annual_averages.melt(id_vars=['City', 'Year'], var_name='Pollutant', value_name='Value')

# Filter the data to only include rows for the selected city
long_table = long_table[long_table['City'] == selected_city]

# Pivot the long_table DataFrame to create a wide format table with columns for each year
pollutant_table = long_table.pivot_table(index='Pollutant', columns='Year', values='Value')

# Reindex the pollutant_table DataFrame to match the order of pollutants in the acceptable_levels DataFrame
pollutant_table = pollutant_table.reindex(acceptable_levels.index)
# Add a column for the acceptable levels
pollutant_table.insert(0, 'Acceptable Level', acceptable_levels['Acceptable Level'])

# Convert the DataFrame to an HTML table
html_table2 = pollutant_table.to_html(formatters={'Acceptable Level': '{:,.0f}'.format})
st.markdown(css_style + html_table2, unsafe_allow_html=True)


st.header("What should I do to improve the situation?")

choice = st.radio("Choose an option:", ["Commute by metro (10 points)", "Car pool (7 points)"])
wallet_points=0
if "Commute by metro" in choice:
    wallet_points += 10
elif "Car pool" in choice:
    wallet_points += 7
    
st.header("WALLET")
st.success(f"Collected Scores: {wallet_points} points")

st.markdown("## Emergency Helpline Numbers")
st.text("National Emergency Number: 112")
st.text("Central Pollution Control Board: +91-11-43102030")
st.text("Relief Commissioner: 1070")
st.text("Disaster Management Services: 108")

# Add "Report an Environmental Issue" section
st.markdown("## Report an Environmental Issue to Authorities via Mail")

# Streamlit API for sending an email
user_email = st.text_input("Your Email:")
issue_description = st.text_area("Describe the environmental issue:")
submit_button = st.button("Submit")

if submit_button:
    # You can use Streamlit's `st.write` to display a confirmation message or integrate with a mail-sending library.
    st.success(f"Thank you for reporting the issue. We will look into it and get back to you at {user_email}.")



    
