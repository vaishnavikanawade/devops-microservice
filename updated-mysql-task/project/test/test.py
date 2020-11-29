import requests
import json

user_config = open("/app/config/user_config.json")
config = json.load(user_config)

url = config.get("url")
port = config.get("port")
URL = "{0}:{1}".format(url,port)
ADDUSER_ENDPOINT = config.get("adduser_endpoint")
SHOWUSER_ENDPOINT = config.get("showuser_endpoint")
DELETEUSER_ENDPOINT = config.get("deleteuser_endpoint")




def showuserTest():
    print("**********showuser Function test start***********")
    newurl = URL + SHOWUSER_ENDPOINT
    response = requests.get(newurl)
    print(response.json())
    print("**********showuser Function test Done***********")

def adduserTest():
    print("**********adduser Function test start***********")
    test_data = open("test_data.json")
    json_data =json.load(test_data)
    id = json_data.get("id")
    name = json_data.get("name")
    age = json_data.get("age")
    department = json_data.get("department")
    subject = json_data.get("subject")

    print("passed parameter")
    print("ID : {}, Name : {}, Age: {}, Department : {}, Subject :{}".format(id, name, age, department, subject))

    query = "?id={0}&name={1}&age={2}&department={3}&subject={4}".format(id, name, age, department, subject)
    newurl = URL + ADDUSER_ENDPOINT + query
    response = requests.post(newurl)
    print(response.json())
    print("**********adduser Function test Done***********")

def deleteuserTest():
    print("**********deleteuser Function test start***********")
    test_data = open("test_data.json")
    json_data = json.load(test_data)
    id = json_data.get("id")
    print("passed parameter")
    print("ID : {}".format(id))
    query = "?id={0}".format(id)
    newurl = URL + DELETEUSER_ENDPOINT + query
    response = requests.delete(newurl)
    print(response.json())
    print("**********deleteuser Function test Done***********")

def mainTest():
    print("**********Test Started***********")
    showuserTest()
    adduserTest()
    deleteuserTest()
    showuserTest()
    print("**********Test Ended***********")

if __name__ == "__main__":
    mainTest()
