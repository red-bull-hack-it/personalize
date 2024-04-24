import streamlit as st  # all streamlit commands will be available through the "st" alias
import ai_lib as glib  # reference to local lib script
import pandas as pd

st.set_page_config(page_title="PersonalAIze",layout="wide")  # HTML title
st.title("PersonalAIze")  # page title

# List of videos with their IDs (used to fetch recommendations)
videos = {
    "Red Bull BC One": "media/MI202307190080.mp4",  # Example video ID
    "Red Bull Formula 1": "media/MI202307200593.mp4",
    "Red Bull MTB": "media/MI202309290139.mp4",
    "Red Bull Cliff Diving": "media/MI202402281377.mp4",
    "Video 5": "media/MI202403050957.mp4",
}
# CSV file path containing recommendations (ensure it's available to the Streamlit app)
csv_file_path = "keyframe/keyframe-data-title.csv"


# Initialize session state for tracking the selected video
if "selected_video" not in st.session_state:
    st.session_state.selected_video = None

# Use buttons to simulate video selection
left_column, right_column = st.columns([1, 3])

with left_column:
    # Add a button for each video
    for video_name, video_id in videos.items():
        if st.button(f"Play {video_name}"):
            st.session_state.selected_video = video_id

# Fetch recommendations based on the selected video
recommendations = ["MI202302151043","MI202210200705","MI202303061472","MI202210200706","MI202303061487","MI201911150039"]
#if st.session_state.selected_video:
    # Make an API call to fetch recommendations for the selected video
    # response = requests.get(f"{api_base_url}/{st.session_state.selected_video}/recommendations")

    #if response.status_code == 200:
    #    recommendations = response.json()  # Assuming the API returns a JSON response
    #else:
    #    st.warning("Failed to fetch recommendations.")

# If recommendations are found, read the CSV file to get details
if recommendations:
    # Read the CSV file and filter by the key from the response
    data = pd.read_csv(csv_file_path)
    # Assuming the key is in the response and it matches a column in the CSV
    filtered_recommendations = data[data["vin"].isin(recommendations)]

    with right_column:
        st.header("Video")
        st.video(st.session_state.selected_video)

        # Display the recommendations in a horizontal scrollable list
        st.header("Recommendations")

        # Horizontal scroll with Streamlit: Create multiple columns and adjust the layout
        cols = st.columns(len(filtered_recommendations))  # Create a column for each recommendation
        for idx, rec in enumerate(filtered_recommendations.itertuples()):
            # Each column displays an image and a title
            with cols[idx]:
                st.image(rec.keyFrame, use_column_width=True)  # Display the image
                st.write(rec.title)  # Display the title