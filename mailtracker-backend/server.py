from flask import Flask, request, send_file
import datetime
import sys

app = Flask(__name__)

@app.route('/track')
def track():
    email_id = request.args.get('email_id', 'unknown')
    time_opened = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    print(f"[OPENED] Email ID: {email_id} at {time_opened}")
    sys.stdout.flush()  # 🔥 This line ensures logs appear in Render
    return send_file("pixel.png", mimetype='image/png')

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)

user_agent = request.headers.get('User-Agent')
print(f"[OPENED] Email ID: {email_id} at {time_opened} | UA: {user_agent}")
sys.stdout.flush()
