# 🧠 Sentiment Analyzer

A simple and aesthetic AI-powered app that analyzes the **sentiment** of what you type — and tracks the vibes over time.

Built with:
- 🤗 Hugging Face Transformers
- 🎛️ Gradio UI
- 📊 Pandas (for vibe logging)

## 🚀 Features

- 🔍 Detects whether your sentence is **Positive**, **Negative**, or **Neutral**
- 😄 Adds emojis to match the mood (😄, 😠, 😐)
- 🕒 Keeps a **vibe history** (last 10 inputs)
- 🧾 Logs all inputs to a CSV file with timestamp, score, and sentiment
- Shows confidence score as a percentage

## 📁 Project Structure

```
sentiment-analyzer/
├── main.py               # Entry point to run the application
├── requirements.txt      # Project dependencies
├── README.md             # Project documentation
├── LICENSE               # License information
└── src/                  # Source code
    ├── app.py            # Main application logic
    ├── models/           # ML model related code
    │   └── sentiment_model.py  # Sentiment analysis model
    ├── utils/            # Utility functions
    │   └── logger.py     # Logging functionality
    └── data/             # Data storage
        └── vibe_log.csv  # Log of sentiment analysis results
```

## 💻 Installation

1. Clone this repository
```bash
git clone https://github.com/ayman-boop/Sentiment-Analyzer.git
cd Sentiment-Analyzer
```

2. Install the required dependencies:
```bash
pip install -r requirements.txt
```

## 🚀 Usage

Run the application:
```bash
python main.py
```

The Gradio interface will launch in your default web browser. Enter text in the input box and click "Analyze 🔍" to see the sentiment analysis results.

## 🧪 Testing

To run the test script:
```bash
python -m src.utils.tests
```

## 📋 Requirements

- Python 3.7+
- transformers
- gradio
- pandas
- torch
