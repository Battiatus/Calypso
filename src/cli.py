from PyInquirer import prompt
from converter import evtx_to_json, evtx_to_csv, evtx_to_xml

def main():
    questions = [
        {
            'type': 'list',
            'name': 'output_format',
            'message': 'Quel format de sortie souhaitez-vous?',
            'choices': ['csv', 'json', 'xml'],
        },
        {
            'type': 'input',
            'name': 'input_path',
            'message': 'Entrez le chemin vers le fichier ou le dossier:',
        }
    ]

    answers = prompt(questions)
    # Ici, vous devrez ajouter la logique pour traiter le chemin d'entrée en fonction du format de sortie choisi.
    print("Conversion en cours...")  # Placeholder pour la logique de conversion

if __name__ == "__main__":
    main()
