import logging

from contextlib import contextmanager

from pika import ConnectionParameters, BlockingConnection, PlainCredentials


logger = logging.getLogger()


class RabbitMQClient(object):

    def __init__(self, username, password, host, port):

        credentials = PlainCredentials(username=username, password=password)

        self.connection_parameters = ConnectionParameters(
            host=host, port=port, credentials=credentials
        )

    @contextmanager
    def open_channel(self, exchange_name, exchange_type):

        connection = BlockingConnection(parameters=self.connection_parameters)

        channel = connection.channel()

        try:
            channel.exchange_declare(exchange=exchange_name,
                                     exchange_type=exchange_type)
            yield channel

        except Exception as e:
            logger.error(e)

        finally:
            connection.close()

    def send_message(self, message):

        logger.debug("Sending message to the RabbitMQ channel.")

        with self.open_channel('poll', 'fanout') as channel:
            channel.basic_publish(
                exchange='poll', routing_key='', body=message
            )
