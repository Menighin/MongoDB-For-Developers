import pymongo

def remove_lowest_homework_score():

	# Connect to the db on standard port
	connection = pymongo.MongoClient('mongodb://localhost')

	# Attach to db
	db = connection.school   
	# Specify the collection        
	students = db.students        

	# Get the data filtered
	try:
		cursor = students.find({})
	except Exception as e:
		print ('Error trying to read collection:', type(e), e)

	# Iterating and saving items for removing
	last_id = -1
	to_delete = []
	for student in cursor:
		scores = student['scores']
		scores.sort(key = lambda x: x['score'])
		to_remove = -1
		for i in range(len(scores)):
			if scores[i]['type'] == 'homework':
				to_remove = i
				break
		if to_remove != -1:
			del scores[to_remove]

		student['scores'] = scores
		students.update_one(
			{'_id': student['_id']},
			{'$set': {'scores': student['scores']}}, upsert=False)
	

remove_lowest_homework_score()