"Builder Concept Sample Code"
from abc import ABCMeta, abstractmethod
import datetime

class IHtmlBuilder(metaclass=ABCMeta):
    "The Html Builder Interface"

    @staticmethod
    @abstractmethod
    def build_header():
        "Build header part "

    @staticmethod
    @abstractmethod
    def build_body_open():
        "Build body opening part "

    @staticmethod
    @abstractmethod
    def build_title(title):
        "Build title part "

    @staticmethod
    @abstractmethod
    def build_paragraph(message):
        "Buil paragraph part"

    @staticmethod
    @abstractmethod
    def build_body_close():
        "Build body closing part "

    @staticmethod
    @abstractmethod
    def get_html_format():
        "Return the final product"


class BuilderHtml(IHtmlBuilder):
    "The Concrete Html Builder."

    def __init__(self):
        self.html_format = HtmlFormat()

    def build_header(self):
        self.html_format.parts.append('<!DOCTYPE html>')
        return self

    def build_body_open(self):
        self.html_format.parts.append("<html>")
        return self
    def build_title(self, title):
        self.html_format.parts.append(f"<h1>{title}</h1>")
        return self
    def build_paragraph(self, message):
        self.html_format.parts.append(f"<p>{message}</p>")
        return self
    def build_body_close(self):
        self.html_format.parts.append("</html>")
        return self

    def get_html_format(self):
        return self.html_format


class HtmlDirector:
    "The Director, building a complex representation."

    @staticmethod
    def construct():
        "Constructs and returns the final product"
        return BuilderHtml()\
            .build_header()\
            .build_body_open()\
            .build_title(f'Planner_{datetime.datetime.now().year}')\
            .build_paragraph('Welcome to html template example!')\
            .build_body_close()\
            .get_html_format()

class HtmlFormat():
    "The Html Format"

    def __init__(self):
        self.parts = []      

    def constructions(self):

       "return the finale html format "

       return '\n'.join(self.parts) 

if __name__ == "__main__":
    print('Hello Design pattern builder')
    PRODUCT = HtmlDirector.construct()
    print(PRODUCT.constructions())
