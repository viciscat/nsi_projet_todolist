<!doctype html>
<html lang="fr">
<head>
    <!-- Required meta tags -->
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">

    <!-- Bootstrap CSS -->
    <link rel="stylesheet" href="Base.css">
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css" integrity="sha384-Vkoo8x4CGsO3+Hhxv8T/Q5PaXtkKtu6ug5TOeNV6gBiFeWPGFN9MuhOf23Q9Ifjh" crossorigin="anonymous">

    <title>ToDoList</title>
</head>
<body>
    <style>
    body {background-color : powderblue;}
    </style>
    <!-- Barre de navigation -->
    <nav class="navbar navbar-expand-lg navbar-dark bg-dark">
        <a class="navbar-brand" href="#">{ ToDoList }</a>
        <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarsExampleDefault" aria-controls="navbarsExampleDefault" aria-expanded="false" aria-label="Toggle navigation">
            <span class="navbar-toggler-icon"></span>
        </button>
        <div class="collapse navbar-collapse" id="navbarsExampleDefault">
            <ul class="navbar-nav mr-auto">
                <li class="nav-item">
                    <a class="nav-link" href="#">Tâches</a>
                </li>
                <li class="nav-item">
                    <a class="nav-link" href="#">Catégories</a>
                </li>
                <li class="nav-item">
                    <a class="nav-link" href="#">Priorités</a>
                </li>
                <li class="nav-item">
                    <a class="nav-link" href="#">États</a>
                </li>
                <li class="nav-item">
                    <a class="nav-link" href="#">Statistiques</a>
                </li>
                <li class="nav-item">
                    <a class="nav-link" href="#">A propos</a>
                </li>

            </ul>
        </div>
        <div>
            <p><input type="button"> </p>
        </div>
    </nav>

    <!-- Zone centrale de la page -->
    <div class="container">

        <!-- Message(s) de notification (si il y en a) -->
        {% with messages = get_flashed_messages() %}
            {% if messages %}
                {% for message in messages %}
                    <input type="color" id="message" name="message" value="FFFFFFF">
                        <div class="alert alert-secondary" role="alert">
                            <CENTER>{{ message }}</CENTER>
                        </div>
                {% endfor %}
            {% endif %}
        {% endwith %}

        <!-- Bloc de contenu géré par les pages héritant de cette page "mère" -->
        <br />
        {% block contenu %}
        {% endblock %}

    </div><!-- /.container -->

    <!-- Chargement des fichier Javascript de Bootstrap à la fin pour ne pas retarder la page -->
    <script src="https://code.jquery.com/jquery-3.4.1.slim.min.js" integrity="sha384-J6qa4849blE2+poT4WnyKhv5vZF5SrPo0iEjwBvKU7imGFAV0wwj1yYfoRSJoZ+n" crossorigin="anonymous"></script>
    <script src="https://cdn.jsdelivr.net/npm/popper.js@1.16.0/dist/umd/popper.min.js" integrity="sha384-Q6E9RHvbIyZFJoft+2mJbHaEWldlvI9IOYy5n3zV9zzTtmI3UksdQRVvoxMfooAo" crossorigin="anonymous"></script>
    <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/js/bootstrap.min.js" integrity="sha384-wfSDF2E50Y2D1uUdj0O3uMBJnjuUD4Ih7YwaYd1iqfktj0Uod8GCExl3Og8ifwB6" crossorigin="anonymous"></script>

</body>
</html>