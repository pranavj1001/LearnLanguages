<?php

	//The values are passed in the link.The values can be used in the usual format.
	//the method to pass the values in the link
	//eg: http://localhost/PHP/Get.php/?name=Dovah&password=lel&gender=male
	//print_r($_GET);
	//echo $_GET["gender"];


	//http://localhost/PHP/Get.php/?name=yo
	echo "Hi there ".$_GET["name"]."!";

	echo "<br><br>";

?>

	<p>What's your name?</p>

	<form>
		<input type="text" name="name">
		<input type="submit" value="Go!">
	</form>
