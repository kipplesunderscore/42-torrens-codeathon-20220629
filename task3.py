from startup import parse_startup_string, Startup

def color_startup_name(name, category):
    if (category == "P1"):
        return f'\033[32;1m{name}\033[0m'
    if (category == "P2"):
        return f'\033[32m{name}\033[0m'
    if (category == "P3"):
        return f'\033[33m{name}\033[0m'
    if (category == "R"):
        return f'\033[31m{name}\033[0m'

def present(startups, classification):
    filtered = list(map(lambda s: s.name, filter(lambda s: s.calculate_classification() == classification, startups)))
    if len(filtered) == 0:
        print(f'No startup satisfied requirement for {classification} ratings.')
    else:
        for s in filtered:
            print(f'{color_startup_name(s, classification)},{classification}')

def present_rejected(startups):
    rejected = list(map(lambda s: s.name, filter(lambda s: s.calculate_classification() == "R", startups)))
    if len(rejected) == 0:
        print("No startup satisfied requirement for R ratings.")
    else:
        for s in rejected:
            print(f'{color_startup_name(s, "R")}')

def invest(startups):
    filtered = list(filter(lambda s: s.calculate_classification() != "R", startups))
    while True:
        s = input(f'How many businesses do you want to invest in (total non-rejected startups: {len(filtered)}):')
        if not s:
            return
        if s.isdecimal():
            n = int(s)
            if (n > len(filtered)):
                print("\033[0;31mInput Error:\033[0m input value was too large please input a number less than or equal to", len(filtered))
            else:
                break
        else:
            print("\033[0;31mInput Error:\033[0m input value was not a valid number please input a valid integer.")

    filtered = filter(lambda s: s.calculate_classification() != "R", startups)
    srt = list(sorted(filtered, key=lambda s: s.calculate_rating(), reverse=True))[:n]
    for startup in srt:
        print(f'{color_startup_name(startup.name, startup.calculate_classification())},{startup.calculate_classification()}')

def print_menu():
    print("1. Present all P1")
    print("2. Present all P2")
    print("3. Present all P3")
    print("4. Present all R")
    print("5. How many businesses do you want to invest in")
    print("6. Terminate")

def main():
    startups = [parse_startup_string("FiveFour Inc,3,4,2,2"),
                parse_startup_string("Rural Distillery,2,0,1,.5"),
                parse_startup_string("Acme corp,3,4,3.5,4.5"),
                # extra data
                parse_startup_string("Doggy Ties,1,1.5,1,0"),
                parse_startup_string("Baby Hatty,2,1.2,1.1,0.5"),
                parse_startup_string("Letus Play,4.5,4,4.5,4"),
                parse_startup_string("Litze,3,2.75,2.1,2"),
                parse_startup_string("Cakes for Days,3.2,2.8,3.5,3"),
                parse_startup_string("Abstrakt,2,2.5,2.3,2.6"),
                parse_startup_string("Performance Duds,2.4,2.25,2.5,2.5")]
    print_menu()
    while s := input("Which option do you want to see: "):
        if s.isdecimal():
            n = int(s)
        else:
            n = 0
        if (n == 6):
            break
        if (n == 1):
            present(startups, "P1")
        elif (n == 2):
            present(startups, "P2")
        elif (n == 3):
            present(startups, "P3")
        elif(n == 4):
            present_rejected(startups)
        elif(n == 5):
            invest(startups)
        else:
            print("\033[0;31mInput Error:\033[0m invalid selection please input a number between: (1 - 6)")
        print_menu()

if __name__ == '__main__':
    main()
