from rest_framework.decorators import action
from rest_framework import response, status, viewsets
from django.shortcuts import get_object_or_404
from .serializers import ClientSerializer, MailingSerializer, MessageSerializer
from models_app.models import Mailing, Client, Message


class MailingViewSet(viewsets.ModelViewSet):

    serializer_class = MailingSerializer
    queryset = Mailing.objects.all()

    @action(methods=['get'], detail=False,
            url_path='all')
    def all_mailing(self, *args, **kwargs):
        messages = Message.objects.order_by('id_mailing', 'status').select_related()
        messages_serializer = MessageSerializer(messages, many=True)
        return response.Response(messages_serializer.data)

    @action(methods=['get'], detail=False,
            url_path='(?P<id_mailing>.+)')
    def mailing(self, *args, **kwargs):
        message = Message.objects.filter(id_mailing=kwargs["id_mailing"]).order_by('status').select_related()
        messages_serializer = MessageSerializer(message, many=True)
        return response.Response(messages_serializer.data)

    @action(methods=['post'], detail=False,
            url_path='add')
    def add_mailing(self, request, *args, **kwargs):
        data = request.data
        serializer = MailingSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return response.Response(serializer.data, status=status.HTTP_201_CREATED)
        return response.Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @action(methods=['delete'], detail=False,
            url_path='remove/(?P<id_mailing>\d+)')
    def delete_mailing(self, request, *args, **kwargs):
            mailing = get_object_or_404(Mailing, id=kwargs['id_mailing'])
            mailing.delete()
            return response.Response("Confirm", status=status.HTTP_204_NO_CONTENT)

    @action(methods=['patch'], detail=False,
            url_path='update_mailing/(?P<id_mailing>\d+)')
    def update_mailing(self, request, *args, **kwargs):
        old_mailing = get_object_or_404(Client, id=kwargs['id_mailing'])
        data_update = request.data
        serializer = MailingSerializer(instance=old_mailing, data=data_update, partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return response.Response(serializer.data, status=status.HTTP_201_CREATED)
        return response.Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ClientViewSet(viewsets.ModelViewSet):

    serializer_class = ClientSerializer
    queryset = Client.objects.all()

    @action(methods=['post'], detail=False,
            url_path='add')
    def add_client(self, request, *args, **kwargs):
        data = request.data
        serializer = ClientSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return response.Response(serializer.data, status=status.HTTP_201_CREATED)
        return response.Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @action(methods=['delete'], detail=False,
            url_path='remove/(?P<id_client>\d+)')
    def delete_client(self, request, *args, **kwargs):
        client = get_object_or_404(Client, id=kwargs['id_client'])
        client.delete()
        return response.Response("Confirm", status=status.HTTP_204_NO_CONTENT)

    @action(methods=['patch'], detail=False,
            url_path='update_client/(?P<id_client>\d+)')
    def update_client(self, request, *args, **kwargs):
        old_client = get_object_or_404(Client, id=kwargs['id_client'])
        data_update = request.data
        serializer = ClientSerializer(instance=old_client, data=data_update, partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return response.Response(serializer.data, status=status.HTTP_201_CREATED)
        return response.Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
