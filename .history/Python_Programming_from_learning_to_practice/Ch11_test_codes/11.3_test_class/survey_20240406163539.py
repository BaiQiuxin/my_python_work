# 向哲煜 2024.4.6

class AnonymousSurvey:
    """收集匿名调查问卷的答案"""
    
    def __init__(self, question):
        """存储一个问题，并为存储答案做准备"""
        self.question = question
        self.responses = []
    
    def show_question(self):
        """显示调查问卷"""
        print(self.question)
    
    def store_