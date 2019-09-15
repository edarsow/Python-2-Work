# Note: Milo and I discussed the data structures that we wanted to
# use in class, as well as laying out some of the main functions in
# broad strokes. All work is my own, however. All country statistics
# are courtesy of the CIA World Factbook.

continents = {'North America':[{'Canada':{'Population':'35,881,659',
	'GDP':'1,774,000,000,000 Dollars','Founding Year':'1867'}}, 
	{'United States of America':{'Population':'329,256,465',
	'GDP':'19,490,000,000,000 Dollars','Founding Year':'1776'}},
	{'Mexico':{'Population':'125,959,205',
	'GDP':'2,463,000,000,000 Dollars','Founding Year':'1810'}}],
	'Asia':[{'China':{'Population':'1,384,688,986',
	'GDP':'23,210,000,000,000 Dollars','Founding Year':'1949'}}, 
	{'Taiwan':{'Population':'23,545,963',
	'GDP':'1,189,000,000,000 Dollars','Founding Year':'1949'}},
	{'Indonesia':{'Population':'262,787,403',
	'GDP':'3,250,000,000,000 Dollars','Founding Year':'1945'}}],
	'South America':[{'Chile':{'Population':'17,925,262',
	'GDP':'425,100,000,000 Dollars','Founding Year':'1810'}}, 
	{'Brazil':{'Population':'208,846,892',
	'GDP':'3,248,000,000,000 Dollars','Founding Year':'1822'}},
	{'Venezuela':{'Population':'31,689,176',
	'GDP':'381,600,000,000 Dollars','Founding Year':'1811'}}]}
	
print(continents['Asia'][1]['Taiwan']['Population'])
