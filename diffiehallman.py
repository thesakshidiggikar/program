from random import randint


def generate_prime(bits):
    # Generate a random number of 'bits' length
    num = randint(2 ** (bits - 1), 2**bits - 1)
    # Keep generating until a prime number is found
    while not is_prime(num):
        num = randint(2 ** (bits - 1), 2**bits - 1)
    return num


def is_prime(n, k=5):
    if n == 2 or n == 3:
        return True
    if n <= 1 or n % 2 == 0:
        return False
    # Write n as 2^r * d + 1
    r, d = 0, n - 1
    while d % 2 == 0:
        r += 1
        d //= 2
    # Witness loop
    for _ in range(k):
        a = randint(2, n - 1)
        x = pow(a, d, n)
        if x == 1 or x == n - 1:
            continue
        for _ in range(r - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False
    return True


def primitive_root(prime):
    primitive_roots = []
    for a in range(2, prime):
        if len(primitive_roots) > 0:
            return primitive_roots
        for i in range(1, prime):
            if (a**i) % prime == 1:
                break
        else:
            primitive_roots.append(a)


def diffie_hellman(prime_length):
    prime = generate_prime(prime_length)
    primitive_roots = primitive_root(prime)
    g = primitive_roots[0]
    private_key_a = randint(2, prime - 1)
    public_key_a = pow(g, private_key_a, prime)
    private_key_b = randint(2, prime - 1)
    public_key_b = pow(g, private_key_b, prime)
    shared_secret_a = pow(public_key_b, private_key_a, prime)
    shared_secret_b = pow(public_key_a, private_key_b, prime)
    return shared_secret_a, shared_secret_b


# Example Usage:
prime_length = 256
shared_secret_a, shared_secret_b = diffie_hellman(prime_length)
print("Shared Secret A:", shared_secret_a)
print("Shared Secret B:", shared_secret_b)
