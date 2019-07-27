fin = open("heatmap_data.txt", "r")

use_heat = []
exp_heat = []
for line in fin:
	line = line.lstrip().lstrip("%").lstrip().rstrip().rstrip("&").rstrip()
	tokens = line.split("  &  ")
	use = []
	exp = []
	avg_use = 0.0
	avg_exp = 0.0
	for i in range(0, len(tokens)):
		tokens2 = tokens[i].split("*")
		use.append(float(tokens2[0])/1000)
		exp.append(float(tokens2[1])/1000)
		avg_use += float(tokens2[0])/1000
		avg_exp += float(tokens2[1])/1000
	use.append(avg_use / (len(tokens) - 1))
	exp.append(avg_exp / (len(tokens) - 1))
	use_heat.append(use)
	exp_heat.append(exp)

fout = open("use_out.txt", "w")
fout2 = open("exp_out.txt", "w")

fout.write("STORAGE,LOCATION,PHONE,CONTACT,CAMERA,MIC,SMS,CALENDAR,non-Diag\n")
fout2.write("STORAGE,LOCATION,PHONE,CONTACT,CAMERA,MIC,SMS,CALENDAR,non-Diag\n")

arraylist = ["STORAGE", "LOCATION", "PHONE", "CONTACT", "CAMERA", "MIC", "SMS", "CALENDAR", "non-Diag"]

for i in range(0, 9):
	fout.write(arraylist[i] + ", ")
	fout2.write(arraylist[i] + ", ")
	use_array = use_heat[i]
	exp_array = exp_heat[i]
	print(len(use_array))
	for j in range(0, len(use_array)):
		if j != len(use_array) - 1:
			fout.write("%.2f" % use_array[j] + ",")
		else:
			fout.write("%.2f" % use_array[j] + "\n")
	for j in range(0, len(exp_array)):
		if j != len(exp_array) - 1:
			fout2.write("%.2f" % exp_array[j] + ",")
		else:
			fout2.write("%.2f" % exp_array[j] + "\n")

fout.close()
fout2.close()

	
