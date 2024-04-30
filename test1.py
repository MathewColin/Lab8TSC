import requests
import unittest

class TestCreateTaskIntegration(unittest.TestCase):
	base_url = "https://todo.pixegami.io"

	def test_create_task_success(self):
		task_data = {
			"user_id": "matei",
			"content": "Il iubim pe Dragos <3",
			"is_done": False
		}

		response = requests.put(f"{self.base_url}/create-task", json=task_data)
		task_id = response.json()['task']['task_id']
		self.assertEqual(response.status_code, 200)

		second_response = requests.get(f"{self.base_url}/get-task/" + task_id)
		self.assertEqual(response.status_code, 200)

		task_from_response = second_response.json()
		self.assertEqual(task_data['content'], task_from_response['content'])
		self.assertEqual(task_data['is_done'], task_from_response['is_done'])
		self.assertEqual(task_data['user_id'], task_from_response['user_id'])

if __name__ == "__main__":
	unittest.main()
