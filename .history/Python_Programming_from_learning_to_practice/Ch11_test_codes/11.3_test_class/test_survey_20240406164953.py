# 向哲煜 2024.4.6

import pytest
from survey import AnonymousSurvey

@pytest.fixture
def language_survey():
    """一个可供所有测试函数使用的AnonymousSurvey实例"""
    question = "What language did you first learn to speak?"
    language_survey = AnonymousSurvey(question)

def test_store_single_response():
    """测试单个答案是否会被妥善地存储"""
    question = 'What language did you first learn?'
    language_survey = AnonymousSurvey(question)
    language_survey.store_response('English')
    assert 'English' in language_survey.responses

def test_store_three_responses():
    """测试三个答案是否能被妥善地存储"""
    question = 'What language did you first learn?'
    language_survey = AnonymousSurvey(question)
    responses = ['Spanish', 'English', 'Mandarin']
    for response in responses:
        language_survey.store_response(response)
    
    for response in responses:
        assert response in language_survey.responses