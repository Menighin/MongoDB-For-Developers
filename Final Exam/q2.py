import pymongo

def filter_messages():

	# Connect to the db on standard port
	connection = pymongo.MongoClient('mongodb://localhost')

	# Attach to db
	db = connection.enron   
	# Specify the collection        
	messages = db.messages        

	# Get the data filtered
	pipeline = [
		{ '$unwind': '$headers.To' },
		{ '$project': { 'from': '$headers.From', 'to' : '$headers.To', '_id' : '$filename' } }
	]

	# Iterating and filtering
	unique_set = set()
	conversation_talks = {}
	for message in list(messages.aggregate(pipeline)):
		set_key = message['_id'] + '_' + message['from'] + '_' + message['to']
		key = message['from'] + '_' + message['to']

		if set_key not in unique_set:
			unique_set.add(set_key)

			if key not in conversation_talks:
				conversation_talks[key] = 1
			else:
				conversation_talks[key] += 1
	
	# Getting pairs who talked most
	max = 0
	pair = ""
	for k, v in conversation_talks.items():
		if v > max:
			max = v;
			pair = k

	print(pair + ': ' + str(max))
	
if __name__ == '__main__':
	filter_messages()