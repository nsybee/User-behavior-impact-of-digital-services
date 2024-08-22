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
        self.client.get("/?page=5")
        self.client.get("/?page=11")
        self.client.get("/?page=7")
        self.client.get("/?page=9")
        self.client.get("/?page=2")
        
        


    