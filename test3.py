import requests
import unittest
import uuid

class TestListTaskIntegration(unittest.TestCase):
	base_url = "https://todo.pixegami.io"

	def test_list_task_success(self):
		unittest_id = str(uuid.uuid4())
		tasks_cnt = 3 

		task_data = [{
			"user_id": unittest_id,
			"content": "Il iubim pe Dragos <3, partea 1",
			"is_done": False
		},{
			"user_id": unittest_id,
			"content": "Il iubim pe Dragos <3, partea 2",
			"is_done": False
		},{
			"user_id": unittest_id,
			"content": "Il iubim pe Dragos <3, partea 3",
			"is_done": False
		}]

		for i in range(tasks_cnt):
			response = requests.put(f"{self.base_url}/create-task", json=task_data[i])
			self.assertEqual(response.status_code, 200)

		list_response = requests.get(f"{self.base_url}/list-tasks/" + unittest_id)
		self.assertEqual(list_response.status_code, 200)

		my_tasks = list_response.json()['tasks']
		
		my_tasks.sort(key=lambda x: str(x['content']))

		self.assertEqual(len(my_tasks), 3)
		
		for i in range(tasks_cnt):
			self.assertEqual(task_data[i]['content'], my_tasks[i]['content'])
			self.assertEqual(task_data[i]['is_done'], my_tasks[i]['is_done'])
			self.assertEqual(task_data[i]['user_id'], my_tasks[i]['user_id'])

		
if __name__ == "__main__":
	unittest.main()
