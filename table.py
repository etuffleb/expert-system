# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    table.py                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: etuffleb <marvin@42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2022/01/26 17:39:50 by etuffleb          #+#    #+#              #
#    Updated: 2022/01/26 17:39:52 by etuffleb         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

variables = dict()
queries = dict()
rules = list()

class Table:
    def __init__(self):
        self._indexes = dict()
        self._table = list()
        self.edit_indexes()
        self.build()

    def edit_indexes(self):
        i = 0
        for v in variables:
            self._indexes.update({v: i})
            i += 1

    def variables_update(self, var_list, i, cols_variation):
        d = 0
        for v in var_list:            
            if variables[v]:
                continue
            var_list[v] = False
            for j in range(cols_variation):
                div = pow(2, d+1)
                if i % div >= (div / 2) and d == j:
                    var_list[v] = True
            d+=1

    def append_cases(self, len, n):
        variables_tmp = variables.copy()
        for i in range(len):
            case = list()
            self.variables_update(variables_tmp, i + 1, n)
            for v in variables_tmp:
                if variables[v]:
                    case.append(variables[v])
                else:
                    case.append(variables_tmp[v])
            self._table.append(case)


    def build(self):
        case = list()        
        n = 0
        for v in variables:
            if (variables[v]):
                case.append(True)
            else:
                case.append(False)
            if not variables[v]:
                n += 1

        self._table.append(case)
        self.append_cases(pow(2, n) - 1, n)
        self._table.sort(key=lambda val: sum(val))
