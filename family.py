AllMales=["Joe","Bill","Paul" ]
AllFemales=["Marie","Helen","Miranda"]
AllPersons=["Joe","Bill","Paul","Marie","Helen","Miranda","Adam","Mike"]

def isMale(x):
	if x in AllMales:
		return True
	return False


parent_of=[("Joe","Helen"),("Joe","Bill"),("Marie","Helen"),("Marie","Bill"),("Bill","Mike"),("Helen","Adam"),("Paul","Miranda"),("Miranda","Mike")]

def parentOf(x):
    for y in parent_of:
        if y[0]==x:
            yield y[1]

def siblingOf(x):
    for z in AllPersons:
        for k in (list(parentOf(z))):
            if k in list(parentOf(x)) and z!=x:
                yield z
            
def sisterOf(x):
    for z in list(siblingOf(x)):
        if not isMale(z):
            yield z

def brotherOf(x):
    for z in list(siblingOf(x)):
        if isMale(z):
            yield z

def motherOf(x):
    for z in parentOf(x):
        if not isMale(z):
            yield z

def fatherOf(x):
    for z in parentOf(x):
        if isMale(z):
            yield z
            
def grandParentOf(x):
    for z in parentOf(x):
        for k in parentOf(z):
            yield k

def cousinOf(x):
    for z in grandParentOf(x):
        for k in AllPersons:
            for m in grandParentOf(k):
                if x!=k and k not in siblingOf(x):
                    yield k
           
            
'''test commands
set(parentOf("Joe"))
set(brotherOf("Marie"))
set(grandParentOf("Joe"))
etc'''

            
