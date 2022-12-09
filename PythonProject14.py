# CONTACT BOOK 
name=["a","b","c"]
total=len(name)
print("Total contacts:",total)
print(name)
phone_numbers=["000","111","323"]
for i in range(total):
    print("{}\t\t\t\t\t\t{}".format(name[i], phone_numbers[i]))
b=True
while b==True:
    search_term = input("\nEnter Search Term: ")
    print("Search Result")
    if search_term in name:
            
            x=name.index(search_term)
            phone_number=phone_numbers[x]
            print("Name {}, Phone Number: {}".format(search_term, phone_number))
        
    else:
        print("Name not found")
    
