from ftpretty import ftpretty

host = input("Enter host: ")

username = input("Enter username")

password = input("Enter password: ")


c = ftpretty(host, username, password)

c.get('someremote/file/on/server.txt', '/tmp/localcopy/server.txt')

c.put('/tmp/localcopy/data.txt', 'someremote/file/on/server.txt')
