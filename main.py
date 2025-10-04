# Ordering Form

from pyscript import display, document

def placeorder(e):
    document.getElementById('showOrder').innerHTML= " "
    str_counter = 0
    itemNames = ['inputBanana', 'inputCookie', 'inputBrow', 'inputVelvet', 'inputCinna', 'inputPie']
    totalValue = 0
    totalOfItems = 0

    for itemName in itemNames:
            if document.getElementById(itemName).checked == True:
                totalValue = totalValue + float(document.getElementById(itemName).value)

    totalOfItems = totalValue

    name = document.getElementById('inputName').value
    email = document.getElementById('inputEmail').value
    phone = document.getElementById('inputPhone').value
    address = document.getElementById('inputAddy').value

    multiline_string = """
    Order for: {}
    Email Address: {}
    Phone Number: {}
    Home Address: {}
    Total: ₱ {:.2F}

    """.format(name, email, phone, address, totalOfItems)

    display(multiline_string, target="showOrder")