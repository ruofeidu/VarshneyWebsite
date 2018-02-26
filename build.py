# author: Ruofei Du
# This script builds the website by parsing the markdown text files and json files in data/
# This script also includes common files such as header and footer, and embed them into the final HTML
from xml.etree import ElementTree as ET
from scripts.types import *
import re, json
import markdown

re_markdown = re.compile("<!--\s*include\s*:\s*data\/(.+)\.txt\s*?-->")
re_html = re.compile("<!--\s*include\s*:\s*(.+)\.html\s*?-->")


def remove_comments(html):
    return re.sub("(<!--.*?-->)", "", html, flags=re.DOTALL)


def remove_blank_lines(html):
    return re.sub("\n\s*\n", "\n", html, flags=re.DOTALL)


def read_str(file_name):
    with open(file_name, 'r') as f:
        s = ''.join(f.readlines())
    return s


def read_html(file_name):
    s = read_str(file_name + '.html')
    while re_html.search(s):
        key = re_html.search(s).groups()[0]
        print("%s\t<=\t%s.html" % (file_name, key))
        s = re.sub("<!--\s*include\s*:\s*" + key + "\.html\s*-->", html[key], s, flags=re.DOTALL)
    return s


def read_content(file_name):
    s = read_html(file_name + '.content')
    while re_markdown.search(s):
        key = re_markdown.search(s).groups()[0]
        print("%s\t<=\t%s.txt" % (file_name, key))
        s = re.sub("<!--\s*include\s*:\s*data\/" + key + "\.txt\s*-->", md[key], s, flags=re.DOTALL)
    while re_html.search(s):
        key = re_html.search(s).groups()[0]
        print("%s\t<=\t%s.html" % (file_name, key))
        s = re.sub("<!--\s*include\s*:\s*" + key + "\.html\s*-->", html[key], s, flags=re.DOTALL)

    s = remove_comments(s)
    s = remove_blank_lines(s)
    return s


def build(file_name):
    print("---")
    s = read_content(file_name)
    # Build to separate folders
    # out_file = "%s.html" % file_name if file_name == 'index' else "%s/index.html" % file_name
    # Build to the root
    out_file = "%s.html" % file_name
    with open(out_file, 'w') as f:
        f.write('<!-- Automatically generated by build.py from MarkDown files -->\n')
        f.write('<!-- Augmentarium | UMIACS | University of Maryland, College Park -->\n')
        f.write(s)


def read_markdown(file_name):
    s = read_str('data/' + file_name + '.txt')
    s = markdown.markdown(s)
    return s


def read_data(file_name):
    return json.load(open('data/' + file_name + '.json'))


def write_bib(b):
    filename = 'bib/' + b['bib'] + '.bib'
    if 'http' in filename:
        return
    print(filename)

    with open(filename, 'w') as f:
        f.write('@%s{%s,<br/>\n' % (b['type'], b['bibname']))
        f.write('&nbsp&nbsptitle = "%s",<br/>\n' % b['title'])
        f.write('&nbsp&nbspauthor = "%s",<br/>\n' % b['author'])
        f.write('&nbsp&nbsp%s = "%s",<br/>\n' % ('journal' if b['type'] == 'article' else 'booktitle', b['booktitle']))
        f.write('&nbsp&nbspyear = "%s",<br/>\n' % b['year'])
        f.write('&nbsp&nbspvolume = "%s",<br/>\n' % b['volume'])
        f.write('&nbsp&nbsppages = "%s"<br/>\n' % b['pages'])
        f.write('}<br/>\n')

    filename = 'bib/' + b['bib'] + '.apa'
    print(filename)

    with open(filename, 'w') as f:
        f.write('%s.' % b['author'])
        f.write(' (%s).<br/> ' % (b['year']))
        f.write('%s.' % b['title'])
        f.write(' <br/><i>%s</i>' % b['booktitle'])
        f.write(', %s' % b['pages'].replace('--', '-'))


def write_data_to_markdown(file_name):
    LINE_MEDIA = '* %s, [%s](%s), %s%s %s, %s.\n'
    LINE_STUDENTS = '<div class="2u 12u$(medium) center"><span class="image fit">' \
                    '<a href="%s" target="_blank"><img src="photos/%s" alt="%s" class="face"/></a></span>' \
                    '<h4 class="center"><a href="%s" target="_blank" class="name">%s</a></h4></div>\n'
    # (m['image'], m['title'], m['url'], m['title'], m['author'], m['booktitle'], m['keywords'], m['url'], m['video'], m['code'], m['slides'], m['apa'], m['bib']  )
    LINE_PAPERS = '<div class="3u 12u$(medium) pub-pic"><span class="image fit"><img src="teaser/%s" alt="%s" /></span></div>' \
                  '<div class="9u 12u$(medium) pub-info"><h4><a href="%s" target="_blank">%s</a></h4>' \
                  '<p class="authors">%s</p>' \
                  '<p class="booktitle">%s</p>' \
                  '<p class="keywords">keywords: %s</p>' \
                  '<div class="downloads">Download: <a href="%s" target="_blank">[pdf]</a>%s %s%s%s%s | ' \
                  'Cite: <a href="%s" class="bibtex">[APA]</a> <a href="%s" class="bibtex">[BibTeX]</a></div>' \
                  '</p></div>'
    LINE_UNPUBLISHED = '<div class="3u 12u$(medium) pub-pic"><span class="image fit"><img src="teaser/%s" alt="%s" /></span></div>' \
                       '<div class="9u 12u$(medium) pub-info"><h4>%s</h4>' \
                       '<p class="authors">%s</p>' \
                       '<p class="booktitle">%s</p>' \
                       '<p class="keywords">keywords: %s</p>' \
                       '<div class="downloads">Download: [pdf] %s%s%s | ' \
                       'Cite: <a href="%s" class="bibtex">[APA]</a> <a href="%s" class="bibtex">[BibTeX]</a></div>' \
                       '</p></div>'

    CATEGORY = '### %s\n'
    YEAR = '### %s\n'
    NEW_ROW = '<div class="row">\n'
    NEW_PUB = '<div class="row pub">\n'
    ROW_END = '</div>\n'

    with open("data/%s.txt" % file_name, 'w') as f:
        f.write('[comment]: <> (This markdown file is generated from %s.json by build.py)\n' % file_name)
        if file_name == 'media':
            for m in reversed(data['media']):
                f.write(LINE_MEDIA % (
                    m['publisher'], m['title'], m['url'], '(Video) ' if m['video'] else '', m['month'], m['day'],
                    m['year']))
        elif file_name == 'students':
            categories = []
            for m in data['students']:
                if m['category'] not in categories:
                    categories.append(m['category'])
            for c in categories:
                f.write(CATEGORY % c)
                count = 0
                f.write(NEW_ROW)
                for m in data['students']:
                    if m['category'] == c and m['visible']:
                        if count and count % 5 == 0:
                            f.write(ROW_END)
                            f.write(NEW_ROW)
                        f.write(LINE_STUDENTS % (m['url'], m['photo'], m['name'] + "'s photo", m['url'], m['name']))
                        count += 1
                f.write(ROW_END)
        elif file_name == 'papers':
            years = []
            for m in data['papers']:
                if m['year'] not in years:
                    years.append(m['year'])
                if not m['bib']:
                    m['bib'] = m['bibname']
                write_bib(m)
                m['url'] = 'papers/' + m['url'] if not 'http' in m['url'] else m['url']
                bib = m['bib']
                m['bib'] = 'bib/' + bib + '.bib'
                m['apa'] = 'bib/' + bib + '.apa'
                if not m['video']:
                    if m['youtube']:
                        m['video'] = m['youtube']
                    else:
                        m['video'] = m['vimeo']
                m['video'] = ' <a href="%s" target="blank">[video]</a>' % m['video'] if m['video'] else ''
                m['code'] = ' <a href="%s" target="blank">[code]</a>' % m['code'] if m['code'] else ''
                m['slides'] = ' <a href="%s" target="blank">[slides]</a>' % m['slides'] if m['slides'] else ''
                if 'web' in m and m['web']:
                    m['web'] = ' <a href="%s" target="blank">[web]</a>' % m['web']
                else:
                    m['web'] = ''
                if not m['published']:
                    m['booktitle'] = 'To Appear In ' + m['booktitle']
                    m['url'] = ''
                if m['award']:
                    m['booktitle'] += '<br/><span class="award">%s</span>' % m['award']
                if m['doi']:
                    m['doi'] = ' <a href="https://doi.org/%s" target="_blank">[doi]</a>' % m['doi']
            for y in sorted(years, reverse=True):
                f.write(YEAR % y)
                count = 0
                for m in data['papers']:
                    if m['year'] == y and m['visible']:
                        f.write(NEW_PUB)
                        if m['published']:
                            f.write(LINE_PAPERS % (
                                m['image'], m['title'], m['url'], m['title'], m['author'], m['booktitle'],
                                m['keywords'],
                                m['url'], m['doi'], m['video'], m['code'], m['slides'], m['web'], m['apa'], m['bib']))
                        else:
                            f.write(LINE_UNPUBLISHED % (
                                m['image'], m['title'], m['title'], m['author'], m['booktitle'],
                                m['keywords'], m['video'], m['code'], m['slides'], m['apa'], m['bib']))
                        f.write(ROW_END)
                        count += 1


html_files = ['header', 'footer', 'contact', 'menu', 'sidebar', 'banner']
data_files = ['media', 'students', 'papers']
md_files = ['bio', 'media', 'activities', 'students', 'ungrads', 'papers']
build_files = ['index', 'media', 'activities', 'students', 'publications']

html, md, data = {}, {}, {}

# First, parse Json Data and write to Markdown files
for f in data_files:
    data[f] = read_data(f)
for m in data['media']:
    m['title'] = smart_title(m['title'])
for f in data_files:
    write_data_to_markdown(f)

# Next, read and parse HTML and MARKDOWN file for including
for f in html_files:
    html[f] = read_html(f)
for f in md_files:
    md[f] = read_markdown(f)

# Finally, generate combined files
for f in build_files:
    build(f)
