#!/usr/bin/env python3


import cgi

our_form = cgi.FieldStorage()

in_name = our_form.getfirst("in_name","не задано")
in_city = our_form.getfirst("in_city","не задано")
in_comment = our_form.getfirst("in_comment","не задано")


print("Content-type: text/html")
print()
print(in_name)
print(in_comment)
