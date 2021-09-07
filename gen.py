import sys

import pygments
from pygments import highlight
from pygments.formatters import HtmlFormatter
from pygments.lexers import PythonLexer
from pygments.styles import get_all_styles

style_block = '<style>\n%s\n</style>'

with open(sys.argv[1]) as f:
  # skip the heading comments
  code = f.read().split('\n\n', 1)[1]

print('Pygments version: %s' % pygments.__version__)
print()

indent = lambda s: '  ' + s.replace('\n', '\n  ')
for style in sorted(get_all_styles()):
  class_tag = 'pygments-%s' % style
  print('%s' % style)
  print('%s' % ('=' * len(style)))
  print()
  formatter = HtmlFormatter(linenos=True, cssclass=class_tag, style=style)
  print('.. raw:: html\n')
  print(indent(style_block % formatter.get_style_defs('.' + class_tag)))
  print(indent(highlight(code, PythonLexer(), formatter)))
  print()
