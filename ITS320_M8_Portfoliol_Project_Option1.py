import sys, csv


class Automobile:  
    def __init__(self, make, model, color, year, miles): 
        self._make = make
        self._model = model
        self._color = color
        self._year = year
        self._miles = miles
        
    def make(self):
        return self._make

    def model(self):
        return self._model

    def color(self):
        return self._color
    
    def year(self):
        return self._year
    
    def miles(self):
        return self._miles


    def print_Automobile(o):
        if not isinstance(o, Automobile):
            raise TypeError('print_Automobile(): requires an Automobile')
        print('This is a {} {} {} {} and has {} miles on it.'.format(o.color(), o.year(), o.make(), o.model(), o.miles()))



def main():
    allInventory = []
    
    
    def add_new_car():
        
        print('Add a new car to the inventory... \n')
        inventory = []
        
        make = input('Enter a car make:\t') 
        inventory.append(make)
              
        model = input('Enter a car model:\t') 
        inventory.append(model)
              
        color = input('Enter a car color:\t') 
        inventory.append(color)
        
        year = input('Enter a car year:\t') 
        inventory.append(year)
              
        mileage = input('Enter a car mileage:\t') 
        inventory.append(mileage)
        
        allInventory.append(inventory)
        
        
        print('The following car was added to inventory:')
        print('{0:<10} {1:<10} {2:<10} {3:<10} {4:<10}'.format(*inventory), '\n')
        #print('The complete vehicle inventory is: ')
        #view_inventory()
        print('\n')
            
    def update_inventory():
       
        
        print('Update a car from the inventory...')
    
        view_inventory()    
        
        
        itemToUpdate1 = input("Enter the name of the data you wish to replace:")
        itemToUpdate2 = input("Enter the new information now:")
        for j in allInventory:
            if itemToUpdate1 in j:
                position = j.index(itemToUpdate1)
                j[position] = itemToUpdate2
                break
    
    def delete_car():
        
        print("Which car do you want to delete?")
        view_inventory()
        
      
        itemDrop = input("Enter the name of the car data to delete.")
        
        for x in allInventory:
            for y in x:
                if y == itemDrop:
                    allInventory.remove(x)
        print('You have deleted', itemDrop)
        
        
    def view_inventory():
        print('Vehicle Inventory'.center(50))
        
        header = ['Make', 'Model', 'Color', 'Year', 'Milage']
    
        print('{0:<10} {1:<10} {2:<10} {3:<10} {4:<10}'.format(*header))
        for x in allInventory:
            print('{0:<10} {1:<10} {2:<10} {3:<10} {4:<10}'.format(*x))
        print('\n')
   
    def print_inventory_file():
        title_header = ['Vehicle Inventory'.center(100)]
        header = ['Make', 'Model', 'Color', 'Year', 'Milage']
        
        
        
        with open('CarInventory.csv', 'w', newline= '') as f:              
            writer = csv.writer(f)
            writer.writerow(title_header)
            writer.writerow(header)
            
            for x in allInventory:
                writer.writerow(x)
            print('Excel file "Vehicle Inventory" has been created.')
     
        
    def main_menu():
        print('-------Car Inventory MAIN MENU-------')
        print('1: Add a new car to the Inventory')
        print('2: Update an existing car in the Inventory')
        print('3: Delete an existing car from the Inventory')
        print('4: View the current car inventory')
        print('5: Print the Vehicle Inventory to a csv file')
        print('6: Enter 6 to stop executing program')
        print('-------------------------------------- \n')
    
    
    while True:
        try:
            main_menu()
            menu = int(input('Enter the number of your selection from Main Menu: \n'))  
            
            
            if menu == 1:
                add_new_car()
            elif menu == 2:
                update_inventory()
            elif menu == 3:
                delete_car()
            elif menu == 4:
                view_inventory()     
            elif menu == 5:
                print_inventory_file()
            elif menu  == 6:
                print('You have selected to Exit the Car Inventory program')
                sys.exit()    
            else:
                print('That number is not valid. Please try 1-6.')
                print('Enter your choice again')
                main_menu()
                             
        except ValueError: 
            print('You may only select values 1-6.')
            main_menu()  

if __name__ == '__main__': main()                  