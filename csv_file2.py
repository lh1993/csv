#!/usr/bin/python
# -*- coding:utf-8 -*-

import csv

rows = [{'Column1': '0', 'Column2': '1', 'Column3': '2', 'Column4': '3'},
        {'Column1': '0', 'Column2': '1', 'Column3': '2', 'Column4': '3'},
        {'Column1': '0', 'Column2': '1', 'Column3': '2', 'Column4': '3'},
        {'Column1': '0', 'Column2': '1', 'Column3': '2', 'Column4': '3'},
        {'Column1': '0', 'Column2': '1', 'Column3': '2', 'Column4': '3'}]

header = rows[0].keys()
print sorted(header)

# 打开文件使用二进制可以避免换行问题
with open('dictcsv.csv', 'wb') as f:
    dict_write = csv.DictWriter(f, sorted(header))
    dict_write.writeheader()
    dict_write.writerows(rows)

f.close()

