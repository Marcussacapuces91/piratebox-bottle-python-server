<!DOCTYPE html>
<html>
<head>
	<link rel="stylesheet" href="style.css" />
	<link rel="localization" href="piratebox10/manifest.json" />
	<title data-l10n-id="page_title">PirateBox - Share Freely</title>
	<script src="jquery.min.js"></script>
	<script src="piratebox10/scripts.js"></script>
	<meta name="viewport" content="initial-scale=1.0, maximum-scale=1.0, user-scalable=no, width=device-width" />
	<script src="l20n.min.js"></script>
</head>
<body>

<header id="header">
	<div class="container">
		<div id="logo">
			<h1>
				<a href="/" data-l10n-id="logo_title">
					<img src="piratebox-logo-horizontal-white.png" alt="PirateBox" title="PirateBox - Share Freely" />
				</a>
			</h1>
		</div>
		<div id="menu-icon"><img src="menu.png" alt="Menu" /></div>
		<nav id="top-nav">
			<ul>
				<li><a href="/" class="current" data-l10n-id="home_menu">Home</a>
			
% for item in topNav:
				<li><a href="{{item['address']}}"\\
    % if 'class' in item:
 class="{{item['class']}}"\\
    % end
    % if 'id' in item:
 id="{{item['id']}}"\\
    % end
    % if 'style' in item:
 style="{{item['style']}}"\\
    % end
    % if 'title' in item:
 title="{{item['title']}}"\\
    % end
>{{!item['text']}}</a></li>
% end
				<li><a href="#about" data-l10n-id="about_menu">About</a>
			</ul>
		</nav>
	</div>
</header>

<section id="content">
	<div class="container">
        <div id="top">
            <div id="welcome" class="card" data-l10n-id="welcome_block">
                <h2>Welcome</h2>
                <p>Now, first of all, there is nothing illegal or scary going on 
                here. This is a social place where you can chat and share files 
                with people around you, <strong>anonymously</strong>! This is an 
                off-line network, specially designed and developed for 
                file-sharing and chat services. Staying off the grid is a 
                precaution to maintain your full anonymity. Please have fun, 
                chat with people, and feel free to share any files you may like.</p>
                <input id="thanks" class="button" type="submit" value="Thanks" />
            </div>
        </div>

        <div id="sidebar">
% for item in contents:	
    % if item['block'] == 'sidebar':   
		    <div\\
        % if 'id' in item:
 id="{{item['id']}}"\\
        % end
 class="card\\
        % if 'class' in item:
,{{item['class']}}\\
        % end
">
        % if 'title' in item:
			    <h2>{{item['title']}}</h2>
        % end
                {{!item['div']}}
            </div>
    %end        
%end	   
        </div>

        <div id="main">
% for item in contents:	
    % if item['block'] == 'main':   
		    <div\\
        % if 'id' in item:
 id="{{item['id']}}"\\
        % end
 class="card\\
        % if 'class' in item:
,{{item['class']}}\\
        % end
">
        % if 'title' in item:
			    <h2>{{item['title']}}</h2>
        % end
                {{!item['div']}}
            </div>
    %end        
%end	   
        </div>
	</div>
</section>

<footer id="about">
	<div class="container" data-l10n-id="footer_block">
        <p class="to-top"><a href="#header">Back to top</a></p>
        <h2>About PirateBox</h2>
        <p>Inspired by pirate radio and the free culture movment, PirateBox is a 
        self-contained mobile collaboration and file sharing device. PirateBox 
        utilizes Free, Libre and Open Source software (FLOSS) to create mobile 
        wireless file sharing networks where users can anonymously share images, 
        video, audio, documents, and other digital content.</p>
		<p>PirateBox is designed to be safe and secure. No logins are required 
        and no user data is logged. The system is purposely not connected to the 
        Internet in order to prevent tracking and preserve user privacy.</p>
		<p style="font-size: small">PirateBox is licensed under GPLv3.</p>
	</div>
</footer>

</body>
</html>