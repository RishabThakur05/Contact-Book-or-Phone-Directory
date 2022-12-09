# CONTACT BOOK 
name=["Karan","Aryan","Rishab","Ashutosh","Abhinav singh","Divesh","Vansh","Amank","Praveen","Vignesh","Harshit","Aryan prasad","Kishlay","Deepti maan","Ashishdeep","Ashish","Bhargav","Vaibahv","Saurabh","Aman","Riya","Pranav","Austin","Piyush","Pranav nanda","Shreya","Ayushi","Ankush","MOhit","Rinchal","Mehak","Sushant"]
total=len(name)
print("Total contacts:",total)
print(name)
phone_numbers=["7651995122","9113194954","6387989439","8603784210","8853490243","7973858382","9928170284","6204560544","62996669821","6361885609","7073039390","7224843905","7357037586","7617610807","7626831001","7705044817","8143173045","8298769986","8539949819","8545007692","8587911162","859096519","8590716857","8699135022","8847007057","90372469227","9129575270","9142348830","9149392194","9520913954","9872865404","9905623177"]
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
    
