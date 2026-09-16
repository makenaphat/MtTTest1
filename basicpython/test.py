import mymodule as mx
import platform

from mymodule import person1

print(person1["age"])

x = platform.system()
print(x)

x = dir(platform)
print(x)

mx.greeting("Jonathan")

a = mx.person1["age"]
print(a)