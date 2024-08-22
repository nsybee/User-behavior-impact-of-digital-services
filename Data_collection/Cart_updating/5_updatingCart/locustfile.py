import time
import random

from locust import HttpUser, task, between, event

class eShopUser(HttpUser):
    wait_time = between(1, 5)

    def on_start(self):
        self.client.verify = False

    @task
    def browse_pages(self):
        self.client.get("/")
        self.client.get("/cart")