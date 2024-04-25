import streamlit as st  # all streamlit commands will be available through the "st" alias
import ai_lib as glib  # reference to local lib script
import pandas as pd
import os
st.set_page_config(page_title="PersonalAIze",layout="wide")  # HTML title
st.title("PersonalAIze")  # page title

# CSV file path containing recommendations (ensure it's available to the Streamlit app)
csv_file_path = "keyframe/keyframe-data-title.csv"

# Read the CSV file and filter by the key from the response
data = pd.read_csv(csv_file_path)

# List of videos with their IDs (used to fetch recommendations)
videos = {
    "Red Bull Street StyleRed Bull Street Style": "media/AA-1MUWP5NGW1W14.mp4",  # Example video ID
    "Driving in Azerbaijan": "media/AA-1VDAA8NQ52112.mp4",
    "Speed & Style – Innsbruck": "media/AA-22HJPNQA12111.mp4",
    "The history of Red Bull Joyride": "media/AACM41S06EU5RAC4TMBN.mp4",
    "Red Bull Flugtag": "media/AANP5Z48DW877UFS7PRH.mp4",
}


# Initialize session state for tracking the selected video
if "selected_video" not in st.session_state:
    st.session_state.selected_video = None

# Use buttons to simulate video selection
left_column, right_column = st.columns([1, 3])
recommendations = []

#recommendations_dict = {
#   'AA-22HJPNQA12111': ['AA-22HJFS1FW1W12', 'AA-259E2TGH51W12', 'AA-27V65SV712111', 'AAFYYXG11B3VIB2GY2BY', 'AA3R6V8BIWRPZT2SSS8Z', 'AAZV1YD46TM2J76A5ZZJ', 'AAUTITP9JXCC4721XMLC'],
#   'AA-1VDAA8NQ52112': ['AA-1AATHIU9M2YZSFUIA387W', 'AA-1VDAA8NQ52112', 'AA-24FPAWS752112', 'AAZJ28EMJQTI1XPF51X5', 'AAQMCGLP8HSTC1VV0J80'],
#   'AACM41S06EU5RAC4TMBN': ['AA-1VDAA8NQ52112', 'AA3BI5PLBXG67HJY1TLI', 'AAYJ3ZX1VXAXHHCID3XP', 'AA-1MXPYCQH91W14', 'AA-1MASUJGHN2114'],
#    'AA-1MUWP5NGW1W14': ['AA-28DX6D73S2111', 'AA-1XC2S8SJW1W12', 'AA-1K4897J3H1W14', 'AA4YWAI7WT747CTM4F14', 'AAGJQ8B73R0NQQH4JHBW'],
#   'AANP5Z48DW877UFS7PRH': ['AA-1M5DFZAD92114', 'AA-1UDSERNK11W12', 'AA8CTIJN9J7JNW83HWJ7', 'AA-1U6CQPDAD1W12', 'AASFGDKFPQMYLVDB6NPP']
#}

with left_column:
    # Add a button for each video
    for video_name, video_id in videos.items():
        if st.button(f"Play {video_name}"):
            recommendations = []
            st.session_state.selected_video = video_id

# Fetch recommendations based on the selected video
if st.session_state.selected_video:

    # Assuming the key is in the response and it matches a column in the CSV

    with right_column:
        st.header("Video")
        st.video(st.session_state.selected_video,start_time=70)

        # Display the recommendations in a horizontal scrollable list
        st.header("Recommendations")
        print('Getting ' + st.session_state.selected_video)
        videoId = st.session_state.selected_video.replace("media/","").replace(".mp4","")
        # Make an API call to fetch recommendations for the selected video
        recommendations = glib.get_suggestions(videoId)# recommendations_dict.get(videoId) #
        print(recommendations)
        filtered_recommendations = data[data["id"].isin(recommendations)]
        # Horizontal scroll with Streamlit: Create multiple columns and adjust the layout
        cols = st.columns(len(filtered_recommendations))  # Create a column for each recommendation
        for idx, rec in enumerate(filtered_recommendations.itertuples()):
            # Each column displays an image and a title
            with cols[idx]:
                st.image(rec.keyFrame, use_column_width=True)  # Display the image
                st.write(rec.title)  # Display the title
