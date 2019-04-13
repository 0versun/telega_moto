import datetime

def return_dif(target_year, target_mont, target_day):

    today = datetime.date.today()
    targer = datetime.date(int(target_year), int(target_mont), int(target_day))
    if targer < today:
        output_day = today - targer
        print('Эта дата уже наступила и прошла', output_day.days)
        return 'нисколько, эта дата уже наступила и прошла'
    elif targer == today:
        return 'нисколько, потому что, этот день настал сегодня'
    else:
        output_day = targer - today
    return output_day.days