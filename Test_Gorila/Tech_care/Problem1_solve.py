def special_data_table( number_of_slots, values, find_item ) :
	####### DO NOT MODIFY BELOW #######
	myTable = MySpecialTable(number_of_slots)
	for val in values:
		myTable.add_item(val)

	return myTable.find_item(find_item)
	####### DO NOT MODIFY ABOVE #######

class MySpecialTable():
		def __init__(self, slots):
			self.slots = slots
			self.table = []
			self.create_table()

		def hash_key(self, value):
			return value % self.slots

		def create_table(self):
			for _ in range(self.slots):
				self.table.append([])

		def add_item(self, value):
			key = self.hash_key(value)
			self.table[key].append(value)

		def find_item(self, item):
			key = self.hash_key(item)
			if item in self.table[key]:
				return key
			else:
				return -1


'''

def special_data_table(number_of_slots, values, find_item):
    myTable = MySpecialTable(number_of_slots)
    for val in values:
        myTable.add_item(val)

    return myTable.find_item(find_item)


# Example usage:
number_of_slots = 3
values = [1, 2, 5, 7, 9]
find_item = 3

output = special_data_table(number_of_slots, values, find_item)
print(output)
'''