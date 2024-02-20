# 向哲煜 2024.2.10

def show_message(texts):
    """打印列表中的每条文本消息"""
    for text in texts:
        print(text)

def send_messages(messages, sent_messages):
    """将每条消息都打印出来并转移到一个名为sent_message的列表中"""
    current_message = messages.pop()
    print(current_message)
    sent_message.append(current_message)

texts = ['word', 'language', 'cell']
sent_texts = []

