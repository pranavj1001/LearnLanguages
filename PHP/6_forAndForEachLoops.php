<?php

	$family = array("Dovah" , "Computer" , "Z1" , "MiPad");

	//similar to javascript.
	for($i = 0; $i < 10; $i++){
		echo $i.".hey there!<br>";
	}
	echo "<br><br>";

	//basic for-loop for traversing the array
	for($i = 0; $i < sizeof($family); $i++){
		echo $family[$i]."<br>";
	}
	echo "<br><br>";


	//foreach loop structure
	foreach ($family as $key => $value) {
		//Appending Jain
		$family[$key] = $value." Witcher";
		//Note: Here Jain will not be printed as the value is set to original value, and not the new appended one.
		echo "Array Item = ".$key." is ".$value.".<br>";
	}
	echo "<br><br>";


	print_r($family);
?>
