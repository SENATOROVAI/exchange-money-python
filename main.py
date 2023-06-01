from run_exchangerates import exchange


if if __name__ == "__main__":
    cur = str(input("Input the curreny:".upper()))    
    amount = input("Input amount: ")
    print(exchange(f"{cur}", f"{amount}"))
