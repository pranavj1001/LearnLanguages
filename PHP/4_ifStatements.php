<?php

	//decalaring a variable.
	$user = "Dovah";

	//the if-else structure.
	//Hello.$user will be only printed if $user is checked with pranav not even Pranav is allowed.
	if($user == "Dovah"){
		echo "Hello ".$user;
	}else{
		echo "Who are You?";
	}
	echo "<br><br>";


	$age = 17;
	if($age >= 18){
		echo "You may proceed.....";
	}else{
		echo "You may not proceed.....";
	}
	echo "<br><br>";


	//if with AND,OR.
	//very similar to javascript.
	$age = 20;
	if($age >= 18 && $user == "pranav"){
		echo "You may proceed.....";
	}else{
		echo "You may not proceed.....";
	}
	echo "<br><br>";

?>
