import os


def create_folder_structure():
    folders = [
        'templates',
        'templates/auth',
        'templates/cattle',
        'static',
        'static/css',
        'static/js',
        'static/images'
    ]

    for folder in folders:
        os.makedirs(folder, exist_ok=True)
        print(f'Created folder: {folder}')

    files = {
 
        'templates/base.html': '''
<!DOCTYPE html>
<html>
<head>
    <title>Cattle Manager</title>
    <link rel="stylesheet" href="{{ url_for('static', filename='css/style.css') }}">
</head>
<body>
    <header>
        <!-- Header content goes here -->
    </header>
    
    <main>
        {% block content %}
        {% endblock %}
    </main>
    
    <footer>
        <!-- Footer content goes here -->
    </footer>

    <script src="{{ url_for('static', filename='js/main.js') }}"></script>
</body>
</html>
''',
        'templates/home.html': '''
{% extends 'base.html' %}

{% block content %}
<h1>Welcome to the Cattle Manager App</h1>
<p>This is the home page.</p>
{% endblock %}
''',
        'templates/auth/login.html': '''
{% extends 'base.html' %}

{% block content %}
<h1>Login</h1>
<form>
    <!-- Login form goes here -->
</form>
{% endblock %}
''',
        'templates/cattle/index.html': '''
{% extends 'base.html' %}

{% block content %}
<h1>Cattle List</h1>
<ul>
    {% for cattle in cattle_list %}
    <li>{{ cattle.name }}</li>
    {% endfor %}
</ul>
{% endblock %}
''',
        'templates/cattle/details.html': '''
{% extends 'base.html' %}

{% block content %}
<h1>Cattle Details</h1>
<p>Name: {{ cattle.name }}</p>
<p>Age: {{ cattle.age }}</p>
<p>Breed: {{ cattle.breed }}</p>
<!-- More cattle details here -->
{% endblock %}
'''
        # Add more files and their content as needed
    }

    for file, content in files.items():
        with open(file, 'w') as f:
            f.write(content)
        print(f'Created file: {file}')


if __name__ == '__main__':
    create_folder_structure()
