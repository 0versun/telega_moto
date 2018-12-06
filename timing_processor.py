import datetime

def return_dif(target_year, target_mont, target_day):

    today = datetime.date.today()
    targer = datetime.date(target_year, target_mont, target_day)
    if targer < today:
        output_day = today - targer
        print('Эта дата уже наступила и прошла', output_day)
    else:
        output_day = targer - today
    return output_day




# print(return_dif(2001, 12, 4))