import datetime

def return_dif(target_year, target_mont, target_day):

    today = datetime.date.today()
    targer = datetime.date(target_year, target_mont, target_day)
    if targer < today:
        output_day = today - targer
        print('Эта дата уже наступила и прошла', output_day.days)
    else:
        output_day = targer - today
    return output_day.days