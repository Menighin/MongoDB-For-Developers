import pymongo

def process_images():

	# Connect to the db on standard port
	connection = pymongo.MongoClient('mongodb://localhost')

	# Attach to db
	db = connection.finalExam   
	# Specify the collections     
	albums = db.albums       
	images = db.images 

	# Iterating 
	cursor = albums.find()
	i = 0
	not_orphan = set()
	for album in cursor:
		for image in album['images']:
			not_orphan.add(image)

	# Removing orphans
	cursor = images.find()
	to_delete = []
	for image in cursor:
		if image['_id'] not in not_orphan:
			to_delete.append(image['_id'])

	images.delete_many({'_id': {'$in': to_delete}})
	
if __name__ == '__main__':
	process_images()