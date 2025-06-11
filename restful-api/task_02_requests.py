#!/usr/bin/python3
"""
Task 02: Requests

This script demonstrates how to make HTTP
requests using the `requests` library.
"""
import requests
import _json


def fetch_and_print_posts():
    """
    a method that peints the posts
    """
    f = requests.get('https://jsonplaceholder.typicode.com/posts')
    print("the status code of the response is {}".format(f.status_code))
    if f.status_code == 200:
        API_data = f.json()
        for key in API_data:
            print(key['title'])


def fetch_and_save_posts():
    """
    writes in csvfile content
    of the posts
    """
    f = requests.get('ttps://jsonplaceholder.typicode.com/posts')
    if f.status_code == 200:
        API_data = f.json()
        posts = [{"id": key["id"], "title": key["title"], "body": key["body"]}
                 for key in API_data]
        with open("posts.csv", "w", encoding="utf-8") as file:
            writer = csv.DictWriter(file, fieldnames=["id", "title", "body"])
            writer.writeheader()
            writer.writerows(posts)
