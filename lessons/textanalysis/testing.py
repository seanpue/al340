# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <codecell>

import PyPDF2

# <codecell>


# <codecell>

# Here let's download a PDF.

import urllib2 # this is a library to download files

text_urls = ['http://spartanhistory.kora.matrix.msu.edu/files/1/4/1-4-F20-54-s0753_1937_1938.pdf',
             'http://spartanhistory.kora.matrix.msu.edu/files/1/4/1-4-F21-54-S0753_1938_1939.pdf',
             'http://spartanhistory.kora.matrix.msu.edu/files/1/4/1-4-F22-54-s0753_1940_1941.pdf']

texts = {} # here we will store the raw PDF data

# <codecell>

# A new command range — gives set of numbers in a particular range
range(10)

# <codecell>

def get_pages_text(pdf_file):
    pdf = PyPDF2.PdfFileReader(pdf_file)
    pages_text = []
    for pn in range(pdf.numPages):
        p = pdf.getPage(pn) 
        p_t = p.extractText()
        pages_text.append(p_t)
    return pages_text

def download_pdfs():
    for u in text_urls:
        response = urllib2.urlopen(u)
        print 'Downloading '+u+'....'
        pdf = response.read()
        assert pdf
        new_name = u[-13:] # this is what we will save the fields as
        with open('data/'+new_name,'wb') as f:
            f.write(pdf)
        print '  Done! Saved as data/'+new_name

# <codecell>

download_pdfs() # downl


# <codecell>

pdf_files = ['data/'+ u[-13:] for u in text_urls]
pdf_files

# <codecell>

pdf_text = {} # save as a dictionary
for fn in pdf_files:
    pages =  get_pages_text(fn)
    pdf_text[fn] = pages

# <codecell>

pdfs_combined = {name: ' '.join(pages) for name,pages in pdf_text.iteritems()}

# <codecell>

pdfs_combined.keys()

# <codecell>

import codecs
for key,value in pdfs_combined.iteritems():
    file_name = key[:-4]+'.txt'
    file_name = file_name.replace('data/','data/texts/')
    print 'outputing to',file_name
    with codecs.open(file_name,'w','utf-8') as f:
        f.write(value)

# <codecell>

%cat data/1937_1938.txt

# <codecell>

corpus.dispersion_plot(["women","girlscitizens", "democracy", "freedom", "duties", "America"])

