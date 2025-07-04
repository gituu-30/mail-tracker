# 📩 MailTracker for Firefox

> A simple **email open tracker** built as a Firefox browser extension + Flask backend
> Inspired by [Mailtrack](https://mailtrack.io), but open-source and customizable.

---

## 🚀 Features

* 🕵️ Tracks when your email is opened using a **tracking pixel**
* 📅 Logs open events with timestamp and unique ID
* 🌐 Uses **Flask backend** and **WebExtensions API**
* 🧪 Works with Gmail inside Firefox
* 🧩 Easy to test, deploy, and extend

---

## 🗂 Folder Structure

```
mailtracker/
├── mailtracker-extension/      # Firefox Extension
│   ├── manifest.json
│   ├── content.js
│   ├── background.js
│   ├── popup.html
│   └── icon.png
│
└── mailtracker-backend/        # Flask Backend Server
    ├── server.py
    ├── pixel.png
    └── requirements.txt
```

---

## 🌐 How It Works

1. The extension injects an invisible `<img>` into every Gmail email you compose:

   ```html
   <img src="https://your-server.com/track?email_id=XYZ" style="display:none;">
   ```
2. When the recipient opens the email, the browser loads the image.
3. The Flask server logs the open event with a timestamp and email ID.

---

## 🧩 Setup: Firefox Extension

1. Clone or download the `mailtracker-extension` folder.
2. Open Firefox and go to `about:debugging`.
3. Click **"Load Temporary Add-on"** and select `manifest.json`.
4. Open Gmail → Compose and send an email.

> 💡 Each email will now include the tracking pixel automatically.

---

## ⚙️ Setup: Flask Backend (Local)

1. Open terminal in the `mailtracker-backend` folder.
2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```
3. Start the server:

   ```bash
   python server.py
   ```
4. Update `content.js` to point to your local server:

   ```js
   const pixelHTML = '<img src="http://localhost:5000/track?email_id=' + Date.now() + '" style="display:none;">';
   ```

---

## 🌍 Deployment: Flask Backend on Render

1. Push backend files (`server.py`, `pixel.png`, `requirements.txt`) to a GitHub repo.
2. Go to [https://render.com](https://render.com) → **New Web Service**
3. Link your GitHub repository.
4. Configuration:

   * **Build Command**: `pip install -r requirements.txt`
   * **Start Command**: `python server.py`
   * **Environment**: Python 3.13+
5. Deploy and get your public HTTPS URL.

Then update your extension’s `content.js`:

```js
const pixelHTML = '<img src="https://your-render-url.onrender.com/track?email_id=' + Date.now() + '" style="display:none;">';
```

---

## 📁 Backend Files Explained

| File               | Description                                |
| ------------------ | ------------------------------------------ |
| `server.py`        | Flask app handling tracking pixel requests |
| `pixel.png`        | A transparent 1×1 PNG image                |
| `requirements.txt` | Contains Python dependencies (`flask`)     |

---

## 🧪 How to Test

1. Run Flask server (or deploy it).
2. Load the extension into Firefox.
3. Send an email to yourself or another account.
4. Open the email.
5. Check your Flask server log:

   ```
   [OPENED] Email ID: 1724883941123 at 2025-06-28 14:45:05

## 👤 Author

Rajveer Kumar
📧 [rajveerkumar6424@gmail.com]
🌐 Built with Flask + JavaScript + Firefox WebExtension

 
 
