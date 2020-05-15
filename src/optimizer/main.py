from __future__ import print_function, unicode_literals
from PyInquirer import prompt, print_json
import os.path

from optimizer.route_creator import RouteCreator
from optimizer.generate_document import generate_doc

def main():
    questions = [{
        'type': 'input',
        'name': 'filepath',
        'message': "What's the absolute filepath to your location csv file?",
        'validate': lambda text: os.path.isfile(text) or "File does not exist"
    }
    ]
    answer = prompt(questions)
    r = RouteCreator(answer['filepath'])
    docName = generate_doc(r)
    fullDocPath = '{}/{}'.format(os.getcwd(), docName)
    print('Your itinerary can be found at: {}'.format(fullDocPath))

if __name__ == "__main__":
    main()