import requests
import datetime


def isLeap(targetYear):     # 윤년 판단
    if targetYear % 4 == 0 and (targetYear % 100 != 0 or targetYear % 400 == 0):
        return 29
    else:
        return 28


def tillWhen(targetPeriod): # 해당 월의 마지막 날짜 판단 (몇일자까지 api호출해야 하는지 판단)
    till31 = ["01", "03", "05", "07", "08", "10", "12"]
    till30 = ["04", "06", "09", "11"]

    if targetPeriod == datetime.datetime.now().strftime("%Y%m"):    # 당월의 경우, 현재일까지만
        return datetime.datetime.now().day
    elif targetPeriod[4:6] in till31:   # 31일까지 있는 달
        return 31
    elif targetPeriod[4:6] in till30:   # 30일까지 있는 달
        return 30
    else:                               # 2월 (윤년 판단 추가)
        return isLeap(int(targetPeriod[0:4]))


def getChgRate(inVal):
    url = 'https://www.koreaexim.go.kr/site/program/financial/exchangeJSON?data=AP01&authkey='
    APIkey = 'a6w51v3PEJEhlv2BeW6iXpTfSBygESpB'
    targetPeriod = datetime.datetime.now().strftime("%Y%m")
    rateDict = {}

    if len(inVal) >= 6:
        targetPeriod = inVal

    endDate = tillWhen(targetPeriod)

    for day in range(1, endDate+1):
        targetDate = targetPeriod + '{:0>2}'.format(day)
        print(targetDate)
        resp = requests.get(url+APIkey+'&searchdate='+targetDate)

        if resp.status_code != 200:
            print("error")

        for rate in resp.json():
            if rate['cur_unit'] == 'USD':
                rateDict[targetDate] = rate['deal_bas_r']

    print(rateDict)

    return rateDict


'''
while True:
    inVal = input("Input: ")
    resultSet = getChgRate(inVal)

    print(resultSet)
'''
