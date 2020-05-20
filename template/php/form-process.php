<?php
$name = $_POST['name'];
$email = $_POST['email'];
$message = $_POST['message'];
$formcontent=" From: $name \n Email $email \n Message: $message";
$recipient = "yourmail@hostlab.com";
$subject = "Contact Form";
$mailheader = "From: $email \r\n";
mail($recipient, $subject, $formcontent, $mailheader) or die("Error!");
echo "<div style='    font-size: 22px; text-align: center; position: relative; font-family: sans-serif; top: 50%; transform: translateY(-50%);'> Thank You!" . " -" . 
"<a href='../contact.html' style='text-decoration:none; color:green; font-size:22px; font-family: sans-serif;'> Return Contact Page</a></div>";
?>