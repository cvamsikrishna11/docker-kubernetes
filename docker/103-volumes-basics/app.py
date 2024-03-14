from flask import Flask
import os

app = Flask(__name__)

def ensure_data_dir_exists():
    data_dir = '/data'
    if not os.path.exists(data_dir):
        os.makedirs(data_dir)

@app.route('/')
def write_message():
    message = "Hello, Docker! Accessed the root URL.\n"
    file_path = '/data/mydata.txt'
    ensure_data_dir_exists()  # Ensure /data directory exists
    with open(file_path, 'a') as file:
        file.write(message)
    return "Message written to /data/mydata.txt"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
