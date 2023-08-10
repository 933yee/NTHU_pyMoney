import sys
from datetime import date 
def confirm():
    """"double check some operations"""
    try:
        choice = int(input("[0] Cancel\n[1] Confirm\n>> "))
        if choice==1:
            return True
        elif choice==0:
            return False
        else:
            raise
    except:
        interval()
        sys.stderr.write("Invalid choice! Try again!\n\n")
        return confirm()
def interval():
    """"print interval"""
    print('\n'+"-"*80)
    print("="*80+'\n')
class Record:
    """Represent a record."""
    def __init__(self, date, category, item, amount):
        """initialize object 'Record'"""
        self._date = str(date)
        self._category = category
        self._item = item
        self._amount = amount
    @property
    def date(self):
        """return the date of the item"""
        return self._date
    @property
    def category(self):
        """return the category of the item"""
        return self._category
    @property
    def item(self):
        """return the name of the item"""
        return self._item
    @property
    def amount(self):
        """return the amount of the item"""
        return self._amount
    def __repr__(self):
        """return this object when called directly"""
        return self
class Records:
    """Maintain a list of all the 'Record's and the initial amount of money."""
    def __init__(self, categories):
        """read the data in the file 'records.txt' and initialize object 'Records' """
        self._records = []
        self._initial_money = 0
        #get the recorded datas
        try:
            with open("records.txt", "r") as file:
                money = file.readline().strip('\n')
                assert money , "The file is empty"
                self._initial_money = int(money)
                for data in file.readlines():
                    item = data.strip('\n').split()
                    int(item[3])
                    assert categories.is_category_valid(item[1]) == True, "Some categories in the file is invalid!\n"    
                    invalid = False             
                    try:
                        date.fromisoformat(item[0])
                    except:
                        invalid = True
                    assert invalid == False , "Some date in the file is invalid!\n"
                    self._records+=[Record(item[0], item[1], item[2], item[3])]
            return
        except AssertionError as err:
            self._records = []
            print(str(err))
        except (ValueError, IndexError):
            sys.stderr.write("The money in the file is invalid!\n")
        except OSError:
            pass
        #initialize the data if the file is broken or empty
           
    def add(self, date, cate, des, amou):
        """add a new item to Records"""
        self._records += [Record(date, cate, des, amou)]
        return
    def view(self):
        """show all the items in Records"""
        sum = 0
        my_header = "‖ Date         ‖ Category        ‖ Description        ‖ Amount     ‖"
        my_headers_space = my_header.split("‖ ")
        spaces = []
        for i in my_headers_space:
            spaces += [len(i)]
        size = len(my_header)
        halfsize = size//2

        print("↭ "*halfsize)
        print(my_header)
        print("↭ "*halfsize)
        for i in self._records:
            print("‖", i.date, end='')
            print(" "*(spaces[1]-len(i.date)), end='')
            print("‖",i.category, end='')
            print(" "*(spaces[2]-len(i.category)), end='')
            print("‖",i.item, end='')
            print(" "*(spaces[3]-len(i.item)), end='')
            print("‖",i.amount, end='')
            print(" "*(spaces[4]-len(i.amount)-1), end='')
            print("‖")
            sum += int(i.amount)
        print("↭ "*halfsize)
        print(f"Now you have {self._initial_money+sum} dollars.\n")
        
    def delete(self, label):
        del self._records[label]
    def find(self, categories):
        """show all the items whcih belong to a specific category"""
        category = input('Which category do you want to find?\n>>')
        if categories.is_category_valid(category) != True:
            interval()
            sys.stderr.write("""\
    The specified category is not in the category list.
    You can check the category list by command "view categories".
    Fail to find a record.\n\n""")
        else:
            p = categories.find_subcategories(category)
            sum = 0
            my_header = "‖ Date         ‖ Category        ‖ Description        ‖ Amount     ‖"
            my_headers_space = my_header.split("‖ ")
            spaces = []
            for i in my_headers_space:
                spaces += [len(i)]
            size = len(my_header)
            halfsize = size//2

            print("↭ "*halfsize)
            print(my_header)
            print("↭ "*halfsize)
            for i in self._records:
                if i.category in p:
                    print("‖", i.date, end='')
                    print(" "*(spaces[1]-len(i.date)), end='')
                    print("‖",i.category, end='')
                    print(" "*(spaces[2]-len(i.category)), end='')
                    print("‖",i.item, end='')
                    print(" "*(spaces[3]-len(i.item)), end='')
                    print("‖",i.amount, end='')
                    print(" "*(spaces[4]-len(i.amount)-1), end='')
                    print("‖")
                    sum += int(i.amount)
            print("↭ "*halfsize)
            print(f"The total amount above is  {sum} dollars.\n")
    def save(self):
        """write the data into 'records.txt'"""
        with open("records.txt", "w") as file:
            file.write(str(self._initial_money)+'\n')
            for data in self._records:
                file.write(data.date+' '+data.category+' '+data.item+' '+data.amount+'\n')

