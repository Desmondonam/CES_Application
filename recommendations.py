def get_recommendations(analysis_results):
    recommendations = []
    
    # Based on average CES score
    avg_score = analysis_results['average_ces_score']
    if avg_score < 3:
        recommendations.append("🚨 URGENT: Your customer experience needs significant improvement.")
        recommendations.append("Conduct in-depth interviews to understand pain points.")
        recommendations.append("Invest in customer support training and process optimization.")
    
    elif avg_score < 5:
        recommendations.append("⚠️ Moderate CES: There's room for improvement.")
        recommendations.append("Review customer journey and identify friction points.")
        recommendations.append("Implement customer feedback mechanisms.")
    
    else:
        recommendations.append("👍 Great CES: Continue maintaining your high standards.")
        recommendations.append("Regularly collect detailed feedback to maintain performance.")
    
    # Based on category percentages
    categories = analysis_results['category_percentages']
    
    if categories.get('Very Difficult', 0) > 20:
        recommendations.append("High percentage of 'Very Difficult' experiences detected.")
        recommendations.append("Immediate intervention required in customer support processes.")
    
    return recommendations