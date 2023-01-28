from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import status, viewsets, filters, generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action
from rest_framework.response import Response
from .serialisers import PollCategorySerializer, PollSerializer, PollListSerializer, QuestionCreateSerializer, QuestionSerializer
from .models import Poll, PollQuestion, PollCategory
from .filters import PollFilter
from account.permissions import IsAdmin


class PollCategoryCreateListAPIView(generics.ListCreateAPIView):
    queryset = PollCategory.objects.all()
    serializer_class = PollCategorySerializer


class PollViewSets(viewsets.ModelViewSet):
    queryset = Poll.objects.all()
    serializer_class = PollSerializer
    http_method_names = ["get", "post", "delete", "put", "patch"]
    filter_backends = [
        DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter,
    ]
    filterset_fields = ["type"]
    filterset_class = PollFilter
    search_fields = ["type", "name"]
    ordering_fields = ["created_at"]
    permission_classes = [IsAuthenticated]

    def get_permissions(self):
        permission_classes = self.permission_classes
        if self.action not in ['create']:
            return [IsAdmin()]
        else:
            return [permission() for permission in permission_classes]

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

    def paginate_results(self, queryset):
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def get_serializer_class(self):
        if self.action == 'list':
            return PollListSerializer
        return super().get_serializer_class()

    @action(methods=['GET', 'POST', 'PUT'],
            detail=True, serializer_class=QuestionCreateSerializer,
            url_path='question')
    def list_create_update_questions(self, request, pk=None):
        poll = self.get_object()
        if request.method == 'GET':
            qs = PollQuestion.objects.filter(poll=poll)
            print('qs', qs)
            serializer = QuestionSerializer(qs, many=True)
            print({"serializer": serializer})
            return Response(
                {'success': True, 'data': serializer.data},
                status=status.HTTP_200_OK)

        elif request.method == 'POST':
            serializer = QuestionCreateSerializer(
                data=request.data, context={'poll': poll})
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(
                {'success': True, 'message': 'question created successfully'},
                status=status.HTTP_201_CREATED)

        elif request.method == 'PUT':
            serializer = QuestionCreateSerializer(
                data=request.data, instance=poll, context={'poll': poll})
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(
                {'success': True, 'message': 'question updated successfully'},
                status=status.HTTP_201_CREATED)
