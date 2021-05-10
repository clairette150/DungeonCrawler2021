import csv

def make_csv(filename, data):
	with open(filename, 'w', encoding='utf-8') as data_file:
		# writer obj nicht vergessen!
		print("-- writing: data")
		writer = csv.writer(data_file, delimiter="|")
		writer.writerow(data)


def read_csv(filename):
	with open(filename, 'r', encoding='utf-8') as data_file:
		reader = csv.reader(data_file, delimiter='|')
		data = []
		for element in reader:
			data.append(element)
	return data


def add_csv(filename, new_data):
	with open(filename, 'a', encoding='utf-8') as data_file:
		writer = csv.writer(data_file, delimiter="|")
		writer.writerow(new_data)
