from flask import Flask, request, send_file
import datetime

app = Flask(__name__)

@app.route('/track')
def track():
    email_id = request.args.get('email_id', 'unknown')
    time_opened = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    print(f"[OPENED] Email ID: {email_id} at {time_opened}")

    return send_file("pixel.png", mimetype='image/png')

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
