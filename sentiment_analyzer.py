import os
import pandas as pd
import gradio as gr
from transformers import pipeline
from datetime import datetime

# Initialize sentiment analysis pipeline
sentiment_analyzer = pipeline("sentiment-analysis")

# Check if log file exists, if not create one with headers
log_file = "vibe_log.csv"
if not os.path.exists(log_file):
    pd.DataFrame(columns=["timestamp", "input_text", "label", "score"]).to_csv(log_file, index=False)

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

# Read previous entries
def get_vibe_history():
    if os.path.exists(log_file):
        df = pd.read_csv(log_file)
        if len(df) > 0:
            # Get the latest 10 entries in reverse order (newest first)
            latest = df.tail(10).iloc[::-1]
            history = ""
            for i, row in latest.iterrows():
                emoji = get_emoji(row["label"])
                history += f"{row['timestamp']}: \"{row['input_text'][:50]}{'...' if len(row['input_text']) > 50 else ''}\" - {row['label']} {emoji} ({row['score']*100:.1f}%)\n"
            return history
    return "No history yet."

# Main function to analyze sentiment
def analyze_sentiment(text):
    if not text.strip():
        return "Please enter some text to analyze.", get_vibe_history()
    
    # Get sentiment analysis result
    result = sentiment_analyzer(text)[0]
    label = result["label"]
    score = result["score"]
    emoji = get_emoji(label)
    
    # Format result output
    output = f"{label} {emoji} (Confidence: {score*100:.1f}%)"
    
    # Log to CSV
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    new_entry = pd.DataFrame({
        "timestamp": [timestamp],
        "input_text": [text],
        "label": [label],
        "score": [score]
    })
    new_entry.to_csv(log_file, mode='a', header=False, index=False)
    
    # Get updated history
    history = get_vibe_history()
    
    return output, history

# Create Gradio interface with Blocks
with gr.Blocks(theme=gr.themes.Soft()) as app:
    gr.Markdown("# 🧠 Sentiment Analyzer")
    
    with gr.Row():
        with gr.Column():
            text_input = gr.Textbox(
                label="Enter text to analyze", 
                placeholder="Type something to analyze the sentiment...",
                lines=5
            )
            analyze_button = gr.Button("Analyze 🔍")
        
        with gr.Column():
            result_output = gr.Textbox(label="Sentiment Result")
            history_output = gr.Textbox(label="Vibe History", lines=10, value=get_vibe_history())
    
    analyze_button.click(
        analyze_sentiment,
        inputs=[text_input],
        outputs=[result_output, history_output]
    )
    
    # Also trigger analysis when pressing Enter in the text box
    text_input.submit(
        analyze_sentiment,
        inputs=[text_input],
        outputs=[result_output, history_output]
    )

# Launch the app
if __name__ == "__main__":
    app.launch() 