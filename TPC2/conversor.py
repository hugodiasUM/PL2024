import re

def markdownToHtml(markdown):   
    expHeaders = '^#{1,3}\s(.+)$'
    expBold = '\*{2}.+\*{2}'
    expItalic = '\*.+\*'


    html = re.sub(expHeaders, convertHeaders, markdown, flags=re.MULTILINE)

# Exemplo de uso
markdown_text = """
# Título Principal

## Subtítulo

Este é um **exemplo** de texto em Markdown.
*exemplo*.

Como pode ser consultado em [página da UC](http://www.uc.pt)

Como se vê na imagem seguinte: ![imagem dum coelho](http://www.coellho.com)
"""

html_output = markdown_to_html(markdown_text)
print(html_output)