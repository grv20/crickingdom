# Getting Started with tutor

=>This project is created with django framework, properly contained in pipenv.
=>You can clone and install all the dependencies with requirements.txt file.
=>Templates Folder consists all the template being rendered out via different apps.
=>API is created, serialized and authenticated with help of Django REST Framework.
=>JSON Web Token(JWT) is used as for authentication.
=>APIs are only accessible when user is logged in and token is assigned to it.
=>Home page renders out data in orm of table. Also there is option to login and logout provided by REST default Auth.
=>Also added button in home page to redirect you to API, they are only accessible when you are logged in.
=>Django Admin site provides interface to add teacher, student or subjct.
=>Also you can register new user, by sending POST request to '/register' giving username, email, password and password2 as a JSON data.