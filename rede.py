import random
import string

def generate_redeem_code():
    code = ''.join(random.choices(string.ascii_uppercase + string.digits, k=16))
    return code

def generate_redeem_codes(num_codes):
    redeem_codes = []
    for _ in range(num_codes):
        code = generate_redeem_code()
        redeem_codes.append(code)
    return redeem_codes

num_codes = 1000
redeem_codes = generate_redeem_codes(num_codes)
