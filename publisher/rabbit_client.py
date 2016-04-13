import logging

from contextlib import contextmanager

from pika import ConnectionParameters, BlockingConnection, PlainCredentials


logger = logging.getLogger()


class RabbitMQClient(object):
    """
    A client for sending messages to RabbitMQ server.
    """

    def __init__(self, username, password, host, port):

        credentials = PlainCredentials(username=username, password=password)

        self.connection_parameters = ConnectionParameters(
            host=host, port=port, credentials=credentials
        )

    @contextmanager
    def open_channel(self, exchange_name, exchange_type):
        logger.debug("Connecting to the RabbitMQ server.")

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
            logger.debug("Connection closed.")

    def send_message(self, exchange_name, message):
        """
        Sends a message to a certain RabbitMQ's exchange. A 'fanout' type
        of exchange is being used here, so this message will be received
        by all consumers connected to the RabbitMQ with the same parameters.

        :param exchange_name: a name of the exchange being used
        :param message: a message that needs to be transferred
        """

        logger.debug("Sending message '%s' to the RabbitMQ channel through "
                     "the exchange '%s'.", message, exchange_name)

        with self.open_channel(exchange_name, 'fanout') as channel:
            channel.basic_publish(
                exchange=exchange_name, routing_key='', body=message
            )
