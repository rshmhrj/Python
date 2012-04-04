'''
Created on Apr 4, 2012

@author: rx342p
'''
#Reverse Index


#Define a procedure, reverse_index, that takes as input a Dictionary, and
#returns a new Dictionary where the keys are the values in the input dictionary.
#The value associated with a key in the result is a list of all the keys in the
#input dictionary that match this value (in any order).

def reverse_index(dict):
    rev = {}
    for year in dict:
        country = dict[year]
        if country in rev:
            rev[country].append(year)
        else:
           rev[country] = [year]
    return rev


#For example,

winners_by_year = {
    1930: 'Uruguay', 1934: 'Italy', 1938: 'Italy', 1950: 'Uruguay',
    1954: 'West Germany', 1958: 'Brazil', 1962: 'Brazil', 1966: 'England',
    1970: 'Brazil', 1974: 'West Germany', 1978: 'Argentina',
    1982: 'Italy', 1986: 'Argentina', 1990: 'West Germany', 1994: 'Brazil',
    1998: 'France', 2002: 'Brazil', 2006: 'Italy', 2010: 'Spain' }

wins_by_country = reverse_index(winners_by_year)

#print wins_by_country
print wins_by_country['Brazil']
#>>> [1958, 2002, 1970, 1994, 1962]

print wins_by_country['England'] 
#>>> [1966]