from pyecharts import options as opts
from pyecharts.charts import Tree

data = [
    {
        "name": "数据类型",
        "children": [
            {
                "name": "数值",
                "children": [{"name": "int(整型)"}, {"name": "float(浮点型)"}]
            },
            {
                "name": "bool(布尔型)",
                "children": [{"name": "True(真)"}, {"name": "False(假)"}]
            },
            {
                "name": "str(字符串)",
                "children": [{"name": "helloworld"}]
            },
            {
                "name": "list(列表)",
                "children": [{"name": "[1,2,3]"}]
            },
            {
                "name": "tuple(元组)",
                "children": [{"name": "(a,b,d)"}]
            },
            {
                "name": "set(集合)",
                "children": [{"name": "{1，2，3}"}]
            },
            {
                "name": "dict(字典)",
                "children": [{"name": "{'name':'LazyCat','age':'18''}"}]
            },
        ]
    }
]
c = (
    Tree()
        .add("", data)
)
c.render_notebook()
