import gradio as gr
from src.models.sentiment_model import initialize_sentiment_analyzer, get_emoji
from src.utils.logger import initialize_log_file, log_sentiment, get_vibe_history, format_history

# Initialize sentiment analyzer and log file
sentiment_analyzer = initialize_sentiment_analyzer()
initialize_log_file()

# Main function to analyze sentiment
def analyze_sentiment(text):
    if not text.strip():
        return "Please enter some text to analyze.", format_history(get_vibe_history())
    
    # Get sentiment analysis result
    result = sentiment_analyzer(text)[0]
    label = result["label"]
    score = result["score"]
    emoji = get_emoji(label)
    
    # Format result output
    output = f"{label} {emoji} (Confidence: {score*100:.1f}%)"
    
    # Log to CSV
    log_sentiment(text, label, score)
    
    # Get updated history
    history = format_history(get_vibe_history())
    
    return output, history

# Create Gradio interface with Blocks
def create_app():
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
                history_output = gr.Textbox(
                    label="Vibe History", 
                    lines=10, 
                    value=format_history(get_vibe_history())
                )
        
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
        
    return app

# Launch the app
def main():
    app = create_app()
    app.launch()

if __name__ == "__main__":
    main() 