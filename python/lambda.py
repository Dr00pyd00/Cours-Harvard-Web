
people =[
    {'name':'Harry', 'house':'Gryffindor' },
    { 'name':'Cho', 'house':'Ravenclaw'},
    {'name':'Draco', 'house':'Slytherin'}
]

# sort() peut avoir un arg 'key' qui demande
# une fonction pour savoir comment trier

# methode basique
def f(person):
    return person['name']

people.sort(key=f)

print(people)


# avec lambda :
people.sort(key= lambda people : people['house'])
print(people)