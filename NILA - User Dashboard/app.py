import streamlit as st

# Define emission factors (example values, replace with accurate data)
EMISSION_FACTORS = {
    "Andhra Pradesh": {
    "Transportation": 0.14,  # kgCO2/km
    "Electricity": 0.82,  # kgCO2/kWh
    "Diet": 1.25,  # kgCO2/meal, 2.5kgco2/kg
    "Waste": 0.1  # kgCO2/kg
},

"Arunachal Pradesh": {
    "Transportation": 0.14,
    "Electricity": 0.82,
    "Diet": 1.25,
    "Waste": 0.1
},

"Assam": {
    "Transportation": 0.14,
    "Electricity": 0.82,
    "Diet": 1.25,
    "Waste": 0.1
},

"Bihar": {
    "Transportation": 0.14,
    "Electricity": 0.82,
    "Diet": 1.25,
    "Waste": 0.1
},

"Chhattisgarh": {
    "Transportation": 0.14,
    "Electricity": 0.82,
    "Diet": 1.25,
    "Waste": 0.1
},

"Goa": {
    "Transportation": 0.14,
    "Electricity": 0.82,
    "Diet": 1.25,
    "Waste": 0.1
},

"Gujarat": {
    "Transportation": 0.14,
    "Electricity": 0.82,
    "Diet": 1.25,
    "Waste": 0.1
},

"Haryana": {
    "Transportation": 0.14,
    "Electricity": 0.82,
    "Diet": 1.25,
    "Waste": 0.1
},

"Himachal Pradesh": {
    "Transportation": 0.14,
    "Electricity": 0.82,
    "Diet": 1.25,
    "Waste": 0.1
},

"Jharkhand": {
    "Transportation": 0.14,
    "Electricity": 0.82,
    "Diet": 1.25,
    "Waste": 0.1
},
"Karnataka": {
    "Transportation": 0.14,
    "Electricity": 0.82,
    "Diet": 1.25,
    "Waste": 0.1
},
"Kerala": {
    "Transportation": 0.14,
    "Electricity": 0.82,
    "Diet": 1.25,
    "Waste": 0.1
},
"Madhya Pradesh": {
    "Transportation": 0.14,
    "Electricity": 0.82,
    "Diet": 1.25,
    "Waste": 0.1
},
"Maharashtra": {
    "Transportation": 0.14,
    "Electricity": 0.82,
    "Diet": 1.25,
    "Waste": 0.1
},
"Manipur": {
    "Transportation": 0.14,
    "Electricity": 0.82,
    "Diet": 1.25,
    "Waste": 0.1
},
"Meghalaya": {
    "Transportation": 0.14,
    "Electricity": 0.82,
    "Diet": 1.25,
    "Waste": 0.1
},
"Mizoram": {
    "Transportation": 0.14,
    "Electricity": 0.82,
    "Diet": 1.25,
    "Waste": 0.1
},
"Nagaland": {
    "Transportation": 0.14,
    "Electricity": 0.82,
    "Diet": 1.25,
    "Waste": 0.1
},
"Odisha": {
    "Transportation": 0.14,
    "Electricity": 0.82,
    "Diet": 1.25,
    "Waste": 0.1
},
"Punjab": {
        "Transportation": 0.14,
        "Electricity": 0.82,
        "Diet": 1.25,
        "Waste": 0.1
    },

    "Rajasthan": {
        "Transportation": 0.14,
        "Electricity": 0.82,
        "Diet": 1.25,
        "Waste": 0.1
    },

    "Sikkim": {
        "Transportation": 0.14,
        "Electricity": 0.82,
        "Diet": 1.25,
        "Waste": 0.1
    },

    "Tamil Nadu": {
        "Transportation": 0.14,
        "Electricity": 0.82,
        "Diet": 1.25,
        "Waste": 0.1
    },

    "Telangana": {
        "Transportation": 0.14,
        "Electricity": 0.82,
        "Diet": 1.25,
        "Waste": 0.1
    },

    "Tripura": {
        "Transportation": 0.14,
        "Electricity": 0.82,
        "Diet": 1.25,
        "Waste": 0.1
    },

    "Uttar Pradesh": {
        "Transportation": 0.14,
        "Electricity": 0.82,
        "Diet": 1.25,
        "Waste": 0.1
    },

    "Uttarakhand": {
        "Transportation": 0.14,
        "Electricity": 0.82,
        "Diet": 1.25,
        "Waste": 0.1
    },


"West Bengal": {
    "Transportation": 0.14,
    "Electricity": 0.82,
    "Diet": 1.25,
    "Waste": 0.1
}

}

# Set wide layout and page name
st.set_page_config(layout="wide", page_title="NILA CarbonHero")

# Streamlit app code
st.title("Nature Inspired Living Approach(NILA) CarbonHero")
st.title("Your personal carbon footprint calculator")


# User inputs
st.subheader("🌍 Select your state in India ")
state = st.selectbox("Select", ["Andhra Pradesh", "Arunachal Pradesh", "Assam", "Bihar", "Chhattisgarh", "Goa", "Gujarat", "Haryana", "Himachal Pradesh", "Jharkhand", "Karnataka", "Kerala", "Madhya Pradesh", "Maharashtra", "Manipur", "Meghalaya", "Mizoram", "Nagaland", "Odisha", "Punjab", "Rajasthan", "Sikkim", "Tamil Nadu", "Telangana", "Tripura", "Uttar Pradesh", "Uttarakhand", "West Bengal"])

col1, col2 = st.columns(2)

with col1:
    st.subheader("🚗 Daily commute distance (in km)")
    distance = st.slider("Distance", 0.0, 100.0, key="distance_input")

    st.subheader("💡 Monthly electricity consumption (in kWh)")
    electricity = st.slider("Electricity", 0.0, 1000.0, key="electricity_input")

with col2:
    st.subheader("🗑️ Waste generated per week (in kg)")
    waste = st.slider("Waste", 0.0, 100.0, key="waste_input")

    st.subheader("🍽️ Number of meals per day")
    meals = st.number_input("Meals", 0, key="meals_input")

# Normalize inputs
if distance > 0:
    distance = distance * 365  # Convert daily distance to yearly
if electricity > 0:
    electricity = electricity * 12  # Convert monthly electricity to yearly
if meals > 0:
    meals = meals * 365  # Convert daily meals to yearly
if waste > 0:
    waste = waste * 52  # Convert weekly waste to yearly

# Calculate carbon emissions
transportation_emissions = EMISSION_FACTORS[state]["Transportation"] * distance
electricity_emissions = EMISSION_FACTORS[state]["Electricity"] * electricity
diet_emissions = EMISSION_FACTORS[state]["Diet"] * meals
waste_emissions = EMISSION_FACTORS[state]["Waste"] * waste

# Convert emissions to tonnes and round off to 2 decimal points
transportation_emissions = round(transportation_emissions / 1000, 2)
electricity_emissions = round(electricity_emissions / 1000, 2)
diet_emissions = round(diet_emissions / 1000, 2)
waste_emissions = round(waste_emissions / 1000, 2)

# Calculate total emissions
total_emissions = round(
    transportation_emissions + electricity_emissions + diet_emissions + waste_emissions, 2
)
threshold_value=3.5
if st.button("Calculate CO2 Emissions - Your Carbon FootPrint"):

    # Display results
    st.header("Results")
    col3, col4 = st.columns(2)

    with col3:
        st.subheader("Carbon Emissions by Category")
        st.info(f"🚗 Transportation: {transportation_emissions} tonnes CO2 per year")
        st.info(f"💡 Electricity: {electricity_emissions} tonnes CO2 per year")
        st.info(f"🍽️ Diet: {diet_emissions} tonnes CO2 per year")
        st.info(f"🗑️ Waste: {waste_emissions} tonnes CO2 per year")

    with col4:
        st.subheader("Total Carbon Footprint for the year")
        st.success(f"🌍 Your total carbon footprint is: {total_emissions} tonnes CO2 per year.")
        st.info("Redeemable points to be awarded based on score")
        st.warning("In 2023, CO2 emissions per capita for India was 1.9 tons of CO2 per capita. The 8.2 per cent rise in India's annual CO2 emissions for 2023 would be more than double the expected increase in China, which is set to see a 4 per cent growth this year.")
        
    if total_emissions>threshold_value:
        st.error("Your carbon footprint is higher than the recommended score")
        choice = st.radio(
            "What will you do? ",
            ["Start using public transport or carpooling (30pt)", "Switch to renewable energy resources (20pt)"])
        st.success("Your points have been added to the wallet!")
        
    else :
        st.success("Your score is within the required threshold! Congratulations for the points credited to the wallet!")
        st.balloons()
