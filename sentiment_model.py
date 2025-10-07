from transformers import pipeline

def analyze_sentiment(prompt):
    """
    Analyze the sentiment of the input text using a pretrained transformer.
    Returns one of: 'positive', 'negative', or 'neutral'.
    """
    sentiment_analyzer = pipeline("sentiment-analysis")
    result = sentiment_analyzer(prompt)[0]
    label = result['label'].lower()

    if 'pos' in label:
        return 'positive'
    elif 'neg' in label:
        return 'negative'
    else:
        return 'neutral'
