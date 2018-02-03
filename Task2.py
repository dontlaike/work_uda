"""
下面的文件将会从csv文件中读取读取短信与电话记录，
你将在以后的课程中了解更多有关读取文件的知识。
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
任务2: 哪个电话号码的通话总时间最长? 不要忘记，用于接听电话的时间也是通话时间的一部分。
输出信息:
"<telephone number> spent the longest time, <total time> seconds, on the phone during
September 2016.".

提示: 建立一个字典，并以电话号码为键，通话总时长为值。
这有利于你编写一个以键值对为输入，并修改字典的函数。
如果键已经存在于字典内，为键所对应的值加上对应数值；
如果键不存在于字典内，将此键加入字典，并将它的值设为给定值。
"""

dic_number_call={}
def add_dic(number,time):
	if number in dic_number_call:
		dic_number_call[number]+=int(time)
	else:
		dic_number_call[number]=int(time)
			
def get_num(): 
	"""
	获取所有电话通话总时长
	"""
	for call in calls:
		add_dic(call[0],call[3])
		add_dic(call[1],call[3])
	
	"""
	取得最长通话记录的电话号码
	"""
	most_number=[]
	num_time=0
	for number in dic_number_call:
		if num_time<dic_number_call[number]:
			most_number=[]
			num_time=dic_number_call[number]
			most_number.append(number)
		elif num_time==dic_number_call[number] and not (number in most_number):
			most_number.append(number)
	if len(most_number)==1:
		return "{0} spent the longest time, {1} seconds, on the phone during September 2016.".format(most_number[0],num_time)
	else:
		for i in range(len(most_number)):
			return "{0} spent the longest time, {1} seconds, on the phone during September 2016.".format(most_number[i],num_time)
	
print(get_num())