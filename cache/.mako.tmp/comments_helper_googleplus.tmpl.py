# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1495191402.3514755
_enable_loop = True
_template_filename = '/home/ali/MyPython3/lib/python3.5/site-packages/nikola/data/themes/base/templates/comments_helper_googleplus.tmpl'
_template_uri = 'comments_helper_googleplus.tmpl'
_source_encoding = 'utf-8'
_exports = ['comment_form', 'comment_link_script', 'comment_link']


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        __M_writer = context.writer()
        __M_writer('\n\n')
        __M_writer('\n\n')
        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_comment_form(context,url,title,identifier):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_writer = context.writer()
        __M_writer('\n<script src="https://apis.google.com/js/plusone.js"></script>\n<div class="g-comments"\n    data-href="')
        __M_writer(str(url))
        __M_writer('"\n    data-first_party_property="BLOGGER"\n    data-view_type="FILTERED_POSTMOD">\n</div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_comment_link_script(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_writer = context.writer()
        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_comment_link(context,link,identifier):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_writer = context.writer()
        __M_writer('\n<div class="g-commentcount" data-href="')
        __M_writer(str(link))
        __M_writer('"></div>\n<script src="https://apis.google.com/js/plusone.js"></script>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "utf-8", "line_map": {"33": 2, "34": 5, "35": 5, "41": 16, "55": 11, "45": 16, "16": 0, "51": 11, "21": 9, "22": 14, "23": 17, "56": 12, "57": 12, "29": 2, "63": 57}, "uri": "comments_helper_googleplus.tmpl", "filename": "/home/ali/MyPython3/lib/python3.5/site-packages/nikola/data/themes/base/templates/comments_helper_googleplus.tmpl"}
__M_END_METADATA
"""
