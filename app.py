import streamlit as st
import requests
import pandas as pd

# Function to fetch data from the Open Notify API
def get_astronaut_data():
    response = requests.get('http://api.open-notify.org/astros.json')
    if response.status_code == 200:
        return response.json()
    else:
        return None

# Function to get the current location of the ISS
def get_iss_location():
    response = requests.get('http://api.open-notify.org/iss-now.json')
    if response.status_code == 200:
        data = response.json()
        latitude = float(data['iss_position']['latitude'])
        longitude = float(data['iss_position']['longitude'])
        
        # Create a DataFrame with latitude and longitude columns
        df = pd.DataFrame({'LATITUDE': [latitude], 'LONGITUDE': [longitude]})
        
        return df
    else:
        return None

# Function to display the Streamlit app
def main():
    # Set page title and description
    st.title("Current Astronauts and ISS Location")
    st.markdown("This app displays the total number of people in space and their names, along with the current location of the International Space Station (ISS).")
    
    # Fetch astronaut data
    astronaut_data = get_astronaut_data()
    
    # Check if data is available
    if astronaut_data:
        total_people = astronaut_data['number']
        st.write(f"Total number of people in space: {total_people}")
        
        # Display names of astronauts
        if total_people > 0:
            astronauts = astronaut_data['people']
            st.write("Names of people in space:")
            for astronaut in astronauts:
                st.write(f"- {astronaut['name']}")
    else:
        st.error("Failed to retrieve astronaut data.")
    
    # Fetch ISS location
    iss_location = get_iss_location()
    if iss_location is not None and not iss_location.empty:
        st.write("Current ISS Location:")
        st.map(iss_location)  # Display ISS location on the map
    else:
        st.error("Failed to retrieve ISS location.")

if __name__ == "__main__":
    main()