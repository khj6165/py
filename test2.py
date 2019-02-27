#!/usr/bin/env python
import ConfigParser

ini = ConfigParser.CenfigParser()
ini.read("data.ini")

print ini.sections()
print ini.options("project")
print ini.get("project","name")
