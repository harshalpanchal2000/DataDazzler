import streamlit as st
import pandas as pd
from pandas_profiling import ProfileReport
import sweetviz as sv

def preprocess_data(data):
    st.title("Preprocessing")

    if data is not None:
        st.write("### Original Dataset")
        st.write(data.head())

        # Generate EDA report using pandas-profiling
        profile = ProfileReport(data, explorative=True)
        st.write("### EDA Report")
        st_profile_report(profile)

        # Generate visualization using sweetviz
        st.write("### Automated Visualization")
        sweet_report = sv.analyze(data)
        sweet_report.show_html()

# Function to display pandas-profiling report
def st_profile_report(profile):
    """Display pandas profiling report in Streamlit."""
    # To prevent the warning: "it=20 is too large for the screen, setting to 10"
    profile.set_variable("html.minify_html", False)

    # Convert the pandas profiling report to an HTML file
    profile_html = profile.to_html()

    # Display the HTML file using st.markdown
    st.markdown(profile_html, unsafe_allow_html=True)
