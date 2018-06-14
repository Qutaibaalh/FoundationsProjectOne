
menu = {
    "original cupcake": 2,
    "signature cupcake": 2.750,
    "coffee": 1,
    "tea": 0.900,
    "bottled water": 0.750
}
original_flavors = ["vanilla", "chocolate", "strawberry", "caramel", "raspberry"]
original_price = 2
signature_price = 2.750

############################# Start Here! ##############################
cupcake_shop_name = "cupncakes"
signature_flavors = ["peanute", "pistachio", "orange"]
order_list = []


def print_menu():
    for item in menu:
        print("- %s (KD %s)" % (item, menu[item]))
    
    


def print_originals():
    print("Our original flavor cupcakes (KD %s each):" % original_price)
    # your code goes here!
    for item in original_flavors:
        print("- \"%s\"" % item)


def print_signatures():
    
    

    print("Our signature flavor cupcake (KD %s each):" % signature_price)
    for item in signature_flavors:
        print("- \"%s\"" % item)


def is_valid_order(order):
    for item in menu: 
        if item == order: 
            return True  
    for item in original_flavors:
        elif item == order:
                return True
    for item in signature_flavors:
        elif item == order 
            return True 
    else:
        return False 





def get_order():
    """
    Repeatedly ask customer for order until they end their order by typing "Exit".
    """
    order_list = []
    # your code goes here!

    return order_list


def accept_credit_card(total):
    
    Return whether an order is eligible for credit card payment.
    if total >= 5:
        return True
    else:
        return False


def get_total_price(order_list):
    
    Calculate and return total price of the order.
    
    total = 0
    for order in order_list:
         if order in menu:
            total += menu[order]
        elif order in original_flavors:
            total += original_price
        elif order in signature_flavors:
            total += signature_price

    return total


def print_order(order_list):
    """
    Print the order of the customer.
    """
    print()
    print("Your order is: ")
    # your code goes here!
