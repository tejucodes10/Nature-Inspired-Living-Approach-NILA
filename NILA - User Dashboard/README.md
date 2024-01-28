# 🚗 User Dashboard for Environmental Enlightenment🧑

As part of our product NILA, focusing on enhanced public awareness and engagement, we created a module called a user dashboard.The application aims to provide users with visualizations of air quality data, information on acceptable pollutant levels, and suggestions and nudges for actions to improve air quality, along with the possible health hazards. It also includes features for reporting environmental issues.

## 📹 Demo - https://drive.google.com/file/d/1gXgfOz9VN2KF3xOLhM4bD282lwKwevFO/view?usp=sharing

![image](https://github.com/tejucodes10/Team-FinSAT-Pragyan-24-Hackathon-PS-3/assets/119094222/d4f61e4d-02bc-4a0e-8764-400ba8d21e8b)


### Multi-lingual options

## Features 🌟
1. We performed data loading, cleaning and preprocessing on the air quality dataset we received. 

2. 🎐Visualisation of Air Quality:
   - Users can select a city using a select box widget.
   - Users can choose pollutants (e.g., PM2.5, PM10, NO2) using a multiselect widget.
   - A scatter plot is generated to display the selected pollutants over time for the chosen city.
   - The plot is created using the Plotly Express library.

3. 🪟Displaying Acceptable Pollutant Levels:
   - A table is created with acceptable levels of various air pollutants.
   - The table includes both the acceptable levels and the actual levels for the selected city.
   - The data is grouped, averaged, and presented in a user-friendly HTML table format.

4. 👛User Engagement and Wallet Points:
   - Users are given options on how they can improve the air quality around them with various measures like metro rides, carpooling and so on
   - Based on the user's choice, "wallet green points" are awarded, as a method of incentivisation. 
- These points can be redeemed as a free metro ride and so on to further incentivise citizens to take up activities contributing to sustainability

5. ☎️Emergency Helpline Numbers:
   - Important emergency helpline numbers related to pollution and disaster management are provided (Particularly intended at cities like Delhi, with alarming AQI values)

6. Reporting Environmental Issues (crowd sourced):
   - Users can input their email and describe environmental issues.
   - A submit button allows users to report the issue, and a success message is displayed.


## Getting Started 🚀

# Running Streamlit App

This guide provides the steps to set up and run your Streamlit app.

## Quick Start

1. **Create `requirements.txt`:**
   - Create a file named `requirements.txt` in your project directory.
   - List required Python packages and versions.

     ```plaintext
     streamlit==1.10.0
     pandas==1.3.3
     matplotlib==3.4.3
     plotly
     # Add other dependencies as needed
     ```

2. **Install Dependencies:**
   - Run the following command in your terminal:

     ```bash
     pip install -r requirements.txt
     ```

3. **Run the Streamlit App:**
   - Execute the following command:

     ```bash
     python -m streamlit run app.py
     ```
  
   

## Note

- Ensure Python is installed.
- Use a virtual environment to avoid conflicts.

After executing these steps, your Streamlit app should launch in a new browser window. Check the terminal for any error messages and ensure all dependencies are installed correctly.

