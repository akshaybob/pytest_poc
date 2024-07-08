"module for unit test for executive operations"
from src.executive_operations import npa_score, progress_report_stats, growth_calculator

def test_npa_score():
    result=npa_score(60)
    assert result == 6*60

def test_progress_report_stats():
    result=progress_report_stats(20)
    assert result['annual'] == 20
    assert result['mid_year'] == 20/2
    assert result['quaterly'] == 20/4

def test_failuer_progress_report_stats():
    result = progress_report_stats('demo_input')
    assert result['status'] =='type error: int expected'
    assert result['status_code'] == 500

def test_growth_calculator(previous_year=2, current_year=4):
    result = growth_calculator(150,200)
    s= 50/150
    assert result == s*100