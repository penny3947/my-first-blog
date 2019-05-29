import requests
import datetime


def is_leap(target_year):     # 윤년 판단
    if target_year % 4 == 0 and (target_year % 100 != 0 or target_year % 400 == 0):
        return 29
    else:
        return 28


def tillWhen(target_period): # 해당 월의 마지막 날짜 판단 (몇일자까지 api호출해야 하는지 판단)
    till31 = ["01", "03", "05", "07", "08", "10", "12"]
    till30 = ["04", "06", "09", "11"]

    if target_period == datetime.datetime.now().strftime("%Y%m"):    # 당월의 경우, 현재일까지만
        return datetime.datetime.now().day
    elif target_period[4:6] in till31:   # 31일까지 있는 달
        return 31
    elif target_period[4:6] in till30:   # 30일까지 있는 달
        return 30
    else:                               # 2월 (윤년 판단 추가)
        return is_leap(int(target_period[0:4]))


def getChgRate(in_val):
    url = 'https://www.koreaexim.go.kr/site/program/financial/exchangeJSON?data=AP01&authkey='
    APIkey = 'a6w51v3PEJEhlv2BeW6iXpTfSBygESpB'
    rateDict = {}

    if not in_val:
        return rateDict

    target_period = in_val["year"] + in_val["month"]
    curr = in_val["curr"]
    end_date = tillWhen(target_period)

    for day in range(1, end_date+1):
        target_date = target_period + '{:0>2}'.format(day)
        print(target_date)
        resp = requests.get(url+APIkey+'&searchdate='+target_date)

        if resp.status_code != 200:
            print("error")

        for rate in resp.json():

            if rate['cur_unit'] == curr:
                rateDict[target_date] = rate['deal_bas_r']

    print(rateDict)

    return rateDict