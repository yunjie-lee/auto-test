# -*-coding:utf-8 -*-
import pytest
import requests
import json
from .const import *


class Test_httpbin:
    def test_get_ip(self):
        url = BASE_URL + IP_URL
        print(url)
        r = requests.get(url)
        print(r.headers)
        response_data = json.loads(r.text)
        print(response_data)
        assert 200 == r.status_code
        assert LOCAL_IP == response_data["origin"]

    def test_post_method(self):
        url = BASE_URL + POST_TEST_URL
        post_data = {"name": "yourname", "pwd": "123456"}
        r = requests.post(url, data=post_data)
        print(r.text)
        response_data = r.json()
        assert 200 == r.status_code
        assert post_data["name"] == response_data["form"]["name"]
        assert post_data["pwd"] == response_data["form"]["pwd"]

    def test_delete_method(self):
        url = BASE_URL + DELETE_TEST_URL
        delete_data = {"name": "lily", "pwd": "123456"}
        r = requests.delete(url, data=delete_data)
        print(r.text)
        response_data = r.json()
        assert 200 == r.status_code
        assert delete_data["name"] == response_data["form"]["name"]
        assert delete_data["pwd"] == response_data["form"]["pwd"]

    def test_put_method(self):
        url = BASE_URL + PUT_TEST_URL
        put_data = {"word": "beauty"}
        r = requests.put(url, data=put_data)
        print(r.headers)
        print(r.text)
        response_data = r.json()
        assert 200 == r.status_code
        assert put_data["word"] == response_data["form"]["word"]

    def test_patch_method(self):
        url = BASE_URL + PATCH_TEST_URL
        patch_data = {"id": "007"}
        r = requests.patch(url, patch_data)
        response_data = json.loads(r.text)
        print(response_data)
        assert 200 == r.status_code
