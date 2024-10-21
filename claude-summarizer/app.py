# app.py
import os
from dotenv import load_dotenv
from flask import Flask, render_template, request
from anthropic import Anthropic

# Load environment variables from .env file
load_dotenv()

app = Flask(__name__)


CLAUDE_API_KEY =  os.getenv('CLAUDE_API_KEY')
CLAUDE_MODEL =  os.getenv('CLAUDE_MODEL')

anthropic = Anthropic(api_key=CLAUDE_API_KEY)

@app.route('/', methods=['GET', 'POST'])
def index():
    summary = None
    if request.method == 'POST':
        user_input = request.form['user_input']
        try:
            response = anthropic.messages.create(
                model=CLAUDE_MODEL,
                messages=[
                    {"role": "user", "content": f"Please summarize the following text:\n\n{user_input}"}
                ],
                max_tokens=300
            )
            summary = response.content[0].text
        except Exception as e:
            summary = f"An error occurred: {str(e)}"
    
    return render_template('index.html', summary=summary)

if __name__ == '__main__':
    app.run(debug=True)