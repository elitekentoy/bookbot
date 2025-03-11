def get_num_words(text):
	words = text.split()
	count = len(words)
	return count

def sort_on(dict):
	return dict["count"]

def get_occurence_count(text):
	words = text.split()
	records = {}

	for word in words:
		for character in word:
			lowered_character = character.lower()
			if lowered_character in records:
				records[lowered_character] += 1
			else:
				records[lowered_character] = 1

	return records

def sort(dictionary):
	list = []
	for key,value in dictionary.items():
		record = {
			"character": key,
			"count" : value
		}
		list.append(record)
	list.sort(reverse=True, key=sort_on)
	return list