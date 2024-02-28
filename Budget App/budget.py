class Category:
    def __init__(self,name):
        self.name=name
        self.ledger=[]
    def deposit(self, amount, description=""):
        self.ledger.append({"amount": amount, "description": description})
    def withdraw(self, amount, description=""):
        if self.check_funds(amount):
            amount=-amount
            self.ledger.append({"amount": amount, "description": description})
            return True
        else:
            return False
    def get_balance(self):
        total=0
        for item in self.ledger:
            total += item["amount"]
        return total
    def transfer(self,amount, sourceCategory):
        if self.check_funds(amount):
            sourceCategory.deposit(amount, f"Transfer from {self.name}")
            self.withdraw(amount, f"Transfer to {sourceCategory.name}")
            return True
        else:
            return False
    def check_funds(self,amount):
        if self.get_balance()>=amount:
            return True
        else:
            return False
    def __str__(self):        
        self.name=self.name.lower().split()
        self.name[0]=self.name[0].capitalize()
        self.name="".join(self.name)
        string=[self.name.center(30,"*")]
        for item in self.ledger:
            line= item["description"][:23].ljust(23," ")+str("{:.2f}".format(item["amount"])).rjust(7," ")
            string.append(line) 
        total=f'Total: {self.get_balance()}'
        string.append(total)
        return "\n".join(string)
def create_spend_chart(categories):
    percentage=100
    total=0
    dicc={}
    for category in categories:
        negativos=[-1*item["amount"] for item in category.ledger if item["amount"]<0]
        total += sum(negativos)
        dicc[category.name]=sum(negativos)
    string="Percentage spent by category\n"
    
    while percentage>=0:
        circulos=["o" if float(dicc[category.name]/total)>=(percentage/100) else " " for category in categories]
        string += f'{str(percentage).rjust(3," ")}| {"  ".join(circulos)}  \n'
        percentage -= 10
    string += " "*4 + "-"*len(categories)*3+"-"+"\n"
    max_len_catgories=max(len(category.name) for category in categories)
    primera_letra=[category.name[0].upper() for category in categories] 
    string += " "*5+"  ".join(primera_letra)
    for i in range(1,max_len_catgories):
        string +="  \n" 
        letra=[category.name[i] if len(category.name)>i else " " for category in categories]
        string += " "*5+"  ".join(letra) 
    string+="  "
    return string
food = Category("Food")
entertainment = Category("Entertainment")
business = Category("Business")
food.deposit(900, "deposit")
entertainment.deposit(900, "deposit")
business.deposit(900, "deposit")
food.withdraw(105.55)
entertainment.withdraw(33.40)
business.withdraw(10.99)
print(create_spend_chart([business, food, entertainment]))