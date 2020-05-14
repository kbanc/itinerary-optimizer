from optimizer.route_creator import RouteCreator

def main():
    r = RouteCreator('/Users/katherinebancroft/Desktop/Book1.csv')

    for location in r.get_locations():
        print(location._street)

if __name__ == "__main__":
    main()