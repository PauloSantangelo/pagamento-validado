from flask import Flask, send_from_directory

app = Flask(__name__, static_folder="static")

@app.route('/static/videos/<path:filename>')
def serve_video(filename):
    return send_from_directory("static/videos", filename)

if __name__ == "__main__":
    app.run(debug=True)
