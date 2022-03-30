import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split

class DataSet:
    #init funciton with self, file, rowAmount
    def __init__(self, file, rowAmount):
        self.rowAmount = rowAmount
        
        self.df = pd.read_csv(file, nrows=rowAmount)
        self.df = self.df.drop(columns=["unix","date","symbol", "Volume BTC"])
        
        #Df to np.array
        self.close = self.df["close"].to_numpy()       

        #Own features
        self.change = np.array([])
        self.tendency = np.array([])
        
        #Feature array
        self.X = np.array([])
    
    def calcChange(self):
        index = 1
        for item in self.close:
            if index > (self.rowAmount - 1):
                break
            
            else:
                increase = float(self.close[index]) - float(self.close[(index - 1)])
                change = increase / (float(self.close[(index - 1)]) * 100)   #Calculate change
                self.change = np.append(self.change, change)
        
        self.change = np.delete(self.change, [0, 1]) #Align values)
                
        return self.change
    
       
    def calcTendency(self):
        index = 2
        self.tendency = np.array([]) #Don't know why it works without this
        
        for item in self.close:
            if index > (self.rowAmount - 1):
                 break
            elif float(self.close[index]) - float(self.close[(index - 2)]) > 0:
                self.tendency = np.append(self.tendency, 1)
                 
            else:
                self.tendency = np.append(self.tendency, 0) 
                
            index += 1
                 
        return self.tendency    
    
    
    
    def makeX(self):
        self.X = np.column_stack((self.calcChange(), self.calcTendency()))
        return self.X
    
    
    #y functions
    def makey(self):  
        index = 1
        self.y = np.array([])
        for item in self.close:
            if index > (self.rowAmount - 1):
                break  
            else:
                if self.close[index] > self.close[(index - 1)]:
                    self.y = np.append(self.y, "1") #Buy

                elif self.close[index] < self.close[(index - 1)]:
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
                    
    
        
df = DataSet("dataBTC_h1.csv", 1000)
        
        
        
        
        
