import requests
import datetime
import matplotlib.pyplot as plt


def draw_rate(chg_rate, rate_ttb, rate_tts, curr):
    x_axis_year = []
    y_axis_rate = []
    y_axis_ttb = []
    y_axis_tts = []

    print("HERE")
    print(x_axis_year, y_axis_rate)
    title = ""

    for k, v in chg_rate.items():
        x_axis_year.append(k[6:8])
        y_axis_rate.append(float(v.replace(",", "")))
        title = k[0:6]

    for k, v in rate_ttb.items():
        y_axis_ttb.append(float(v.replace(",", "")))

    for k, v in rate_tts.items():
        y_axis_tts.append(float(v.replace(",", "")))

    print(x_axis_year, y_axis_rate)
    plt.grid(True)
    plt.title('Year: '+title[0:4]+', Month: '+title[4:6]+", Currency: "+curr)
    plt.xlabel("Day")
    plt.ylabel("Won")
    plt.plot(x_axis_year, y_axis_rate, 'rs--', label = 'Basic rate')
    plt.plot(x_axis_year, y_axis_ttb, '-', label = 'Receiving rate')
    plt.plot(x_axis_year, y_axis_tts, '-', label = 'Sending rate')
    plt.legend()
    plt.savefig('blog/static/img/'+title+curr+'.png', dpi=300)
    plt.clf()


def is_leap(target_year):     # 윤년 판단
    if target_year % 4 == 0 and (target_year % 100 != 0 or target_year % 400 == 0):
        return 29
    else:
        return 28


def till_when(target_period): # 해당 월의 마지막 날짜 판단 (몇일자까지 api호출해야 하는지 판단)
    till31 = ["01", "03", "05", "07", "08", "10", "12"] # 31일까지 있는 달
    till30 = ["04", "06", "09", "11"]                   # 30일까지 있는 달

    if target_period == datetime.datetime.now().strftime("%Y%m"):    # 당월의 경우, 현재일까지만
        return datetime.datetime.now().day
    elif target_period[4:6] in till31:
        return 31
    elif target_period[4:6] in till30:
        return 30
    else:                               # 2월 (윤년 판단 추가)
        return is_leap(int(target_period[0:4]))


def get_chg_rate(in_val):
    url = 'https://www.koreaexim.go.kr/site/program/financial/exchangeJSON?data=AP01&authkey='
    APIkey = 'a6w51v3PEJEhlv2BeW6iXpTfSBygESpB'
    rate_dict = {}
    rate_ttb = {}
    rate_tts = {}


    if not in_val or in_val["year"] == "0000":      # 초기값일 경우 아무처리 없이 바로 응답
        return "000000000"

    target_period = in_val["year"] + in_val["month"]
    curr = in_val["curr"]
    end_date = till_when(target_period)

    for day in range(1, end_date+1):
        target_date = target_period + '{:0>2}'.format(day)
        #print(target_date)
        resp = requests.get(url+APIkey+'&searchdate='+target_date)

        if resp.status_code != 200:
            print("error")

        for rate in resp.json():

            if rate['cur_unit'] == curr:
                rate_dict[target_date] = rate['deal_bas_r']
                rate_ttb[target_date] = rate['ttb']
                rate_tts[target_date] = rate['tts']

    draw_rate(rate_dict, rate_ttb, rate_tts, curr)

    return target_period+curr
