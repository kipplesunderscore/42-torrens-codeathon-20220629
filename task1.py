from startup import parse_startup_string, Startup

def main():
    while info := input("Enter a Start-up's factor ratings (seperated by comma):\n"):
        if startup := parse_startup_string(info):
            print(startup.calculate_classification())

if __name__ == '__main__':
    main()
