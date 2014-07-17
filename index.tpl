<!DOCTYPE html>
<html>
<head>
	<link rel="stylesheet" href="style.css" />
	<title>{{webTitle}}</title>
	<script src="jquery.min.js"></script>
	<script src="scripts.js"></script>
	<meta name="viewport" content="initial-scale=1.0, maximum-scale=1.0, user-scalable=no, width=device-width">
</head>
<body>

<header id="header">
	<div class="container">
		<div id="logo">
			<h1>
				<a href="/">
					<img src="piratebox-logo-horizontal-white.png" alt="PirateBox" title="{{iconTitle}}" />
				</a>
			</h1>
		</div>
		<div id="menu-icon"><img src="menu.png" alt="Menu" /></div>
		<nav id="top-nav">
			<ul>
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

<footer id="about">
	<div class="container">
	   {{!footer}}
	</div>
</footer>

</body>
</html>