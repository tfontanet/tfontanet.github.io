<?php 
  $methode = "Inconnue";
  $nom = "Anonyme";
  $nsi = "et vous auriez mieux fait de choisir NSI ;-(";
  if (isset($_GET['nom'])) {
    $methode = "GET";
    $nom = $_GET['nom'];
    if ($_GET['nsi'] == "Yes") {$nsi = "et vous avez bien fait de choisir NSI ;-)";}
  } elseif (isset($_POST['nom'])) {
    $methode = "POST";
    $nom = $_POST['nom'];
    if ($_POST['nsi'] == "Yes") {$nsi = "et vous avez bien fait de choisir NSI ;-)";}
  }
?>
<!doctype html>
<html lang="fr">
    <title>Votre nom</title>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <style>
      body {background-color: #e8e8e8; font-family: sans-serif}
      div {margin: auto; max-width: 400px; background-color: #ffffff; padding: 30px}
      fieldset {background-color: #f8f8f8; padding: 15px; border: 3px solid #d4d4d4; border-radius: 10px}
    </style>
  </head>
  <body>
    <br><br>
    <div>
      <fieldset>
        <legend>Bonjour <?php echo $nom ?></legend>
        <p>Vous avez utilisé la méthode : <?php echo $methode ?></p>
        <p><?php echo "Il est ".date("H:i:s").", votre IP est ".$_SERVER['REMOTE_ADDR']; ?></p>
        <p><?php echo $nsi ?></p>
      </fieldset>
    </div>
    <br><br>
  </body>
</html>
