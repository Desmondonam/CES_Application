import pandas as pd
import numpy as np

def analyze_ces_data(df):
    # Calculate overall metrics
    total_responses = len(df)
    average_ces = df['ces_score'].mean()
    
    # Categorize CES Levels
    def categorize_ces(score):
        if score <= 2:
            return 'Very Difficult'
        elif score <= 4:
            return 'Difficult'
        elif score <= 6:
            return 'Easy'
        else:
            return 'Very Easy'
    
    df['ces_category'] = df['ces_score'].apply(categorize_ces)
    
    # Count of each category
    category_counts = df['ces_category'].value_counts()
    
    # Percentage of each category
    category_percentages = df['ces_category'].value_counts(normalize=True) * 100
    
    # Prepare analysis results
    analysis_results = {
        'total_responses': total_responses,
        'average_ces_score': round(average_ces, 2),
        'category_counts': category_counts.to_dict(),
        'category_percentages': category_percentages.to_dict()
    }
    
    return analysis_results