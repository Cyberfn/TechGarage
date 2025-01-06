from datetime import datetime

def calcula_diferenca_datas(date1, date2, date_format="%Y-%m-%d"):
    d1 = datetime.strptime(date1, date_format)
    d2 = datetime.strptime(date2, date_format)
    return abs((d2 - d1).days)