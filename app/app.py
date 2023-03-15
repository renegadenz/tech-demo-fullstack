from flask import Flask
from flask_restful import Api, Resource
from flask_restful_swagger import swagger

app = Flask(__name__)
api = Api(app)

class HelloWorld(Resource):
    @swagger.operation(
        notes='Get a greeting',
        parameters=[
            {
              "name": "name",
              "description": "Your name",
              "required": True,
              "type": "string",
              "in": "query"
            }
          ],
        responseMessages=[
            {
              "code": 200,
              "message": "Success"
            },
            {
              "code": 400,
              "message": "Bad Request"
            },
            {
              "code": 500,
              "message": "Internal Server Error"
            }
          ]
    )
    def get(self):
        return {'message': 'Hello, World!'}

api.add_resource(HelloWorld, '/')

if __name__ == '__main__':
    app.run(debug=True)
