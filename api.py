from flask import Flask, request
from flask_restful import Api, Resource

from lib.redis_client import RedisClient

app = Flask(__name__)
api = Api(app)

class Test(Resource):
    def get(self):
        return {"success": "true"}, 200

class InsertAccountInCategory(Resource):
	def post(self):
		RedisClient().insert_into_a_category(
			request.form['category'], request.form['account_id'], request.form['domain']
		)
		return { "success": "true" }, 201

	def get(self):
		data = RedisClient().get_category_data(request.form['category'])
		if data:
			return data, 200
		else:
			return '', 404

api.add_resource(InsertAccountInCategory, "/category")

if __name__ == "__main__":
	app.run(debug=True)