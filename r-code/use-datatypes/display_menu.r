if(F){
"
Author: Viernes, Michael
Date: 3:47 PM 5/4/2022
Objective: Use your knowledge in constructing variables.
Program: Restaurant name_menu
Description: Display a list of mneu in a sample restaurant. We shall call it 'Carenderiahan'.
"
}

# Make 6 items each in the list of name_menu appetizer, drinks and sweets with tagged prices.
name_menu <- c("Price", "Appetizer", "Drinks", "Sweets", "Services")

price_appetizer <- c(100.00, 140.00, 200.00, 175.00, 325.00, 215.00)
price_drinks <- c(15.00, 50.00, 50.00, 100.00, 100.00, 70.00)
price_sweets <- c(25.00, 25.00, 60.00, 50.00, 25.00, 25.00)
price_services <- c(400.00, 5000.00, 275.00, 100.00, 300.00, 500.00)

appetizer <- c("Adobo", "Kaldereta", "Sinigang", "Spaghetti", "Pancit", "Bulalo")
drinks <- c("Iced Water", "Milk Tea (assorted)", "Mogu-mogu", "Frappe (assorted)", "Fruit Juice", "Hot/Iced Coffee")
sweets <- c("Banana Sundae", "Cheuffan", "Swiss Roll", "Ensaymada", "Cupcake", "Maruya")
services <- c("Guest Reservation", "Birthday Reservation", "Waiter Assistance", "Television", "High Speed Wi-Fi", "Playground Pass")

list_appetizer <- matrix(c(price_appetizer, appetizer), nrow=6, ncol=2, byrow=F, dimnames=list(LETTERS[1:6], name_menu[1:2]))
list_drinks <- matrix(c(price_drinks, drinks), nrow=6, ncol=2, byrow=F, dimnames=list(LETTERS[1:6], c(name_menu[1],name_menu[3])))
list_sweets <- matrix(c(price_sweets, sweets), nrow=6, ncol=2, byrow=F, dimnames=list(LETTERS[1:6], c(name_menu[1],name_menu[4])))
list_services <- matrix(c(price_services, services), nrow=6, ncol=2, byrow=F, dimnames=list(LETTERS[1:6], c(name_menu[1],name_menu[5])))

menu <- list(list_appetizer, list_drinks, list_sweets, list_services)

print("Carenderiahan's Menu")
print(menu)

# Requesting for user input. to be added ...