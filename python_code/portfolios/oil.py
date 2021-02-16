import pandas
from sklearn import linear_model
import matplotlib.pyplot as plt

df = pandas.read_csv('C:/Users/kinak/Desktop/Finance/oil_market_analysis_1.csv')

average_vol_fut = df[['CL=F_Vol']].mean()
#print(average_vol_fut)
average_vol_uso = df[['USO_Vol']].mean()
#print(average_vol_uso)
#correlate btwn just prices
X = df[['CL=F']]
y = df['USO']
#correlate btwn price and volume
#X = df[['CL=F', 'CL=F_Vol']]
#y = df[['USO','USO_Vol']]

#plot the data
#plt.scatter(X,y)
#plt.show()

#perform regression
regr = linear_model.LinearRegression()
regr.fit(X, y)

#input the price you want to predict and display
future_price = input('Enter OIL FUTURES value to gauge USO price? ')
predict_oil = regr.predict([[future_price]])
#predict_oil = regr.predict([[future_price, average_vol_fut]])
print(predict_oil) 
#print(regr.coef_) 