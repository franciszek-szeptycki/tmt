from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from scenarios.infrastructure.models.project_model import Project


class ProjectCreateTestCase(APITestCase):

    def setUp(self):
        self.url = reverse('projects_items-list')

    def test_create_project(self):
        data = {
            'name': 'Test Project',
        }

        response = self.client.post(self.url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Project.objects.count(), 1)
        self.assertEqual(Project.objects.get().name, 'Test Project')

    def update_project(self):
        project = Project.objects.create(name='Test Project')
        data = {
            'name': 'Updated Project',
        }

        response = self.client.put(f'{self.url}/{project.id}', data, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Project.objects.get().name, 'Updated Project')

    def test_delete_project(self):
        project = Project.objects.create(name='Test Project')

        response = self.client.delete(f'{self.url}/{project.id}')

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Project.objects.count(), 0)

    def test_get_project(self):
        project = Project.objects.create(name='Test Project')

        response = self.client.get(f'{self.url}/{project.id}')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], 'Test Project')

    def test_get_project_list(self):
        Project.objects.create(name='Test Project 1')
        Project.objects.create(name='Test Project 2')

        response = self.client.get(self.url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    def tearDown(self):
        Project.objects.all().delete()
