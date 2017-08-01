#!/usr/bin/env pyhon3
#-*- coding:utf-8 -*-
H=input('请输入你的身高（m）:')
H=float(H)
W=input('请输入你的体重(kg):')
W=float(W)
BMI=W/(H**2)
Result=int(BMI)
if Result<18.5:
	print('您的体重过轻')
elif Result>=18.5 and Result<25:
	print('您的体重正常')
elif Result>=25 and Result<28:
	print('您的体重过重')
elif Result>=28 and Result<32:
	print('您的体型肥胖')
else:
	print('您的体型严重肥胖')