from textblob import TextBlob

def analyze_sentiment(text:str):
    blob = TextBlob(text)
    polarity = blob.sentiment.polarity

    #Polarity -> [-1,1]
    if polarity > 0:
        sentiment = "Positive"
    elif polarity < 0:
        sentiment= "Negative"
    else:
        sentiment = "Neutral"
    return {
        "Polarity": polarity,
        "Sentiment":sentiment
    }

def smart_search(students,query:str):
    query = query.lower()
    results=[]

    for student in students:
        if (query in student.name.ower() or query in student.course.lower()):
            results.append(student)

    return results