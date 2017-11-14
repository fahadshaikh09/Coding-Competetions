"""
	PROBLEM STATMENT:
	Lazy Bartender
	there are N number of possible drinks (n1, n2, ...)
	has C number of fixed customers
	every customer has fixed set of favourite drinks
	bartender has to create least possible number of drinks to suffice need of all customers

	Example :

	"cust1" : "n3", "n7", "n5", "n2", "n9"
	"cust2" : "n5"
	"cust3" : "n2", "n3"
	"cust4" : "n4"
	"cust5" : "n3", "n4", "n3", "n5", "n7", "n4"

	Output :
	3 ["n3", "n4", "n5"]

"""
from collections import defaultdict
from pprint import pprint

def find_max(data_dict):
	max_key = None
	max_len = float('-inf')

	for key, value in data_dict.iteritems():
		if len(value) > max_len:
			max_key = key
			max_len = len(value)

	return max_key

def make_pivot_data(input_data):
	pivot_data = defaultdict(set)
	for cust, drinks in input_.iteritems():
		for d in drinks:
			pivot_data[d].add(cust)

	return pivot_data

def lazy_bartender(input_data):
	pivot_data = make_pivot_data(input_data)

	result = []
	sufficed_customers = set()

	while True:

		max_key = find_max(pivot_data)
		result.append(max_key)
		max_key_values = pivot_data[max_key]

		sufficed_customers = sufficed_customers | max_key_values #adding 2 sets

		if len(sufficed_customers)==len(input_data):
			break

		for k, v in pivot_data.iteritems():
			pivot_data[k] = pivot_data[k].difference(max_key_values)

		del pivot_data[max_key]
		
	return result

if __name__ == '__main__':
	input_ = {
		"cust1" : ["n3", "n7", "n5", "n2", "n9"],
		"cust2" : ["n5"],
		"cust3" : ["n2", "n3"],
		"cust4" : ["n4"],
		"cust5" : ["n3", "n4", "n3", "n5", "n7", "n4"]
	}

	result = lazy_bartender(input_)
	print len(result), result