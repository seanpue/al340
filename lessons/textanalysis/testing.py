# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <codecell>

import PyPDF2

# <codecell>

import urllib2

# <codecell>

response = urllib2.urlopen('http://spartanhistory.kora.matrix.msu.edu/files/1/4/1-4-F20-54-s0753_1937_1938.pdf')
html = response.read()
with open ('1-4-F20-54-s0753_1937_1938.pdf','wb') as f:
    f.write(html)

# <codecell>

f=PyPDF2.PdfFileReader('1-4-F20-54-s0753_1937_1938.pdf')

# <codecell>

f.numPages

# <codecell>

five=f.getPage(5)

# <codecell>

five.extractText()

# <codecell>

page_text = []
for x in range (f.numPages):
    p = f.getPage(x)
    p_t = p.extractText()
    page_text.append(p_t)

# <rawcell>

# len(page_text)

# <codecell>

page_text

# <codecell>


