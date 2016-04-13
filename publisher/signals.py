
def on_model_save(sender, rabbit_client, **kwargs):
    print("===on_model_save===")
    instance = kwargs.get('instance')
    is_created = kwargs.get('created')

    rabbit_client.send_message("{} model {}".format(
        str(sender), 'created' if is_created else 'modified')
    )


def on_model_delete(sender, rabbit_client, **kwargs):
    print("===on_model_delete===")
    print(sender)
    instance = kwargs.get('instance')

    rabbit_client.send_message("{} model deleted".format(str(sender)))
