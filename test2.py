ACCESS_TOKEN = '12400~838tVeyBXC9t9JfmcJrzDBz4ey3JQy2WhhUDcWTLHWLychzk77nQQVYcUHctPfyY'
import requests

# Vervang deze met je eigen Canvas API toegangstoken
ACCESS_TOKEN = 'jouw_toegangstoken'
BASE_URL = 'https://canvas.kdg.be/api/v1'

# Headers voor authenticatie
headers = {
    'Authorization': f'Bearer {ACCESS_TOKEN}'
}

# Functie om alle cursussen van de gebruiker op te halen (met paginering)
def get_courses():
    courses = []
    url = f'{BASE_URL}/courses'

    while url:
        try:
            response = requests.get(url, headers=headers)
            print(f"Opgevraagde URL: {url}")  # Debugging: toon de gevraagde URL
            print(f"Statuscode: {response.status_code}")  # Debugging: toon de statuscode van de API-response
            
            if response.status_code == 200:
                # Voeg de cursussen van de huidige pagina toe aan de lijst
                courses.extend(response.json())
                print(f"Aantal cursussen opgehaald: {len(response.json())}")  # Debugging: toon aantal cursussen op deze pagina

                # Check of er een volgende pagina is
                next_page = response.links.get('next')
                if next_page:
                    url = next_page['url']
                    print(f"Volgende pagina URL: {url}")  # Debugging: toon de volgende pagina-URL
                else:
                    url = None
            else:
                print(f"Fout bij ophalen van cursussen: {response.status_code}")
                break
        except Exception as e:
            print(f"Er is een fout opgetreden: {e}")
            break
    
    return courses

# Functie om de volledige JSON-respons van de cursussen af te drukken
def print_courses_json():
    # Verkrijg de cursussen van de gebruiker (met paginering)
    courses = get_courses()
    
    # Print de volledige JSON-respons
    if courses:
        print("JSON-antwoord van Canvas API voor cursussen:")
        print(courses)
    else:
        print("Geen cursussen gevonden.")

# Start het script
if __name__ == "__main__":
    print_courses_json()
