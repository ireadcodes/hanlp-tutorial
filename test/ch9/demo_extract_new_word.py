from mining.word.new_word_discover import NewWordDiscover


def test_extract_new_word():
    with open('../data/三国演义.txt', encoding='utf8') as f:
        docs = f.readlines()
    discover = NewWordDiscover(4, 0, .5, 100)
    word_info_list = discover.discover(docs, 100)
    print(word_info_list)


if __name__ == '__main__':
    test_extract_new_word()
