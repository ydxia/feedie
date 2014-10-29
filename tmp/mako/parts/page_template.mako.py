# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1414130289.961
_enable_loop = True
_template_filename = u'templates/parts/page_template.mako'
_template_uri = u'parts/page_template.mako'
_source_encoding = 'ascii'
_exports = ['render_page']


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        __M_writer = context.writer()
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_render_page(context,load_asset):
    __M_caller = context.caller_stack._push_frame()
    try:
        caller = context.get('caller', UNDEFINED)
        __M_writer = context.writer()
        __M_writer(u'\r\n\t<!DOCTYPE html>\r\n\t<!--[if IE 9]><html class="ie9"><![endif]-->\r\n\t<!--[if lte IE 8]><html class="ie8"><![endif]-->\r\n\t<!-- <![if gte IE 10]> --><html><!-- <![endif]-->\r\n\t\t<head>\r\n\t\t\t<meta charset="utf-8" />\r\n\t\t\t<meta http-equiv="X-UA-Compatible" content="IE=edge" />\r\n\t\t\t<meta name="viewport" content="width=device-width, initial-scale=1.0, user-scalable=no" />\r\n\t\t\t<meta name="description" content="Feedie amateur cook" />\r\n\t\t\t<link rel="shortcut icon" href="')
        __M_writer(unicode(load_asset('pyramid-16x16.png')))
        __M_writer(u'" />\r\n\r\n\t\t\t<title>Feedie</title>\r\n\t\t\t<link href="')
        __M_writer(unicode(load_asset('css/style.css')))
        __M_writer(u'" rel="stylesheet" />\r\n\t\t\t<script src="')
        __M_writer(unicode(load_asset('js/jquery-1.11.0.min.js')))
        __M_writer(u'"></script>\r\n\t\t\t<script src="')
        __M_writer(unicode(load_asset('js/script.js')))
        __M_writer(u'"></script>\r\n\r\n\t\t\t<!--[if lt IE 9]>\r\n\t\t\t\t<script src="//oss.maxcdn.com/libs/html5shiv/3.7.0/html5shiv.js"></script>\r\n\t\t\t\t<script src="//oss.maxcdn.com/libs/respond.js/1.3.0/respond.min.js"></script>\r\n\t\t\t<![endif]-->\r\n\t\t</head>\r\n\t\t<body class="fixed-header" ontouchstart>')
        __M_writer(unicode(caller.body()))
        __M_writer(u'</body>\r\n\t</html>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "ascii", "line_map": {"32": 11, "33": 14, "34": 14, "35": 15, "36": 15, "37": 16, "38": 16, "39": 23, "40": 23, "46": 40, "15": 0, "25": 1, "30": 1, "31": 11}, "uri": "parts/page_template.mako", "filename": "templates/parts/page_template.mako"}
__M_END_METADATA
"""
