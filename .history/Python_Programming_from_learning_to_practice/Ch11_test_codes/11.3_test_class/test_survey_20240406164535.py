# 向哲煜 2024.4.6

from survey import AnonymousSurvey

def test_store_single_response():
    """测试单个答案是否会被妥善地存储"""
    question = 'What language did you first learn?'
    language_survey = AnonymousSurvey(question)
    language_survey.store_response('English')
    assert 'English' in language_survey.responses

def 