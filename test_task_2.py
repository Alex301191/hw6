import unittest
from unittest import TestCase
from main_task_2 import get_headers, create_new_folder, delete_new_folder
import requests


class YaTestCase(TestCase):
    def test_with_right_data(self):
        yandex_token = "y0_AgAAAABpDcb9AADLWwAAAADds8KTDK5fHsL1TtG4I8Hv9WgGdtfY7u8"
        folder_name = 'Folder name'
        expected_result = 201
        delete_new_folder(folder_name, yandex_token)
        res = create_new_folder(folder_name, yandex_token)
        self.assertEqual(res, expected_result)

    @unittest.expectedFailure
    def test_with_wrong_exp_res(self):
        yandex_token = "y0_AgAAAABpDcb9AADLWwAAAADds8KTDK5fHsL1TtG4I8Hv9WgGdtfY7u8"
        folder_name = 'Folder name'
        expected_result = 409
        delete_new_folder(folder_name, yandex_token)
        res = create_new_folder(folder_name, yandex_token)
        self.assertEqual(res, expected_result)

    @unittest.expectedFailure
    def test_with_wrong_token(self):
        yandex_token = ""
        folder_name = 'Folder name'
        expected_result = 201
        delete_new_folder(folder_name, yandex_token)
        res = create_new_folder(folder_name, yandex_token)
        self.assertEqual(res, expected_result)

    @unittest.expectedFailure
    def test_without_delete(self):
        yandex_token = "y0_AgAAAABpDcb9AADLWwAAAADds8KTDK5fHsL1TtG4I8Hv9WgGdtfY7u8"
        folder_name = 'Folder name'
        expected_result = 201
        # delete_new_folder(folder_name, yandex_token)
        res = create_new_folder(folder_name, yandex_token)
        self.assertEqual(res, expected_result)
