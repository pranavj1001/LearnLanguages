<?php

	//Declaration of Array
	$myArray = array("Yo","This","is","Dovah");
	//Print Array. View Page Source to get a better view of the array.
	print_r($myArray);

	//like javascript we can also print individual elements of array in the following way.
	echo $myArray[1];

	//for leaving lines we can use break tags or old way of using the p tags.
	echo "<br><br>";


	//another way(Manually adding them) of making an array.
	$anotherArray[0] = "pizza";
	$anotherArray[1] = "pasta";
	$anotherArray[2] = "burger";
	//we can place value in any position.
	$anotherArray[5] = "paneer tikka";
	//the position can also be a string. also known as associative array.
	$anotherArray["myFavouriteFood"] = "idk Yet";
	print_r($anotherArray);
	echo "<br><br>";


	//example of associative array. Commonly used for key and value problems.
	//The latter one is the cleaner one for representing the array.
	//$thirdArray = array("France" => "French" , "USA" => "English" , "India" => "Hindi");
	$thirdArray = array(

		"France" => "French" ,
		"USA" => "English" ,
		"India" => "Hindi"

	);
	print_r($thirdArray);

	//printing the size of array.
	echo sizeof($thirdArray);
	echo "<br><br>";


	//a way to add another element at the last position of the non-associative array.
	$myArray[] = "Jain";
	//Remember changes to the myArray are done after printing it for the first time. therefore it wont be shown there.
	//to show the changes, print it again.
	print_r($myArray);
	echo "<br><br>";


	//for deleting a member, we use the unset.
	unset($thirdArray["France"]);
	print_r($thirdArray);
	echo sizeof($thirdArray);

?>
