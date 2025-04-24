from transformers import pipeline

# Initialize sentiment analysis pipeline
sentiment_analyzer = pipeline("sentiment-analysis")

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
    
    # Format result output in both ways to compare
    decimal_output = f"{label} (Confidence: {score:.4f})"
    percentage_output = f"{label} (Confidence: {score*100:.1f}%)"
    
    print(f"Text: {text}")
    print(f"Decimal format: {decimal_output}")
    print(f"Percentage format: {percentage_output}")
    print("-" * 50) 