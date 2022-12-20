from collections import namedtuple

from flask import Flask, render_template, request
from cal_func import *
import csv
import pandas as pd

app = Flask(__name__)


@app.route('/')  # 跳转之前的页面函数
def record():
    return render_template('record.html')


@app.route('/result', methods=["POST", "GET"])
def result():
    if request.method == "POST":
        results = request.form
        save = {
            'no': results.get('no'),  # 编号
            'model': results.get('model'),  # 型号
            'run_time': results.get('run_time'),  # 运行时间
            'load_time': results.get('load_time'),
            'ori_power': results.get('ori_power'),  # 额定功率
            'air': results.get('air'),  # 气量
            'brand': results.get('brand'),  # 品牌
            'isFC': results.get('isFC'),  # 变频：1 非变频：0
            'origin_pre': results.get('origin_pre'),  # 额定压力
            'actucal_pre': results.get('actucal_pre'),  # 实际压力
        }
        with open('test.csv', 'a', newline='') as f:
            writer = csv.writer(f)
            for row in save.items():
                writer.writerow(row)
        return render_template("result.html", result=results)


@app.route('/generate', methods=["POST", "GET"])
def generate():#TODO
    new_eq = [
        {'brand': '捷豹',
         'model': 'ZLS150-2iG',
         'ori_power': '110',
         'air': '23.2',
         'isFC': '变频',
         'energy_con': 5.9,
         'energy_con_min': round(5.9 / 60, 4)
         },
        {'brand': '捷豹',
         'model': 'ZLS150-2iG',
         'ori_power': '110',
         'air': '23.2',
         'isFC': "变频",
         'energy_con': 5.9,
         'energy_con_min': round(5.9 / 60, 4)}]
    if request.method == "POST":
        all_list = []
        with open('test.csv') as f:
            f_csv = csv.reader(f)
            i = 0
            dict_save_all = {}
            for row in f_csv:
                i += 1
                dict_save_all[row[0]] = row[1]
                if i is 9:
                    all_list.append(dict_save_all)
                    i = 0
        final_results_excel(all_list, new_eq)

    return render_template("generate.html", result='')


if __name__ == '__main__':
    app.run(debug=True)
