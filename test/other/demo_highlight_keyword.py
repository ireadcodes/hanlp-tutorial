def highlight(text, keyword_list):
    result = ""
    index = 0
    while index < len(text):
        found = False
        for keyword in keyword_list:
            if text.startswith(keyword, index):
                result += f"<span style='color:red;'>{keyword}</span>"
                index += len(keyword)
                found = True
                break
        if not found:
            result += text[index]
            index += 1
    return result


def test_highlight_keyword():
    text = "天气预报说明天出太阳"
    keyword_list = ["明天", "太阳"]
    result = highlight(text, keyword_list)
    print(result)


if __name__ == '__main__':
    test_highlight_keyword()
