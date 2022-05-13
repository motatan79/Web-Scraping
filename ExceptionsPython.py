ItemsInCart = 0
# 2 items will be added to cart

if ItemsInCart != 2: # raise Exception("Products Cart count not matching")
    pass

assert(ItemsInCart == 0)

# try , except
try:
    with open('filelog.txt', 'r') as reader:
        reader.read()

except:
    print("Some how I reached this block because there is failure in try block")


# try , except
try:
    with open('filelog.txt', 'r') as reader:
        reader.read()
except Exception as e:
    print(e)
finally:
    print("cleaning your resources")