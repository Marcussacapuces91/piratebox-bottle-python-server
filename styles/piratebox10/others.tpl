<!DOCTYPE html>
<html>
    <head>
    	<link rel="stylesheet" href="/style.css" />
    	<link rel="localization" href="/manifest.json" />
    	<title data-l10n-id="page_title">PirateBox - Share Freely</title>
    	<script src="/jquery.min.js"></script>
    	<script src="/scripts.js"></script>
    	<meta name="viewport" content="initial-scale=1.0, maximum-scale=1.0, user-scalable=no, width=device-width" />
    	<script src="/l20n.min.js"></script>
    </head>
    <body>
        <header id="header">
        	<div class="container">
        		<div id="logo">
        			<h1>
        				<a href="/" data-l10n-id="logo_title">
        					<img src="/piratebox-logo-horizontal-white.png" alt="PirateBox" title="PirateBox - Share Freely" />
        				</a>
        			</h1>
        		</div>
        		<div id="menu-icon"><img src="/menu.png" alt="Menu" /></div>
        		<nav id="top-nav">
        			<ul>
        				<li><a href="/" class="current" data-l10n-id="home_menu">Home</a></li>
% for item in topNav:
        				<li>{{!item}}</li>
% end
        				<li><a href="#about" data-l10n-id="about_menu">About</a></li>
        			</ul>
        		</nav>
        	</div>
        </header>

        <div class="container">
        	<div class="card">
{{!content}}
        	</div>
        </div>

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
    <body>
</html>