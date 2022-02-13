<?php
function getClasses(PDO $dbh)
{
    $stmt = $dbh->query("SELECT distinct classe FROM qcms;");
    return $stmt->fetchAll(PDO::FETCH_ASSOC);
}

function getQcms(PDO $dbh, string $classe)
{
    $stmt = $dbh->prepare("SELECT * FROM qcms WHERE classe = :classe;");
    $stmt->execute([':classe' => $classe]);
    return $stmt->fetchAll(PDO::FETCH_ASSOC);
}

function getDates(PDO $dbh, int $qcm_id)
{
    $stmt = $dbh->prepare("SELECT distinct DATE(date_rep) as date_rep FROM answers WHERE qcm_id = :qcm_id;");
    $stmt->execute([':qcm_id' => $qcm_id]);
    return $stmt->fetchAll(PDO::FETCH_ASSOC);
}

function getAnswers(PDO $dbh, int $qcm_id, string $startDate, string $endDate)
{
    $stmt = $dbh->prepare("SELECT * FROM answers 
    WHERE qcm_id = :qcm_id AND 
          date_rep BETWEEN :startDate AND :endDate
    ORDER BY date_rep DESC;");
    $stmt->execute([
        ':qcm_id' => $qcm_id,
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
    if ($_SESSION['classe'] != $_POST['classe']) {
        $_SESSION['classe'] = $_POST['classe'];
        $classe = $_POST['classe'];
        unset($_SESSION['qcm_id']);
        unset($_SESSION['startDate']);
        unset($_SESSION['endDate']);
    } else if ($_SESSION['qcm_id'] != $_POST['qcm_id']) {
        $_SESSION['qcm_id'] = $_POST['qcm_id'];
        $qcm_id = $_POST['qcm_id'];
        unset($_SESSION['startDate']);
        unset($_SESSION['endDate']);
    } else if ($_SESSION['startDate'] != $_POST['start_date']) {
        $_SESSION['startDate'] = $_POST['start_date'];
        $startDate = $_POST['start_date'];
        unset($_SESSION['endDate']);
    } else if ($_SESSION['endDate'] != $_POST['end_date']) {
        $_SESSION['endDate'] = $_POST['end_date'];
        $endDate = $_POST['end_date'];
    }
}

function splitAnswer(string $answer)
{
    $i = 0;
    $n = strlen($answer);
    $answer = strtoupper($answer);
    $ans = [];
    while ($i < $n) {
        $subans = "";
        while ($i < $n && $answer[$i] >= "0" && $answer[$i] <= "9") {
            $subans .= $answer[$i];
            $i++;
        }
        while ($i < $n && $answer[$i] >= "A" && $answer[$i] <= "Z") {
            $subans .= $answer[$i];
            $i++;
        }
        $ans[] = $subans;
    }
    return $ans;
}

function getMarks($modelanswer, $useranswer)
{
    $ga = 0;
    $ba = 0;
    $good = [];
    foreach ($useranswer as $ans) {
        $is_good = in_array($ans, $modelanswer);
        if ($is_good) {
            $ga++;
        } else {
            $ba++;
        }
        $good[] = $is_good;
    }
    return [$ga, $ba, $good];
}

$classe = (isset($_SESSION['classe'])) ? $_SESSION['classe'] : reset($classes)['classe'];
$qcms = getQcms($dbh, $classe);
$qcm_id = (isset($_SESSION['qcm_id'])) ? $_SESSION['qcm_id'] : reset($qcms)['id'];
$dates = getDates($dbh, $qcm_id);
$startDate = (isset($_SESSION['startDate'])) ? $_SESSION['startDate'] : reset($dates)['date_rep'];
$endDate = (isset($_SESSION['endDate'])) ? $_SESSION['endDate'] : end($dates)['date_rep'];

$_SESSION['classe'] = $classe;
$_SESSION['qcm_id'] = $qcm_id;
$_SESSION['startDate'] = $startDate;
$_SESSION['endDate'] = $endDate;

$selected_qcm = [];
foreach ($qcms as $qcm) {
    if ($qcm['id'] == $qcm_id) {
        $selected_qcm = $qcm;
        break;
    }
}

$answers = getAnswers($dbh, $qcm_id, $startDate, $endDate);
/*
[id] => 12 
[qcm_id] => 1
[nom_prenom] => Mohamed Anis MANI 
[date_rep] => 2022-02-12 19:24:45 
[ip_addr] => 127.0.0.1 
[reponse] => 1A2A3A4A5A6A7A8A9A10A )
*/
?>
<form method="post">
    <div class="row">
        <div class="col-3">
            <label for="classes">Classes</label>
            <select name="classe" id="classes" class="form-control">
                <?php foreach ($classes as $cls) {
                    echo "<option" . (($classe == $cls['classe']) ? " selected" : "") . ">{$cls['classe']}</option>";
                } ?>
            </select>
        </div>
        <div class="col-3">
            <label for="qcm_ids">Titre</label>
            <select name="qcm_id" id="qcm_ids" class="form-control">
                <?php
                foreach ($qcms as $qcm) {
                    echo "<option value=\"{$qcm['id']}\"" . (($qcm_id == $qcm['id']) ? " selected" : "") . ">{$qcm['titre']}</option>";
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
$modelanswer = splitAnswer($selected_qcm['reponses']);

echo "<h2>{$selected_qcm['titre']}</h2>";
echo "<p>{$selected_qcm['description']}</p>";
echo "<p><strong>Classe :</strong> {$classe}</p>";
echo "<p><strong>Date :</strong> {$startDate} &rarr; {$endDate}</p>";
echo "<p><strong>Réponses :</strong> ";
foreach ($modelanswer as $idx => $ans) {
    echo "<span>$ans</span>";
    echo "/";
}
echo "</p>";
echo "<table class=\"table table-sm table-bordered table-striped border-dark align-middle\">";
echo "<tr>";
echo "<th>&nbsp;</th>";
echo "<th>Nom & Prénom</th>";
echo "<th width=\"100\">Date</th>";
echo "<th width=\"100\">Adr. IP</th>";
echo "<th>Réponse</th>";
echo "<th width=\"140\">Note</th>";
echo "</tr>";

foreach ($answers as $idx => $answer) {
    $useranswer = splitAnswer($answer['reponse']);
    $marks = getMarks($modelanswer, $useranswer);
    echo "<tr>";
    echo "<td>" . ($idx + 1) . "</td>";
    echo "<td>" . $answer['nom_prenom'] . "</td>";
    echo "<td>" . $answer['date_rep'] . "</td>";
    echo "<td>" . $answer['ip_addr'] . "</td>";
    echo "<td>";
    foreach ($useranswer as $idx => $ans) {
        if ($marks[2][$idx]) {
            echo "<span class=\"text-success\">$ans</span>";
        } else {
            echo "<span class=\"text-danger\"><strike>$ans</strike></span>";
        }
        echo "/";
    }    
    echo "</td>";
    echo "<td><small>{$marks[0]} - {$marks[1]} = " . ($marks[0] - $marks[1]) . "</small></td>";
    echo "</tr>";
}
echo "</table>";
