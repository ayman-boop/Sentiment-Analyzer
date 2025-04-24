import os
import pandas as pd
from datetime import datetime

# Define log file path
LOG_FILE = "src/data/vibe_log.csv"

# Function to initialize log file
def initialize_log_file():
    if not os.path.exists(LOG_FILE):
        # Create directory if it doesn't exist
        os.makedirs(os.path.dirname(LOG_FILE), exist_ok=True)
        # Create initial CSV with headers
        pd.DataFrame(columns=["timestamp", "input_text", "label", "score"]).to_csv(LOG_FILE, index=False)

# Function to log sentiment analysis result
def log_sentiment(text, label, score):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    new_entry = pd.DataFrame({
        "timestamp": [timestamp],
        "input_text": [text],
        "label": [label],
        "score": [score]
    })
    new_entry.to_csv(LOG_FILE, mode='a', header=False, index=False)
    return timestamp

# Function to get sentiment history
def get_vibe_history():
    if os.path.exists(LOG_FILE):
        df = pd.read_csv(LOG_FILE)
        if len(df) > 0:
            # Get the latest 10 entries in reverse order (newest first)
            latest = df.tail(10).iloc[::-1]
            return latest
    return pd.DataFrame(columns=["timestamp", "input_text", "label", "score"])

# Function to format history for display
def format_history(history_df):
    from src.models.sentiment_model import get_emoji
    
    if len(history_df) == 0:
        return "No history yet."
        
    history_text = ""
    for i, row in history_df.iterrows():
        emoji = get_emoji(row["label"])
        history_text += f"{row['timestamp']}: \"{row['input_text'][:50]}{'...' if len(row['input_text']) > 50 else ''}\" - {row['label']} {emoji} ({row['score']*100:.1f}%)\n"
    return history_text 