from hanlp.collection.trie.bintrie.bin_trie import BinTrie


def test_put():
    trie = BinTrie()
    trie.put("加入", True)
    assert trie.get("加入") is True
    trie.put("加入", False)
    assert trie.get("加入") is False


if __name__ == '__main__':
    test_put()
