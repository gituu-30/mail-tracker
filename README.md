
# 📩 MailTracker for Firefox

MailTracker is a Firefox browser extension that helps you **track when your emails are opened**, similar to Mailtrack for Chrome. This project includes both the **browser extension** and a **Flask backend server** that handles tracking pixel requests.

---

## 🚀 Features

- ✅ Injects an invisible tracking pixel into Gmail emails
- ✅ Logs email opens with timestamps using a backend server
- ✅ Built for Firefox using the WebExtensions API
- ✅ Open-source and easily deployable

---

## 🛠️ Folder Structure

```
mailtracker-extension/      <-- Firefox extension
├── manifest.json
├── content.js
├── background.js
├── popup.html
├── icon.png

mailtracker-backend/        <-- Flask backend server
├── server.py
├── pixel.png
└── requirements.txt
```

---

## 🌐 How It Works

1. When you open Gmail in Firefox, the extension injects a 1×1 transparent image:
   ```
   <img src="https://your-server.com/track?email_id=XYZ" style="display:none;">
   ```
2. When the recipient opens the email, the browser tries to load the image.
3. Your Flask backend receives this request and logs the email open with a timestamp.

---

## 🧩 Browser Extension Setup (Firefox)

1. Clone or download the `mailtracker-extension` folder.
2. Go to `about:debugging` in Firefox.
3. Click **"Load Temporary Add-on"** and select `manifest.json`.
4. Open Gmail → Compose a new email → Send it.

---

## ⚙️ Backend Setup (Local Testing)

1. Navigate to the `mailtracker-backend` folder.
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the server:
   ```bash
   python server.py
   ```
4. Update your extension's `content.js` with:
   ```js
   const pixelHTML = '<img src="http://localhost:5000/track?email_id=' + Date.now() + '" style="display:none;">';
   ```

---

## 🌍 Backend Deployment (Render)

1. Upload `server.py`, `pixel.png`, and `requirements.txt` to a GitHub repo.
2. Go to [https://render.com](https://render.com) → "New Web Service"
3. Connect your GitHub repo.
4. Set:
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `python server.py`
5. Deploy and get your public HTTPS URL.

Update `content.js`:
```js
const pixelHTML = '<img src="https://your-render-url.onrender.com/track?email_id=' + Date.now() + '" style="display:none;">';
```

---

## 📦 Backend Files Explained

| File         | Description                               |
|--------------|-------------------------------------------|
| `server.py`  | Flask app that handles tracking requests  |
| `pixel.png`  | 1×1 transparent image used for tracking    |
| `requirements.txt` | Lists Python dependencies (`flask`)   |

---

## 🧪 Testing It End-to-End

1. Run your Flask server (or deploy it).
2. Reload the extension.
3. Send an email to yourself or another account.
4. Open the email.
5. Check your server log:
   ```
   [OPENED] Email ID: 1724883941123 at 2025-06-28 14:45:05
   ```

---

## 🔐 Limitations & Notes

- Gmail caches and proxies images, so local servers (`localhost`) won't work directly.
- Use HTTPS for production to ensure Gmail loads your tracking pixel.
- This extension is designed for personal/educational use only.

---

## 📢 Credits

Created by **Rajveer Kumar**  
Inspired by [Mailtrack](https://mailtrack.io/)  
Built with 💻 Flask + JavaScript + Firefox WebExtensions API

---

## 📜 License

This project is licensed under the MIT License.
