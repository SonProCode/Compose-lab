from flask import Flask
import psycopg2
app = Flask(__name__)

@app.route('/')
def home():
    try:
        conn = psycopg2.connect(
            host="db",
            database="testdb",
            user="testuser",
            password="testpass"
        )
        return "Connected to PostgreSQL!"
    except:
        return "Database connection failed."

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
