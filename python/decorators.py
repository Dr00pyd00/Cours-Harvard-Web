
# une fonction qui modifie une autre fonction:

def announce(f):
    # je créé une fonction qui entoure l'autre entre 2 prints par exemple:
    def wrapper():
        print('About to run the fonction...')
        f()
        print('Done with this fonction.')
    return wrapper  # je dois apeler wrapper pour la lancer...


def hello():
    print('Hello, world!') 
    
# test basique :
announce(hello)() # ne pas oublier d'appeler la fonction () 

# test avec vrai decorateur :

@announce
def goodbye():
    print('Cia, world!')

goodbye()    