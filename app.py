from flask import Flask, request, jsonify, render_template
import sqlite3
from db_scripts import get_batch, get_post_by_id, update_count_view

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    posts = get_batch(8, 1)
    print(posts)
    return render_template('index.html', posts=posts)  # Render the template with users data

@app.route('/post', methods=['GET'])
def get_post():
    post_id = request.args.get('id', default=1)
    update_count_view(post_id)
    post = get_post_by_id(post_id)
    tags = post["tags"].split("|")
    return render_template('post.html',
                           post=post, tags=tags)


if __name__ == "__main__":
    app.run(debug=True)