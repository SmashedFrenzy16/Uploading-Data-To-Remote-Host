from ftpretty import ftpretty

host = input("Enter host: ")

username = input("Enter username")

password = input("Enter password: ")


c = ftpretty(host, username, password)

c.get()

c.put()
