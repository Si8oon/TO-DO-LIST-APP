from flask import Flask, request, render_template, redirect, url_for

app = Flask(__name__)
tasks = [] 

@app.route('/')
def index():
    return render_template("index.html", tasks=tasks)

@app.route('/add', methods=['POST'])
def add_task():
    if request.form['task']:
        tasks.append({'id': len(tasks)+1, 'name': request.form['task']})
    return redirect('/')

@app.route('/delete/<int:task_id>')
def delete_task(task_id):
    global tasks
    tasks = [task for task in tasks if task['id'] != task_id]
    return redirect(url_for('index'))

if __name__ == "__main__":
    app.run(debug=True)
