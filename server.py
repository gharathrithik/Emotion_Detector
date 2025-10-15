from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def sent_detector():
    text_to_analyze = request.args.get('textToAnalyze')
    output = emotion_detector(text_to_analyze)
    return f"For the given statement, the system response is '{output[0]}'. The dominant_emotion is {output[-1]}"

@app.route("/")
def render_index_page():
    return render_template('index.html')

if __name__ == "__main__":
    app.run()
