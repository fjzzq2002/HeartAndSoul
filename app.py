from flask import Flask, render_template, jsonify, request
import random

from prompt_flashthinking import get_chat_session, generate_topic

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/roll_topic', methods=['POST'])
def roll_topic():
    print('Rolling topic...')
    api_key = request.headers.get('X-Gemini-Api-Key')
    if not api_key:
        return jsonify({'error': 'Missing API key'}), 401
        
    response = generate_topic(api_key)
    parts = response.candidates[0].content.parts
    txt = parts[-1].text.strip()
    print(f'Raw topic: {txt}')
    for punc in '*，。.？':
        txt = txt.replace(punc, ' ')
    txt = txt.strip()
    txt = txt.replace('  ',' ')
    txt = txt.replace('  ',' ')
    txt = txt.replace('  ',' ')
    return jsonify({'topic': txt})

@app.route('/api/roll_lyrics', methods=['POST'])
def roll_lyrics():
    print('Rolling lyrics...')
    api_key = request.headers.get('X-Gemini-Api-Key')
    if not api_key:
        return jsonify({'error': 'Missing API key'}), 401
        
    topic = request.json.get('topic', '')
    chat_session = get_chat_session(api_key)
    response = chat_session.send_message('写得很好，接下来写一段有关以下主题的歌词：'+topic)
    print(response)
    parts = response.candidates[0].content.parts
    return jsonify({'lyrics': '\n\n\n'.join(t.text for t in parts[::-1])})

@app.route('/api/evaluate', methods=['POST'])
def evaluate_lyrics():
    print('Evaluating lyrics...')
    api_key = request.headers.get('X-Gemini-Api-Key')
    if not api_key:
        return jsonify({'error': 'Missing API key'}), 401
        
    user_lyrics = request.json.get('lyrics', '')
    topic = request.json.get('topic', '')
    chat_session = get_chat_session(api_key)
    response = chat_session.send_message(f'写得很好，接下来评价一下我写的以下歌词，主题：{topic}\n\n{user_lyrics}')
    print(response)
    feedback = response.candidates[0].content.parts[-1].text
    return jsonify({'feedback': feedback})

if __name__ == '__main__':
    app.run(debug=True, port=5000) 