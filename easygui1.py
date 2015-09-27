import easygui as g
import sys

while 1:
	g.msgbox("嗨，这是第一个界面游戏")

	msg="请问你希望学到什么？"
	title="小游戏互动"
	chioces = ["谈恋爱","编程","xxoo","氢气书画"]

	choice=g.choicebox(msg,title,choices)
	g.msgbox("你的选择是:" +str(choice),"结果"）
	msg="你想希望重新开始游戏嘛？"
	title="请选择"

	if g.ccbox(msg,title):
		pass
	else:
		sys.exit(0)

