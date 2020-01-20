phone_book = {}
print('1.Add to phone_book\n2.Delete from phone_book\n3.Search\n4.Show all\n5.quit\n')
choice = int(input())
def add():
	x = input('input name of person')
	y = input('input number')
	phone_book[x] = y
add()
print(phone_book)