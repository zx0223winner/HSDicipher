import os
import sys

# HSD_categories.py counts the number of HSDs with two, three, and more than four categories, which is helpful when evaluating the distribution of duplicate groups within HSDs
if len(sys.argv)!=4: #if the input arguments not 4, showing the usage.
    print("Usage:python3 HSD_categories.py <path to HSD species folder> <format of HSD file. e.g., 'txt' or 'tsv'> <output file name. e,g. species_groups.tsv>")
    sys.exit()

root = sys.argv[1]
folder = os.listdir(root)
folder.sort()
result_list = []
for file in sorted(folder):
	file_paths = os.path.join(root, file)
	if not os.path.isdir(file_paths) and file.split('.')[-1] == sys.argv[2]:
		with open (file_paths, 'r') as f:
			lines = f.read().split("\n")
			i = 0
			j = 0
			k = 0
			for line in lines:
				if line != "":
					array =line.split("\t")
					array2 = array[1].split("; ")
					if len(array2) == 2:
						i = i + 1
					elif len(array2) == 3:
						j =j + 1
					elif len(array2) >= 4:
						k = k + 1
		result_list.append(".".join(file.split('.')[:-1]) + '\t' + str(i) + '\t' + str(j) + '\t' + str(k))
		#print ("2-group: "+ str(i) + "\n" + "3-group: " + str(j) +'\n' + ">3-group: " + str(k) + '\n')
with open(os.path.join(root, sys.argv[3]), 'w') as out:
    out.write("File_name\t2-group_HSDs#\t3-group_HSDs#\t>=4-group_HSDs#\n")
    for r in result_list:
    	out.write(r + '\n')
