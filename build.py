from xml.etree import ElementTree as ET
import re


def remove_comments(html):
    return re.sub("(<!--.*?-->)", "", html, flags=re.DOTALL)


def read_str(file_name):
    with open(file_name, 'r') as f:
        s = ''.join(f.readlines())
    return s


def read_html(file_name):
    return read_str(file_name + '.html')


def read_content(file_name):
    s = read_html(file_name + '.content')
    s = remove_comments(s)
    return s


def read_markdown(file_name):
    s = read_str('data/' + file_name + '.txt')

    return s


header, footer = read_html('header'), read_html('footer')
data = {
    'bio' : read_markdown('bio'),
}
index = read_content('index')

with open("index.html", 'w') as f:
    f.write(header)
    f.write(index)
    f.write(footer)
