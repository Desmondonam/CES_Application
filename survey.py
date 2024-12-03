import streamlit as st
import pandas as pd
import os

def create_ces_survey():
    st.header("Customer Effort Score (CES) Survey")
    
    # Collect customer information
    customer_name = st.text_input("Customer Name")
    customer_email = st.text_input("Customer Email")
    
    # CES Survey Question
    st.write("How easy was it to resolve your issue today?")
    ces_score = st.slider("Customer Effort Score", 
                          min_value=1, 
                          max_value=7, 
                          value=4,
                          help="1 = Very Difficult, 7 = Very Easy")
    
    # Additional feedback
    additional_feedback = st.text_area("Additional Comments (Optional)")
    
    # Submit button
    if st.button("Submit Survey"):
        # Validate inputs
        if customer_name and customer_email:
            # Prepare survey response
            survey_data = {
                'customer_name': [customer_name],
                'customer_email': [customer_email],
                'ces_score': [ces_score],
                'additional_feedback': [additional_feedback]
            }
            
            # Convert to DataFrame
            df = pd.DataFrame(survey_data)
            
            # Ensure data directory exists
            os.makedirs('data', exist_ok=True)
            
            # Append to CSV or create new
            file_path = 'data/ces_responses.csv'
            if os.path.exists(file_path):
                df.to_csv(file_path, mode='a', header=False, index=False)
            else:
                df.to_csv(file_path, index=False)
            
            st.success("Survey submitted successfully!")
        else:
            st.error("Please fill in customer name and email.")
