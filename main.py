from textblob import TextBlob

def request_statement() -> str:
    return input("Express a sentiment: ")


def determine_polarity(a) -> str:
    polarity = a.sentiment.polarity
    if polarity > 0:
        return "Positive"
    elif polarity < 0:
        return "Negative"
    else:
        return "Neutral"


if __name__ == '__main__':
    analysis = TextBlob(request_statement())
    sentiment = determine_polarity(analysis)
    print(f"Sentiment Score: {sentiment}")

