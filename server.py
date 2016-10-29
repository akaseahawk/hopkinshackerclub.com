from flask import Flask, render_template, url_for, request
app = Flask(__name__)

def getAnnouncements():
    #will eventually read announcements from data base
    return [
            ['Test Header', 'This is a test body'],
            ['Test Header', 'This is a test body'],
            ['Test Header', 'This is a test body']
        ]

@app.route('/', methods = ['GET'])
def index():
    if request.method == 'GET':
        return render_template('index.html', announcements = getAnnouncements())

if __name__ == '__main__':
    app.run(debug = True)
