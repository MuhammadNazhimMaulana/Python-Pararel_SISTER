import random

# Function ini membuat sebuah kalkulasi sederhana, termasuk membuat list integer yang dipilih secara acak
def do_something(count,out_list):
	for i in range(count):
		out_list.append(random.random())

