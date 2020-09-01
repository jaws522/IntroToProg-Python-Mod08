# ------------------------------------------------------------------------ #
# Title: Assignment 08
# Description: Working with classes

# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# RRoot,1.1.2030,Added pseudo-code to start assignment 8
# JBrecht,8.25.2020,Modified code to complete assignment 8
# ------------------------------------------------------------------------ #

# Data -------------------------------------------------------------------- #
import pickle

strFileName = 'products.txt'
lstOfProductObjects = []
strChoice = ""  # Captures the user option selection
strProduct = ""  # Captures the user product data
fltPrice = ""  # Captures the user price data
strStatus = ""  # Captures the status of processing functions


class Product:
    """Stores data about a product:

    properties:
        product_name: (string) with the product's  name
        product_price: (float) with the product's standard price
    methods:
    changelog: (When,Who,What)
        RRoot,1.1.2030,Created Class
        JBrecht,8.25.2020,Modified code to complete assignment 8
    """

    # -- Constructor --
    def __init__(self, prod_name, prod_price):
        # -- Attributes --
        self.product_name = prod_name
        self.product_price = prod_price

    # -- Properties --
    # Product name
    @property  # getter
    def product_name(self):
        return str(self.__product_name).upper()  # Upper case

    @product_name.setter
    def product_name(self, value):
        if not str(value).isnumeric():
            self.__product_name = value
        else:
            raise Exception("Product names cannot be numbers.")

    # Product price
    @property  # getter
    def product_price(self):
        return self.__product_price

    @product_price.setter
    def product_price(self, value):
        try:
            self.__product_price = float(value)
        except ValueError:
            print("Product price should be numeric.")
        self.__product_price = value


# Data -------------------------------------------------------------------- #

# Processing  ------------------------------------------------------------- #
class FileProcessor:
    """Processes data to and from a file and a list of product objects:

    methods:
        save_data_to_file(file_name, list_of_products):

        read_data_from_file(file_name): -> (a list of product objects)

        add_data_to_list(product, price, list_of_products): -> (a list of product objects, a status string)

    changelog: (When,Who,What)
        RRoot,1.1.2030,Created Class
        JBrecht,8.25.2020,Modified code to complete assignment 8
    """

    @staticmethod
    def save_data_to_file(file_name, list_of_products):
        """ Writes data from a list of object rows into a file

        :param file_name: (string) with name of file
        :param list_of_products: (list) you want filled with file data
        :return: (list) of object rows, (string) status
        """
        file = open(file_name, "wb")
        pickle.dump(list_of_products, file)  # the pickle
        file.close()
        return list_of_products, 'Success!'

    @staticmethod
    def read_data_from_file(file_name, list_of_products):
        """ Reads data from a file into a list of object rows

        :param file_name: (string) with name of file:
        :param list_of_products: (list) you want filled with file data:
        :return: (list) of object rows, (string) status
        """
        list_of_products.clear()  # clear current data
        try:
            file = open(file_name, "rb")
            list_of_products = pickle.load(file)  # the un-pickle
            file.close()
        except FileNotFoundError:
            file = open(file_name, "wb")
            file.close()
            print("Product list empty.")
        except EOFError:
            print("No data in file.")
        return list_of_products

    @staticmethod
    def add_data_to_list(product, price, list_of_products):
        """ Adds a new object row into a list of object rows

        :param product: (string) name of product
        :param price: (string) price of product
        :param list_of_products: (list) you want filled with file data
        :return: (list) of object rows, (string) status
        """
        list_of_products.append(Product(product, price))
        return list_of_products, 'Success!'


# Processing  ------------------------------------------------------------- #

# Presentation (Input/Output)  -------------------------------------------- #
class IO:
    """ Performs Input and Output tasks:

    methods:
        print_menu_products():

        input_menu_choice(): -> (a string with the user's choice)

        input_yes_no_choice(message): -> (a string with the user's choice)

        print_current_products_in_list(list_of_products):

        input_press_to_continue(optional_message=''):

        input_new_product_and_price(product_message, price_message): -> (two strings with the product name & price)

    changelog: (When,Who,What)
        RRoot,1.1.2030,Created Class
        JBrecht,8.25.2020,Modified code to complete assignment 8
    """

    @staticmethod
    def print_menu_Products():
        """  Display a menu of choices to the user

        :return: nothing
        """
        print('''
        Menu of Options
        1) Show Current List
        2) Add a new Product
        3) Save Data to File        
        4) Exit Program
        ''')
        print()  # Add an extra line for looks

    @staticmethod
    def input_menu_choice(message):
        """ Gets the menu choice from a user

        :return: string
        """
        choice = str(input(message)).strip()
        print()  # Add an extra line for looks
        return choice

    @staticmethod
    def input_yes_no_choice(message):
        """ Gets a yes or no choice from the user

        :return: string
        """
        return str(input(message)).strip().lower()

    @staticmethod
    def print_current_Products_in_list(list_of_products):
        """ Shows the current products in the list of object rows

        :param list_of_products: (list) of products you want to display
        :return: nothing
        """
        print("******* The current Products listed are: *******")
        for row in list_of_products:
            print(row.product_name + " (" + str(row.product_price) + ")")
        print("*******************************************")
        print()  # Add an extra line for looks

    @staticmethod
    def input_press_to_continue(optional_message=''):
        """ Pause program and show a message before continuing

        :param optional_message:  An optional message you want to display
        :return: nothing
        """
        print(optional_message)
        input('Press the [Enter] key to continue.')

    @staticmethod
    def input_new_product_and_price(product_message, price_message):
        """ Gets a product name and price from the user

        :param product_message: (string) request for product name
        :param price_message: (string) request for product price
        :return: (string) product name, product price
        """
        return str(input(product_message)).strip().lower(), str(input(price_message)).strip().lower()


# Presentation (Input/Output)  -------------------------------------------- #

# Main Body of Script  ---------------------------------------------------- #
# Load data from file into a list of product objects when script starts
lstOfProductObjects = FileProcessor.read_data_from_file(strFileName, lstOfProductObjects)  # read file data

# Show user a menu of options
while (True):
    IO.print_menu_Products()  # Shows menu

    # Get user's menu option choice
    strChoice = IO.input_menu_choice("Which option would you like to perform? [1 to 4] - ")  # message
    while strChoice not in str("1, 2, 3, 4"):
        strChoice = IO.input_menu_choice("Entry should be 1, 2, 3, or 4 - ")  # message

    # Show user current data in the list of product objects
    if strChoice.strip() == '1':  # Show products in memory
        IO.print_current_Products_in_list(lstOfProductObjects)  # Show current data in the list/table
        IO.input_press_to_continue(strStatus)
        continue  # to show the menu

    # Let user add data to the list of product objects
    if strChoice.strip() == '2':  # Add a new product
        strProduct, fltPrice = IO.input_new_product_and_price("Enter product name: ", "Enter product price: ")
        lstOfProductObjects, strStatus = FileProcessor.add_data_to_list(strProduct, fltPrice, lstOfProductObjects)
        IO.input_press_to_continue(strStatus)
        continue  # to show the menu

    # let user save current data to file and exit program
    elif strChoice == '3':  # Save Data to File
        strChoice = IO.input_yes_no_choice("Save this data to file? (y/n) - ")
        if strChoice.lower() == "y":
            lstOfProductObjects, strStatus = FileProcessor.save_data_to_file(strFileName, lstOfProductObjects)
            IO.input_press_to_continue(strStatus)
        else:
            IO.input_press_to_continue("Save Cancelled!")
            continue  # to show the menu
        print("\nGoodbye!")
        break  # and Exit

    # Exit Program
    elif strChoice == '4':
        print("\nGoodbye!")
        break  # and Exit

# Main Body of Script  ---------------------------------------------------- #
