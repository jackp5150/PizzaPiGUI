from pizzapi import *
from tkinter import *
from PIL import ImageTk, Image
import time

firstName=""
lastName=""
emailAddress=""
phoneNumber=""
cust=Customer("","","","")
add=Address("","","","")
count=0
store= None
menu=None

global secondWindow
secondWindow=False
#establish interface
root = Tk()
root.title("Dominos project")
root.geometry("400x400")

#gathering user data
mainlabel=Label(root, text="Hello! Welcome to Dominos")
mainlabel.grid(row=0, column=0, columnspan=3)

#First Name
nameLabel=Label(root, text="Enter your first name:")
nameLabel.grid(row=1, column=0)

Name = Entry(root)
Name.grid(row=1, column=1)

#Last Name
lastLabel=Label(root, text="Enter your last name:")
lastLabel.grid(row=2, column=0)

lastNa = Entry(root)
lastNa.grid(row=2, column=1)

#Email
emailLabel=Label(root, text="Enter your email address:")
emailLabel.grid(row=3, column=0)

email = Entry(root)
email.grid(row=3, column=1)

#Phone Number
phoneLabel=Label(root, text="Enter your phone number:")
phoneLabel.grid(row=4, column=0)

phone = Entry(root)
phone.grid(row=4, column=1)


#get info

def clicked():
   global firstName
   global count
   global lastName
   global emailAddress
   global phoneNumber
   firstName=Name.get()
   lastName=lastNa.get()
   emailAddress=email.get()
   phoneNumber=phone.get()
   labelConfirm=Label(root, text="Thank you " + firstName + " " + lastName + " at " + emailAddress + " and " + phoneNumber + " for continuing")
   labelConfirm.grid(row=6, column=0, columnspan=3)
   global cust
   cust=Customer(firstName, lastName, emailAddress, phoneNumber)
   count+=1


   # also destroys other labels

   mainlabel.destroy()
   nameLabel.destroy()
   Name.destroy()
   lastLabel.destroy()
   lastNa.destroy()
   emailLabel.destroy()
   email.destroy()
   phone.destroy()
   phoneLabel.destroy()
   confirmation.destroy()

   continu =Button(root, text="Click to continue", command=openaddwindow)
   continu.grid(row=7, column=0)







#Confirmation
confirmation=Button(root, text="Click to confirm details", command=clicked)
confirmation.grid(row=5, column=0, columnspan=3)




# creates second window
def openaddwindow():
   global fullAddress
   secondStep = Toplevel()
   secondStep.title("Step 2: Getting the address")
   secondStep.geometry("400x500")
   secondWindow = True
   #address questions
   steptwo = Label(secondStep, text="Now its time to get your address!")
   steptwo.grid(row=0, column=0, columnspan=2)
#second window questions
   addressLabel= Label(secondStep, text="Enter your address:")
   addressLabel.grid(row=1, column=0)

   addressEntry = Entry(secondStep)
   addressEntry.grid(row=1, column=1)

   stateLabel= Label(secondStep, text="Enter your state:")
   stateLabel.grid(row=2, column=0)

   stateEntry = Entry(secondStep)
   stateEntry.grid(row=2, column=1)

   cityLabel= Label(secondStep, text="Enter your city:")
   cityLabel.grid(row=3, column=0)

   cityEntry = Entry(secondStep)
   cityEntry.grid(row=3, column=1)

   zipLabel= Label(secondStep, text="Enter your zipcode:")
   zipLabel.grid(row=4, column=0)

   zipEntry = Entry(secondStep)
   zipEntry.grid(row=4, column=1)

   # assign to variables
   def addressclicked():
      global count
      global address
      global state
      global city
      global zip
      confirmationAddress.destroy()
      address = addressEntry.get()
      state = stateEntry.get()
      city = cityEntry.get()
      zip = zipEntry.get()
      #make address
      add=Address(address, state, city, zip)
      count+=1
      store = add.closest_store()
      menu=store.get_menu()

      def placeOrder():
         numbers=cardNumbersEntry.get()
         expDate=expirationEntry.get()
         secCode=securityCodeEntry.get()
         card= PaymentObject(numbers, expDate, secCode, zip)
         order.pay_with(card)
         orderConfirmation=Label(secondStep, text="Order placed!")
         orderConfirmation.grid(row=23, column=0)

      def search():
         searchTerm=searchEntry.get()
         searchResults=Label(secondStep, text="Please look at the console for the menu code. Ex:20BCOKE")
         searchResults.grid(row=9, column=0, columnspan=2)
         menu.search(Name=searchTerm)
         print("\n\n\n")

      def Add():
         orderCode=orderEntry.get()
         order.add_item(orderCode)
         addconfirmation = Label(secondStep, text="Item Added!")
         addconfirmation.grid(row=12, column=0)
         #time.sleep(2)
         #addconfirmation.destroy()

      def remove():
         ordercode=orderRemoveEntry.get()
         order.remove_item(ordercode)
         removeconfirmation = Label(secondStep, text="Item Removed!")
         removeconfirmation.grid(row=14, column=0)


      def payment():
         global cardNumbersEntry
         global expirationEntry
         global securityCodeEntry
         cardNumbers= Label(secondStep, text="Enter credit card number:")
         cardNumbers.grid(row=18, column=0)
         cardNumbersEntry=Entry(secondStep)
         cardNumbersEntry.grid(row=18, column=1)

         expiration = Label(secondStep, text="Enter expiration date without /:")
         expiration.grid(row=19, column=0)
         expirationEntry = Entry(secondStep)
         expirationEntry.grid(row=19, column=1)

         securityCode = Label(secondStep, text="Enter security code:")
         securityCode.grid(row=20, column=0)
         securityCodeEntry = Entry(secondStep)
         securityCodeEntry.grid(row=20, column=1)

         confirmationButton= Button(secondStep, text="Click to place order", command=placeOrder)
         confirmationButton.grid(row=21, column=1)







      #time to add searching
      searchLabel =Label(secondStep, text="Enter what you would like to search for:")
      searchLabel.grid(row=6, column=0)

      searchEntry=Entry(secondStep)
      searchEntry.grid(row=6, column=1)

      searchButton=Button(secondStep, text="Search", command=search)
      searchButton.grid(row=8, column=1)

      orderLabel= Label(secondStep, text="Enter the code for your wanted item:")
      orderLabel.grid(row=10, column=0)

      orderEntry= Entry(secondStep)
      orderEntry.grid(row=10, column=1)

      allDone=Button(secondStep, text="Pay", command=payment)
      allDone.grid(row=15, column=0)


      #add item
      orderAdd=Button(secondStep, text="Add to order", command=Add)
      orderAdd.grid(row=11, column=1)
      order=Order(store, cust, add)

      orderRemove=Label(secondStep, text="Enter the code for the item you want removed:")
      orderRemove.grid(row=13, column=0)


      #remove item
      orderRemoveEntry=Entry(secondStep)
      orderRemoveEntry.grid(row=13, column=1)

      orderRemoveButton=Button(secondStep, text="Remove Item", command=remove)
      orderRemoveButton.grid(row=14, column=1)

      #doneButton=Button(secondStep, text="Click if done", command=payment())
      #doneButton.grid(row=16, column=1)



# Address Confirm
   confirmationAddress = Button(secondStep, command=addressclicked, text="Click to confirm address")
   confirmationAddress.grid(row=5, column=1)





























root.mainloop()
