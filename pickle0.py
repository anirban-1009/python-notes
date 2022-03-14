import pickle
EmpID = {1:"Zack",2:"53050",3:"IT",4:"38",5:"Flipkart"}
pickling_on = open("EmpID.pickle","wb")
pickle.dump(EmpID, pickling_on)
pickling_on.close()