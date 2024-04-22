import requests
import sys

def fetch_todo_progress(employee_id):
    # Base URL of the API
    base_url = 'https://jsonplaceholder.typicode.com'

    # Endpoint for fetching user data
    user_endpoint = f'{base_url}/users/{employee_id}'

    # Endpoint for fetching todos for the user
    todo_endpoint = f'{base_url}/todos?userId={employee_id}'

    try:
        # Fetch user data
        user_response = requests.get(user_endpoint)
        user_data = user_response.json()
        
        # Fetch todo list for the user
        todo_response = requests.get(todo_endpoint)
        todo_data = todo_response.json()

        # Calculate number of completed tasks
        completed_tasks = [todo for todo in todo_data if todo['completed']]
        num_completed_tasks = len(completed_tasks)

        # Display the progress
        print(f"Employee {user_data['name']} is done with tasks ({num_completed_tasks}/{len(todo_data)}):")
        for task in completed_tasks:
            print(f"\t{task['title']}")

    except requests.exceptions.RequestException as e:
        print("Error fetching data:", e)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 <script_name.py> <employee_id>")
        sys.exit(1)
    
    employee_id = sys.argv[1]
    fetch_todo_progress(employee_id)

