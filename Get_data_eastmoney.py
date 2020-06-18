#-*- codeing = utf-8 -*-
#@Time : 2020/6/18 20:32
#@Author : Andy Zhu
#@File : Get_data_eastmoney.py
#@Software : PyCharm

import requests
import pandas as pd
from threading import Timer
import time
import json
from pandas import json_normalize
import matplotlib
import matplotlib.pyplot as plt




def get_n_data():
    # plt.cla()
    cookies = {
        'cowCookie': 'true',
        'qgqp_b_id': '3134705a3135c517777b407db2f6a9dd',
        'st_si': '99846396600030',
        'st_asi': 'delete',
        'intellpositionL': '629px',
        '_qddaz': 'QD.rbol34.u54ci4.kbjaw5zs',
        'pgv_pvi': '27656192',
        'pgv_si': 's9727063040',
        'intellpositionT': '2149.67px',
        'st_pvi': '67868090420501',
        'st_sp': '2020-06-17^%^2019^%^3A51^%^3A30',
        'st_inirUrl': 'https^%^3A^%^2F^%^2Fcn.bing.com^%^2F',
        'st_sn': '15',
        'st_psi': '20200617201720709-113300300813-6037096727',
    }

    headers = {
        'Connection': 'keep-alive',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36',
        'Accept': '*/*',
        'Referer': 'http://data.eastmoney.com/zjlx/detail.html',
        'Accept-Language': 'en-US,en;q=0.9,zh;q=0.8,zh-TW;q=0.7,zh-CN;q=0.6',
    }

    params = (
        ('pn', '1^'),  # 77^代表第77页数据
        ('pz', '50^'),
        ('po', '1^'),
        ('np', '1^'),
        ('ut', 'b2884a393a59ad64002292a3e90d46a5^'),
        ('fltt', '2^'),
        ('invt', '2^'),
        ('fid0', 'f4001^'),
        ('fid', 'f62^'),
        ('fs', 'm:0 t:6 f:^!2,m:0 t:13 f:^!2,m:0 t:80 f:^!2,m:1 t:2 f:^!2,m:1 t:23 f:^!2^'),
        ('stat', '1^'),
        ('fields', 'f12,f14,f2,f3,f62,f184,f66,f69,f72,f75,f78,f81,f84,f87,f204,f205,f124^'),
        ('rt', '53079874^'),
        # ('cb', 'jQuery18308748778805485093_1592395188934^'),
        ('_', '1592396243859'),
    )

    response = requests.get('http://push2.eastmoney.com/api/qt/clist/get', headers=headers, params=params,
                            cookies=cookies, verify=False)

    # NB. Original query string below. It seems impossible to parse and
    # reproduce query strings 100% accurately so the one below is given
    # in case the reproduced version is not "correct".
    # response = requests.get('http://push2.eastmoney.com/api/qt/clist/get?pn=2^&pz=50^&po=1^&np=1^&ut=b2884a393a59ad64002292a3e90d46a5^&fltt=2^&invt=2^&fid0=f4001^&fid=f62^&fs=m:0+t:6+f:^!2,m:0+t:13+f:^!2,m:0+t:80+f:^!2,m:1+t:2+f:^!2,m:1+t:23+f:^!2^&stat=1^&fields=f12,f14,f2,f3,f62,f184,f66,f69,f72,f75,f78,f81,f84,f87,f204,f205,f124^&rt=53079874^&cb=jQuery18308748778805485093_1592395188934^&_=1592396243859', headers=headers, cookies=cookies, verify=False)
    # response.text

    dict = json.loads(response.text)['data']['diff']

    df = json_normalize(dict)
    df2 = df.set_index(['f12'])
    # change_ratio = df2.loc['002279']['f3']
    # main_money = df2.loc['002279']['f62']
    # print("change ratio:" + str(change_ratio))
    # print("main money:" + str(main_money))

    t = Timer(10, get_n_data)
    t.start()

    change_ratio.append(df2.loc['002279']['f3'])
    main_money.append(df2.loc['002279']['f62'])
    print(change_ratio)
    print(main_money)

    #plt.close(fig)
    # plt.plot(change_ratio)
    # plt.plot(main_money)


    ax1.plot(change_ratio,'.')
    #ax2.plot(main_money,'.')

    plt.draw()  # 注意此函数需要调用
    time.sleep(0.5)



    # plt.plot(change_ratio,'.')
    # plt.draw()


if __name__ == "__main__":
    plt.ion()  # 开启interactive mode 成功的关键函数
    # fig = plt.figure()

    # ax1 = fig.add_subplot(111)
    # ax2 = ax1.twinx()

    fig, ax1 = plt.subplots()
    ax1.set_xlabel("Index")
    ax1.set_ylabel("change_ratio", color="r")
    ax1.tick_params("y", color="b")
    ax2 = ax1.twinx()
    ax2.set_ylabel("main_money", color="r")
    ax2.tick_params("y", colors="r")

    i = 0
    change_ratio = []
    main_money = []
    get_n_data()