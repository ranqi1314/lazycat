# encoding=utf8

from lxml import html
etree=html.etree

html = '<html><body><h1>This is a test</h1></body></html>'
# 将html转换成_Element对象
_element = etree.HTML(html)
# 通过xpath表达式获取h1标签中的文本
text = _element.xpath('//h1/text()')
print('result is: ', text)