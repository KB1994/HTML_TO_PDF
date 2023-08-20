"""importing packages and libraries """
import os
import datetime
from jinja2 import Environment, FileSystemLoader




def jinja_template(template_file, data):

    """This method return html file content in a string format"""

    env = Environment(loader = FileSystemLoader("html_templates"))
    template = env.get_template(template_file)

    output = template.render(data)
    return output


def html_file(content_template, path_output ,html_name):

    """This method insert the html content into a file and return 
    the path to the html file generated"""

    print("Hello html file")

    path_file = os.path.join(path_output,html_name)

    with open(path_file, 'w', encoding= 'UTF-8') as file:
        file.write(content_template)

    file.close()

    return path_file






if __name__ == "__main__":

    print("Hello HTML TO PDF")

    CURRENT_DIR = os.getcwd()
    IMG_PATH = os.path.join(CURRENT_DIR , 'images\pic_trulli.jpg')
    PATH_OUT_HTML = os.path.join(CURRENT_DIR , 'html_templates\Output_html')

    template_data = {
        'title': f'Planner_{datetime.datetime.now().year}',
        'message': 'Welcome to Jinja2 template example!',
        'image_path' : IMG_PATH
        }

    rendered_template = jinja_template('template.html', template_data)

    RNDERED_HTML_PATH = html_file(rendered_template, PATH_OUT_HTML ,
                                f'{template_data["title"]}.html')


    print(rendered_template)