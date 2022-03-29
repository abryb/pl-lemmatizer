#!/usr/bin/env python
import json
import markdown

from os.path import dirname, realpath
from concraft_pl2 import Server, Concraft
from flask import Flask, request
from morfeusz2 import Morfeusz
from lemmatizer import Lemmatizer

app = Flask(__name__)


@app.route('/')
def index():
    root_dir = dirname(dirname(realpath(__file__)))
    with open(f"{root_dir}/README.md") as readme_file:
        return markdown.markdown(readme_file.read())


@app.route('/lemmatize', methods=['POST'])
def lemmatize():
    request_body = json.loads(request.data)
    texts = request_body['texts']
    result = []
    for text in texts:
        result.append({
            'text': text,
            'lemmatized': lemmatizer.fast_lemmatize(text)
        })
    return json.dumps({
        'result': result
    })


print("Running Concraft server...")
concraft_server = Server(
    model_path="/app/data/model.gz",
)
lemmatizer = Lemmatizer(
    Morfeusz(expand_tags=True),
    Concraft()
)

print("Running Flask server...")
app.run(
    host="0.0.0.0"
)