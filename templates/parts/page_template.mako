<%def name="render_page(load_asset)">
	<!DOCTYPE html>
	<!--[if IE 9]><html class="ie9"><![endif]-->
	<!--[if lte IE 8]><html class="ie8"><![endif]-->
	<!-- <![if gte IE 10]> --><html><!-- <![endif]-->
		<head>
			<meta charset="utf-8" />
			<meta http-equiv="X-UA-Compatible" content="IE=edge" />
			<meta name="viewport" content="width=device-width, initial-scale=1.0, user-scalable=no" />
			<meta name="description" content="Feedie amateur cook" />
			<link rel="shortcut icon" href="${load_asset('pyramid-16x16.png')}" />

			<title>Feedie</title>
			<link href="${load_asset('css/style.css')}" rel="stylesheet" />
			<script src="${load_asset('js/jquery-1.11.0.min.js')}"></script>
			<script src="${load_asset('js/script.js')}"></script>

			<!--[if lt IE 9]>
				<script src="//oss.maxcdn.com/libs/html5shiv/3.7.0/html5shiv.js"></script>
				<script src="//oss.maxcdn.com/libs/respond.js/1.3.0/respond.min.js"></script>
			<![endif]-->
		</head>
		<body class="fixed-header" ontouchstart>${caller.body()}</body>
	</html>
</%def>