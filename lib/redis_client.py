import redis

class RedisClient:
	def __init__(self):
		self.connection = redis.Redis(host='localhost', port=6379, decode_responses=True)

	def insert_into_a_category(self, category, account_id, domain):
		self.connection.hset(category, account_id, domain)

	def get_category_data(self, category):
		return self.connection.hgetall(category)