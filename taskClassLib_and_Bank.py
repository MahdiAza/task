"""
1. تسک اول:
    ساخت یک کلاس شیء گرا در پایتون برای مدیریت کتابخانه.
این کلاس باید دارای توابعی برای اضافه کردن کتاب، حذف کتاب، جستجو بر اساس نام کتاب، نام نویسنده یا ژانر کتاب باشد.
همچنین باید قابلیت بروزرسانی اطلاعات کتاب را داشته باشد.
برای هر کتاب باید اطلاعاتی مانند نام کتاب، نام نویسنده، ژانر و تعداد صفحات ذخیره شود. 

2. تسک دوم:
    ساخت یک کلاس در پایتون برای مدیریت یک بانک. 
این کلاس باید دارای توابعی برای ایجاد حساب بانکی، بستن حساب، برداشت وجه، واریز وجه و چاپ موجودی حساب باشد.
برای هر حساب باید اطلاعاتی مانند شماره حساب، نام صاحب حساب، موجودی حساب و رمز عبور ذخیره شود.
همچنین باید قابلیت بروزرسانی اطلاعات حساب و تغییر رمز عبور را داشته باشد.
"""

class Lib:
    
    def __init__(self) -> None:
        self.books=[]
    
    def addbook(self,bookName,authorName,genre,totalNumPage):
        self.books.append([bookName,authorName,genre,totalNumPage])
    
    def showAllBooks(self,books=None):
        
        if books==None:
            books=self.books
        for index,book in enumerate(books):
            print("{}-bookName:{} ,authorName:{} ,genre:{} ,totalNumPage:{}".format(index,book[0],book[1],book[2],book[3]))
            
    
    def deleteBook(self):
        self.showAllBooks()
        num=int(input("enter the number: "))
        del self.books[num]
        print("removed successfuly")
    
    def searchByNameBook(self,nameBook):
        templist=[]
        for book in self.books:
            if book[0]==nameBook:
                templist.append(book)
        if len(templist)==0:
            print('not fund')
        self.showAllBooks(templist)    
    
    def searchByAuthorBook(self,authorBook):
        templist=[]
        for book in self.books:
            if book[1]==authorBook:
                templist.append(book)
        if len(templist)==0:
            print('not fund')
        self.showAllBooks(templist)    
    
    def searchByGenreBook(self,genreBook):
        templist=[]
        for book in self.books:
            if book[2]==genreBook:
                templist.append(book)
        if len(templist)==0:
            print('not fund')
        self.showAllBooks(templist)            
        

#-------------------------- task2 Bank class ------------------------------
class Bank:
    def __init__(self) -> None:
        self.accounts=[]
    
    def addAcount(self,accountNum,accountName,balance,password):
        self.accounts.append([accountNum,accountName,balance,password])
   
    def showAllAccount(self):
        print(self.accounts)    
    
    def searchByAccountNum(self,accountNum):
        for account in self.accounts:
            if account[0]==accountNum:
                return self.accounts.index(account)
        return None        
        
    def closeAccount(self,accountNum):
        indexAccount=self.searchByAccountNum(accountNum)
        if indexAccount!=None:
            del self.accounts[self.accounts.index(indexAccount)]
            print("closed successfuly")
        else:
            print("account not fund")
        
    def Withdrawal(self,accountNum,amount):
        indexAccont=self.searchByAccountNum(accountNum)
        if indexAccont!=None:
            if self.accounts[indexAccont][2]-amount<0:
                print('not enough money')
            else:
                self.accounts[indexAccont][2]-=amount
                print("withdrawal successfuly")
        else:
            print("account not fund")    
    
    def deposit(self,accountNum,amount):
        indexAccont=self.searchByAccountNum(accountNum)
        if indexAccont!=None:
            self.accounts[indexAccont][2]+=amount
            print("deposit successfuly")
        else:
            print("account not fund")
   
    def balance(self,accountNum):
        indexAccont=self.searchByAccountNum(accountNum)
        if indexAccont!=None:
            print("balance=",self.accounts[indexAccont][2])
        else:
            print("account not fund")
    
    def updateAccount(self,accountNum,accountName,balance):
        indexAccont=self.searchByAccountNum(accountNum)
        if indexAccont!=None:
            self.accounts[indexAccont][1]=accountName
            self.accounts[indexAccont][2]=balance
            print("updated")
        else:
            print("account not fund")
    def updatePass(self,accountNum,oldPass,NewPass):
        indexAccont=self.searchByAccountNum(accountNum)
        if indexAccont!=None:
            if self.accounts[indexAccont][3]==oldPass:
                self.accounts[indexAccont][3]=NewPass
                print("updated")
            else:
                print("The old password is not equal")
        else:
            print("account not fund")
