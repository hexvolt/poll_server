import json

from django.conf import settings


def on_model_save(sender, rabbit_client, **kwargs):
    instance = kwargs.get('instance')
    is_created = kwargs.get('created')

    message = {
        'model': sender.__name__,
        'action': 'created' if is_created else 'updated',
        'instance': instance.serialized_data,
    }

    rabbit_client.send_message(
        exchange_name=settings.RABBITMQ_APP_EXCHANGE,
        message=json.dumps(message)
    )


def on_model_delete(sender, rabbit_client, **kwargs):
    instance = kwargs.get('instance')

    message = {
        'model': sender.__name__,
        'action': 'deleted',
        'instance': instance.serialized_data,
    }

    rabbit_client.send_message(
        exchange_name=settings.RABBITMQ_APP_EXCHANGE,
        message=json.dumps(message)
    )
