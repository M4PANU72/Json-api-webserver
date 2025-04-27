headers = {
    'Authorization': 'Bearer 12400~cKeaCecuKBv2F3k3h9LwcCvz8Z3U4PaPaLYtutk7knFCBVRV6z7DGLymB2vx9BZk'
}

import requests

response = requests.get('https://canvas.kdg.be/api/v1/users/self', headers=headers)
user_data = response.json()
print(user_data)
print("###################")

response = requests.get('https://canvas.kdg.be/api/v1/courses', headers=headers)
courses = response.json()
for course in courses:
    print(course['name'])
print("###################")

course_id = 49875  # Vervang door het echte cursus-ID
response = requests.get(f'https://canvas.kdg.be/api/v1/courses/{course_id}/assignments', headers=headers)
assignments = response.json()
for assignment in assignments:
    print(assignment['name'])


print("###################")

assignment_id = 221532  # Vervang door het echte opdracht-ID
user_id = 49951  # Gebruik je eigen gebruikers-ID
response = requests.get(f'https://canvas.kdg.be/api/v1/courses/{course_id}/assignments/{assignment_id}/submissions/{user_id}?include[]=rubric_assessment', headers=headers)
submission = response.json()
print(submission)