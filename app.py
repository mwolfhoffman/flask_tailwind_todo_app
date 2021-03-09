from flask import Flask, render_template, request, redirect  
from flask_sqlalchemy import SQLAlchemy  
from datetime import datetime  

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todo.db'  
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  
db = SQLAlchemy(app)  




class Task(db.Model):
   id = db.Column(db.Integer, primary_key=True)
   name = db.Column(db.String(80), nullable=False)
   created_at = db.Column(db.DateTime, nullable=False,
                          default=datetime.now)

   def __repr__(self):
       return f'Todo : {self.name}'


@app.route("/", methods=['POST', 'GET'])
def home():
   if request.method == "POST":
       name = request.form['name']
       new_task = Task(name=name)
       db.session.add(new_task)
       db.session.commit()
       return redirect('/')
   else:
       tasks = Task.query.order_by(Task.created_at).all()  
   return render_template("home.html", tasks=tasks)  

@app.route('/delete/<int:id>')
def delete(id):
   task = Task.query.get_or_404(id)

   try:
       db.session.delete(task)
       db.session.commit()
       return redirect('/')
   except Exception:
       return "There was a problem deleting data."

@app.route('/update/<int:id>', methods=['GET', 'POST'])
def update(id):
   task = Task.query.get_or_404(id)

   if request.method == 'POST':
       task.name = request.form['name']

       try:
           db.session.commit()
           return redirect('/')
       except:
           return "There was a problem updating data."

   else:
       title = "Update Task"
       return render_template('update.html', title=title, task=task)

@app.route('/cron-job-reset')
def chron_job_reset():
    tasks = Task.query.order_by(Task.created_at).all()  
    #1. Delete all Todos
    for task in tasks:
        db.session.delete(task)
        db.session.commit()
    #2. Create two new default Todos
    name_one = "Todo 1"
    new_task_one = Task(name=name_one)
    db.session.add(new_task_one)
    db.session.commit()
    name_two = "Todo 2"
    new_task_two = Task(name=name_two)
    db.session.add(new_task_two)
    db.session.commit()
    tasks = [new_task_one, new_task_two]
    #. Re-render home page to show new todos
    return render_template("home.html", tasks=tasks)  

if __name__ == "__main__":
   app.run(debug=True)