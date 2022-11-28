import config, excel, time

start_time = '2022-07-01'
end_time = '2022-11-25'
excel_name = 'Gerrit统计2022-11-25.xlsx'

if __name__ == "__main_":
    datas = excel.get_total_data(start_time, end_time, config.user_dict)
    excel.create_total_excel_file(datas, excel_name)
    time.sleep(3)
    excel.get_user_data(start_time, end_time, config.user_dict, excel_name)
