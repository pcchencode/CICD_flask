from flask import Flask
app = Flask(__name__)


@app.route('/')
def index():
    return 'hello 123123aaa3aaa'

if __name__ == '__main__':
    app.debug = True
    # app.run(debug=True, host='0.0.0.0', port=8888)
    app.run(debug=True, host='0.0.0.0', port=5000)
    # docker run -p 80:8888 flask_im, -p 將主機 8888 port 與 container的 80 port 綁定
    # http://0.0.0.0:80/

    # docker run - p 80:5000
    # http://0.0.0.0:80/
