import requests
import json

# Vul hier je eigen Canvas API-token in
access_token = '12400~838tVeyBXC9t9JfmcJrzDBz4ey3JQy2WhhUDcWTLHWLychzk77nQQVYcUHctPfyY'

# Canvas API basis-URL
base_url = 'https://canvas.kdg.be/api/v1'
headers = {
    'Authorization': f'Bearer {access_token}'
}

# 🔹 Huidige gebruiker ophalen
def get_user_id():
    url = f'{base_url}/users/self'
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json().get('id')
    else:
        print("❌ Fout bij ophalen gebruiker:", response.status_code)
        return None

# 🔹 Opdrachten ophalen voor een specifieke cursus (ID 49875)
def get_assignments_for_course(course_id):
    url = f'{base_url}/courses/{course_id}/assignments'
    response = requests.get(url, headers=headers)
    return response.json() if response.status_code == 200 else []

# 🔹 Inzending en rubric-assessment ophalen voor een specifieke opdracht
def get_submission_and_rubric(course_id, assignment_id, user_id):
    url = f'{base_url}/courses/{course_id}/assignments/{assignment_id}/submissions/{user_id}'
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        submission_data = response.json()
        # Haal rubric_assessment op als het beschikbaar is
        if 'rubric_assessment' in submission_data:
            return submission_data['rubric_assessment']
        else:
            return None
    else:
        print(f"❌ Fout bij ophalen inzending voor opdracht {assignment_id}: {response.status_code}")
        return None

# 🔹 Alles ophalen voor de specifieke cursus met ID 49875 en printen
def print_course_assignments_with_grades(course_id):
    user_id = get_user_id()
    if not user_id:
        return

    assignments = get_assignments_for_course(course_id)
    result = {
        'course_id': course_id,
        'assignments': []
    }

    for assignment in assignments:
        rubric_assessment = get_submission_and_rubric(course_id, assignment['id'], user_id)
        assignment_data = {
            'assignment_id': assignment.get('id'),
            'assignment_name': assignment.get('name'),
            'rubric_assessment': rubric_assessment
        }

        result['assignments'].append(assignment_data)

    # Print alles als JSON
    print(json.dumps(result, indent=2, ensure_ascii=False))

# 🔸 Start het script voor de specifieke cursus (ID 49875)
course_id = 49875
print_course_assignments_with_grades(course_id)
