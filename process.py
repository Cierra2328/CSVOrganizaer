import math
class Process_file:
    def __init__(self, text):
        self.text = text
        self.items = self.text.split(',') #get list of data items
        self.ID = self.items[0].rjust(10, 'X') #rjust() just adds left padding if necessary and an X if necessary
        self.name = self.items[1].rjust(20)
        self.contact = self.items[2]
        self.names = self.contact.split(' ') #split it up so we have a first and last name
        self.contactFirstName = self.names[0].rjust(15)
        self.contactLastName = self.names[1].rjust(20)
        self.compStreetAddress = self.items[3].rjust(30)
        self.compAddressCity = self.items[4].rjust(20)
        self.compAddressSt = self.items[5]
        self.compAddressZip = self.items[6].rjust(5)
        self.compContact = self.items[7].rjust(10).replace('-', '') #phone numbers don't need hyphens!
        self.altContact = self.items[8].rjust(10).replace('-', '')
        self.alphaKey = self.items[9][0:9]
        self.betaKey = self.items[9][-26:].rjust(28, 'x')
        self.compCode = self.items[10].rjust(7)
        self.regions = self.items[11].ljust(5)
        self.limit = self.items[12]
        self.bool = 0 #heres where its checking to see how big the number is
        if len(self.limit) > 6: #if its over 6 numbers long, its not a K, its an M (million)
            self.bool = 1
            self.limit = int(self.limit) / 1000 #just divide it again
        self.limit = int(self.limit) / 1000
        self.limit = math.trunc(self.limit) #this is just getting rid of the decimals, youd think int would do that, but it didn't work so here we are
        self.custType = self.items[13].rjust(1)

    @classmethod    #this is just to make sure that the objects can use this method
    def state(self, text):
          states = { #a dicitonary of states and their abbreviations
            "Alabama": "AL",
            "Alaska": "AK",
            "Arizona": "AZ",
            "Arkansas": "AR",
            "California": "CA",
            "Colorado": "CO",
            "Connecticut": "CT",
            "Delaware": "DE",
            "Florida": "FL",
            "Georgia": "GA",
            "Hawaii": "HI",
            "Idaho": "ID",
            "Illinois": "IL",
            "Indiana": "IN",
            "Iowa": "IA",
            "Kansas": "KS",
            "Kentucky": "KY",
            "Louisiana": "LA",
            "Maine": "ME",
            "Maryland": "MD",
            "Massachusetts": "MA",
            "Michigan": "MI",
            "Minnesota": "MN",
            "Mississippi": "MS",
            "Missouri": "MO",
            "Montana": "MT",
            "Nebraska": "NE",
            "Nevada": "NV",
            "New Hampshire": "NH",
            "New Jersey": "NJ",
            "New Mexico": "NM",
            "New York": "NY",
            "North Carolina": "NC",
            "North Dakota": "ND",
            "Ohio": "OH",
            "Oklahoma": "OK",
            "Oregon": "OR",
            "Pennsylvania": "PA",
            "Rhode Island": "RI",
            "South Carolina": "SC",
            "South Dakota": "SD",
            "Tennessee": "TN",
            "Texas": "TX",
            "Utah": "UT",
            "Vermont": "VT",
            "Virginia": "VA",
            "Washington": "WA",
            "West Virginia": "WV",
            "Wisconsin": "WI",
            "Wyoming": "WY",
            "District of Columbia": "DC"
            }
          abbrev = states.setdefault(text); #grabs the value of the given key
          return abbrev; #returns that value
          
                  
              
                


        

    
