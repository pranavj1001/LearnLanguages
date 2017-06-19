<?php

	$family = array("Dovah" , "Computer" , "Z1" , "MiPad");

	$i = 0;
	//while structure. similar to javascript.
	while($i < 10) {
		echo $i."<br>";
		$i++;
	}
	echo "<br><br>";


	$i = 1;
	while ($i <= 10) {
		echo "5 x ".$i." = ".($i*5)."<br>";
		$i++;
	}
	echo "<br><br>";

	//traversing the array
	$i = 0;
	while ($i < sizeof($family)) {
		echo $family[$i]."<br>";
		$i++;
	}

?>
