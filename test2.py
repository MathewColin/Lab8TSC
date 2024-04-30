import requests
import unittest

class TestUpdateTaskIntegration(unittest.TestCase):
	base_url = "https://todo.pixegami.io"

	def test_update_task_success(self):
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

		new_task_data = {
			"task_id": task_id,
			"user_id": "matei",
			"content": "Il iubim pe Dragos <3, varianta modificata",
			"is_done": True
		}

		# Trimitem update
		third_request = requests.put(f"{self.base_url}/update-task", json=new_task_data)
		self.assertEqual(third_request.status_code, 200)

		fourth_request = requests.get(f"{self.base_url}/get-task/" + task_id)
		task_from_fourth_request = fourth_request.json()

		# Verificam sa fie diferit de varianta precedenta, chiar daca e redundant :))))
		self.assertNotEqual(task_data['content'], task_from_fourth_request['content'])
		self.assertEqual(new_task_data['content'], task_from_fourth_request['content'])
		self.assertEqual(new_task_data['is_done'], task_from_fourth_request['is_done'])
		self.assertEqual(new_task_data['user_id'], task_from_fourth_request['user_id'])


if __name__ == "__main__":
	unittest.main()
