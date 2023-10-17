import json
import pickle
import numpy as np

# """To resolve the issue-
# __model=pickle.load(file)
#             ^^^^^^^^^^^^^^^^^
# ModuleNotFoundError: No module named 'sklearn' """
# import sklearn

__locations=None
__data_columns=None
__model=None

def get_location_names():
    #Reads Column.json and returns the list of Locations
    #But as we have already loaded and saved it inside __locations variable
    #We can simply return it
    global __locations
    return __locations

def load_saved_artifacts():
    #Load saved Artifacts'Columns.json' and 'Banglore_House_Price_Model'
    #And save them in Global variables
    global __data_columns
    global __locations
    global __model
    #Reading the variables as Global variables

    #Opening JSON File
    with open("./Artifacts/Columns.json","r") as file:#r-Reading the file
        f=json.load(file)#Loaded File is loaded as Dictionary
        __data_columns=f["data_columns"]
        #Elements starting from index 3 are Locations
        __locations=__data_columns[3:]#Using Python Indexing
        
    #Opening Saved Pickle Model
    with open("./Artifacts/Banglore_House_Price_Model.pickle","rb") as file:
        __model=pickle.load(file)
    print("Loading Operation Successful")

def get_estimated_price(inputlocation,sqft,bhk,bath):#App routine to get estimated price
    #x=np.zeros(245)

    global __data_columns
    try:#Excception Handling because if index is not found,error will be thrown
        inputlocation_index=__data.columns.index(inputlocation.lower())
    except:
        inputlocation_index=-1

    x=np.zeros(len(__data_columns))
    x[0]=sqft
    x[1]=bath
    x[2]=bhk
    if(inputlocation_index>=0):
        x[inputlocation_index]=1
    estimated_price=__model.predict([x])
    return round(estimated_price,2)

if __name__=="__main__":
    load_saved_artifacts()
    print(get_location_names())
    print(get_estimated_price("1st Phase JP Nagar",1000,3,3))
    print(get_estimated_price("1st Phase JP Nagar",1000,2,2))
    print(get_estimated_price("Kalhalli",1000,2,2))#Other location
    print(get_estimated_price("Ejipura",1000,2,2))#Other location