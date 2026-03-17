import os
nbr=0
def back(what_search):
    txt_files=[]
    find=0
    while find == 0 :
        os.chdir('..')
        liste=os.listdir('.')
        if what_search in liste:
            #print('i find ')
            #print(os.listdir('.'))
            find=1
            os.chdir(what_search)
            print('-----------'*40)
            print(os.listdir('.'))
        else :
            print('not found ')
        print(os.getcwd())
        

print('hello  what can search for you ')
print('seacrh fichier ')

what_search=input('what you serch about  ::')
back(what_search)