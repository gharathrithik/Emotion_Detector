'''
This is a Module for Emotion Detection in the user provided text using an API
'''

from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def sent_detector():
    '''
    Function to run the emotion detection API
    '''
    text_to_analyze = request.args.get('textToAnalyze')
    output = emotion_detector(text_to_analyze)
    if output['dominant_emotion'] is None:
        return "Invalid text! Please try again!."
    return f'''For the given statement, the system response is 'anger': {output['anger']}',
    'disgust': {output['disgust']}, 'fear': {output['fear']}, 'joy': {output['joy']},
    and 'sadness': {output['sadness']}. The dominant emotion is {output['dominant_emotion']}'''

@app.route("/")
def render_index_page():
    '''
    Function to render the home page
    '''
    return render_template('index.html')

if __name__ == "__main__":
    app.run(port=5000)
