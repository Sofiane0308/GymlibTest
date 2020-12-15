from django.test import TestCase

from rest_framework.test import APITestCase
from rest_framework import status



class JobsTest(APITestCase):

    def test_jobs(self):
        
        jobsURL = '/jobs'
        jobURL = '/job'

        data = [1, 2, 6, 4, 5, 1, 3]
        for input in data:
            self.client.post(jobsURL, {  'input' : input }, format='json')

        response = self.client.get(jobsURL)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, [3, 5, 4, 6, 2, 1])

        response = self.client.get(jobURL)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, 1)

        response = self.client.get(jobURL)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, 2)

        response = self.client.get(jobsURL)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, [3, 5, 4, 6])

        response = self.client.delete(jobsURL)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(response.data, None)

        response = self.client.get(jobsURL)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, [])

        response = self.client.get(jobURL)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(response.data, None)
