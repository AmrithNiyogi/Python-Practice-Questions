def calculate_simple_interest(p, t, r):
    return (p * t * r) / 100


if __name__ == '__main__':
    principal = int(input("Enter the principal amount(in Rs.)"))
    time_period = int(input("Enter the time period(in years): "))
    rate = int(input("Enter the rate of interest(in %): "))
    simple_interest = calculate_simple_interest(principal, time_period, rate)
    print(f"Simple Interest for principal amount - Rs.{principal}, time period - {time_period} years, and rate - "
          f"{rate}%: Rs. {simple_interest}")
