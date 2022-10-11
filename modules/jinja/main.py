#!/usr/bin/python
import jinja2

templateLoader = jinja2.FileSystemLoader(searchpath="./")
templateEnv = jinja2.Environment(loader=templateLoader)
TEMPLATE_FILE = "template.html"
template = templateEnv.get_template(TEMPLATE_FILE)

dict_vars = {"test": "Suraj"}

outputText = template.render(dict_vars)  # this is where to put args to the template renderer

print(outputText)