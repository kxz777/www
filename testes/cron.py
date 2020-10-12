from datetime import datetime
now = datetime.now()
now = now.strftime("%H:%M:%S")

f= open("/home/centos/www/temp/" + now  + ".txt","w+")
for i in range(10):
     f.write("This is line %d\r\n" % (i+1))
f.close()