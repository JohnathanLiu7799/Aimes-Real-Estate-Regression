
# Predicting Ames Iowa Real Estate Prices

We aim to predict Ames Iowa sale prices based on a variety of features that exist in 
each property.


## Problem Statement

What features of a property are most critical in predicting it's sale price?
## Data Dictionary

Refer to [this](https://www.kaggle.com/c/dsir-111-project-2-regression-challenge/data).
## Analysis Summary

Upon initial inspection of the linear regression results, it appears as though the quality
of any aspect of the house, regardless of whether it's the basement, garage, etc can result
in an increase of thousands of dollars in sales price.

That having been said increases in basement quality are by far less impactful, resulting in 
only 63% of the increases in sale price any improvement to exterior or kitchen wouldve.

The same trend continues for square feet, as an extra square foot of basement nets only 8.3%
of the benefit an extra square foot of above basement would've increased sale price.
## Conclusion

That having been said, the characteristics that impact sale price the most are

1. Neighborhood
2. Above Ground Living Area
3. Overall Quality

and we come to this conclusion from the coefficients we draw from our coefficients of the linear regression model.

| feature                  	| coefficient           	|
|--------------------------	|-----------------------	|
| [('overall_qual',        	| 10473.291639488461),  	|
| ('year_built',           	| 79.9295482732932),    	|
| ('year_remod/add',       	| 137.45247188496307),  	|
| ('mas_vnr_area',         	| 24.451957224250542),  	|
| ('exter_qual',           	| 10575.711395593822),  	|
| ('bsmt_qual',            	| 7021.4962632434535),  	|
| ('total_bsmt_sf',        	| 3.4168080423089897),  	|
| ('1st_flr_sf',           	| 13.729240330216205),  	|
| ('gr_liv_area',          	| 37.278795852453825),  	|
| ('kitchen_qual',         	| 10914.708160136173),  	|
| ('garage_score',         	| 1.860077998482449),   	|
| ('neighborhood_Blmngtn', 	| -21839.313446877375), 	|
| ('neighborhood_Blueste', 	| -26840.42723472683),  	|
| ('neighborhood_BrDale',  	| -33803.260354693746), 	|
| ('neighborhood_BrkSide', 	| -3252.260548491978),  	|
| ('neighborhood_ClearCr', 	| 17989.020250776895),  	|
| ('neighborhood_CollgCr', 	| -7212.241256950574),  	|
| ('neighborhood_Crawfor', 	| 21752.243493478127),  	|
| ('neighborhood_Edwards', 	| -15571.905526027074), 	|
| ('neighborhood_Gilbert', 	| -5220.564931529876),  	|
| ('neighborhood_Greens',  	| -26860.320223113496), 	|
| ('neighborhood_GrnHill', 	| 95931.61600003064),   	|
| ('neighborhood_IDOTRR',  	| -16113.773365606949), 	|
| ('neighborhood_Landmrk', 	| -23889.280122654596), 	|
| ('neighborhood_MeadowV', 	| -18260.86682910468),  	|
| ('neighborhood_Mitchel', 	| -4773.130906205378),  	|
| ('neighborhood_NAmes',   	| -2609.5175752326154), 	|
| ('neighborhood_NPkVill', 	| -20037.430418298634), 	|
| ('neighborhood_NWAmes',  	| -6218.3821796701195), 	|
| ('neighborhood_NoRidge', 	| 29772.65274947804),   	|
| ('neighborhood_NridgHt', 	| 35451.44958663525),   	|
| ('neighborhood_OldTown', 	| -16832.53521139034),  	|
| ('neighborhood_SWISU',   	| -10028.401037754174), 	|
| ('neighborhood_Sawyer',  	| -2311.8579039576725), 	|
| ('neighborhood_SawyerW', 	| -14403.849683750592), 	|
| ('neighborhood_Somerst', 	| -7147.752059399798),  	|
| ('neighborhood_StoneBr', 	| 55632.47022903444),   	|
| ('neighborhood_Timber',  	| 12809.065637043337),  	|
| ('neighborhood_Veenker', 	| 13888.552868959843)]  	|

By examining which coefficients had the strongest impact on saleprice while account for scale:

ie. Dummy variables such as neighborhood that would be either 0 or 1
    Area which is usually measured in sq ft and can vary from 100s to 1000s
    Quality that range from 0-10
    
All only being compared with those of similar scales for interpretibility.

With all else held equal:

    1: The same house in Greenhill vs Briardale would have a 128k difference in price.
    2: The same an increase in overall quality can add 10k to the saleprice for each tier moved up


These characteristics are relatively immutable for anything short of a large scale renovation
and it might hold merit to instead look deeper into more mutable characteristics of properties.

Combined with a way to asses cost, this could result in a method to classify potentially flippable houses
as well as their ROI
## Acknowledgements

 - [Ames Iowa Dataset](https://www.kaggle.com/c/dsir-111-project-2-regression-challenge/data)
 - [Inman](https://www.inman.com/2017/08/07/6-factors-that-influence-a-homes-value/)

 
 
