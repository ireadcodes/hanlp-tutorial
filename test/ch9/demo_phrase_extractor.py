def test_phrase_extractor():
    text = "算法工程师\n" + \
           "算法（Algorithm）是一系列解决问题的清晰指令，也就是说，能够对一定规范的输入，在有限时间内获得所要求的输出。" + \
           "如果一个算法有缺陷，或不适合于某个问题，执行这个算法将不会解决这个问题。不同的算法可能用不同的时间、" + \
           "空间或效率来完成同样的任务。一个算法的优劣可以用空间复杂度与时间复杂度来衡量。算法工程师就是利用算法处理事物的人。\n" + \
           "\n" + \
           "1职位简介\n" + \
           "算法工程师是一个非常高端的职位；\n" + \
           "专业要求：计算机、电子、通信、数学等相关专业；\n" + \
           "学历要求：本科及其以上的学历，大多数是硕士学历及其以上；\n" + \
           "语言要求：英语要求是熟练，基本上能阅读国外专业书刊；\n" + \
           "必须掌握计算机相关知识，熟练使用仿真工具MATLAB等，必须会一门编程语言。\n" + \
           "\n" + \
           "2研究方向\n" + \
           "视频算法工程师、图像处理算法工程师、音频算法工程师 通信基带算法工程师\n" + \
           "\n" + \
           "3目前国内外状况\n" + \
           "目前国内从事算法研究的工程师不少，但是高级算法工程师却很少，是一个非常紧缺的专业工程师。" + \
           "算法工程师根据研究领域来分主要有音频/视频算法处理、图像技术方面的二维信息算法处理和通信物理层、" + \
           "雷达信号处理、生物医学信号处理等领域的一维信息算法处理。\n" + \
           "在计算机音视频和图形图像技术等二维信息算法处理方面目前比较先进的视频处理算法：机器视觉成为此类算法研究的核心；" + \
           "另外还有2D转3D算法(2D-to-3D conversion)，去隔行算法(de-interlacing)，运动估计运动补偿算法" + \
           "(Motion estimation/Motion Compensation)，去噪算法(Noise Reduction)，缩放算法(scaling)，" + \
           "锐化处理算法(Sharpness)，超分辨率算法(Super Resolution),手势识别(gesture recognition),人脸识别(face recognition)。\n" + \
           "在通信物理层等一维信息领域目前常用的算法：无线领域的RRM、RTT，传送领域的调制解调、信道均衡、信号检测、网络优化、信号分解等。\n" + \
           "另外数据挖掘、互联网搜索算法也成为当今的热门方向。\n" + \
           "算法工程师逐渐往人工智能方向发展。"
    # 分词后的结果
    sentence_list = [["算法", "工程师"], ["算法", "解决问题", "清晰", "指令"], ["也就是说"],
                     ["能够", "规范", "输入"], ["有限", "时间", "获得", "要求", "输出"], ["算法", "缺陷"],
                     ["适合于", "问题"], ["执行", "算法", "不会", "解决", "问题"],
                     ["不同", "算法", "可能", "不同", "时间", "空间", "效率", "完成", "同样", "任务"],
                     ["算法", "优劣", "空间", "复杂度", "时间", "复杂度", "衡量"],
                     ["算法", "工程师", "利用", "算法", "处理", "事物"], ["职位", "简介"],
                     ["算法", "工程师", "非常", "高端", "职位"],
                     ["专业", "要求", "计算机", "电子", "通信", "数学", "相关", "专业"],
                     ["学历", "要求", "本科", "学历"], ["硕士", "学历"], ["语言", "要求", "英语", "要求", "熟练"],
                     ["基本上", "阅读", "国外", "专业", "书刊"], ["必须", "掌握", "计算机", "相关", "知识"],
                     ["熟练", "使用", "仿真", "工具"], ["必须", "会", "门", "编程语言"], ["研究", "方向"],
                     ["视频", "算法", "工程师", "图像处理", "算法", "工程师", "音频", "算法", "工程师"],
                     ["通信", "基", "带", "算法", "工程师"], ["国内外", "状况"],
                     ["国内", "从事", "算法", "研究", "工程师"], ["高级", "算法", "工程师", "很少"],
                     ["非常", "紧缺", "专业", "工程师"],
                     ["算法", "工程师", "研究", "领域", "音频", "视频", "算法", "处理", "图像", "技术", "方面", "信息",
                      "算法", "处理", "通信", "物理", "雷达", "信号", "处理", "生物", "医学", "信号", "处理", "领域",
                      "一维", "信息", "算法", "处理"],
                     ["计算机", "音", "视频", "图形", "图像", "技术", "信息", "算法", "处理", "方面", "比较", "先进",
                      "视频", "处理", "算法", "机器", "视觉", "成为", "算法", "研究", "核心"], ["转", "算法"], [],
                     ["隔行", "算法"], ["运动", "估计", "运动", "补偿", "算法"], [], [], ["噪", "算法"], [],
                     ["缩放", "算法"], ["锐", "化", "处理", "算法", ], ["超", "分辨率", "算法"], [],
                     ["手势", "识别"], [], ["人脸", "识别"], [],
                     ["通信", "物理", "一维", "信息", "领域", "常用", "算法", "领域"],
                     ["传送", "领域", "调制", "解调", "信道", "均衡", "信号", "检测", "网络", "优化", "信号", "分解"],
                     ["数据挖掘", "互联网", "搜索", "算法", "成为", "热门", "方向"],
                     ["算法", "工程师", "逐渐", "人工智能", "方向", "发展"]]


if __name__ == '__main__':
    test_phrase_extractor()
