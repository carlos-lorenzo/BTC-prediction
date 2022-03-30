import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split


class DataSet:
    def __init__(self, file, rowAmount):
        #Fetching values from file
        self.df = pd.read_csv(file, nrows=rowAmount)
        self.df = self.df.drop(columns=["Date"])
        self.rowAmount = rowAmount
        
        self.df = self.df.astype("str")
        self.df['High'] = self.df['High'].str.replace(',','', regex=True)
        self.df["Low"] = self.df['Low'].str.replace(',','', regex=True)
        self.df["Price"] = self.df['Price'].str.replace(',','', regex=True)
        self.df["Open"] = self.df['Open'].str.replace(',','', regex=True)
        self.df["Change"] = self.df["Change"].str.replace("%", "", regex=True)


        #Converting to np. array
        self.high = self.df["High"].to_numpy()
        self.low = self.df["Low"].to_numpy()
        self.openP = self.df["Open"].to_numpy()
        self.volume = self.df["Vol"].to_numpy()
        self.price = self.df["Price"].to_numpy()
        self.df = self.df.astype("float")

        #X features
        self.X = np.array([], dtype="float")
        self.change = self.df["Change"].to_numpy()
        self.change = np.delete(self.change, [0, 1]) #Align values  
        
        self.tendency = np.array([])
        self.vpt = np.array([])
        
        #y features
        self.y = np.array([], dtype="int")
             
    #X funcitons
    def tendencyCalc(self):
        index = 2
        self.tendency = np.array([])
        for item in self.price:
            if index > (self.rowAmount - 1):
                 break
            elif float(self.price[index]) - float(self.price[(index - 2)]) > 0:
                self.tendency = np.append(self.tendency, 1)
            
            else:
                self.tendency = np.append(self.tendency, 0)     
            
                    
       
            index += 1
              
        return self.tendency
            
    def vptCalc(self):
        index = 1
        #VPT = Previous VPT + Volume x (Today’s Closing Price – Previous Closing Price) / Previous Closing Price
        for item in self.openP:
            if index > (self.rowAmount - 1):
                break
            currentVPT = float(self.volume[index]) * (float(self.openP[index]) - float(self.openP[(index - 1)])) / float(self.openP[(index - 1)])
            self.vpt = np.append(self.vpt, currentVPT)
            
        self.vpt = np.delete(self.vpt, [0, 1]) #Align values 
        return self.vpt
    
    def makeX(self):
        #Add vpt later...
            self.X = np.column_stack((self.change, self.tendencyCalc())) #Create "X" array with features 

            return self.X
    
    #y functions
    def makey(self):  
        index = 1
        self.y = np.array([])
        for item in self.price:
            if index > (self.rowAmount - 1):
                break  
            else:
                if self.price[index] > self.price[(index - 1)]:
                    self.y = np.append(self.y, "1") #Buy

                elif self.price[index] < self.price[(index - 1)]:
                    self.y = np.append(self.y, "0") #Sell

                else:
                    self.y = np.append(self.y, "1") #XD
                    
            index += 1
        
        self.y = np.delete(self.y, [0])
        return self.y
    
    #Create DataSet
    def createDataSet(self):
        X = self.makeX()
        y = self.makey()
        X_train, X_test, y_train, y_test = train_test_split(X, y)
        return [X_train, X_test, y_train, y_test]
