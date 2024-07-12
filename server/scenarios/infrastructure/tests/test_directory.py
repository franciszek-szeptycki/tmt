from rest_framework.test import APITestCase, APIClient

from scenarios.infrastructure.models.directory import Directory


class TestGenericMethods(APITestCase):
    URL = "/scenarios/directories/items/"

    def setUp(self):
        self.client = APIClient()

    def test_create_directory(self):
        response = self.client.post(self.URL, {"name": "test"})
        self.assertEqual(response.status_code, 201)
        self.assertEqual(Directory.objects.count(), 1)

    def test_delete_directory(self):
        directory = Directory.objects.create(name="test")
        response = self.client.delete(f"{self.URL}{directory.id}/")
        self.assertEqual(response.status_code, 204)
        self.assertEqual(Directory.objects.count(), 0)

    def tearDown(self):
        Directory.objects.all().delete()


class TestStructuredDirectories(APITestCase):
    URL = "/scenarios/directories/items/"

    def setUp(self):
        self.client = APIClient()

        self.root_dir = Directory.objects.create(name="root")
        self.sub_dir = Directory.objects.create(name="sub", parent=self.root_dir)
        self.sub_sub_dir_1 = Directory.objects.create(name="sub_sub", parent=self.sub_dir)
        self.sub_sub_dir_2 = Directory.objects.create(name="sub_sub", parent=self.sub_dir)

    def test_get_directory_tree(self):
        response = self.client.get(self.URL)
        root_item = response.data[0]
        self.assertEqual(root_item.get("children")[0].get("id"), str(self.sub_dir.id))
        sub_root_item = root_item.get("children")[0]
        self.assertEqual(sub_root_item.get("children")[0].get("id"), str(self.sub_sub_dir_1.id))
        self.assertEqual(sub_root_item.get("children")[1].get("id"), str(self.sub_sub_dir_2.id))
