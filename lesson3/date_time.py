from datetime import date, datetime, timedelta
from collections import OrderedDict

def print_days():
    frmt = '%d.%m.%Y'
    dts = OrderedDict()
    dts['today'] = date.today()
    dts['yesterday'] = dts['today'] - timedelta(days=1)
    dts['month_ago'] = dts['today'] - timedelta(days=dts['today'].day)
    if dts['month_ago'].day > dts['today'].day:
         dts['month_ago'] = date(
            year=dts['month_ago'].year, 
            month=dts['month_ago'].month, 
            day=dts['today'].day
        )
    for k, v in dts.items():
        print('{}: {}'.format(k.replace('_', ' '), v.strftime(frmt)))

    
    
def str_2_datetime(str_dt):
    frmt = '%d/%m/%y %H:%M:%S.%f'
    return datetime.strptime(str_dt, frmt)

if __name__ == "__main__":
    print_days()
    print(str_2_datetime("01/01/17 12:10:03.234567"))