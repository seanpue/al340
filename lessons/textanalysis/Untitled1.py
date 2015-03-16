# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <codecell>

import nltk
sentence = "Hello my name is joe."
tokens = nltk.word_tokenize(sentence)
tokens

# <codecell>

tagged = nltk.pos_tag(tokens)

# <codecell>

tagged

# <codecell>

entities = nltk.chunk.ne_chunk(tagged)

# <codecell>

type(entities)

# <codecell>

%pylab inline

# <codecell>

 from nltk.corpus import treebank

# <codecell>

t = treebank.parsed_sents('wsj_0001.mrg')[0]

# <codecell>

t.draw()

# <codecell>



from pylab import *


x = linspace(0, 5, 10)
y = x ** 2
figure()
plot(x, y, 'r')
xlabel('x')
ylabel('y')
title('title')
show()

# <codecell>


