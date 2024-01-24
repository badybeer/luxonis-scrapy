from flask import Flask, render_template
import psycopg2

app = Flask(__name__)

def get_data():
    connection = psycopg2.connect(
    host="db",
    database="sreality",
    user="admin",
    password="admin"
)
    cursor = connection.cursor()
    cursor.execute("SELECT title, image_url FROM flats")
    flats = cursor.fetchall()
    cursor.close()
    connection.close()
    return flats

@app.route('/')
def index():
    flats = get_data()
    return render_template('index.html', flats=flats)

if __name__ == '__main__':
    app.run(debug=True)
