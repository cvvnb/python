#coding:gbk
"""
RPSLS��Ϸ
���ߣ���ΰ
2019/11/20
"""

print("��ӭʹ��RPSLS��Ϸ")
print("----------------")
print("����������ѡ��:")

import random

def name_to_number(name):
	if name=="ʯͷ":
		return 0#��Ϊ����Ҫ���ֵ�����Բ���print����
	elif name=="ʷ����":
		return 1
	elif name=="ֽ":
		return 2
	elif name=="����":
		return 3
	elif name=="����":
		return 4


def number_to_name(number):
	if number==0:
		return 'ʯͷ'#��Ϊ����Ҫ���ֵ�����Բ���print����
	elif number==1:
		return 'ʷ����'
	elif number==2:
		return 'ֽ'
	elif number==3:
		return '����'
	elif number==4:		
		return '����'

def rpsls(player_choice):
	print("����ѡ����",player_choice)
player_choice=input()
rpsls(player_choice)
player_choice_number=name_to_number(player_choice)


comp_number=random.randrange(0,4)
comp_choice=number_to_name(comp_number)
print("�������ѡ����",comp_choice)

print("---------")


result=(comp_number-player_choice_number)
if result==-4 or result==-3 or result==1 or result==2:
	print("�����Ӯ��")
elif result==0:
	print("ƽ��")
else:
	print("��Ӯ��")













	
		
		
