if (top.frames.length != 0)
{
  top.location.href = window.location.href;
}

function avertissement()
{
  var message = "Il y a beaucoup de mauvaises façons d'utiliser ce corrigé :\n";
  message +=    "  - le parcourir sans même avoir fait l'exercice pour voir \"si on aurait su faire\".\n";
  message +=    "  - le consulter dès que l'on commence à sécher...\n\n";
  message +=    "Il y a une seule bonne façon de l'utiliser :\n";
  message +=    "  - faire l'exercice en entier sans regarder le corrigé\n";
  message +=    "    et en rédigeant complètement la solution,\n";
  message +=    "    puis, à la fin seulement, comparer avec le corrigé !";
  alert(message);
}

function sessionAplusix()
{
  var numerosession = prompt("Quel est le numéro de la session Aplusix que vous voulez revoir ?", "");
  if (numerosession != null && parseInt(numerosession) && !isNaN(numerosession))
  {
    document.location.href="http://epsilon-publi.net/_programs/apx_get_trace_html.php?lang=fr&IdSession="+parseInt(numerosession);
  }
}
