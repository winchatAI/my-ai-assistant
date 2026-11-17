
print("===== 我的AI知识库助手 =====")

knowledge = {
    "Python": "Python是一种非常流行的编程语言。",
    "GitHub": "GitHub是一个代码托管和协作平台。",
    "AI": "AI就是人工智能。",
    "Dify": "Dify是一个帮助开发AI应用的平台。",
    "机器学习": "机器学习是人工智能的一个重要领域。",
    "大模型": "大语言模型可以理解和生成文字。"
}

print("你好！欢迎使用我的AI知识库助手。")
print("你可以问我Python、GitHub、AI、Dify、机器学习或大模型。")
print("输入 exit 可以结束聊天。")

while True:
    question = input("你：")

    if question == "exit":
        print("小AI：再见！")
        break

    found = False

    for keyword in knowledge:
        if keyword in question:
            print("小AI：" + knowledge[keyword])
            found = True
            break

    if found == False:
        print("小AI：我的知识库暂时没有这个答案。")
