<?php
function getClasses(PDO $dbh)
{
    $stmt = $dbh->query("SELECT distinct classe FROM answers;");
    return $stmt->fetchAll(PDO::FETCH_ASSOC);
}

function getTitres(PDO $dbh, string $classe)
{
    $stmt = $dbh->prepare("SELECT distinct titre FROM answers WHERE classe = :classe;");
    $stmt->execute([':classe' => $classe]);
    return $stmt->fetchAll(PDO::FETCH_ASSOC);
}

function getDates(PDO $dbh, string $classe, string $titre)
{
    $stmt = $dbh->prepare("SELECT distinct DATE(date_rep) as date_rep FROM answers WHERE classe = :classe AND titre = :titre;");
    $stmt->execute([':classe' => $classe, ":titre" => $titre]);
    return $stmt->fetchAll(PDO::FETCH_ASSOC);
}

function getAnswers(PDO $dbh, string $classe, string $titre, string $startDate, string $endDate)
{
    $stmt = $dbh->prepare("SELECT * FROM answers 
    WHERE classe = :classe AND 
          titre = :titre AND 
          date_rep BETWEEN :startDate AND :endDate
    ORDER BY date_rep DESC;");
    $stmt->execute([
        ':classe' => $classe,
        ":titre" => $titre,
        ':startDate' => "$startDate 00:00:00",
        ':endDate' => "$endDate 23:59:59"
    ]);
    return $stmt->fetchAll(PDO::FETCH_ASSOC);
}

$errors = [];
try {
    $dbh = new PDO("mysql:dbname={$base};host=$host", $user, $pass);
} catch (PDOException $e) {
    $errors[] = "Connexion impossible : " . $e->getMessage();
}
if (count($errors)) {
    echo json_encode(["isok" => false, "errors" => $errors]);
    exit();
}

$classes = getClasses($dbh);
if (isset($_POST['classe'])) {
    if ($_SESSION['titre'] != $_POST['titre']) {
        $_SESSION['titre'] = $_POST['titre'];
        $titre = $_POST['titre'];
        unset($_SESSION['classe']);
        unset($_SESSION['startDate']);
        unset($_SESSION['endDate']);
    }
    else if ($_SESSION['classe'] != $_POST['classe']) {
        $_SESSION['classe'] = $_POST['classe'];
        $classe = $_POST['classe'];        
        unset($_SESSION['startDate']);
        unset($_SESSION['endDate']);
    }
    else if ($_SESSION['startDate'] != $_POST['start_date']) {
        $_SESSION['startDate'] = $_POST['start_date'];
        $startDate = $_POST['start_date'];
        unset($_SESSION['endDate']);
    } else if ($_SESSION['endDate'] != $_POST['end_date']) {
        $_SESSION['endDate'] = $_POST['end_date'];
        $endDate = $_POST['end_date'];
    }
}

$classe = (isset($_SESSION['classe'])) ? $_SESSION['classe'] : reset($classes)['classe'];
$titres = getTitres($dbh, $classe);
$titre = (isset($_SESSION['titre'])) ? $_SESSION['titre'] : reset($titres)['titre'];
$dates = getDates($dbh, $classe, $titre);
$startDate = (isset($_SESSION['startDate'])) ? $_SESSION['startDate'] : reset($dates)['date_rep'];
$endDate = (isset($_SESSION['endDate'])) ? $_SESSION['endDate'] : end($dates)['date_rep'];

$_SESSION['classe'] = $classe;
$_SESSION['titre'] = $titre;
$_SESSION['startDate'] = $startDate;
$_SESSION['endDate'] = $endDate;


$answers = getAnswers($dbh, $classe, $titre, $startDate, $endDate);
/*
[id] => 12 
[classe] => 2TI 
[titre] => Structures itératives 
[description] => QCM Structures itératives 
[nbr_questions] => 10 
[nom_prenom] => Mohamed Anis MANI 
[date_rep] => 2022-02-12 19:24:45 
[ip_addr] => 127.0.0.1 
[reponse] => 1A2A3A4A5A6A7A8A9A10A )
*/
?>
<form method="post">
    <div class="row">
        <div class="col-3">
            <label for="titres">Titre</label>
            <select name="titre" id="titres" class="form-control">
                <?php foreach ($titres as $tit) {
                    echo "<option" . (($titre == $tit['titre']) ? " selected" : "") . ">{$tit['titre']}</option>";
                } ?>
            </select>
        </div>
        <div class="col-3">
            <label for="classes">Classes</label>
            <select name="classe" id="classes" class="form-control">
                <?php foreach ($classes as $cls) {
                    echo "<option" . (($classe == $cls['classe']) ? " selected" : "") . ">{$cls['classe']}</option>";
                } ?>
            </select>
        </div>
        <div class="col-3">
            <label for="start-date">Date début</label>
            <select name="start_date" id="start-date" class="form-control">
                <?php foreach ($dates as $dt) {
                    echo "<option" . (($startDate == $dt['date_rep']) ? " selected" : "") . ">{$dt['date_rep']}</option>";
                } ?>
            </select>
        </div>
        <div class="col-3">
            <label for="end-date">Date finale</label>
            <select name="end_date" id="end-date" class="form-control">
                <?php foreach ($dates as $dt) {
                    echo "<option" . (($endDate == $dt['date_rep']) ? " selected" : "") . ">{$dt['date_rep']}</option>";
                } ?>
            </select>
        </div>
        <div class="col-3 my-2"><button class="btn btn-secondary">Modifier</button></div>
    </div>
</form>
<?php
echo "<h2>{$titre}</h2>";
echo "<p><strong>Classe :</strong> {$classe}</p>";
echo "<p><strong>Date :</strong> {$startDate} &rarr; {$endDate}</p>";

echo "<table class=\"table table-sm table-bordered border-dark\">";
echo "<tr>";
echo "<th>&nbsp;</th>";
echo "<th>Nom & Prénom</th>";
echo "<th>Date réponse</th>";
echo "<th>Adresse IP</th>";
echo "<th>Réponse</th>";
echo "</tr>";
foreach ($answers as $idx => $answer) {
    echo "<tr>";
    echo "<td>" . ($idx + 1) . "</td>";
    echo "<td>" . $answer['nom_prenom'] . "</td>";
    echo "<td>" . $answer['date_rep'] . "</td>";
    echo "<td>" . $answer['ip_addr'] . "</td>";
    echo "<td>" . $answer['reponse'] . "</td>";
    echo "</tr>";
}
echo "</table>";
