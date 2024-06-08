from sow.util import generate_web_page

# PYTHONPATH=.. python bang.py
# cp output.html index.html
# patch index.html index.patch

# diff -u output.html index.html > index.patch

word_points = 'bang_train1_0_test1_points_label0.csv'
word_extent = 'bang_train1_0_test1_render10b_extent.json'
word_corpus = 'bang_all_test_filtered.txt'

generate_web_page("bang", word_points, word_extent, word_corpus)
