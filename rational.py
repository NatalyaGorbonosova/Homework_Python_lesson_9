import re
from tkinter import messagebox
def rational(math_note):
    def text_in_list(text):
        new_text = text.replace(' ', '')
        if new_text[0] == '-': i =1
        else: i = 0
        list_operate = ['+', '-', '*', '/', '(', ')']
        while i < len(new_text):
            if new_text[i] in list_operate:
                new_text = new_text[0:i] + ' ' + new_text[i] + ' ' + new_text[i+1:len(new_text)]
                i += 2
            else: i += 1
        list_el = re.split(r' ', new_text) 
        for e in list_el:
            if e == '': list_el.pop(list_el.index(e))    
        return list_el
    def find_ind_operation(operate, list):
        for i in range(len(list)):
            ind_op = -1
            if list[i] == operate:
                ind_op = i
                break
        return ind_op
    def find_mult_div(list):
        while '*' in list or '/' in list:
            ind_m = find_ind_operation('*', list)
            ind_d = find_ind_operation('/', list)
            if ind_m != -1 and ind_d == -1:
                result = float(list[ind_m - 1]) * float(list[ind_m + 1])
                list[ind_m] = str(result)
                list.pop(ind_m - 1)
                list.pop(ind_m )
            if ind_d != -1 and ind_m == -1:
                result = float(list[ind_d - 1]) / float(list[ind_d + 1])
                list[ind_d] = str(result)
                list.pop(ind_d - 1)
                list.pop(ind_d)
            if ind_m != -1 and ind_d != -1:
                if ind_m < ind_d:
                    result = float(list[ind_m - 1]) * float(list[ind_m + 1])
                    list[ind_m] = str(result)
                    list.pop(ind_m - 1)
                    list.pop(ind_m )
                elif ind_m > ind_d:
                    result = float(list[ind_d - 1]) / float(list[ind_d + 1])
                    list[ind_d] = str(result)
                    list.pop(ind_d - 1)
                    list.pop(ind_d)
        return list
    def find_sum_sub(list):
        while '+' in list or '-' in list:
            ind_sum = find_ind_operation('+', list)
            ind_sub = find_ind_operation('-', list)
            if ind_sum != -1 and ind_sub == -1:
                result = float(list[ind_sum - 1]) + float(list[ind_sum + 1])
                list[ind_sum] = str(result)
                list.pop(ind_sum - 1)
                list.pop(ind_sum )
            if ind_sub != -1 and ind_sum == -1:
                result = float(list[ind_sub - 1]) - float(list[ind_sub + 1])
                list[ind_sub] = str(result)
                list.pop(ind_sub - 1)
                list.pop(ind_sub )
            if ind_sum != -1 and ind_sub != -1:
                if ind_sum < ind_sub:
                    result = float(list[ind_sum - 1]) + float(list[ind_sum + 1])
                    list[ind_sum] = str(result)
                    list.pop(ind_sum - 1)
                    list.pop(ind_sum )
                elif ind_sub < ind_sum:
                    result = float(list[ind_sub - 1]) - float(list[ind_sub + 1])
                    list[ind_sub] = str(result)
                    list.pop(ind_sub - 1)
                    list.pop(ind_sub )
        return list
    def find_staples(list):
        while '(' in list:
            ind_first_st = find_ind_operation('(', list)
            ind_second_st = find_ind_operation(')', list)
            new_list = []
            for i in range(ind_first_st + 1, ind_second_st):
                new_list.append(list[i])
            new_list = find_mult_div(new_list)
            new_list = find_sum_sub(new_list)
            list[ind_first_st] = new_list[0]
            for i in range(ind_first_st+1, ind_second_st+1):
                list[i] = ''
            i = 0
            while i < len(list):
                if list[i] == '': list.pop(i)
                else: i += 1
        return list
    try:
        list_note = text_in_list(math_note)
        list_note = find_staples(list_note)
        list_note = find_mult_div(list_note)
        list_note = find_sum_sub(list_note)
        return list_note[0]
    except: messagebox.showerror("Error!", "Check the correctness of data")
    