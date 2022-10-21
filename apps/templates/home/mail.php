<?php
if(isset($_POST["Submit"])){

$to = "letgis@br.ibm.com";
$subject = "Contact mail: CMPA Checklist Application";
$from = $_POST["email"];
$msg = $_POST["message"];
$headers = "From: $from";

mail($to,$subject,$msg,$headers);
echo "Email successfully sent.";
}
?>