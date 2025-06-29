from flask import Flask, request, send_file
import datetime
import sys

app = Flask(__name__)
log_data = []

@app.route('/')
def home():
    return "✅ MailTracker server is running."

@app.route('/track')
def track():
    email_id = request.args.get('email_id', 'unknown')
    time_opened = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    log_entry = f"[OPENED] Email ID: {email_id} at {time_opened}"
    print(log_entry)
    log_data.append(log_entry)
    sys.stdout.flush()

    return send_file("pixel.png", mimetype='image/png')

@app.route('/logs')
def logs():
    return "<br>".join(log_data) or "No opens yet."

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
