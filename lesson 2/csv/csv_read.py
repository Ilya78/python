import csv
import re
import os

match_dict = dict(os_prod_list='Изготовитель системы',
                  os_name_list='Название ОС',
                  os_code_list='Код продукта',
                  os_type_list='Тип системы'
                  )
main_list = [['Изготовитель системы', 'Название ОС', 'Код продукта', 'Тип системы']]
os_prod_list = []
os_name_list = []
os_code_list = []
os_type_list = []

def get_data():

        for file in os.listdir("./"):
            if file.endswith(".txt"):
                with open(file) as f_n:
                    f_n_reader = csv.reader(f_n)

                    for row in f_n_reader:
                        for key in match_dict:
                            match = re.search(match_dict[key], ''.join(row))
                            new_list = ''.join(row).split(":")

                            if match:
                                if key == 'os_prod_list':
                                    os_prod_list.append(new_list[1])
                                    #main_list.append(os_prod_list)
                                if key == 'os_name_list':
                                    os_name_list.append(new_list[1])
                                    #main_list.append(os_name_list)
                                if key == 'os_code_list':
                                    os_code_list.append(new_list[1])
                                    #main_list.append(os_code_list)
                                if key == 'os_type_list':
                                    os_type_list.append(new_list[1])
                                    #main_list.append(os_type_list)

        main_list.extend(os_prod_list)

        return main_list

def write2csv(cvs_file_name):
    list2cvs = get_data()
    with open(cvs_file_name, 'w') as f_n:
        f_n_writer = csv.writer(f_n)
        f_n_writer.writerows(list2cvs)

    return 0


write2csv('result.csv')
