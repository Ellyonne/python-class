

names = ["kelly rowlan", "john doe", "james matt", "janet jackson"]
count = len(names)
first_names = []
last_names = []

def process_names (names):
    for name in names:
        first_names.append(name.split(' ')[0])
        last_names.append(name.split(' ')[1])

process_names(names)
print(count, first_names, last_names)



#when you are done with the whole thing type the following in your vs code taminal
#    git init
#    git config--global user.email 'ellyonne@gmail.com'
#to add git hubs File type 
#(1)git add
#(2)git commit -m 'first commit'
#(3)git branch -M main
#(4)git remote origin add(copy your url from your browser and add it here)
#(5) git push -u origin main





#first_names = ['kelly', "john", "james", "janet"]
#last_names = ["rowlan","doe", "matt", "jackson"]