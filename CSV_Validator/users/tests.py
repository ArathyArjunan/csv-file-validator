from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from django.core.files.uploadedfile import SimpleUploadedFile

class FileUploadViewsetTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.url = "/api/file-upload/"  

    def create_file(self, content, filename="test.csv", content_type="text/csv"):
        """
         method to create a test file.
        """
        return SimpleUploadedFile(
            filename, content.encode("utf-8"), content_type=content_type
        )

    def test_valid_csv_upload(self):
        """
        Test uploading a valid CSV file.
        """
        file_content = (
            "first_name,last_name,email,age,phone\n"
            "tiny,tiny,tinytiny@example.com,30,1234567890\n"
            "james,john,jamesjohn@example.com,25,9876543210\n"
        )
        file = self.create_file(file_content)
        response = self.client.post(self.url, {"file": file}, format="multipart")
                
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["data"]["valid_records"], 2)
        self.assertEqual(response.data["data"]["rejected_records"], 0)
        print(response.data)


    def test_invalid_csv_upload(self):
        """
        Test uploading an invalid CSV file with missing fields(first name missing).
        """
        file_content = (
            "first_name,last_name,email,age,phone\n"
            ",arjunan,arathyarjunan@example.com,21,9072715750\n"
        ) 
        file = self.create_file(file_content)
        response = self.client.post(self.url, {"file": file}, format="multipart")
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["data"]["valid_records"], 0)
        self.assertEqual(response.data["data"]["rejected_records"], 1)
        print(response.data)


    def test_duplicate_csv_upload(self):
        """
        Test uploading a CSV file with same email addresses.
        """
        file_content = (
            "first_name,last_name,email,age,phone\n"
            "aaa,bb,aaabb@example.com,30,7898654328\n"
            "cc,dd,aaabb@example.com,15,1234567890\n"
        )
        file = self.create_file(file_content)
        response = self.client.post(self.url, {"file": file}, format="multipart")
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["data"]["valid_records"], 1)
        self.assertEqual(response.data["data"]["rejected_records"], 1)
        print(response.data)


    def test_non_csv_file_upload(self):
        """
        Test uploading a non-CSV file ( .pdf file).
        """
        file_content = "This is a plain text file."
        file = self.create_file(file_content, filename="test.pdf", content_type="text/plain")
        response = self.client.post(self.url, {"file": file}, format="multipart")
        self.assertIn("Only .csv files are accepted.", response.data["message"])
        print(response.data) 

