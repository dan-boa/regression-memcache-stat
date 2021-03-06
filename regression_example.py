import numpy as np
import scikits.statsmodels.api as sm

"""
Example code to understand the input required to the 
numpy's regression formulas and the output derived
"""

y = [29.4, 29.9, 31.4, 32.8, 33.6, 34.6, 35.5, 36.3, 37.2, 37.8, 38.5, 38.8,
            38.6, 38.8, 39, 39.7, 40.6, 41.3, 42.5, 43.9, 44.9, 45.3, 45.8, 46.5,
            77.1, 48.2, 48.8, 50.5, 51, 51.3, 50.7, 50.7, 50.6, 50.7, 50.6, 50.7]
        #tuition
x1 = [376, 407, 438, 432, 433, 479, 512, 543, 583, 635, 714, 798, 891,
            971, 1045, 1106, 1218, 1285, 1356, 1454, 1624, 1782, 1942, 2057, 2179,
            2271, 2360, 2506, 2562, 2700, 2903, 3319, 3629, 3874, 4102, 4291]
        #research and development
x2 = [28740.00, 30952.00, 33359.00, 35671.00, 39435.00, 43338.00, 48719.00, 55379.00, 63224.00,
            72292.00, 80748.00, 89950.00, 102244.00, 114671.00, 120249.00, 126360.00, 133881.00, 141891.00,
            151993.00, 160876.00, 165350.00, 165730.00, 169207.00, 183625.00, 197346.00, 212152.00, 226402.00, 
            267298.00, 277366.00, 276022.00, 288324.00, 299201.00, 322104.00, 347048.00, 372535.00,
            397629.00]
        #one/none parents 
x3 = [11610, 12143, 12486, 13015, 13028, 13327, 14074, 14094, 14458, 14878, 15610, 15649,
            15584, 16326, 16379, 16923, 17237, 17088, 17634, 18435, 19327, 19712, 21424, 21978,
            22684, 22597, 22735, 22217, 22214, 22655, 23098, 23602, 24013, 24003, 21593, 22319]


x = np.column_stack((x1,x2,x3))  #stack explanatory variables into an array
x = sm.add_constant(x, prepend=True) #add a constant

res = sm.OLS(y,x).fit() #create a model and fit it
print res.params
print res.bse
print res.summary()
