def luhn_check(number):
    digits = [int(d) for d in str(number)]
    total = 0
    reverse_digits = digits[::-1]

    for i, d in enumerate(reverse_digits):
        if i % 2 == 1:  
            d = d * 2
            if d > 9:
                d -= 9
        total += d

    return total % 10 == 0


# Example usage
card_number = "4539578763621486"
if luhn_check(card_number):
    print(f"{card_number} is VALID")
else:
    print(f"{card_number} is INVALID")
