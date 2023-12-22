from locust import HttpUser, task, between


class QuickstartUser(HttpUser):

    def on_start(self):
        response = self.client.post(
            url="/accounts/api/v2/jwt/create/",
            data={
                "email": "test.test@gmail.com",
                "password": "a123456d"
            }).json()

        self.client.headers = {"Authorization": "Bearer {}".format(response.get("access", None))}

    @task
    def app_blog_api_v1_post_list(self):
        self.client.get("/blog/api/v1/posts/")

    @task
    def app_todo_api_v1_job_list(self):
        self.client.get("/todo/api/v1/jobs/")
