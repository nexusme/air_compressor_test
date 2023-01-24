from cal_func import *

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)

if __name__ == '__main__':
    machines = [{
        'no': 1,  # 编号
        'model': 'BSG-50A',  # 型号
        'run_time': 36417,  # 运行时间
        'load_time': 10872,
        'ori_power': 37,  # 额定功率
        'air': 6.3,  # 气量
        # 'd_val': 0.35,  # 压降
        'brand': '博世格',  # 品牌
        'isFC': 0,  # 变频：1 非变频：0
        'origin_pre': 8,  # 额定压力
        'actucal_pre': 7,  # 实际压力
    }


    ]
    new_eq = [
        {'brand': '捷豹',
         'model': 'ZLS50-2iG',
         'ori_power': '37',
         'air': '7.1',
         'isFC': '变频',
         'energy_con': 6.36,
         'energy_con_min': round(6.36 / 60, 4)
         },

    ]

    final_results_excel(machines, new_eq)
