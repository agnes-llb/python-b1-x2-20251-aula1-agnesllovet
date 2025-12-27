# Write your imports here
from .entity import Buyer, Seller
from .item import *

class OrderType:
    # Do not change this enum
    ASC = 0
    DES = 1


class Statistics:
    def __init__(self, bills: list[Bill]):
        # Do not change this method
        self.bills = bills

    def find_top_sell_product(self) -> tuple [Product, int]:
        # Write here your code
        # calculem un dictionari on hi hagi el producte i elc cops que apareix
        products_list ={}
        for bill in self.bills:
            for product in bill.products:
                if product in products_list:
                    products_list [product] = products_list.get (product) + 1
                else:      
                    products_list [product]=1
        # Un cop tenim diccionari -> mirem quin producte ha sortit mes
        return (max(products_list.items(), key= lambda item : item[1]))


    def find_top_two_sellers(self) -> list:
        # Write here your code
        sellers_list ={}
        for bill in self.bills:
            if bill.seller in sellers_list:
                sellers_list [bill.seller]= sellers_list.get (bill.seller) + bill.calculate_total()
            else:
                sellers_list [bill.seller]= bill.calculate_total()  
        # Retornem els dos millors
        top_two= sorted(sellers_list.items(), key= lambda item: item[1], reverse =True)[0:2]
        return [seller for seller,_ in top_two]
        pass

    def find_buyer_lowest_total_purchases(self) -> tuple [Buyer, float]:
        # Write here your code
        buyer_list={}
        for bill in self.bills:
            buyer_list [bill.buyer] = buyer_list.get (bill.buyer, 0) + bill.calculate_total()
        return (min(buyer_list.items(), key= lambda item: item[1]))
        pass

    def order_products_by_tax(self, order_type: OrderType) -> tuple:
        # Write here your code
        products_list={}
        for bill in self.bills:
            for product in bill.products:
                products_list [product] = products_list.get (product, 0)+ product.calculate_total_taxes()
        if (order_type == OrderType.ASC):  # Ordenem en sentit ascendent
            return sorted (products_list.items(), key= lambda item: item[1], reverse= False)
        elif order_type == OrderType.DES:
            return sorted (products_list.items(), key= lambda item: item[1], reverse= True)
        pass

    def show(self):
        # Do not change this method
        print("Bills")
        for bill in self.bills:
            bill.print()
