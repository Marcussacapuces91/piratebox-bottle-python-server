<html>
    <head>
    	<meta http-equiv='cache-control' content='no-cache' />
    	<meta name='GENERATOR' content='ShoutBox plugin' />
    	<title>Shout-Out Data</title>
    </head>
    <body>
% for line in reversed(chat):    
    	<div class='message'>
    		<date>{{line[0].strftime("%X")}}</date>
    		<name>{{line[1]}}:</name>
    		<data class='{{line[3]}}'>{{line[2]}}</data>
    	</div>
% end
    </body>
</html>