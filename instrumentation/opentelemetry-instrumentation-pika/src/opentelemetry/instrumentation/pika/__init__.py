# Copyright The OpenTelemetry Authors
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""
Instrument `pika` to trace RabbitMQ applications.

Usage
-----

* Start broker backend

.. code-block:: python

    docker run -p 5672:5672 rabbitmq


* Run instrumented task

.. code:: python
    import pika
    from opentelemetry.instrumentation.pika import PikaInstrumentation

    connection = pika.BlockingConnection(pika.URLParameters('amqp://localhost'))
    channel = connection.channel()
    channel.queue_declare(queue='hello')

    pika_instrumentation = PikaInstrumentation()
    pika_instrumentation.instrument(channel=channel)


    channel.basic_publish(exchange='', routing_key='hello', body=b'Hello World!')

    pika_instrumentation.uninstrument(channel=channel)


PikaInstrumentation also supports instrumentation without creating an object, and receiving a tracer_provider

.. code:: Python
    PikaInstrumentation.instrument_channel(channel, tracer_provider=tracer_provider)

API
---
"""


from .version import __version__
from .pika_instrumentor import PikaInstrumentation
