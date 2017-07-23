#!/usr/bin/python
# -*- coding:utf-8 -*-

import csv

# 写入csv文件
def csv_writer(data, filename):
    with open(filename, 'wb') as csv_file:
        writer = csv.writer(csv_file, delimiter=',')
        for wline in data:
            writer.writerow(wline)

# 读取csv文件
def csv_reader(filename):
    with open(filename, 'rb') as f:
        reader = csv.reader(f)
        for rline in reader:
            print rline

# 使用DictReader查找csv文件中的某条记录
def csv_select(filename):
    with open(filename, 'rb') as f:
        reader = csv.DictReader(f)
        for sline in reader:
            # print sline
            if sline['mem'] in ['16g', '32g']:
                print sline

if __name__ == "__main__":
    data = []
    with open("data.txt") as f:
        for line in f:
            data.append(line.strip().split(','))
    # print data
    filename = 'output.csv'
    csv_writer(data, filename)
    csv_reader(filename)
    csv_select(filename)
