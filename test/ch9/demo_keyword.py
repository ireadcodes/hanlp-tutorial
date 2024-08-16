from hanlp.summary.text_rank_keyword import TextRankKeyword


def test_keyword():
    # 程序员(英文Programmer)是从事程序开发、维护的专业人员。一般将程序员分为程序设计人员和程序编码人员，
    # 但两者的界限并不非常清楚，特别是在中国。软件从业人员分为初级程序员、高级程序员、系统分析员和项目经理四大类。
    # 以下分词是经过停用词处理后的结果
    content = ["程序员", "英文", "Programmer", "从事", "程序", "开发", "维护", "专业", "人员", "程序员", "分为", "程序",
               "设计", "人员", "程序", "编码", "人员", "界限", "并不", "非常", "清楚", "特别", "中国", "软件", "人员",
               "分为", "程序员", "高级", "程序员", "系统分析", "员", "项目", "经理", "四大"]
    text_rank_keyword = TextRankKeyword()
    keywords = text_rank_keyword.get_keywords(content, 5)
    print(keywords)


if __name__ == '__main__':
    test_keyword()
