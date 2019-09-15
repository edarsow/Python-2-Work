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
	
def mainmenu():
	print("\nHello, welcome to the World Factbook! Choose a continent" + 
		" from the options below to see a list of countries within" + 
		"that continent. To add a continent, type 'Add'. To" +
		" delete a continent, type 'Delete'.\n")
	for continent in continents.keys():
		print(continent, end='    ')
	print("\n")
	
	wrong = True
	while wrong == True:
		usr_cont = input("Your choice: ")
		if usr_cont.title() in continents.keys():
			continentmenu(usr_cont)
			wrong = False
		elif usr_cont.title() == 'Add':
			add()
			wrong = False
		elif usr_cont.title() == 'Delete':
			delete()
			wrong = False
		else:
			print("Invalid input, try again.")
			
def continentmenu(selection):
	print("\nWelcome to the continent menu. Here are the countries " +
	"currently listed for the continent you chose. To view details " +
	"about a country, enter its name. To add a country to this " +
	"continent list, enter 'Add'. To delete a country and its " +
	"associated information, enter 'Delete'. To go back to" +
	" the main menu, enter 'Main'. \n")
	
	for country_dict in continents[selection.title()]:
		for country in country_dict.keys():
			print(country, end='    ')
	print("\n")
	
	wrong = True
	while wrong:
		usr_country = input("Your choice: ")
		for country_dict in continents[selection.title()]:
			for country in country_dict.keys():
				if country == usr_country.title():
					wrong = False
					countrymenu(usr_country)
				elif usr_country.title() == 'Add':
					break
				elif usr_country.title() == 'Delete':
					break
				elif usr_country.title() == 'Main':
					break
				else:
					continue
		if usr_country.title() == 'Add':
			wrong = False
			add()
		elif usr_country.title() == 'Delete':
			wrong = False
			delete()
		elif usr_country.title() == 'Main':
			wrong = False
			mainmenu()
		else:
			print("Invalid input, try again.")
def countrymenu(selection):
	print(selection.title())

def add():
	print('add')
	
def delete():
	print('delete')
	
mainmenu() 
