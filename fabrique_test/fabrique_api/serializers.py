from rest_framework import serializers
from models_app.models import Mailing, Client, Message


class MailingSerializer(serializers.ModelSerializer):
    """
    Создание рассылки.
    Поля: date_time_start, text_message, client_filter, date_time_finish
    """
    def create(self, validated_data):
        return Mailing.objects.create(**validated_data)
    """
    Редактирование рассылки
    """
    def update(self, instance, validated_data):
        instance.date_time_start = validated_data.get('date_time_start', instance.date_time_start)
        instance.text_message = validated_data.get('text_message', instance.text_message)
        instance.client_filter = validated_data.get('client_filter', instance.client_filter)
        instance.date_time_finish = validated_data.get('date_time_finish', instance.date_time_finish)
        instance.save()

        return instance

    class Meta:
        model = Mailing
        fields = '__all__'


class ClientSerializer(serializers.ModelSerializer):
    """
    Создание пользователя.
    Поля: phoneNumber, phoneCode, tag, timeZone
    """
    def create(self, validated_data):
        return Client.objects.create(**validated_data)
    """
    Редактирование пользователя
    """
    def update(self, instance, validated_data):
        instance.phoneNumber = validated_data.get('phoneNumber', instance.phoneNumber)
        instance.phoneCode = validated_data.get('phoneCode', instance.phoneCode)
        instance.tag = validated_data.get('tag', instance.tag)
        instance.timeZone = validated_data.get('timeZone', instance.timeZone)
        instance.save()

        return instance

    class Meta:
        model = Client
        fields = '__all__'


class MessageSerializer(serializers.ModelSerializer):
    """
    Создание сообщения.
    Поля: date_time_start, status, id_mailing, id_client
    """
    def create(self, validated_data):
        return Message.objects.create(**validated_data)

    id_mailing = MailingSerializer()
    id_client = ClientSerializer()

    class Meta:
        model = Message
        fields = '__all__'
