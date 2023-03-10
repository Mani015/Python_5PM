# Static method: It is a general utility method that performs a task in isolation. Inside this method,
# we don’t use instance or class variable because this static method doesn’t take any parameters like self and cls.


class Calculator:
    @staticmethod
    def Addition(x1,x2):
        print('x1 ',x1 ,'--->','x2',x2)
        print('addition of x1 and x2:',x1 + x2)
        return x1 +x2



object=  Calculator()
print(object.Addition(12,15))

# x1  12 ---> x2 15
# addition of x1 and x2: 27
# 27




