#coding:gbk
"""
RPSLS游戏
作者：崔伟
2019/11/20
"""

print("欢迎使用RPSLS游戏")
print("----------------")
print("请输入您的选择:")

import random

def name_to_number(name):
	if name=="石头":
		return 0#因为不需要这个值，所以不用print出来
	elif name=="史波克":
		return 1
	elif name=="纸":
		return 2
	elif name=="蜥蜴":
		return 3
	elif name=="剪刀":
		return 4


def number_to_name(number):
	if number==0:
		return '石头'#因为不需要这个值，所以不用print出来
	elif number==1:
		return '史波克'
	elif number==2:
		return '纸'
	elif number==3:
		return '蜥蜴'
	elif number==4:		
		return '剪刀'

def rpsls(player_choice):
	print("您的选择是",player_choice)
player_choice=input()
rpsls(player_choice)
player_choice_number=name_to_number(player_choice)


comp_number=random.randrange(0,4)
comp_choice=number_to_name(comp_number)
print("计算机的选择是",comp_choice)

print("---------")


result=(comp_number-player_choice_number)
if result==-4 or result==-3 or result==1 or result==2:
	print("计算机赢了")
elif result==0:
	print("平局")
else:
	print("您赢了")













	
		
		
