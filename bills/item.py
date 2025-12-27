from enum import Enum
import datetime
from .entity import *

# Do not change the value of ISD_FACTOR var
ISD_FACTOR = 0.25


class TaxType(Enum):
    # Do not change this enum
    IVA = 1
    ISD = 2


class Tax:
    # Write the parameters in the next line
    def __init__(self, tax_id:str, tax_type:TaxType, percentage:float):
        # Write here your code
        self.tax_id=tax_id
        self.tax_type=tax_type
        self.percentage=percentage
        pass


class Product:
     # Write the parameters in the next line
    def __init__(self, product_id: str, name:str, expiration_date:datetime, bar_code:str, quantity:int, price:float, taxes: list[Tax]):
        # Write here your code
        self.product_id=product_id
        self.name=name
        self.expiration_date=expiration_date
        self.bar_code=bar_code
        self.quantity=quantity
        self.price=price
        self.taxes=taxes
        pass        

    def calculate_tax(self, tax: Tax) -> float:
        # Write here your code
        per_tax=0
        if tax.tax_type == TaxType.IVA: # calculate IVA
            per_tax = tax.percentage
        elif tax.tax_type == TaxType.ISD:
            per_tax = ISD_FACTOR * tax.percentage
        return (self.quantity * self.price * per_tax)
        pass

    def calculate_total_taxes(self) -> float:
        # Write here your code
        total_taxes=0
        for taxe in self.taxes:
            total_taxes += self.calculate_tax(taxe)
            #print(f"calculant taxes {total_taxes}")
        return total_taxes    
        pass

    def calculate_total(self) -> float:
        # Write here your code
        #print (f"calculant el total {self.price}")
        return (self.quantity * self.price + self.calculate_total_taxes())
        pass

    def __eq__(self, another):
        # Do not change this method
        return hasattr(another, 'product_id') and self.product_id == another.product_id

    def __hash__(self):
        # Do not change this method
        return hash(self.product_id)

    def print(self):
        # Do not change this method
        print(
            f"Product Id:{self.product_id} , name:{self.name}, quantity:{self.quantity}, price:{self.price}")
        for tax in self.taxes:
            print(f"Tax:{tax.tax_type} , percentage:{tax.percentage}")


class Bill:
    def __init__(self, bill_id: str, sale_date: datetime, seller: Seller, buyer: Buyer, products: list[Product]):
        # Write here your code
        self.bill_id=bill_id
        self.sale_date=sale_date
        self.seller=seller
        self.buyer=buyer
        self.products=products
        pass
       
    def calculate_total(self) -> float:
        # Write here your code
        total_prod=0
        for product in self.products:
             total_prod += product.calculate_total()   
        return (total_prod)
        pass

    def print(self):
        # Do not change this method
        self.buyer.print()
        self.seller.print()
        for product in self.products:
            product.print()