class Book:
  def __init__(self, bookName = None, bookPrice = 0, bookDiscountRate = 0):
    self.__bookName = bookName
    self.__bookPrice = bookPrice
    self.__bookDiscountRate = bookDiscountRate

  def setBookPrice(self, bookPrice):
    self.__bookPrice = bookPrice

  def getBookPrice(self):
    return self.__bookPrice

  def getDiscountBookPrice(self):
    return self.__bookPrice - self.__bookPrice * (self.__bookDiscountRate/100)

  def __str__(self):
    return '%s %d %d%%' % (self.__bookName, self.__bookPrice, self.__bookDiscountRate)


bo1 = Book("SQL Plus", 50000, 5)
bo2 = Book("Java 2.0", 40000, 3)
bo3 = Book("JSP Servlet", 60000, 6)
bookList = [bo1, bo2, bo3]

for book in bookList:
  print(book)

print()

print(f"책 가격의 합 : {bo1.getBookPrice()+bo2.getBookPrice()+bo3.getBookPrice()}원")
print(f"할인 된 책 가격의 합: {bo1.getDiscountBookPrice()+bo2.getDiscountBookPrice()+bo3.getDiscountBookPrice()}원")