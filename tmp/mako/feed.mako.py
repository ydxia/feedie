# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1414130289.889
_enable_loop = True
_template_filename = 'templates/feed.mako'
_template_uri = 'feed.mako'
_source_encoding = 'ascii'
_exports = []


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    ns = runtime.TemplateNamespace(u'page_template', context._clean_inheritance_tokens(), templateuri=u'parts/page_template.mako', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, u'page_template')] = ns

def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        _import_ns = {}
        _mako_get_namespace(context, u'page_template')._populate(_import_ns, [u'render_page'])
        load_asset = _import_ns.get('load_asset', context.get('load_asset', UNDEFINED))
        page_template = _mako_get_namespace(context, 'page_template')
        __M_writer = context.writer()
        __M_writer(u'\n')
        def ccall(caller):
            def body():
                range = _import_ns.get('range', context.get('range', UNDEFINED))
                __M_writer = context.writer()
                __M_writer(u'\n\t<script>new PageController();</script>\n\t<ul id="left-menu" class="action-list no-select">\n\t\t<li>\n\t\t\t<a id="my-profile" class="action-item">\n\t\t\t\t<div class="avatar">\n\t\t\t\t\t<img src="https://lh3.googleusercontent.com/uFp_tsTJboUY7kue5XAsGA=s120" height="64" width="64" />\n\t\t\t\t</div>\n\t\t\t\t<p class="no-text-overflow"><strong>John Doe</strong></p>\n\t\t\t\t<p class="no-text-overflow">@johndoe</p>\n\t\t\t</a>\n\t\t</li>\n\t\t<li><a class="action-item">Update profile</a></li>\n\t\t<li><a class="action-item">Upload new photo</a></li>\n\t\t<li><a class="action-item">Log Out</a></li>\n\t</ul>\n\t<div id="header">\n\t\t<a id="menu-button" class="icon-button menu-toggle">\n\t\t\t<div class="bar one"></div>\n\t\t\t<div class="bar two"></div>\n\t\t\t<div class="bar three"></div>\n\t\t</a>\n\t</div>\n\t<div id="photo-box">\n\t\t<div id="background"></div>\n\t\t<div id="photo">\n\t\t\t<img src="http://www.wonderplugin.com/wp-content/plugins/wonderplugin-lightbox/images/demo-image2.jpg" />\n\t\t\t<p id="date">2014/10/25</p>\n\t\t</div>\n\t\t<div id="scroll-area">\n\t\t\t<div id="info">\n\t\t\t\t<ul id="photo-menu" class="action-list">\n\t\t\t\t\t<li><a class="action-item">Delete</a></li>\n\t\t\t\t\t<li><a class="action-item">Report image</a></li>\n\t\t\t\t</ul>\n\t\t\t\t<div class="summary">\n\t\t\t\t\t<a href="#" class="user-handle no-text-overflow">@johndoe</a>\n\t\t\t\t\t<div class="description no-text-overflow">Chicken Tikka Masala</div>\n\t\t\t\t\t<a id="photo-menu-button" class="icon-button menu-toggle dark">\n\t\t\t\t\t\t<div class="bar one"></div>\n\t\t\t\t\t\t<div class="bar two"></div>\n\t\t\t\t\t\t<div class="bar three"></div>\n\t\t\t\t\t</a>\n\t\t\t\t\t<a id="favourite-button" class="icon-button dark"></a>\n\t\t\t\t\t<p id="favourite-count">1.2K</p>\n\t\t\t\t</div>\n\t\t\t\t<div id="get-recipe">\n\t\t\t\t\t<p>Like what you see?</p>\n\t\t\t\t\t<button>Get the recipe!</button>\n\t\t\t\t</div>\n\t\t\t\t<div id="recipe">\n\t\t\t\t\t<p>Blah Blah Blah</p>\n\t\t\t\t</div>\n\t\t\t</div>\n\t\t\t<div class="avatar">\n\t\t\t\t<img src="https://lh3.googleusercontent.com/uFp_tsTJboUY7kue5XAsGA=s120" height="64" width="64" />\n\t\t\t</div>\n\t\t</div>\n\t\t<a id="close" class="icon-button close">\n\t\t\t<div class="bar one"></div>\n\t\t\t<div class="bar two"></div>\n\t\t</a>\n\t</div>\n\t<div id="page-content" class="no-select">\n\t\t<div id="feed-selector" class="select-row">\n\t\t\t<div class="option no-text-overflow"  data-value="popular">POPULAR</div>\n\t\t\t<div class="option no-text-overflow"  data-value="my-feed">MY FEED</div>\n\t\t\t<div class="underline"></div>\n\t\t</div>\n\t\t<div id="panel-area">\n')
                for x in range(10):
                    __M_writer(u'\t\t\t\t<div class="panel" data-photo-id="')
                    __M_writer(unicode(x))
                    __M_writer(u'">\n\t\t\t\t\t<img class="thumb" src="http://www.wonderplugin.com/wp-content/plugins/wonderplugin-lightbox/images/demo-image2.jpg" />\n\t\t\t\t\t<div class="fader"></div>\n\t\t\t\t\t<p class="user no-text-overflow">@johndoe</p>\n\t\t\t\t\t<p class="stars no-text-overflow">10</p>\n\t\t\t\t</div>\n')
                __M_writer(u'\t\t</div>\n\t</div>\n')
                return ''
            return [body]
        context.caller_stack.nextcaller = runtime.Namespace('caller', context, callables=ccall(__M_caller))
        try:
            __M_writer(unicode(page_template.render_page(load_asset=(load_asset))))
        finally:
            context.caller_stack.nextcaller = None
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "ascii", "line_map": {"34": 1, "39": 2, "40": 72, "41": 73, "42": 73, "43": 73, "44": 80, "49": 2, "22": 1, "57": 49, "25": 0}, "uri": "feed.mako", "filename": "templates/feed.mako"}
__M_END_METADATA
"""
