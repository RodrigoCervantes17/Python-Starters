for fizz_buzz in range(51):
 if fizz_buzz%3== 0 and fizz_buzz%5==0:
    print ('Fizzbuzz')
    continue
 elif fizz_buzz%3==0:
    print ('Fizz')
    continue
 elif fizz_buzz%5==0:
    print ('Buzz')
    continue
 else:
    print (fizz_buzz)