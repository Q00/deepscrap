import json
import os


def make_json():

	name = input()

	file_list = os.listdir('../../result/result_file_'+name)

	file_list.sort()

	real_list = []

	for i in range(1, len(file_list)):
		if name in file_list[i] : real_list.insert(i,file_list[i])

	filenames = real_list

	with open('../../result/result_file_'+name,'w') as outfile:
		for fname in filenames:
			with open(fname) as infile:
				outfile.write(infile.read()+', \n')
				replace1 = infile.replace('{','[{',1)
				replace2 = replaceRight(replace1,',',']',1)

if __name__ == '__main__':
	make_json()