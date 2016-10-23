import bottle
import pymongo

@bottle.route('/')
def index():

	# Open connection with MongoDB
	connection = pymongo.MongoClient('localhost', 27017)

	# Connect to test database
	db = connection.test

	# Get handle of names collection
	name = db.names

	# Get an item from the collection
	item = name.find_one();

	return '<b>Hello {}</b>!'.format(item['name'])

bottle.run(host='localhost', port=8080)