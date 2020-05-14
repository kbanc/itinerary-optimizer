from optimizer.route_creator import RouteCreator
from optimizer.generate_document import generate_doc

def main():
    r = RouteCreator('/Users/katherinebancroft/Desktop/Book1.csv')
    generate_doc(r)

if __name__ == "__main__":
    main()