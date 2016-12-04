from flask import Flask, render_template, url_for, request, redirect
app = Flask(__name__)

announcementsLog = []

projectList = []

def getAnnouncements():
    return announcementsLog

def getProjects():
    return projectList

@app.route('/', methods = ['GET'])
def index():
    if request.method == 'GET':
        return render_template('index.html', announcements = getAnnouncements(), projects = getProjects())

@app.route('/submitAnnouncement', methods = ['GET', 'POST'])
def submitAnnouncement():
    if request.method == 'GET':
        return render_template('submitAnnouncement.html')
    if request.method == 'POST':
        header = str(request.form['Header'])
        body = str(request.form['Body'])
        announcementsLog.append([header, body])
        return redirect(url_for('index'))
    return 404

@app.route('/submitProject', methods = ['GET', 'POST'])
def submitProject():
    if request.method == 'GET':
        return render_template('submitProject.html')
    if request.method == 'POST':
        name = str(request.form['Name'])
        desc = str(request.form['Desc'])
        images = str(request.form['Images']) #string of image paths separated by commas
        imageList = images.split(",")
        projectList.append([name, desc, imageList])
        return redirect(url_for('submitProject'))
    return 404


if __name__ == '__main__':
    app.run(debug = True)
