from flask import Flask, render_template, jsonify, request
import random

app = Flask(__name__)

# Placeholder topics and reference lyrics for now
TOPICS = [
    "失恋", "初恋", "友情", "家乡", "梦想", "成长",
    "旅行", "孤独", "希望", "回忆", "城市生活", "乡村",
    "四季", "爱情", "亲情", "理想", "奋斗", "青春"
]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/roll_topic', methods=['POST'])
def roll_topic():
    topic = random.choice(TOPICS)
    return jsonify({'topic': topic})

@app.route('/api/roll_lyrics', methods=['POST'])
def roll_lyrics():
    # Placeholder for Gemini API call
    return jsonify({
        'lyrics': '这里将是AI生成的参考歌词\n根据主题生成\n展示创作方向'
    })

@app.route('/api/evaluate', methods=['POST'])
def evaluate_lyrics():
    user_lyrics = request.json.get('lyrics', '')
    topic = request.json.get('topic', '')
    
    # Placeholder for Gemini API call
    return jsonify({
        'feedback': '这里将是对歌词的评价和建议',
        'improved': '这里将是改进后的版本'
    })

if __name__ == '__main__':
    app.run(debug=True, port=5000) 