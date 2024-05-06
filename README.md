### DJANGO REST FRAMEWORK

We used django rest framework in this projets

## Making the folder and setting up Django Project in Virtual Environment

- 1.Make a new folder

```bash
mkdir myproject

```

- 2.Go to that folder

```bash
cd myproject
```

- 3.Make a Virtual Environment

```bash
python -m venv djangoenv
```

here `djangoenv` is the name of environment.

- 4. Activate the environment \
     In Linux/Unix system `source djangoenv/bin/activate`

In Windows using command prompt

```bash
djangoenv\Scripts\activate
```

If using git bash terminal you can execute `cd djangoenv` and then `. Scripts/activate`

if the environment is activated you can see `(djangoenv)` in the terminal \
Now go to project folder by executing `cd ..` only if you are inside environment folder use `ls` or `pwd` command to check your location

install django

```bash
pip install django
```

### Create Django Project

```bash
django-admin startproject testproject .
```

Here `testproject` is the name of django project and `.` tells to create the project in current folder i.e `myproject` \

Now you can see files and folder created

- `testproject`
- `manage.py`

You can run the development server using command `python manage.py runserver`
