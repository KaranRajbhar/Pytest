class InsufficientException(Exception):
    pass

class MobileInventory:
    @classmethod
    def __init__(cls,inventory=None):
        if inventory == None:
            cls.balance_inventory = {}
        else:
            if not(isinstance(inventory,dict)):
                raise TypeError("Input inventory must be a dictionary")
            for k,v in inventory.items():
                if not isinstance(k,str):
                    raise ValueError("Mobile model name must be a string")
                if not(isinstance(v,int) and v >= 0):
                    raise ValueError("No. of mobiles must be a positive integer")
            cls.balance_inventory = inventory
    @classmethod
    def add_stock(cls,new_stock):
        if not(isinstance(new_stock,dict)):
                raise TypeError("Input inventory must be a dictionary")
        for k,v in new_stock.items():
            if not isinstance(k,str):
                raise ValueError("Mobile model name must be a string")
            if not(isinstance(v,int) and v >= 0):
                raise ValueError("No. of mobiles must be a positive integer")
        cls.balance_inventory.update(new_stock)

    @classmethod
    def sell_stock(cls,requested_stock):
        if not(isinstance(requested_stock,dict)):
                raise TypeError("Requested stock must be a dictionary")
        for k,v in requested_stock.items():
            if not isinstance(k,str):
                raise ValueError("Mobile model name must be a string")
            if not(isinstance(v,int) and v >= 0):
                raise ValueError("No. of mobiles must be a positive integer")
            
            if k not in cls.balance_inventory:
                raise InsufficientException("No Stock. New Model Request")
            if cls.balance_inventory[k] < v:
                raise InsufficientException("Insufficient Stock")
                                
