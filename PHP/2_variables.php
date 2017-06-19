<?php

	//Declaration of variable
	$name = "Dovah";

	//printing the variable
	//p tag is to print this in one and the start one on a new line.
	echo "<p>My Name is $name </p>";

	$string1 = "<p>This is String 1</p>";
	$string2 = "<p>This is String 2</p>";

	//Unlike in javascript where '+' sign is used for concatenation.
	//Here in php '.' is used for concatenation.
	echo $string1." ".$string2;

	//sample calculation problem
	$myNumber = 45;
	$calculation = $myNumber + 3244 / 213;
	echo "The result of the calculation is ".$calculation;

	//boolean variables
	//on the browser it will be printed 1 if the value is true.
	//on the browser nothing or 0 will be printed  if the value is false.
	$myBool = true;
	echo "<p>This statement is true? ".$myBool."</p>";

	//another fancy way of calling variable name
	//this way of using '$$' calls the variable whose name is stored in typed variable name.
	$variableName = "name";
	echo "<p>".$$variableName."</p>";

?>
