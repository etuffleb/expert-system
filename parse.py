# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    parse.py                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: etuffleb <marvin@42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2022/01/26 17:39:41 by etuffleb          #+#    #+#              #
#    Updated: 2022/01/26 17:39:43 by etuffleb         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from main import *
from parse import *

def pol_notation(input):
    priority = ["!","+","|","^",">","<","(",")"]
    p_stack = []
    out = ""
    for i in input:
        if i not in priority:
            out += i
        else:
            if not p_stack:
                p_stack.append(i)
            elif i == "(":
                p_stack.append(i)
            elif i == ")":
                while p_stack[-1] != "(":
                    out += p_stack.pop()
                p_stack.pop()
            elif priority.index(p_stack[-1]) > priority.index(i):
                p_stack.append(i)
            elif priority.index(p_stack[-1]) <= priority.index(i):
                while p_stack and priority.index(p_stack[-1]) <= priority.index(i):
                    out += p_stack.pop()
                if not p_stack:
                    p_stack.append(i)
                # on or off?
                # elif priority.index(p_stack[-1]) > priority.index(i):
                #     p_stack.append(i)
    while p_stack:
        out += p_stack.pop()
    return out

def set_true(a):
    for v in a:
        variables.update({v: True})

def updete_vars(nn):
    for n in nn:
        n = n.strip(' ')
        if len(n) == 1:
            variables.update({n: False})
        elif n.startswith("!") and len(n) == 2:
            variables.update({n.strip('!'): False})
        elif len(n) > 2:
            sp = n.replace(' ', '')
            for s in sp:
                if s.isalpha():
                    variables.update({s: False})

                    
def parse_expresions(a):
    updete_vars(a.split('+'))
    updete_vars(a.split('|'))
    updete_vars(a.split('^'))

def parse_input_variables(path):
    f = open(path, "r")
    lines = f.readlines()
    flag = False
    for line in lines:
        if line.startswith("#"):
            continue
        if not flag:            
            l = line.strip('\n')
            l = l.split('#')[0]
            split = l.split('=')
            if len(split) < 2:
                flag = True
                continue
            a = split[0].strip('<').strip(' ')
            b = split[1].strip('>').strip(' ')
            parse_expresions(a)
            parse_expresions(b)
        else:
            line = line.split('#')[0].strip(' ')
            if line.startswith("="):
                set_true(line.strip('=').strip('\n').strip(' '))
            elif line.startswith("\n"):
                continue
            elif line.startswith("?"):
                for v in line.strip('?').strip('\n').strip(' '):
                    if v in variables:
                        queries.update({v: variables[v]})
                    else:
                        print('Error! There is no initial facts or expresions for ' + v)
                        exit()
        
def add_rule(l, r, e):
    l = l.replace(' ', '').replace('\t', '')
    r = r.replace(' ', '').replace('\t', '')
    rules.append(pol_notation(l + e + r))

def parse_input_rules(path):
    f = open(path, "r")
    lines = f.readlines()
    flag = False
    for line in lines:
        if line.startswith("#") or line == " ":
            continue
        if line.startswith("\n"):
            break
        l = line.strip('\n')
        l = l.split('#')[0]
        l = l.strip(' ')
        if "=>" in l:
            split = l.split("=>")
            left = split[0].strip(' ')
            right = split[1].strip(' ')
            add_rule(left, right, ">")
        elif "<=>" in l:
            split = l.split("<=>")
            left = split[0].strip(' ')
            right = split[1].strip(' ')
            add_rule(left, right, "<")
        else:
            print('Error! Rules should contains \'=>\' or \'<=>\'')
            exit()

