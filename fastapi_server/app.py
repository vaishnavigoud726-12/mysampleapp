from fastapi import FastAPI 
from pydantic import BaseModel
class Student(BaseModel):
    stuname:str
    studept:str
    stuusername:str
    stupassword:str
    stuage:int
    stumark:int
app=FastAPI()
#localhost:8000/getStudents
@app.get("/getStudents")
def getStudents():
    return "Get Students method called"
#localhost:8000/addStudent
@app.post("/addStudent")
def addStudent():
    return "Add Student method called"
@app.put("/updateStudent")
def updateStudent():
    return "Update Student method called"
@app.delete("/deleteStudent")
def deleteStudent():
    return "Delete Student method called"
@app.get("/getParticularStudent/{id}")
def getParticularStudent(id:int):
    return {"userid":id}
#localhost:8000/filterdept?dept="CSE" &mark=65
@app.get("/filterdept")
def filterdept(dept:str,mark:int):
    return {"dept":dept,"mark":mark}