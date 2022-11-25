from wrappers import (
    EnvironmentWrapper,
    PymongoWrapper,
)
from celery import Celery


class Dependencies:
    def env_wrapper(self):
        return EnvironmentWrapper()

    def pymongo_wrapper(self):
        return PymongoWrapper(self.env_wrapper())

    def mongo(self):
        return self.pymongo_wrapper().get_client()

    def celery(self):
        env = self.env_wrapper()
        queue_host = env.get_var("RABBITMQ_HOST")
        queue_user = env.get_var("RABBITMQ_USERNAME")
        queue_pass = env.get_var("RABBITMQ_PASSWORD")

        queue_uri = f"amqp://{queue_user}:{queue_pass}@{queue_host}:5672"
        return Celery(
            "onlingo_background",
            broker=queue_uri,
            backend="rpc://",
            include=["background_jobs"],
        )
