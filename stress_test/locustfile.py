from locust import HttpUser, TaskSet, task, between
class UserBehavior(HttpUser):

    wait_time = between(1, 5)

    @task(1)
    def index(self):
        self.client.get("http://0.0.0.0/")

    @task(3)
    def predict(self):
        files = [
            ("file", ("dog.jpeg", open("dog.jpeg", "rb"), "image/jpeg"))
        ]
        headers = {}
        payload = {}
        self.client.post(
            "http://0.0.0.0/predict",
            headers = headers,
            data = payload,
            files = files,
        )
