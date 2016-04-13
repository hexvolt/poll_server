from django.conf import settings


def on_model_save(sender, rabbit_client, **kwargs):
    instance = kwargs.get('instance')
    is_created = kwargs.get('created')

    message = "{} model {}".format(
        str(sender), 'created' if is_created else 'modified')

    rabbit_client.send_message(
        exchange_name=settings.RABBITMQ_APP_EXCHANGE, message=message
    )


def on_model_delete(sender, rabbit_client, **kwargs):
    print(sender)
    instance = kwargs.get('instance')

    message = "{} model deleted".format(str(sender))

    rabbit_client.send_message(
        exchange_name=settings.RABBITMQ_APP_EXCHANGE, message=message
    )
