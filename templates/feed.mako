<%namespace name="page_template" file="parts/page_template.mako" import="render_page"/>
<%page_template:render_page load_asset="${load_asset}">
	<script>new PageController();</script>
	<ul id="left-menu" class="action-list no-select">
		<li>
			<a id="my-profile" class="action-item">
				<div class="avatar">
					<img src="https://lh3.googleusercontent.com/uFp_tsTJboUY7kue5XAsGA=s120" height="64" width="64" />
				</div>
				<p class="no-text-overflow"><strong>John Doe</strong></p>
				<p class="no-text-overflow">@johndoe</p>
			</a>
		</li>
		<li><a class="action-item">Update profile</a></li>
		<li><a class="action-item">Upload new photo</a></li>
		<li><a class="action-item">Log Out</a></li>
	</ul>
	<div id="header">
		<a id="menu-button" class="icon-button menu-toggle">
			<div class="bar one"></div>
			<div class="bar two"></div>
			<div class="bar three"></div>
		</a>
	</div>
	<div id="photo-box">
		<div id="background"></div>
		<div id="photo">
			<img src="http://www.wonderplugin.com/wp-content/plugins/wonderplugin-lightbox/images/demo-image2.jpg" />
			<p id="date">2014/10/25</p>
		</div>
		<div id="scroll-area">
			<div id="info">
				<ul id="photo-menu" class="action-list">
					<li><a class="action-item">Delete</a></li>
					<li><a class="action-item">Report image</a></li>
				</ul>
				<div class="summary">
					<a href="#" class="user-handle no-text-overflow">@johndoe</a>
					<div class="description no-text-overflow">Chicken Tikka Masala</div>
					<a id="photo-menu-button" class="icon-button menu-toggle dark">
						<div class="bar one"></div>
						<div class="bar two"></div>
						<div class="bar three"></div>
					</a>
					<a id="favourite-button" class="icon-button dark"></a>
					<p id="favourite-count">1.2K</p>
				</div>
				<div id="get-recipe">
					<p>Like what you see?</p>
					<button>Get the recipe!</button>
				</div>
				<div id="recipe">
					<p>Blah Blah Blah</p>
				</div>
			</div>
			<div class="avatar">
				<img src="https://lh3.googleusercontent.com/uFp_tsTJboUY7kue5XAsGA=s120" height="64" width="64" />
			</div>
		</div>
		<a id="close" class="icon-button close">
			<div class="bar one"></div>
			<div class="bar two"></div>
		</a>
	</div>
	<div id="page-content" class="no-select">
		<div id="feed-selector" class="select-row">
			<div class="option no-text-overflow"  data-value="popular">POPULAR</div>
			<div class="option no-text-overflow"  data-value="my-feed">MY FEED</div>
			<div class="underline"></div>
		</div>
		<div id="panel-area">
			% for x in range(10):
				<div class="panel" data-photo-id="${x}">
					<img class="thumb" src="http://www.wonderplugin.com/wp-content/plugins/wonderplugin-lightbox/images/demo-image2.jpg" />
					<div class="fader"></div>
					<p class="user no-text-overflow">@johndoe</p>
					<p class="stars no-text-overflow">10</p>
				</div>
			% endfor
		</div>
	</div>
</%page_template:render_page>