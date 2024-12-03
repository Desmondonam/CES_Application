import streamlit as st
import pandas as pd
import base64
from survey import create_ces_survey
from analysis import analyze_ces_data
from recommendations import get_recommendations

def main():
    st.title("Customer Effort Score (CES) Survey & Analysis")
    
    # Sidebar navigation
    page = st.sidebar.radio("Navigate", 
        ["Survey", "View Past Responses", "Analysis & Recommendations"])
    
    if page == "Survey":
        create_ces_survey()
    
    elif page == "View Past Responses":
        view_past_responses()
    
    elif page == "Analysis & Recommendations":
        analyze_and_recommend()

def view_past_responses():
    st.header("Past CES Survey Responses")
    
    try:
        df = pd.read_csv('data/ces_responses.csv')
        st.dataframe(df)
        
        # Download button for CSV
        csv = df.to_csv(index=False)
        b64 = base64.b64encode(csv.encode()).decode()
        href = f'<a href="data:file/csv;base64,{b64}" download="ces_responses.csv">Download CSV File</a>'
        st.markdown(href, unsafe_allow_html=True)
    
    except FileNotFoundError:
        st.warning("No survey responses found yet.")

def analyze_and_recommend():
    st.header("CES Analysis & Recommendations")
    
    try:
        df = pd.read_csv('data/ces_responses.csv')
        
        # Perform analysis
        analysis_results = analyze_ces_data(df)
        st.write("### Analysis Results")
        st.write(analysis_results)
        
        # Get recommendations
        recommendations = get_recommendations(analysis_results)
        st.write("### Business Recommendations")
        for rec in recommendations:
            st.markdown(f"- {rec}")
    
    except FileNotFoundError:
        st.warning("Please complete some surveys first.")

if __name__ == "__main__":
    main()