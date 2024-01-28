
# 🌍 NILA CarbonHero - Your Personal Carbon Footprint Calculator 

## Module Overview

NILA CarbonHero is a module designed to assess and visualize individual carbon footprints, focusing on daily commute, electricity usage, waste generation, and meals.

### 📹  Demo Video

## Carbon Foot Print Calculator


### 📊 User Input

- Select your state in India.
- Provide daily commute distance, monthly electricity usage, weekly waste generation, and meals per day.

### 🔄 Normalization

Inputs are normalized to yearly values for consistent calculations.

### 🌱 Carbon Emission Calculation

Emission factors for transportation, electricity, diet, and waste are defined by state. Yearly carbon emissions are then calculated based on normalized inputs and state-specific factors.

### 📈 Display Results

View calculated carbon emissions categorized by transportation, electricity, diet, and waste.

### 🌿 Environmental Impact Assessment

- Compare your total carbon footprint to a threshold (3.5 tons CO2 per year).
- Receive personalized recommendations for eco-friendly actions.
- Earn redeemable points based on your eco-friendly choices.

### 🤝 User Interaction

- Receive prompts for actions if your carbon footprint exceeds the threshold.
- Accumulate points for making eco-friendly decisions.
- Track your points in the user's wallet.

### 📸 App Screenshots

![WhatsApp Image 2024-01-28 at 14 48 04_acf0bd52](https://github.com/adithya-vedhamani/NILA-CarbonHero-Your-Personal-Carbon-Footprint-Calculator/assets/73640313/17e9beb8-a3b6-4962-9cd2-d3ddfad4c7b3)
![WhatsApp Image 2024-01-28 at 14 48 04_5c092486](https://github.com/adithya-vedhamani/NILA-CarbonHero-Your-Personal-Carbon-Footprint-Calculator/assets/73640313/b6155674-582d-48d4-b2b4-d8f65c6a1fca)

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



