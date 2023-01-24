from cal_func import *

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)

if __name__ == '__main__':
    machines = [{
        'no': 1,  # 编号
        'model': 'DSD241',  # 型号
        'run_time': 80644,  # 运行时间
        'load_time': 69589,
        'ori_power': 132,  # 额定功率
        'air': 20.3,  # 气量
        # 'd_val': 0.35,  # 压降
        'brand': '凯撒',  # 品牌
        'isFC': 0,  # 变频：1 非变频：0
        'origin_pre': 1.1,  # 额定压力
        'actucal_pre': 0,  # 实际压力
    }
        ,
        {
            'no': 2,  # 编号
            'model': 'DSD241',  # 型号
            'run_time': 105920,  # 运行时间
            'load_time': 91201,
            'ori_power': 132,  # 额定功率
            'air': 20.3,  # 气量
            'brand': '凯撒',  # 品牌
            'isFC': 0,  # 变频：1 非变频：0
            'origin_pre': 1.1,  # 额定压力
            'actucal_pre': 0,  # 实际压力
        }

    ]
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
         'energy_con_min': round(5.9 / 60, 4)}
    ]

    final_results_excel(machines, new_eq)
