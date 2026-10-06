from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)

@app.route('/emotionDetector', methods=['GET'])
def emotionDetector():
    text_to_analyze = request.args.get('textToAnalyze')
  
    result= emotion_detector(text_to_analyze)
    result_text=f"For the given statement, the system response is 'anger': {result['anger']}, 'disgust': {result['disgust']}, 'fear': {result['fear']}, 'joy': {result['joy']}, 'sadness': {result['sadness']}. The dominant emotion is {result['dominant_emotion']}."
    return result_text
@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    # port 5000
    app.run(port = 5000, debug=True)