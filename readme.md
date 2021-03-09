# Flask Tailwind Todo App

This is a Todo Application written with Flask (Python). It uses SQLite and SQLAlchemy.

In the past I have only used Python for scripting so I wanted to try building a web application with it. Django seemed like overkill for a small web app so I tried out Flask.

I also am using this project to experiment with Tailwind CSS. 


<br/>

## Hosted Project:

The hosted project is at: https://todo-flask-tailwindcss.herokuapp.com/

<br/>

## Cron Job:

I haven't added any authentication to this application yet. It is really just an experiment to get my feet wet with Flask and using Python for web apps. 

To limit the risk of tons of todos adding up in the UI and DB, I created a cron job that runs on [cron-jobs.org] every 5 minutes to reset the Todos. 

## Complete Stack:

Flask 

Python

Tailwind CSS

HTML

SQLite

SQLAlchemy

Heroku

Cron-jobs.org

<br/>

## To Run:  

```
git clone https://github.com/mwolfhoffman/flask_tailwind_todo_app.git

pip install

python app.py -- setup

pthon app.py
```

This will run the application at http://localhost:5000