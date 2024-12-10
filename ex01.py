#Function test

def test (n):
    return (n >= 100) and (n < 1000)

#Function sum_digits

def sum_digits (n):
    a = (n // 100)
    b = (n // 10)%10
    c = n%10
    return (a+b+c)

#Function product_digits

def product_digits (n):
    a = (n // 100)
    b = (n // 10)%10
    c = (n % 10)

    return (a*b*c)

#Function abs

def abs (n):
  if n < 0 :
      return n
  else :
      return -n

  #Function loop

def lp(n):
    n = abs(n)  # On prend la valeur absolue de n
    if sum_digits(n) == product_digits(n):  # Comparaison avec "=="
        return n  # On retourne n si la condition est remplie
    else:
        return lp(n + 1)  # Sinon, on fait appel récursivement à lp(n + 1)
