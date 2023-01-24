import pandas as pd

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)

service_para_dict = {"阿特拉斯": 1.15, "凯撒": 1.15, "英格索兰": 1.2, "复盛": 1.3}
por_dict = {"阿特拉斯": 0.98, "凯撒": 0.98, "英格索兰": 0.98, "复盛": 0.9}
year_running_time = 5040
actucal_pre = 0.75


def complete_data(air_dict):
    for row in air_dict:
        if row['brand'] in service_para_dict:
            row['ser_p'] = service_para_dict[row['brand']]
            row['por'] = por_dict[row['brand']]
        else:
            row['ser_p'] = 1.3
            row['por'] = 0.9
    return air_dict


def calculate_process(air_dict):
    return calculate_it_noneFC(air_dict) if not air_dict['isFC'] else calculate_it_FC(air_dict)


def read_dict(air_dict):
    no, model, run_time, load_time = air_dict['no'], air_dict['model'], air_dict['run_time'], air_dict['load_time']
    ori_power, air = air_dict['ori_power'], air_dict['air']
    brand, ori_pre, actual_pre = air_dict['brand'], air_dict['origin_pre'], air_dict['actucal_pre']
    ser_p = air_dict['ser_p']
    por = air_dict['por']
    d_val = round(ori_pre - actual_pre, 3)

    return [no, model, run_time, load_time, ori_power, air, brand, ori_pre, actual_pre, ser_p, d_val, por]


def calculate_it_noneFC(air_dict):
    dict_read = read_dict(air_dict)
    no, model, run_time, load_time = dict_read[0], dict_read[1], dict_read[2], dict_read[3]
    ori_power, air = dict_read[4], dict_read[5]
    brand, ori_pre, actual_pre = dict_read[6], dict_read[7], dict_read[8]
    ser_p = dict_read[9]
    # 空载浪费
    d_val = dict_read[10]

    empty_waste = round((run_time - load_time) / run_time * 0.4 * ori_power, 4)
    str_empty_waste = '(' + str(run_time) + '-' + str(load_time) + ')' + '/' + str(run_time) + '*40%' + '*' + str(
        ori_power) + '=' + str(empty_waste)

    # 工频压降浪费
    d_val_waste = round(ori_power * d_val * 0.07, 4)
    str_d_val_waste = str(ori_power) + '*' + '(' + str(d_val) + ')*7%=' + str(round(ori_power * d_val * 0.07, 3))

    # 总计浪费
    total_waste = round(empty_waste + d_val_waste, 4)
    # print(total_waste)

    por = float(round(load_time / run_time, 4))

    actual_energyE = round((float(ori_power) * float(ser_p) * por + empty_waste + d_val_waste) / (air * por), 2)
    str_actual_energyE = '(' + str(ori_power) + '*' + str(ser_p) + '*' + str(por) + '+' + str(
        total_waste) + ')/(' + str(air) + '*' + str(por) + ')=' + str(actual_energyE)
    print(no, brand, model, run_time, load_time, ori_power, air, d_val, '实加载比例：', str(por), '实用气量：',
          str(round(por * air, 4)), '实比功率：' + str(actual_energyE))
    isFccn = '变频 ' if air_dict['isFC'] else '工频'
    return [[str(no), model, str(run_time), str(load_time), str(ori_power), str_empty_waste, str_d_val_waste,
             str(total_waste), str_actual_energyE, round(por * air, 4)],
            [str(ori_power), str(air), str(ori_pre), str(actual_pre), str(model), str(brand)],
            [brand, model, ori_power, isFccn, actual_energyE, round(actual_energyE / 60, 4)]]


def calculate_it_FC(air_dict):
    dict_read = read_dict(air_dict)
    no, model, run_time, load_time = dict_read[0], dict_read[1], dict_read[2], dict_read[3]
    ori_power, air = dict_read[4], dict_read[5]
    brand, ori_pre, actual_pre = dict_read[6], dict_read[7], dict_read[8]
    ser_p = dict_read[9]
    por = dict_read[11]

    # 空载浪费
    d_val = dict_read[10]

    # 空载浪费
    empty_waste = 0
    str_empty_waste = '0'
    # 压降浪费
    d_val_waste = round(ori_power * d_val * 0.07, 4)
    d_cal_wast_por = 1 - round(d_val * 0.07, 4)
    str_d_val_waste = str(ori_power) + '*' + '(' + str(d_val) + ')*7%=' + str(round(ori_power * d_val * 0.07, 3))

    # 总计浪费
    total_waste = round(empty_waste + d_val_waste, 4)
    # print(total_waste)
    actual_energyE = round((float(ori_power) * ser_p * d_cal_wast_por) / (air * por), 2)
    str_actual_energyE = '(' + str(ori_power) + '*' + str(ser_p) + '*' + str(d_cal_wast_por) + ')/(' + str(
        air) + '*' + str(por) + ')=' + str(actual_energyE)
    print(no, brand, model, run_time, load_time, ori_power, air, d_val, '实加载比例：', str(por), '实用气量：',
          str(round(por * air, 4)), '实比功率：' + str(actual_energyE))
    isFccn = '变频 ' if air_dict['isFC'] else '工频'
    return [[str(no), model, str(run_time), str(load_time), str(ori_power), str_empty_waste, str_d_val_waste,
             str(total_waste), str_actual_energyE, round(por * air, 4)],
            [str(ori_power), str(air), str(ori_pre), str(actual_pre), str(model), str(brand)],
            [brand, model, ori_power, isFccn, actual_energyE, round(actual_energyE / 60, 4)]]


def originEC_to_dataframe(machine1, new_machine):
    machine1 = complete_data(machine1)
    no_list, type_list, run_list, load_list, ori_list = [], [], [], [], []
    empty_list, d_list, total_list, actual_list, ori_kw_list = [], [], [], [], []
    ori_pre_list, ori_air_list, act_air_list, act_pre_list = [], [], [], []
    ee_lists = []
    all_year_savings = 0
    ee_dicts = []
    for one in machine1:
        data_list, eq_list, ee_list = calculate_process(one)
        tmp_dict = {'brand': ee_list[0],
                    'model': ee_list[1],
                    'ori_power': ee_list[2],
                    'air': eq_list[1],
                    'isFC': ee_list[3],
                    'energy_con': ee_list[4],
                    'energy_con_min': round(ee_list[4] / 60, 4)
                    }
        ee_lists.append(tmp_dict)
        act_air_list.append(data_list[9])
        no_list += data_list[0]
        type_list.append(data_list[1])
        run_list.append(data_list[2])
        load_list.append(data_list[3])
        ori_list.append(data_list[4])
        empty_list.append(data_list[5])
        d_list.append(data_list[6])
        total_list.append(data_list[7])
        actual_list.append(data_list[8])

        ori_kw_list.append(eq_list[0])
        ori_pre_list.append(eq_list[2])
        ori_air_list.append(eq_list[1])
        act_pre_list.append(eq_list[3])

    all_table = pd.DataFrame({'空压机编号': no_list,
                              '原设备型号': type_list,
                              '运行时间': run_list,
                              '加载时间': load_list,
                              '额定功率': ori_list,
                              '空载浪费': empty_list,
                              '工频压降浪费': d_list,
                              '总计浪费': total_list,
                              '实际比功率': actual_list
                              })
    # print(all_table)
    ori_eq_table = pd.DataFrame({'No': no_list,
                                 '额定功率': ori_kw_list,
                                 '额定排量': ori_air_list,
                                 '额定压力': ori_pre_list,
                                 '实际运行压力': act_pre_list,
                                 '型号': type_list,
                                 })
    # print(ee_lists)
    # print(new_machine)
    for i in range(len(ee_lists)):
        saving = round(ee_lists[i]['energy_con'] - new_machine[i]['energy_con'], 4)
        saving_portion = round(saving / ee_lists[i]['energy_con'] * 100, 2)
        saving_per_hour = round(saving * act_air_list[i], 4)
        saving_per_year = round(saving_per_hour * year_running_time)
        # print(act_air_list[i],saving_per_hour,saving_per_year)

        all_year_savings += saving_per_year
        ee_lists[i]['saving_portion'] = saving_portion
        ee_lists[i]['saving_per_hour'] = saving_per_hour
        ee_lists[i]['saving_per_year'] = saving_per_year
        new_machine[i]['saving_portion'] = saving_portion
        new_machine[i]['saving_per_hour'] = saving_per_hour
        new_machine[i]['saving_per_year'] = saving_per_year

    for i in range(len(ee_lists)):
        ee_lists[i]['all_year_savings'] = all_year_savings
        new_machine[i]['all_year_savings'] = all_year_savings
        ee_dicts.append(new_machine[i])
        ee_dicts.append(ee_lists[i])

    ee_dicts_output = {}
    brand_d, model_d, ori_power_d, air_d, isFC_d, energy_con_d = [], [], [], [], [], []
    energy_con_min_d, saving_portion_d = [], []
    saving_per_hour_d, saving_per_year_d, all_year_savings_d = [], [], []
    # print(ee_dicts)
    for row in ee_dicts:
        brand_d.append(row['brand'])
        model_d.append(row['model'])
        ori_power_d.append(row['ori_power'])
        air_d.append(row['air'])
        isFC_d.append(row['isFC'])
        energy_con_d.append(row['energy_con'])
        energy_con_min_d.append(row['energy_con_min'])
        saving_portion_d.append(row['saving_portion'])
        saving_per_hour_d.append(row['saving_per_hour'])
        saving_per_year_d.append(row['saving_per_year'])
        all_year_savings_d.append(row['all_year_savings'])

    ee_dicts_output['品牌'] = brand_d
    ee_dicts_output['型号'] = model_d
    ee_dicts_output['功率'] = ori_power_d
    ee_dicts_output['气量'] = air_d
    ee_dicts_output['控制方式'] = isFC_d
    ee_dicts_output['实比功率'] = energy_con_d
    ee_dicts_output['均每立方耗电'] = energy_con_min_d
    ee_dicts_output['节点比例'] = saving_portion_d
    ee_dicts_output['小时节电'] = saving_per_hour_d
    ee_dicts_output['年节电'] = saving_per_year_d
    ee_dicts_output['年总节电'] = all_year_savings_d

    ee_pd_da = pd.DataFrame.from_dict(ee_dicts_output, orient='index')

    return all_table, ori_eq_table, ee_pd_da


def final_results_excel(machines, eqs):
    origin_final_table, origin_eq_table, energy_table = originEC_to_dataframe(machines, eqs)
    excel_writer = pd.ExcelWriter('空压机概况表.xlsx')
    origin_eq_table.to_excel(excel_writer, sheet_name="原有设备一览")
    origin_final_table.to_excel(excel_writer, sheet_name="原有设备能耗")
    energy_table.to_excel(excel_writer, sheet_name="能效对比")
    excel_writer.save()
