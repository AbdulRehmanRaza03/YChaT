# 💬 ChatApp — Real-time WhatsApp-inspired Chat

Full-stack real-time chat app: Flask + SocketIO + PostgreSQL + Google OAuth.

---

## 📁 Folder Structure

```
chatapp/
├── app/
│   ├── __init__.py          # App factory
│   ├── models.py            # SQLAlchemy models (User, Message)
│   ├── routes/
│   │   ├── auth.py          # Google OAuth, login, logout
│   │   ├── main.py          # Home, search, profile
│   │   ├── chat.py          # Conversation, image send
│   │   └── api.py           # JSON API endpoints
│   ├── services/
│   │   └── socket_events.py # All SocketIO events
│   ├── utils/
│   │   └── helpers.py       # Image save, username gen
│   ├── static/
│   │   ├── css/main.css
│   │   ├── js/app.js
│   │   ├── js/chat.js
│   │   ├── js/home.js
│   │   └── img/
│   └── templates/
│       ├── base.html
│       ├── auth/login.html
│       ├── chat/conversation.html
│       └── main/{landing,home,search,profile}.html
├── config.py
├── app.py                   # Dev entry point
├── wsgi.py                  # Prod entry point (gunicorn)
├── init_db.py               # DB table creation
├── Procfile
├── render.yaml
├── requirements.txt
└── .env.example
```

---

## ⚙️ Step 1 — Environment Setup

```bash
# Clone / open project in VS Code
cd chatapp

# Create virtual env
python -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate

# Install deps
pip install -r requirements.txt

# Copy env file
cp .env.example .env
# Then edit .env with your values
```

---

## 🗄️ Step 2 — Database Setup

### Option A: SQLite (dev, no setup needed)
Leave `DATABASE_URL` blank in `.env`. App auto-uses `chatapp.db`.

### Option B: PostgreSQL (recommended)
```bash
# Install PostgreSQL, then:
createdb chatapp
# Set in .env:
# DATABASE_URL=postgresql://youruser:yourpass@localhost:5432/chatapp
```

Then create tables:
```bash
python init_db.py
```

---

## 🔑 Step 3 — Google OAuth Setup

1. Go to [console.cloud.google.com](https://console.cloud.google.com)
2. Create project → **APIs & Services** → **Credentials**
3. **Create OAuth 2.0 Client ID** → Web application
4. Add Authorized redirect URIs:
   - Dev: `http://localhost:5000/auth/google/authorized`
   - Prod: `https://your-app.onrender.com/auth/google/authorized`
5. Copy **Client ID** and **Client Secret** → paste in `.env`

```env
GOOGLE_CLIENT_ID=xxxx.apps.googleusercontent.com
GOOGLE_CLIENT_SECRET=GOCSPX-xxxx
SECRET_KEY=any-random-long-string
```

---

## ▶️ Step 4 — Run Locally

```bash
python app.py
# Open http://localhost:5000
```

---

## 🚀 Step 5 — Deploy to Render

### Method A: render.yaml (auto)
```bash
git init && git add . && git commit -m "init"
# Push to GitHub, then:
# render.com → New → Web Service → connect repo
# Render auto-reads render.yaml
```

### Method B: Manual
1. render.com → **New Web Service** → connect GitHub repo
2. Settings:
   - **Build command:** `pip install -r requirements.txt`
   - **Start command:** `gunicorn --worker-class eventlet -w 1 wsgi:app --bind 0.0.0.0:$PORT --timeout 120`
3. Add **PostgreSQL** database → copy connection string
4. Set env vars:
   ```
   FLASK_ENV=production
   SECRET_KEY=<generate random>
   DATABASE_URL=<from render postgres>
   GOOGLE_CLIENT_ID=<yours>
   GOOGLE_CLIENT_SECRET=<yours>
   ```
5. After first deploy, open Render shell:
   ```bash
   python init_db.py
   ```

---

## 🚂 Deploy to Railway

```bash
# Install Railway CLI
npm install -g @railway/cli
railway login
railway init
railway add postgresql
railway up
# Set env vars in Railway dashboard
```

---

## ✨ Features

| Feature | Status |
|---------|--------|
| Google Sign-In | ✅ |
| Real-time messaging | ✅ |
| Typing indicator | ✅ |
| Online/offline status | ✅ |
| Last seen | ✅ |
| Read receipts (blue ticks) | ✅ |
| Image sharing | ✅ |
| User search | ✅ |
| Profile editing | ✅ |
| Mobile-first UI | ✅ |
| CSRF protection | ✅ |

---

## 🔮 Future Upgrades

1. **Group chats** — Add `Group` and `GroupMember` models
2. **Voice messages** — MediaRecorder API + audio player bubble
3. **Push notifications** — Web Push API + service worker
4. **Cloud storage** — Replace local uploads with AWS S3 / Cloudinary
5. **End-to-end encryption** — Signal protocol / libsodium
6. **Message reactions** — Emoji reactions on bubbles
7. **Message search** — Full-text search with PostgreSQL `tsvector`
8. **Blocked users** — Block/unblock + filter messages
9. **Story/Status** — 24h disappearing media posts
10. **Redis + Celery** — Background jobs, better socket scaling

---

## 🛠️ Tech Stack

- **Backend:** Python Flask, Flask-SocketIO, Flask-Login, Flask-Dance
- **Database:** PostgreSQL (SQLite for dev)
- **ORM:** SQLAlchemy
- **Real-time:** Socket.IO (eventlet async)
- **Auth:** Google OAuth 2.0
- **Frontend:** Vanilla HTML/CSS/JS, mobile-first
- **Deploy:** Render / Railway / VPS

---

> Built with ❤️ — Production-ready foundation. Extend freely.
