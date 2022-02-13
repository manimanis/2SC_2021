<?php
require_once 'dbconnect.php';

$_POST['REMOTE_ADDR'] = $_SERVER['REMOTE_ADDR'];
$_POST['AT_TIME'] = date("Y-m-d H:i:s");
/*
nom_prenom	"Mohamed Anis MANI"
questions_count	"10"
classe	"2TI"
description	"Structures itératives"
q1	"1A"
q2	"2A"
q3	"3A"
q4	"4A"
q5	"5B"
q6	"6C"
q7	"7D"
q8	"8C"
q9	"9B"
q10	"10B"
REMOTE_ADDR	"127.0.0.1"
AT_TIME	"2022-02-12 17:55:55"
*/
$fields = ["nom_prenom", "questions_count", "qcm_id", "REMOTE_ADDR", "AT_TIME"];
$errors = [];
foreach ($fields as $field) {
    if (!isset($_POST[$field])) {
        $errors[] = "'$field' est requis.";
    }
}
$reponse = "";
for ($i = 1; $i <= intval($_POST['questions_count']); $i++) {
    if (!isset($_POST["q{$i}"])) {
        $errors[] = "La réponse à la question q{$i} est requise.";
    } else {
        $reponse .= $_POST["q{$i}"];
    }
}
try {
    $dbh = new PDO("mysql:dbname={$base};host=$host", $user, $pass);
}
catch (PDOException $e) {
    $errors[] = "Connexion impossible : " . $e->getMessage();
}
if (count($errors)) {
    echo json_encode(["isok" => false, "errors" => $errors]);
    exit();
}

$stmt = $dbh->prepare("INSERT INTO answers (qcm_id, nom_prenom, date_rep, ip_addr, reponse) 
                       VALUES (:qcm_id, :nom_prenom, :date_rep, :ip_addr, :reponse)");
$data = [
    ':qcm_id'=> $_POST['qcm_id'],
    ':nom_prenom' => $_POST['nom_prenom'],
    ':date_rep' => $_POST['AT_TIME'],
    ':ip_addr' => $_POST['REMOTE_ADDR'],
    ':reponse' => $reponse
];

if (!$stmt->execute($data)) {
    $errors[] = "La réponse n'a pas été enregistrée : ".$stmt->errorInfo()[2];
    echo json_encode(["isok" => false, "errors" => $errors]);
    exit();
} else {
    echo json_encode(["isok" => true]);
}
