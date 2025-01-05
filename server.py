''' Executing this function initiates the application of sentiment
    analysis to be executed over the Flask channel and deployed on
    localhost:5000.
'''
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def emo_detector():
    ''' This code receives the text from the HTML interface and 
        runs emotion dectection over it using emotion_detector()
        function. 
    '''
    # Retrieve the text to analyze from the request arguments
    text_to_analyze = request.args.get('textToAnalyze')
    # Pass the text to the emotion_detector function and store the response
    response = emotion_detector(text_to_analyze)

    # Extract the label and score from the response
    anger_score = response['anger']
    disgust_score = response['disgust']
    fear_score = response['fear']
    joy_score = response['joy']
    sadness_score = response['sadness']
    dominant_emo = response['dominant_emotion']
    if dominant_emo == '':
        result =  "Invalid text! Please try again!"
    else:
        result = f'''For the given statement, \
        the system response is 'anger': {anger_score}, \
        'disgust': {disgust_score}, 'fear': {fear_score}, \
        'joy': {joy_score} and 'sadness': {sadness_score}. \
        The dominant emotion is {dominant_emo}.'''
    return result

@app.route("/")
def render_index_page():
    ''' This function initiates the rendering of the main application
        page over the Flask channel
    '''
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="localhost", port=5000)
