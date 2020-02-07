#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
fake_data_tj

@Author  : Zuturn.Lee<zuturn.lee@gmail.com>
@Date    : 2020-02-04
@File    : fake_data_tj.py
@License : (C)Copyright 2020-2020 Zuturn Lee. All rights reserved.
"""
import random
import datetime
import os
import hashlib
import csv

data_dir = './fake_data'

if not os.path.exists(data_dir):
   os.mkdir(data_dir)

def main():
    cars = [(u'津A'+str(i)+'000000')[:7] for i in range(500000) ]
    pay_type = {c: (random.randint(30, 35) ,hashlib.md5(c.encode('utf-8')).hexdigest()) for c in cars }
    stations = [ str(i).zfill(4) for i in range(200) ]
    today = datetime.datetime.today()
    info = []
    for i in range(60):
        s = random.sample(cars, 10)
        t = today - datetime.timedelta(days=i)
        for c in s:
            at = t.replace(hour=random.randint(0,23), minute=random.randint(0, 59), second=random.randint(0, 59))
            lt = at + datetime.timedelta(minutes=random.randint(5, 30))
            pt = ((lt-at) * 0.8) + at
            amount = random.randint(200, 500)
            order_id = pt.strftime('%s')
            sta = random.sample(stations, 1)[0]
            ptype = pay_type[c]
            # 车牌, 到站时间, 离站时间, 支付时间, 加油站编号, 订单编号, 支付方式, 支付id(三方ID), 金额
            info.append((c, at, lt, pt, sta, order_id, ptype[0], ptype[1], '{:.2f}'.format(amount)))
    print(len(info))
    writer = csv.writer(open(os.path.join(data_dir, 'data.csv'),'w'))
    writer.writerows(info)

if __name__ == "__main__":
    main()
