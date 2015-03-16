# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <codecell>

import nltk

%matplotlib inline

# <codecell>

import os

from nltk.corpus.reader.plaintext import PlaintextCorpusReader

corpusdir = 'data/texts/' # Directory of corpus.
corpus0 = PlaintextCorpusReader(corpusdir, '.*')
corpus  = nltk.Text(corpus0.words())

# <codecell>

corpus.concordance('girls')

# <codecell>

corpus.concordance("'", lines=all)

# <codecell>

len(set(corpus))

# <codecell>

len(corpus)

# <codecell>

corpus.common_contexts(['general'])

# <codecell>

from nltk.corpus import stopwords
stopwords = stopwords.words(‘english’)

# <codecell>

corpus.dispersion_plot(["women","girls","fire"])

# <codecell>

import mpld3

# <codecell>

mpld3.enable_notebook()

# <codecell>

corpus.dispersion_plot(["women","girls","fire"], )

# <codecell>

len(corpus)

# <codecell>

len(set(corpus)) / len(corpus)

# <codecell>

corpus[0:100]

# <codecell>

fdist1 = nltk.FreqDist(corpus)

# <codecell>

fdist1.most_common(50)

# <codecell>

 fdist1.plot(50, cumulative=True)

# <codecell>

corpus[w.upper() for w in corpus]

