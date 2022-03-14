from flask import Flask
#request allows us to put
from flask_restful import Api, Resource, reqparse, abort

app = Flask(__name__)
api = Api(app)


#make request parser object, automaticly parse through the object
#that is being sent, and make sure it fits the guidlines below
video_put_args = reqparse.RequestParser()
#help sends to user a message if we don't send what it wants
video_put_args.add_argument("name", type=str, help= "Name of the video is required", required=True)
video_put_args.add_argument("views", type=int, help= "Views of the video", required=True)
video_put_args.add_argument("likes", type=int, help= "Likes on the video", required=True)


videos = {}

def abort_if_video_id_doesnt_exist(video_id):
	if video_id not in videos:
		abort(404, message="Could not find video...")

def abort_if_video_exists(video_id):
	if video_id in videos:
		abort(409, message="Video already exists with that ID...")

class Video(Resource):
	def get(self, video_id):
		abort_if_video_id_doesnt_exist(video_id)
		return videos[video_id]

	def put(self, video_id):
		abort_if_video_exists(video_id)
		args = video_put_args.parse_args()#get arguments above
		#print(request.form)
		#print(request.form) gets a form of the request
		#argument parcles
		videos[video_id] = args #where args is a dictionary
		return videos[video_id], 201

	def delete(self, video_id):
		abort_if_video_id_doesnt_exist(video_id)
		del videos[video_id]
		return '', 204



#register as a resource
api.add_resource(Video, "/video/<int:video_id>")

if __name__ == "__main__":
	app.run(debug=True)