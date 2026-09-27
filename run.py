import sys
from package_of_amur.hello import say_hello



from package_of_amur.hello import say_hello_v2

say_hello_v2()
if len(sys.argv) > 1 and sys.argv[1] == "say_hello_v2":
    say_hello_v2()
else:
    say_hello()




say_hello()

