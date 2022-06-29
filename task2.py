from startup import parse_startup_string, Startup, Factor

def main():
    startups = []
    while info := input("Enter a Start-up's factor ratings (seperated by comma):\n"):
        if info == "N":
            break
        if startup := parse_startup_string(info):
            startups.append(startup)
    if (len(startups) == 0):
        print("No startups given. exiting...")
        return
    print("Number of Start-ups:", len(startups))
    p1 = list(map(lambda s: s.name, filter(lambda s: s.calculate_classification() == "P1", startups)))
    p2 = list(map(lambda s: s.name, filter(lambda s: s.calculate_classification() == "P2", startups)))
    p3 = list(map(lambda s: s.name, filter(lambda s: s.calculate_classification() == "P3", startups)))
    rejected = list(map(lambda s: s.name, filter(lambda s: s.calculate_classification() == "R", startups)))
    print("Start-up progression rate:", '{:.0%}'.format((len(p1) + len(p2) + len(p3)) / len(startups)))
    factor1 = list(map(lambda s: s.founder, startups))
    print("Average rating for factor 1:", '{:.2f}'.format(sum(factor1) / len(startups)))
    factor2 = list(map(lambda s: s.industry, startups))
    print("Average rating for factor 2:", '{:.2f}'.format(sum(factor2) / len(startups)))
    factor3 = list(map(lambda s: s.traction, startups))
    print("Average rating for factor 3:", '{:.2f}'.format(sum(factor3) / len(startups)))
    factor4 = list(map(lambda s: s.gut, startups))
    print("Average rating for factor 4:", '{:.2f}'.format(sum(factor4) / len(startups)))
    print(f'Number of P1s: {len(p1)}{"," if len(p1) > 0 else ""}{",".join(p1)}')
    print(f'Number of P2s: {len(p2)}{"," if len(p2) > 0 else ""}{",".join(p2)}')
    print(f'Number of P3s: {len(p3)}{"," if len(p3) > 0 else ""}{",".join(p3)}')
    print(f'Number of Rs: {len(rejected)}{"," if len(rejected) > 0 else ""}{",".join(rejected)}')


if __name__ == '__main__':
    main()
