"module deals with executive represntation"

def npa_score(days=30):
    return 6*days

def progress_report_stats(profit=10):
    try:
        int(profit)
        return {'annual': profit, 'mid_year': profit/2, 'quaterly': profit/4}
    except:
        return {'status': 'type error: int expected', 'status_code': 500}

def growth_calculator(previous_year=2, current_year=4):
    growth=(current_year-previous_year)/previous_year
    return growth* 100
