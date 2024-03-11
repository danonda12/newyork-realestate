import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

# Simulated Data
def generate_data():
    np.random.seed(0)  # For reproducible results
    neighborhoods = ['Williamsburg', 'Long Island City', 'Jersey City', 'Upper East Side', 'Silicon Alley']
    data = pd.DataFrame({
        'Neighborhood': np.random.choice(neighborhoods, 100),
        'Average Rent': np.random.randint(2000, 5000, 100),
        'Amenities Score': np.random.randint(1, 10, 100),
        'Tech Proximity': np.random.choice(['High', 'Medium', 'Low'], 100),
        'Cultural Hotspots': np.random.choice(['High', 'Medium', 'Low'], 100),
    })
    return data

data = generate_data()

# Streamlit App
st.title('NYC Real Estate Explorer for Young Professionals')

# Neighborhood Selection
selected_neighborhood = st.selectbox('Select a Neighborhood', data['Neighborhood'].unique())

# Filter data based on selection
filtered_data = data[data['Neighborhood'] == selected_neighborhood]

# Display Data
st.write(f"Data for {selected_neighborhood}:")
st.dataframe(filtered_data)

# Average Rent Visualization
st.header("Average Rent in Selected Neighborhood")
fig = px.histogram(filtered_data, x='Average Rent', nbins=20, title=f"Average Rent Distribution in {selected_neighborhood}")
st.plotly_chart(fig)

# Amenities Score Visualization
st.header("Amenities Score")
amenities_fig = px.histogram(filtered_data, x='Amenities Score', nbins=10, title=f"Amenities Score Distribution in {selected_neighborhood}")
st.plotly_chart(amenities_fig)

# Additional Insights (Placeholder)
st.header("Additional Insights")
st.markdown("This section could include further analysis and insights such as comparison with other neighborhoods, detailed amenity descriptions, and recommendations based on user preferences.")

# Reminder
st.sidebar.markdown("**Note:** This app uses simulated data for demonstration purposes.")
