from flask import jsonify, request, session
from main import app
from MallGraph.Graph import generate_random_string,MakeGraph
from MallGraph.PathDrawer import Drawer

@app.route("/getPath",methods=["GET","POST"])
def getPath():

	if request.method=="POST":
		start=request.form.get("start")
		destination=request.form.get("destination")
		step1 = MakeGraph()
		step1.create_connections()
		values=step1.find_path(start, destination)
		filename=generate_random_string(10)+".png"
		step2=Drawer()
		step2.draw_for_floor_1(filename,values)

		return {"status":"ok",
			"1":{"img":"/static/"+filename,"floor":"1"},
			"2":{"img":"/static/"+"public/2.png","floor":"2"},
			"3":{"img":"/static/"+"public/3.png","floor":"3"},
			},200