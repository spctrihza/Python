from flask import Flask, request, jsonify, render_template, redirect
# from librouteros.query import Key
# import paramiko 
import time
# from librouteros import connect
import sqlite3
from datetime import datetime




app = Flask(__name__)

@app.route('/', methods=['POST','GET'])
def index():
    sqliteConnection = sqlite3.connect('coba.db')
    cursor = sqliteConnection.cursor()
    cursor.execute("select * from id")
    datatest=cursor.fetchall()
    # result_len2=len(datatest)
    return render_template ('index.html', datatest=datatest)

    # return render_template('index.html')

@app.route('/view/<int:no>',methods=['POST','GET'])
def view(no):
    sqliteConnection = sqlite3.connect('coba.db')
    cursor = sqliteConnection.cursor()
    cursor.execute("select * from id where nomor={}".format(no))
    result = cursor.fetchall()
    return render_template('view.html',result=result)

@app.route('/update', methods=['POST','GET'])
def update():
    namadepan = request.form['nd']
    namabelakang = request.form['nb']
    pilihan = request.form['pl']
    nomor = request.form['no']
    sqliteConnection = sqlite3.connect('coba.db')
    cursor = sqliteConnection.cursor()
    cursor.execute("update id set nama_depan='{}', nama_belakang='{}', pilihan='{}' where nomor={}".format(namadepan,namabelakang,pilihan,nomor))
    sqliteConnection.commit()
    # cursor.execute("select * from identitas")
    # datatest = cursor.fetchall()
    # return render_template('index.html',datatest=datatest)
    return redirect('/')

@app.route("/test", methods=['GET', 'POST'])
def test():
    sqliteConnection = sqlite3.connect('coba.db')
    cursor = sqliteConnection.cursor()
    cursor.execute("select * from skills")
    result = cursor.fetchall()
    total = len(result)
    return render_template('test.html',result=result)

    # if total == 0:
    #     return render_template('test.html')
    # elif total > 0:
    #     return render_template('test1.html', total=total, result=result)

@app.route('/coba', methods=['POST','GET'])
def coba():
    sqliteConnection = sqlite3.connect('coba.db')
    cursor = sqliteConnection.cursor()
    if request.method == 'POST':
        skills = request.form.getlist('skill[]')
        for value in skills:  
            cursor.execute("INSERT INTO skills (skillname) VALUES ('{}')".format(value))
            sqliteConnection.commit()
        msg = 'New record created successfully'    
    return redirect('test')
    # return jsonify(msg)


#host dibawah adalah ip server ZTP
if __name__ == '__main__':
    #app.run(debug='True')
    app.run(debug=True)