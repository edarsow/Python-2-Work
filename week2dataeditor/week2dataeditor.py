# Note: Milo and I discussed the data structures that we wanted to
# use in class, as well as laying out some of the main functions in
# broad strokes. All work is my own, however. All country statistics
# are courtesy of the CIA World Factbook.

import sys

continents = {'North America':[{'Canada':{'Population':'35,881,659',
	'GDP':'1,774,000,000,000 Dollars','Founding Year':'1867'}}, 
	{'United States Of America':{'Population':'329,256,465',
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
	
valid_africa = ['Algeria', 'Angola', 'Benin', 'Botswana', 'Burkina',
		'Burundi', 'Cameroon', 'Cape Verde', 'Central African Republic',
		'Chad', 'Comoros', 'Congo', 'Congo, Democratic Republic of',
		'Djibouti', 'Egypt', 'Equatorial Guinea', 'Eritrea', 'Ethiopia',
		'Gabon', 'Gambia', 'Ghana', 'Guinea', 'Guinea-Bissau', 
		'Ivory Coast', 'Kenya', 'Lesotho', 'Liberia', 'Libya', 
		'Madagascar', 'Malawi', 'Mali', 'Mauritania', 'Mauritius',
		'Morocco', 'Mozambique', 'Namibia', 'Niger', 'Nigeria', 'Rwanda',
		'Sao Tome and Principe', 'Senegal', 'Seychelles', 'Sierra Leone',
		'Somalia', 'South Africa', 'South Sudan', 'Sudan', 'Swaziland',
		'Tanzania', 'Togo', 'Tunisia', 'Uganda', 'Zambia', 'Zimbabwe']
	
valid_asia = ['Afghanistan', 'Bahrain', 'Bangladesh', 'Bhutan', 
		'Brunei', 'Burma', 'Cambodia', 'China', 'East Timor', 'India',
		'Indonesia', 'Iran', 'Iraq', 'Israel', 'Japan', 'Jordan',
		'Kazakhstan', 'Kuwait', 'Kyrgyzstan', 'Laos', 'Lebanon',
		'Malaysia', 'Maldives', 'Mongolia', 'Nepal', 'North Korea',
		'Oman', 'Pakistan','Philippines', 'Qatar', 'Russia', 
		'Saudi Arabia', 'Singapore', 'South Korea',
		'Sri Lanka', 'Syria', 'Tajikistan', 'Thailand', 'Turkey', 
		'Turkmenistan', 'United Arab Emirates', 'Uzbekistan', 'Vietnam',
		'Yemen']
     
valid_europe = ['Albania', 'Andorra', 'Armenia', 'Austria', 
		'Azerbaijan', 'Belarus', 'Belgium', 'Bosnia and Herzegovina',
		'Bulgaria', 'Croatia', 'Cyprus', 'Czech Republic', 'Denmark',
		'Estonia', 'Finland', 'France', 'Georgia', 'Germany', 'Greece',
		'Hungary', 'Iceland', 'Ireland', 'Italy', 'Latvia', 
		'Liechtenstein', 'Lithuania', 'Luxembourg', 'Macedonia', 
		'Malta', 'Moldova', 'Monaco', 'Montenegro', 'Netherlands',
		'Norway', 'Poland', 'Portugal', 'Romania', 'San Marino', 'Serbia',
		'Slovakia', 'Slovenia', 'Spain', 'Sweden', 'Switzerland',
		'Ukraine', 'United Kingdom', 'Vatican City']
  
valid_north_america = ['Antigua and Barbuda', 'Bahamas', 'Barbados',
	'Belize', 'Canada', 'Costa Rica', 'Cuba', 'Dominica', 'Dominican Republic',
	'El Salvador', 'Grenada', 'Guatemala', 'Haiti', 'Honduras', 
	'Jamaica', 'Mexico', 'Nicaragua', 'Panama', 'Saint Kitts and Nevis',
	'Saint Lucia', 'Saint Vincent and the Grenadines', 'Trinidad and Tobago',
	'United States of America']
	
valid_australia = ['Australia', 'Fiji', 'Kiribati', 'Marshall Islands',
		'Micronesia', 'Nauru', 'New Zealand', 'Palau', 'Papau New Guinea',
		'Samoa', 'Solomon Islands', 'Tonga', 'Tuvalu', 'Vanuatu']
		
valid_south_america = ['Argentina', 'Bolivia', 'Brazil', 'Chile',
		'Colombia', 'Ecuador', 'Guyana', 'Paraguay', 'Peru', 'Suriname',
		'Uruguay', 'Venezuela']
		
valid_antarctica = ['Antarctica']

valid_continents = ['North America', 'South America', 'Europe',
		'Africa', 'Asia', 'Australia', 'Antarctica']
		
	
def mainmenu():
	print("\nHello, welcome to the World Factbook! Choose a continent" + 
		" from the options below to see a list of countries within" + 
		"that continent. To add a continent, type 'Add'. To" +
		" delete a continent, type 'Delete'. To quit the Factbook " +
		"type 'Quit'.\n")
	for continent in continents.keys():
		print(continent, end='    ')
	print("\n")
	
	wrong = True
	while wrong == True:
		usr_cont = input("Your choice: \n\n")
		if usr_cont.title() in continents.keys():
			continentmenu(usr_cont)
			wrong = False
		elif usr_cont.title() == 'Add':
			contadd()
			wrong = False
		elif usr_cont.title() == 'Delete':
			contdelete()
			wrong = False
		elif usr_cont.title() == 'Quit':
			sys.exit()
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
		usr_country = input("Your choice: \n\n")
		for country_dict in continents[selection.title()]:
			for country in country_dict.keys():
				if country == usr_country.title():
					wrong = False
					countrymenu(selection, usr_country)
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
			countryadd(selection)
		elif usr_country.title() == 'Delete':
			wrong = False
			countrydelete(selection)
		elif usr_country.title() == 'Main':
			wrong = False
			mainmenu()
		else:
			print("Invalid input, try again.")
def countrymenu(selection, usr_country):
	print("\nThe following is all the information we have for %s:" % usr_country.title())
	for country_dict in continents[selection.title()]:
		for country in country_dict.keys():
			a = country
			if a == usr_country.title():
				b = continents[selection.title()].index(country_dict)
				break
			else: 
				continue
	
	for key, value in continents[selection.title()][b][usr_country.title()].items():
		print("%s: %s" % (key, value))
	print("\n")
	
	wrong = True
	while wrong == True:
		response = input("What would you like to do now? View your options" +
		"below:\n\n" +
		"Add information about this country: type 'Add'\n" + 
		"Delete informaiton about this country: type 'Delete'\n" + 
		"Edit information about this country: type 'Edit'\n" + 
		"Go back to the previous menu: type 'Previous'\n" + 
		"Go back to the main menu: type 'Main'\n\n")
		
		if response.title() == 'Add':
			wrong = False
			infoadd(selection, usr_country, b)
		elif response.title() == 'Delete':
			wrong = False
			infodelete(selection, usr_country, b)
		elif response.title() == 'Edit':
			wrong = False
			infoedit(selection, usr_country, b)
		elif response.title() == 'Previous':
			wrong = False
			continentmenu(selection)
		elif response.title() == 'Main':
			wrong = False
			mainmenu()
		else:
			print("Invalid input, try again.")

def contadd():
	continent = input("Enter the name of the continent you want to add" +
	" to the Factbook: \n\n")
	if continent.title() not in valid_continents:
		print("%s is not a real continent!" % continent.title())
	elif continent.title() in continents.keys():
		print("%s is already in the Factbook!" % continent.title())
	else:
		continents[continent.title()] = []
		print("%s added to the Factbook!" % continent.title())
		mainmenu()
	
def countryadd(continent):
	country = input("Enter the name of the country you want to add" +
	" to %s: \n\n" % continent.title())
	if continent.title() == 'Africa':
		c = []
		for country_dict in continents[continent.title()]:
			for state in country_dict.keys():
				c.append(state)
		if country.title() not in valid_africa:
			print("%s is not a real country in Africa!" % country.title())
		elif ((country.title() in valid_africa) and (country.title() not in c)):
			a = {country.title(): {}}
			continents['Africa'].append(a)
			print("%s added to %s!" % (country.title(), continent.title()))
		else:
			print("%s is already in %s!" % (country.title(), continent.title()))
	elif continent.title() == 'Asia':
		c = []
		for country_dict in continents[continent.title()]:
			for state in country_dict.keys():
				c.append(state)
		if country.title() not in valid_asia:
			print("%s is not a real country in Asia!" % country.title())
		elif ((country.title() in valid_asia) and (country.title() not in c)):
			a = {country.title(): {}}
			continents['Asia'].append(a)
			print("%s added to %s!" % (country.title(), continent.title()))
		else:
			print("%s is already in %s!" % (country.title(), continent.title()))
	elif continent.title() == 'Europe':
		c = []
		for country_dict in continents[continent.title()]:
			for state in country_dict.keys():
				c.append(state)
		if country.title() not in valid_europe:
			print("%s is not a real country in Europe!" % country.title())
		elif ((country.title() in valid_europe) and (country.title() not in c)):
			a = {country.title(): {}}
			continents['Europe'].append(a)
			print("%s added to %s!" % (country.title(), continent.title()))
		else:
			print("%s is already in %s!" % (country.title(), continent.title()))
	elif continent.title() == 'Australia':
		c = []
		for country_dict in continents[continent.title()]:
			for state in country_dict.keys():
				c.append(state)
		if country.title() not in valid_australia:
			print("%s is not a real country in Australia!" % country.title())
		elif ((country.title() in valid_australia) and (country.title() not in c)):
			a = {country.title(): {}}
			continents['Australia'].append(a)
			print("%s added to %s!" % (country.title(), continent.title()))
		else:
			print("%s is already in %s!" % (country.title(), continent.title()))
	elif continent.title() == 'North America':
		c = []
		for country_dict in continents[continent.title()]:
			for state in country_dict.keys():
				c.append(state)
		if country.title() not in valid_north_america:
			print("%s is not a real country in North America!" % country.title())
		elif ((country.title() in valid_north_america) and (country.title() not in c)):
			a = {country.title(): {}}
			continents['North America'].append(a)
			print("%s added to %s!" % (country.title(), continent.title()))
		else:
			print("%s is already in %s!" % (country.title(), continent.title()))
	elif continent.title() == 'South America':
		c = []
		for country_dict in continents[continent.title()]:
			for state in country_dict.keys():
				c.append(state)
		if country.title() not in valid_south_america:
			print("%s is not a real country in South America!" % country.title())
		elif ((country.title() in valid_south_america) and (country.title() not in c)):
			a = {country.title(): {}}
			continents['South America'].append(a)
			print("%s added to %s!" % (country.title(), continent.title()))
		else:
			print("%s is already in %s!" % (country.title(), continent.title()))
	elif continent.title() == 'Antarctica':
		c = []
		for country_dict in continents[continent.title()]:
			for state in country_dict.keys():
				c.append(state)
		if country.title() not in valid_antarctica:
			print("%s is not a real country in Antarctica!" % country.title())
		elif ((country.title() in valid_antarctica) and (country.title() not in c)):
			a = {country.title(): {}}
			continents['Antarctica'].append(a)
			print("%s added to %s!" % (country.title(), continent.title()))
		else:
			print("%s is already in %s!" % (country.title(), continent.title()))
	
	continentmenu(continent)
	
def infoadd(selection, usr_country, b):
	category = input("Enter the new data category you would like to " +
		"add to this country: \n\n")
	data = input("Enter the value for the data you would like to " +
		"enter for this category: \n")
	if ((category.title() in continents[selection.title()][b][usr_country.title()].keys())
		or (category.upper() in continents[selection.title()][b][usr_country.title()].keys())):
		print("Category already exists, please use the edit function.")
		countrymenu(selection, usr_country)
	else:
		continents[selection.title()][b][usr_country.title()][category.title()] = data.title()
	
	countrymenu(selection, usr_country)
		
def infodelete(selection, usr_country, b):
	category = input("Enter the category of data you would like to " +
		"delete for this category: \n\n")
	if ((category.title() not in continents[selection.title()][b][usr_country.title()].keys())
		and (category.upper() not in continents[selection.title()][b][usr_country.title()].keys())):
		print("Category is not available for this country, please use" +
		" add function.")
		countrymenu(selection, usr_country)
	elif category.title() in continents[selection.title()][b][usr_country.title()].keys():
		if len(continents[selection.title()][b][usr_country.title()].keys()) > 1:
			del continents[selection.title()][b][usr_country.title()][category.title()]
		else:
			print("Cannot delete final piece of information from a country!")
	elif category.upper() in continents[selection.title()][b][usr_country.title()].keys():
		if len(continents[selection.title()][b][usr_country.title()].keys()) > 1:
			del continents[selection.title()][b][usr_country.title()][category.upper()]
		else:
			print("Cannot delete final piece of information from a country!")
			
	countrymenu(selection, usr_country)
	
def infoedit(selection, usr_country, b):
	category = input("Enter the category for the data you would like to " +
		"edit for this category: \n\n")
	if ((category.title() not in continents[selection.title()][b][usr_country.title()].keys())
		and (category.upper() not in continents[selection.title()][b][usr_country.title()].keys())):
		print("Category is not available for this country, please use" +
		" add function.")
		countrymenu(selection, usr_country)
	elif category.title() in continents[selection.title()][b][usr_country.title()].keys():
		data = input("Enter the new value for the data you would like to " +
		"enter for this category: \n\n")
		continents[selection.title()][b][usr_country.title()][category.title()] = data
	elif category.upper() in continents[selection.title()][b][usr_country.title()].keys():
		data = input("Enter the new value for the data you would like to " +
		"enter for this category: \n\n")
		continents[selection.title()][b][usr_country.title()][category.upper()] = data
	
	countrymenu(selection, usr_country)
	
def contdelete():
	continent = input("Enter the name of the continent you want to "
	"delete from the Factbook. WARNING: Deleting a continent" +
	" will delete all its associated countries and data. \n\n")
	if continent.title() not in continents.keys():
		print("%s is not in the Factbook" % continent)
	elif continent.title() in continents.keys():
		if len(continents.keys()) > 1:
			del continents[continent.title()]
			print("%s removed from the Factbook!" % continent)
			mainmenu()
		else:
			print("Cannot delete final continent!\n")
			mainmenu()
		
def countrydelete(continent):
	country = input("Enter the name of the country you want to delete." +
	" WARNING: Deleting a country will delete all its " +
	"associated data.\n\n")
	a = []
	for country_dict in continents[continent.title()]:
		for state in country_dict.keys():
			a.append(state)
	
	if country.title() not in a:
		print("%s is not in the Factbook" % country.title())
	elif country.title() in a:
		if len(a) > 1:	
			b = a.index(country.title())
			del continents[continent.title()][b]
			print("%s removed from %s!" % (country.title(), continent.title()))
			continentmenu(continent)
		else:
			print("Cannot delete final country from a continent!\n")
			continentmenu(continent)
	
mainmenu() 
