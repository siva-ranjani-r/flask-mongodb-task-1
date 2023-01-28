from flask import Flask, render_template,request,json
from pymongo import MongoClient
import csv


app=Flask(__name__)
client=MongoClient("mongodb://127.0.0.1:27017" )

# header=["name","age","standard","rollnumber"]

# csv_file=csv.reader(open("ab.csv","r"),delimiter=",")
# # for each in csv_file:
# #     print(each[0])

# for each in csv_file:
#     row={}
#     for field in header:
#         row[field] = each[field]
#     print(row)


# if client:
#     print("connected")
# client.close()
# database=client.users
# collection=database.students
# collection.insert_one({
#   "name":"siva",
#   "age":20,
# "standard":12,
# "rollnumber":25
# })
# print("inserted")
# client.close()

@app.route("/api",methods=["post","get"])
def fun():
    lis=request.json
    database=client.users
    collection=database.students
    for i in lis:
        collection.insert_one(i)
    print("inserted")
    client.close()
    return "successfully insert"

@app.route("/",methods=["post","get"])
def form_data():
    if request.form.get("id")!=None:
        id=request.form.get("id")
        name=request.form.get("name")
        title=request.form.get("title")
        author=request.form.get("author")
        database=client.users
        collection=database.students
        collection.insert_one({"id":id,"name":name,"title":title,"author":author})
        print("inserted")
        client.close()
        return "successfully insert"
    return render_template("index.html")

    


if __name__=="__main__":
    app.run(debug=True)

