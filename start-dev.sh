#!/usr/bin/env bash

set -e  # stop on error

APP_MODULE="app.main:app"
HOST="0.0.0.0"
PORT="8000"

echo "🚀 Starting development server..."

# 1️⃣ Create virtual environment if not exists
if [ ! -d "venv" ]; then
  echo "📦 Creating virtual environment..."
  python3 -m venv venv
fi

# 2️⃣ Activate virtual environment
echo "🔧 Activating virtual environment..."
source venv/bin/activate

# 3️⃣ Upgrade pip
pip install --upgrade pip > /dev/null

# 4️⃣ Install dependencies if requirements.txt exists
if [ -f "requirements.txt" ]; then
  echo "📚 Installing dependencies..."
  pip install -r requirements.txt
else
  echo "⚠️  requirements.txt not found. Installing minimal dependencies..."
  pip install fastapi uvicorn reportlab
fi

# 5️⃣ Start server
echo "🌍 Running server on http://$HOST:$PORT"
uvicorn $APP_MODULE --host $HOST --port $PORT --reload
