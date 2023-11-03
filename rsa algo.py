import random, math, time

def generate_prime_numbers():
  # Generates two random prime numbers
  while True:
    number1 = random.randint(2, 10000)
    number2 = random.randint(2, 10000)
    if is_prime(number1) and is_prime(number2):
      return number1, number2

def is_prime(number):
  # Checks if a number is prime.
  for i in range(2, number):
    if number % i == 0:
      return False
  return True

#1: Get two prime numbers
p, q = generate_prime_numbers()
print("two numbers are", p, q)

#2: multiply both of them
N = p*q
print("Multiply of numbers is", N)

#3: find the number of co-prime numbers of N
phi_n = (p-1)*(q-1)
print("phi of N", phi_n)

#4: chose a number with (i)range 1 and phi_n (ii) co-prime with phi_n and N

# Function to find all co-prime numbers relative to two given numbers in a specified range
start_time = time.time()
def coprimes_in_range(num1, num2, end):
    is_coprime = [True] * (end + 1)
    is_coprime[0] = is_coprime[1] = False

    for n in range(2, end + 1):
        if is_coprime[n]:
            if math.gcd(num1, n) != 1 or math.gcd(num2, n) != 1:
                for i in range(n, end + 1, n):
                    is_coprime[i] = False

    coprime_list = [n for n in range(1, end + 1) if is_coprime[n]]
    return coprime_list
end_time = time.time()

ek = random.choice(coprimes_in_range(N, phi_n, phi_n))
print("encryption key with time", ek, end_time-start_time)

print("Encryption Key is: (",ek,",", N,")")

#5: now find out the encryption key by the formula dk*ek(mod phi_n) = 1

def extended_gcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, x, y = extended_gcd(b % a, a)
        return (g, y - (b // a) * x, x)

def mod_inverse(e, phi_N):
    g, x, _ = extended_gcd(e, phi_N)
    if g != 1:
        raise ValueError("The modular inverse does not exist.")
    else:
        return x % phi_N

d = mod_inverse(ek, phi_n)
print("Decryption key is: (",d,",",N,")")

