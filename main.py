from flask import Flask,render_template,request,redirect
from pymongo import MongoClient
from validator import CourseForm

app = Flask(__name__)
client = MongoClient('mongodb://localhost:27017')
db = client['courses']
courses_collection = db['entries']

if __name__ == '__main__':
    app.run(debug=True)

@app.route('/', methods=['GET'])
def home():
    courses = courses_collection.find()
    return render_template("index.html",courses=courses)



@app.route('/add', methods=['GET','POST'])
def add_course():
    form = CourseForm(request.form)

    if(request.method == 'POST') and form.validate():
        entry = {
            "name":form.name.data,
            "category":form.category.data,
            "price":form.price.data,
            "city":form.city.data,
            "hours":form.hours.data
        }
        #print(entry)
        courses_collection.insert_one(entry)
        return redirect('/')

    return render_template("add.html", form=form)