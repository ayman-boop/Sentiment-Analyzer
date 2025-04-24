from transformers import pipeline

# Initialize sentiment analysis pipeline with device detection
def initialize_sentiment_analyzer():
    sentiment_analyzer = pipeline("sentiment-analysis")
    return sentiment_analyzer

# Function to get emoji based on sentiment label
def get_emoji(label):
    if "POSITIVE" in label:
        return "😄"
    elif "NEGATIVE" in label:
        return "😠"
    elif "NEUTRAL" in label:
        return "😐"
    else:
        return "🤔" 