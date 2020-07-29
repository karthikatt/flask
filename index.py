from flask import Flask, render_template, redirect, url_for
from flask import request
import mysql.connector
import datetime
import time


app = Flask(__name__)

@app.route("/")
def index():
   return render_template("index.html")
@app.route("/faculty")
def faculty():
   return render_template("faculty.html")
@app.route("/student")
def student():
   return render_template("student.html")
@app.route("/submit_student",methods = ['POST'])
def submit_student():
	if request.method == 'POST':
		try:
			name = request.form['name']
			branch = request.form['branch']
			mode = request.form['mode']
			mobileNo = request.form['mobileno']
			email = request.form['email']
			currentAdd = request.form['cd']
			parmanentAdd = request.form['pd']
			fatherName = request.form['fname']
			fatherMobileNo = request.form['fmobileno']
			ts = time.time()
			timestamp = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')

			with mysql.connector.connect(user='root', password='infiniti', host='127.0.0.1', database='demo') as con:
				cur = con.cursor()
				query=("INSERT INTO students (name,branch,mode,mobileNo,email,currentAdd,parmanentAdd,fatherName,fatherMobileNo) VALUES (%s, %s, %s, %s, %s,%s, %s, %s, %s)")
				data=(name,branch,mode,mobileNo,email,currentAdd,parmanentAdd,fatherName,fatherMobileNo)
				cur.execute(query,data)	
				con.commit()
				auditQuery =("INSERT INTO auditInfo (id,facultyId,processTime) VALUES (%s, %s, %s)")
				auditData = (cur.lastrowid,1,timestamp)
				cur.execute(auditQuery,auditData)	
				con.commit()
				msg = "Record successfully added"
		except Exception as e:
			print(e)
			con.rollback()
			msg = "error in insert operation"
		finally:
			# return render_template("result.html",msg = msg)
			con.close()
			return msg
			# return redirect(url_for('student'))
@app.route("/search_student",methods = ['POST'])
def search_student():
	if request.method == 'POST':
		try:
			id = request.form['id']
			with mysql.connector.connect(user='root', password='infiniti', host='127.0.0.1', database='demo') as con:
				cur = con.cursor()
				query='SELECT * from students WHERE id ='+id
				cur.execute(query)
				result = cur.fetchall();
		except Exception as e:
			return render_template("faculty.html",noRecord = 'noRecord')
		con.close()
		data = [result,id]
		return render_template("faculty.html",data = data)

@app.route("/verifyAndUpdate_student",methods = ['POST'])
def verifyAndUpdate_student():
	if request.method == 'POST':
		try:
			id = request.form['id']
			name = request.form['name']
			branch = request.form['branch']
			mode = request.form['mode']
			mobileNo = request.form['mobileno']
			email = request.form['email']
			currentAdd = request.form['cd']
			parmanentAdd = request.form['pd']
			fatherName = request.form['fname']
			fatherMobileNo = request.form['fmobileno']
			ts = time.time()
			timestamp = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
			with mysql.connector.connect(user='root', password='infiniti', host='127.0.0.1', database='demo') as con:
				cur = con.cursor()
				sql = 'UPDATE students SET name ='+"'"+name+"'"+',branch = '+"'"+branch+"'"+',mode = '+"'"+mode+"'"+',mobileNo = '+"'"+mobileNo+"'"+',email = '+"'"+email+"'"+',currentAdd = '+"'"+currentAdd+"'"+',parmanentAdd = '+"'"+parmanentAdd+"'"+',fatherName = '+"'"+fatherName+"'"+',fatherMobileNo = '+"'"+fatherMobileNo+"'"+' WHERE id = '+id
				cur.execute(sql)
				con.commit()
				auditQuery = ("UPDATE auditInfo set facultyId = 1,processTime = "+"'"+timestamp+"'"+" WHERE id="+id)
				cur.execute(auditQuery)
				con.commit()
		except Exception as e:
			pass
		finally:
			# return render_template("result.html",msg = msg)
			con.close()
			return render_template("faculty.html")
if __name__ == '__main__':
   app.run(debug = True)