def compounded_interest(p, t, r, n):
    r = r / 100
    return p * ((1 + r/n) ** (n*t))


if __name__ == '__main__':
    principal = float(input("Enter the principal amount(in Rs.)"))
    time_period = float(input("Enter the time period(in years): "))
    rate = float(input("Enter the rate of interest(in %): "))
    no_of_times_interest_applied = float(input("Enter the number of times interest is applied in a time period: "))
    compound_interest = compounded_interest(principal, time_period, rate, no_of_times_interest_applied)
    print(f"Compound Interest for principal amount - Rs.{principal}, time period - {time_period} years, rate - "
          f"{rate}%, interest applied - {no_of_times_interest_applied} times: Rs. {compound_interest}")
