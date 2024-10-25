import justpy as jp

import inspect
from webapp.about import About
from webapp.home import Home
from webapp.dictionary import Dictionary
from webapp.page import Page

all_imports = list(globals().values())

for obj in all_imports:
    if inspect.isclass(obj):
        if issubclass(obj, Page) and obj is not Page:
            jp.Route(obj.path, obj.serve)

# jp.Route(Home.path, Home.serve)
# jp.Route(About.path, About.serve)
# jp.Route(Dictionary.path, Dictionary.serve)

jp.justpy(port=8001)
