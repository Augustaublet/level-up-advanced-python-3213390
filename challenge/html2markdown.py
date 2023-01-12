"""
'This is the <a href="https://pypi.org/project/html2markdown/">link</a> to the html2markdown package and '
 'here is <a href="https://github.com/dlon/html2markdown">another link</a> to the project homepage'

<a href="https://pypi.org/project/html2markdown/">link</a>
"""


def changeLink(markdown):
    start = markdown.find('<a')
    end = markdown.find("</a>")
    link_string = markdown[start: end]
    href = link_string[link_string.find('"')+1: link_string.find('">')]
    link_text = link_string[link_string.find('">')+2:]

    in_format = f'[{link_text}]({href})'
    # end+4 is because I also whant to relpace the substring(</a>).
    markdown = markdown.replace(markdown[start: end+4], in_format)

    return markdown


def html2markdown(html):
    '''Take in html text as input and return markdown'''
    markdown = html
    markdown = " ".join(markdown.split())

    if "<em>" in html:
        markdown = markdown.replace("<em>", "*")
        markdown = markdown.replace("</em>", "*")
    if "</p><p>" in html:
        markdown = markdown.replace("</p><p>", "\n\n")
    if "<p>" in html:
        markdown = markdown.replace("<p>", "")
        markdown = markdown.replace("</p>", "")
    while "<a" in markdown:
        markdown = changeLink(markdown)

    return markdown
