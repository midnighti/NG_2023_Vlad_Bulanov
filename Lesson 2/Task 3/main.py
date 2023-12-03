def find_divisors(num):
    return [element for element in range(1, num + 1) if num % element == 0]

def is_prime(num):
    return len(find_divisors(num)) == 2

def generate_table(limit):
    return [(num, find_divisors(num)) for num in range(1, limit + 1)]

def main():
    try:
        limit = int(input("Enter the upper limit for the table: "))
        if limit < 1:
            print("Please enter a number greater than 0.")
            return

        table = generate_table(limit)

        print("\nTable of numbers and their divisors:")
        print("Number | Divisors")
        print("-" * 20)
        for num, divisors in table:
            print(f"{num}      | {', '.join(map(str, divisors))}")

        primes = [num for num in range(1, limit + 1) if is_prime(num)]
        print("\nPrime numbers:")
        print(", ".join(map(str, primes)))

    except ValueError:
        print("Please enter a valid number.")

if __name__ == "__main__":
    main()
