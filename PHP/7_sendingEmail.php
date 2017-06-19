<?php

	$emailTo = "receiver@email.com";
	$subject = "Sending this message through php code";
	$body = "I hope it works!";
	$headers = "From: sender@eail.com";

	if(mail($emailTo, $subject, $body, $headers)){
		echo "The E-mail was sent successfully";
	}else{
		echo "The E-mail could not be sent";
	}

?>
