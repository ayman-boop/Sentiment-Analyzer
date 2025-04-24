from src.models.sentiment_model import initialize_sentiment_analyzer

def test_sentiment_analysis():
    """Test the sentiment analysis functionality with various example texts."""
    # Initialize sentiment analysis pipeline
    sentiment_analyzer = initialize_sentiment_analyzer()

    # Test texts
    test_texts = [
        "I am very happy today",
        "This is terrible",
        "This is just okay"
    ]

    for text in test_texts:
        result = sentiment_analyzer(text)[0]
        label = result["label"]
        score = result["score"]
        
        # Format result output in both ways
        decimal_output = f"{label} (Confidence: {score:.4f})"
        percentage_output = f"{label} (Confidence: {score*100:.1f}%)"
        
        print(f"Text: {text}")
        print(f"Decimal format: {decimal_output}")
        print(f"Percentage format: {percentage_output}")
        print("-" * 50)

if __name__ == "__main__":
    test_sentiment_analysis() 