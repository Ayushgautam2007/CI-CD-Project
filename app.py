from flask import Flask, render_template, request, redirect, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from dotenv import load_dotenv
import certifi
import os

# Load environment variables
load_dotenv()

app = Flask(__name__)

# Configuration
app.config["MONGO_URI"] = os.getenv("MONGO_URI")
app.secret_key = os.getenv("SECRET_KEY")

# Initialize MongoDB
mongo = PyMongo(app, tlsCAFile=certifi.where())


# Home Page
@app.route('/')
def index():
    students = mongo.db.students.find()
    return render_template('index.html', students=students)


# Add Student
@app.route('/add', methods=['GET', 'POST'])
def add_student():

    if request.method == 'POST':

        mongo.db.students.insert_one({
            "name": request.form["name"],
            "email": request.form["email"],
            "course": request.form["course"]
        })

        return redirect(url_for("index"))

    return render_template("add_student.html")


# Update Student
@app.route('/update/<student_id>', methods=['GET', 'POST'])
def update_student(student_id):

    student = mongo.db.students.find_one(
        {"_id": ObjectId(student_id)}
    )

    if request.method == 'POST':

        mongo.db.students.update_one(
            {"_id": ObjectId(student_id)},
            {
                "$set": {
                    "name": request.form["name"],
                    "email": request.form["email"],
                    "course": request.form["course"]
                }
            }
        )

        return redirect(url_for("index"))

    return render_template(
        "update_student.html",
        student=student
    )


# Delete Student
@app.route('/delete/<student_id>')
def delete_student(student_id):

    mongo.db.students.delete_one(
        {"_id": ObjectId(student_id)}
    )

    return redirect(url_for("index"))


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=5000,
        debug=True
    )
