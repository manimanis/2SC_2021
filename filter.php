<?php
session_start();
?>
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>QCM Module n°4</title>
    <link rel="stylesheet" href="resources/css/bootstrap.min.css">
    <link rel="stylesheet" href="resources/css/default.css">
    <link rel="stylesheet" href="resources/css/style.css">
</head>

<body>
    <aside>
        <nav class="navbar navbar-expand-xl navbar-dark bg-dark">
            <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#aside_navbar" aria-controls="navbarNavDropdown" aria-expanded="false" aria-label="Toggle navigation">
                <span class="navbar-toggler-icon"></span> Menu
            </button>
            <div class="collapse navbar-collapse" id="aside_navbar"></div>
        </nav>
    </aside>
    <main class="container my-4">
        <h1></h1>

        <?php
        require_once 'dbconnect.php';

        if ($_SERVER['REMOTE_ADDR'] != "127.0.0.1") {
            echo "Non autorisé!";
        } else {
            require_once 'filterrequire.php';
        }
        ?>
    </main>
    <footer class="d-print-none bg-dark text-white p-2">
        <div class="text-center">Page créée avec ♥ par Mohamed Anis MANI</div>
        <div class="text-center small">Année scolaire : 2021/2022</div>
    </footer>
    <script src="resources/js/jquery.min.js"></script>
    <script src="resources/js/bootstrap.min.js"></script>
    <script src="resources/js/highlight.pack.js"></script>
    <script src="resources/js/hljs.algorithm.js"></script>
    <script src="resources/js/clipboard.min.js"></script>
    <script src="resources/js/pages.js"></script>
    <script src="resources/js/savecontent.js"></script>
    <script src="resources/js/vue.min.js"></script>
</body>

</html>