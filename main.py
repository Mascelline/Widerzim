import os    # for reading file in different OS systems
import time
import pandas as pd
import xml.etree.ElementTree as ET   # importing xml operations enabler

xml_data = open('orders.xml', 'r').read()  # Read data file

tree = ET.ElementTree(file="orders.xml")
root = tree.getroot()   # getting the parent tag of the xml document



print("start time:")
print(time.time())

def show_orders ():  # printing all orderbooks
    for child in root:
        data = {'Buy': [child.attrib],
                'Sell': [child.attrib]}
        print("====================")
        df = pd.DataFrame(data, columns=['Buy', 'Sell'])
        print(child.tag, child.attrib)


    df = pd.DataFrame(data, columns=['Buy', 'Sell'])
    print([df.child.attrib])
    #print(child.tag, child.attrib)



def add_orders():
    orders = tree.findall('AddOrder')  #Look up the order book based upon the book attribute.
    if orders.child.__getattribute__('orderID') == True:
            print ()
    else:                               #If the book does not exist create it.
        orders.child.append(['Addorder'])

    for i in orders:
        if orders.child.__getattribute__('volume') == orders.child.__getattribute__['volume'] == True:  # if there are matching elements,Orders having their whole quantity being matched (i.e. volume == 0) are removed from the book.
            orders.child.__getattribute__['volume'].remove()
        else: #If the incoming order is either partly or not matched the order is inserted into the book.
            orders.child.__getattribute__['volume'].insert()
            return  orders

def delete_orders():
    orders = tree.findtext("Book")
    if orders.child.attrib == "Book" : #   if child.attrib ==  # Look up of Book Attribute is
        orders.index() #Locate the order in the book based upon the orderId attribute.
    else:        # If the order is not found just ignore the operation and just continue.
        if orders.__eq__('orderId')   == True:
            orders.child.attrib('orderID').remove()#If found remove the order from the book.

show_orders()
print ("end time:")
print ( time.time())
