<!DOCTYPE html>
<html>
<head>
	<link rel="stylesheet" href="style.css" />
	<link rel="localization" href="piratebox10/manifest.json" />
	<title data-l10n-id="page_title">PirateBox - Share Freely</title>
	<script src="jquery.min.js"></script>
	<script src="scripts.js"></script>
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
% for item in contents:	
    % if item['block'] == 'top':   
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

<footer id="about" data-l10n-id="footer">
	<div class="container">
        <p class="to-top"><a href="#header">Back to top</a></p>
        <h2>{{footerTitle}}</h2>
        {{!footerContent}}
	</div>
</footer>

</body>
</html>