# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    main.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: etuffleb <marvin@42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2022/01/26 17:39:58 by etuffleb          #+#    #+#              #
#    Updated: 2022/01/26 17:40:01 by etuffleb         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import argparse
from table import *
from parse import *

def print_result(answers, indexes):
    for q in queries:
        ans = answers[indexes[q]]
        if ans:
            print(q + " is" + "\033[32m\033[1m {}\033[0m" .format(str(ans)))
        else:
            print(q + " is" + "\033[31m\033[1m {}\033[0m" .format(str(ans)))

actions = {
    '+': lambda x, y: x and y,
    '|': lambda x, y: x or y,
    '^': lambda x, y: x != y,
    '>': lambda x, y: not (x and (not y)),
    '<': lambda x, y: x == y,
    }

def solve(table):
    for s in table._table:
        answers = []
        for rule in rules:
            neg = False
            stack = []
            if (rule == None):
                print('Error! there is no rules!')
                exit()
            for c in rule:
                if c == '!':
                    neg = True
                elif c in variables:
                    if neg:
                        stack.append(not s[table._indexes[c]])
                        neg = False
                    else:
                        stack.append(s[table._indexes[c]])
                elif c in actions:
                    x = stack.pop()
                    y = stack.pop()
                    u = actions[c](y, x)
                    stack.append(u)
                    #print("y=" + str(y) + " x=" + str(x) + " c=" + str(c) + " u=" + str(u))
            
            answers.append(stack[0])

        if sum(answers) == len(rules):
            return s
     
def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', dest="file_name")
    args = parser.parse_args()
    if args.file_name == None:
       print('Error! File name (using -f) must be given!')
       exit()

    parse_input_variables(args.file_name)
    parse_input_rules(args.file_name)
    
    # print(variables)
    # print(queries)
    # print(rules)
    table = Table()
    s = solve(table)
    # print(s)
    # print()
    if (s == None):
       print('Error! Conflicting conditions!')
       exit()
    print_result(s, table._indexes)

    

if (__name__ == '__main__'):
    main()
