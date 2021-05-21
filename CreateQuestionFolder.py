"""
用于创建题目文件夹的模板
1. 题目文件夹 Question
2. 解答文件 Answer.py
3. 题目描述 description.txt
"""
import os

# 准备创建的题目文件夹个数，数据来自于LeetCode网站
Question_numbers = 1800

# 开始创建
for i in range(1, Question_numbers + 1):  # 从1开始循环
    current_question_folder = "./Question_{}".format(i)  # 文件夹变量
    if not os.path.exists(current_question_folder):  # 如果文件夹不存在，才会创建
        os.mkdir(current_question_folder)

    question_answer_file = "./{}/Answer_1.py".format(current_question_folder)  # 解答文件变量
    if not os.path.exists(question_answer_file):  # 如果文件不存在，才会创建
        answer_file = open(question_answer_file, "w")
        answer_file.close()

    question_description = "./{}/description.txt".format(current_question_folder)  # 题目描述文件变量
    if not os.path.exists(question_description):  # 如果文件不存在，才会创建
        answer_file = open(question_description, "w")
        answer_file.close()
