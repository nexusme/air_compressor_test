from cal_func import *

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)

if __name__ == '__main__':
    actucal_pre = 0.75
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
        'actucal_pre': actucal_pre,  # 实际压力
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
            'actucal_pre': actucal_pre,  # 实际压力
        },
        {
            'no': 3,  # 编号
            'model': 'DSD201',  # 型号
            'run_time': 88103,  # 运行时间
            'load_time': 52861,
            'ori_power': 110,  # 额定功率
            'air': 16.1,  # 气量
            'brand': '凯撒',  # 品牌
            'isFC': 0,  # 变频：1 非变频：0
            'origin_pre': 1.2,  # 额定压力
            'actucal_pre': actucal_pre,  # 实际压力
        },
        {
            'no': 4,  # 编号
            'model': 'DSD201',  # 型号
            'run_time': 111565,  # 运行时间
            'load_time': 94439,
            'ori_power': 110,  # 额定功率
            'air': 16.1,  # 气量
            'brand': '凯撒',  # 品牌
            'isFC': 0,  # 变频：1 非变频：0
            'origin_pre': 1.2,  # 额定压力
            'actucal_pre': actucal_pre,  # 实际压力
        },
        {
            'no': 5,  # 编号
            'model': 'SA120A',  # 型号
            'run_time': 30503,  # 运行时间
            'load_time': 21762,
            'ori_power': 120,  # 额定功率
            'air': 22,  # 气量
            'brand': '复盛',  # 品牌
            'isFC': 0,  # 变频：1 非变频：0
            'origin_pre': 1,  # 额定压力
            'actucal_pre': actucal_pre,  # 实际压力
        },
        {
            'no': 6,  # 编号
            'model': 'SA120A',  # 型号
            'run_time': 15499,  # 运行时间
            'load_time': 10898,
            'ori_power': 120,  # 额定功率
            'air': 22,  # 气量
            'brand': '复盛',  # 品牌
            'isFC': 0,  # 变频：1 非变频：0
            'origin_pre': 1,  # 额定压力
            'actucal_pre': actucal_pre,  # 实际压力
        },

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
         'energy_con_min': round(5.9 / 60, 4)},
        {'brand': '捷豹',
         'model': 'ZLS125-2iG',
         'ori_power': '90',
         'air': '19.3',
         'isFC': "变频",
         'energy_con': 6,
         'energy_con_min': round(6 / 60, 4)},
        {'brand': '捷豹',
         'model': 'ZLS125-2iG',
         'ori_power': '90',
         'air': '19.3',
         'isFC': "变频",
         'energy_con': 6,
         'energy_con_min': round(6 / 60, 4)},
        {'brand': '捷豹',
         'model': 'ZLS150-2iG',
         'ori_power': '110',
         'air': '23.2',
         'isFC': "变频",
         'energy_con': 5.9,
         'energy_con_min': round(5.9 / 60, 4)},
        {'brand': '捷豹',
         'model': 'ZLS150-2iG',
         'ori_power': '110',
         'air': '23.2',
         'isFC': "变频",
         'energy_con': 5.9,
         'energy_con_min': round(5.9 / 60, 4)}
    ]

    final_results_excel(machines, new_eq)
