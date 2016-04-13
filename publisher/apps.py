from functools import partial

from django.apps import AppConfig
from django.conf import settings
from django.db.models.signals import post_save, post_delete

from publisher.signals import on_model_save, on_model_delete
from publisher.rabbit_client import RabbitMQClient


class PublisherConfig(AppConfig):
    name = 'publisher'

    def ready(self):
        # initializing a RabbitMQ client
        rabbit_client = RabbitMQClient(
            username=settings.RABBITMQ_USERNAME,
            password=settings.RABBITMQ_PASSWORD,
            host=settings.RABBITMQ_HOST,
            port=settings.RABBITMQ_PORT,
        )

        # connecting signals
        model_save_handler = partial(
            on_model_save, rabbit_client=rabbit_client
        )
        model_delete_handler = partial(
            on_model_delete, rabbit_client=rabbit_client
        )

        post_save.connect(receiver=model_save_handler, weak=False)
        post_delete.connect(receiver=model_delete_handler, weak=False)
