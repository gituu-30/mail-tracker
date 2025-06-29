from flask import Flask, request, send_file
import datetime

app = Flask(__name__)
logs = []  # Store logs in memory

@app.route('/track')
def track():
    email_id = request.args.get('email_id', 'unknown')
    time_opened = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    log_entry = f"[OPENED] Email ID: {email_id} at {time_opened}"
    logs.append(log_entry)
    print(log_entry)
    return send_file("pixel.png", mimetype='image/png')

@app.route('/logs')
def view_logs():
    if not logs:
        return "No opens yet."
    return "<br>".join(logs)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
