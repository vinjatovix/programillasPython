import random

def premiado():
    for i in range(6):
        yield random.randint(1,50)
    
    yield random.randint(1,10)

# generado automatico
for i in premiado():
    print('el siguiente numero es %d' %(i))

#generado manual

print(next(premiado()))