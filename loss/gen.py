from sow.util import generate_web_page

# PYTHONPATH=.. python gen.py
# cp output.html index.html
# patch index.html index.patch

# diff -u output.html index.html > index.patch

word_points = 'loss_train2_2_test1_points_label0.csv'
word_extent = 'loss_train2_2_test1_render10b_extent.json'
word_corpus = 'loss_all_test_filtered.txt'

generate_web_page("loss", word_points, word_extent, word_corpus)
