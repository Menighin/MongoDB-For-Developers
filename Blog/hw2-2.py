import pymongo

def remove_lowest_homework_score():

	# Connect to the db on standard port
	connection = pymongo.MongoClient("mongodb://localhost")

	# Attach to db
	db = connection.students   
	# Specify the collection        
	grades = db.grades        

	# Get the data filtered
	try:
		cursor = grades.find({}).sort([('student_id', pymongo.ASCENDING), ('score', pymongo.ASCENDING)])
	except Exception as e:
		print ("Error trying to read collection:", type(e), e)

	# Iterating and saving items for removing
	last_id = -1
	to_delete = []
	for data in cursor:
		if last_id != data['student_id'] and data['type'] == 'homework':
			to_delete.append(data['_id'])
			last_id = data['student_id']
			print(data)
			

	
	# Removing items
	print('Deleting {0} items...'.format(len(to_delete)))
	for item in to_delete:
		try:
			grades.delete_one({'_id' : item})
		except Exception as e:
			print ("Error trying to read collection:", type(e), e)

remove_lowest_homework_score()