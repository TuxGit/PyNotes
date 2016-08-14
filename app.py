from flask import Flask, render_template
from config_provider import ConfigProvider
import os
import function

app = Flask(__name__)

config = ConfigProvider()


# Получение содержимого страницы
def get_page(name):
    file = os.path.join(config.pages_folder, name + '.md')

    # Если страница существует
    if function.check_found_file(file):
        page = function.markdown_to_html(file)
    else:
        page = config.not_found_text
    return page


@app.route('/')
def hello():
    return render_template(
        'page.html',
        title=config.main_title,
        side=get_page(config.side_bar),
        content=get_page(config.start_page)
    )


@app.route('/<name>')
def page(name):
    return render_template(
        'page.html',
        title=config.main_title,
        side=get_page(config.side_bar),
        content=get_page(name)
    )


if __name__ == '__main__':
    app.run(port=config.port)
