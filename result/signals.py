import paho.mqtt.client as mqtt
from .models import ConfigParameter 
from django.dispatch import receiver
from django.db.models.signals import post_save


@receiver(post_save, sender=ConfigParameter)
def new_config(sender, instance, **kwargs):
    mqttBroker = "broker.emqx.io"
    client = mqtt.Client("Backend")
    client.connect(mqttBroker)
    client.publish(f"CONFIGURATION_{instance.mxid}", "update")
    print(instance.mxid)
    print("signal")