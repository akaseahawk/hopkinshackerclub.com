from flask import Flask, render_template, url_for, request, redirect
from functools import wraps
app = Flask(__name__)


def checkAuth(password):
    f = open('static/cred.txt')
    return password == f.readline().rstrip()

announcementsLog = []
def getAnnouncements():
    return announcementsLog

@app.route('/', methods = ['GET'])
def index():
    if request.method == 'GET':
        return render_template('index.html', announcements = getAnnouncements())

@app.route('/submitAnnouncement', methods = ['GET', 'POST'])
def submitAnnouncement():
    if request.method == 'GET':
        return render_template('submitAnnouncement.html')
    if request.method == 'POST':
        header = str(request.form['Header'])
        body = str(request.form['Body'])
        cred = str(request.form['Cred'])
        print cred
        if checkAuth(cred):
            announcementsLog.append([header, body])
        return redirect(url_for('index'))
    return 404

if __name__ == '__main__':
    app.run(debug = True)
