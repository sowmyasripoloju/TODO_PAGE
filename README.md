📝 Django To-Do Application

A simple and user-friendly To-Do List web application built using Django.
The application allows users to add and delete tasks, with real-time feedback using Django’s messaging framework.

📌 Features

Add new to-do items using a form

View tasks sorted by most recent date

Delete existing tasks

User-friendly success and error messages

Clean MVC (Model–View–Template) architecture

Secure form handling using Django Forms and ORM

🛠️ Tech Stack

Backend: Python, Django

Frontend: HTML, CSS, Bootstrap

Database: SQLite (default Django database)

Tools & Concepts:

Django ORM

Django Forms

Messages Framework

Virtual Environment (venv)

📂 Project Structure (Relevant Files)
todo_site/
│
├── todo/
│   ├── views.py        # Application views
│   ├── models.py      # Todo model
│   ├── forms.py       # TodoForm
│   ├── urls.py        # App routing
│   └── templates/
│       └── todo/
│           └── index.html
│
├── manage.py
└── requirements.txt

⚙️ How the Application Works
1. Display To-Do Items

Fetches all to-do items from the database

Orders tasks by latest date first

2. Add New Task

Accepts user input via TodoForm

Validates and saves data using Django ORM

Displays success message after submission

3. Remove Task

Deletes task by ID

Handles errors if task does not exist

Shows appropriate feedback messages

🚀 Setup Instructions
1. Clone the Repository
git clone <repository-url>
cd todo_site

2. Create & Activate Virtual Environment

Windows

python -m venv myenv
myenv\Scripts\activate


macOS / Linux

python3 -m venv myenv
source myenv/bin/activate

3. Install Dependencies
pip install django
pip install django-crispy-forms


(Optional if Bootstrap is used)

pip install crispy-bootstrap4

4. Apply Migrations
python manage.py makemigrations
python manage.py migrate

5. Run the Server
python manage.py runserver


Visit:

http://127.0.0.1:8000/

🧠 Key Concepts Demonstrated

MVC architecture in Django

Form validation and secure data handling

CRUD operations using Django ORM

Error handling using try–except

Agile-style iterative development

📌 Sample Code (views.py)
def index(request):
    item_list = Todo.objects.order_by("-date")
    form = TodoForm()

    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Item added successfully!')
            return redirect('todo')

    page = {
        'forms': form,
        'list': item_list,
        'title': 'TODO LIST',
    }
    return render(request, 'todo/index.html', page)

🎯 Future Enhancements

User authentication

Task update/edit feature

Task completion status

Deployment on cloud (AWS / GCP)

👤 Author

Poloju Sowmya Sri
Computer Science Graduate
LinkedIn: https://linkedin.com/in/poloju-sowmya-sri
