from run_exchangerates import exchange


if __name__ == "__main__":
    cur = input("Input the curreny:").upper()
    amount = input("Input amount: ")
    # print(exchange(cur, amount))
    print(exchange(f"{cur}", f"{amount}"))
    