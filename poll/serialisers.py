from rest_framework import serializers
from .models import Poll, PollQuestion, PollCategory, PollQuestionOption


class PollCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = PollCategory
        fields = '__all__'


class PollSerializer(serializers.ModelSerializer):
    class Meta:
        model = Poll
        fields = '__all__'
        extra_kwargs = {
            'created_by': {'read_only': True},
        }

    def create(self, validated_data):
        return super().create(validated_data)

    def to_representation(self, instance):
        data = super().to_representation(instance)
        return data


class QuestionOptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = PollQuestionOption
        fields = '__all__'
        extra_kwargs = {
            'question': {'read_only': True}
        }


class QuestionSerializer(serializers.ModelSerializer):
    options = QuestionOptionSerializer(many=True, write_only=True)

    class Meta:
        model = PollQuestion
        fields = '__all__'
        extra_kwargs = {
            'position': {'read_only': True},
            'poll': {'read_only': True},
        }

    def to_representation(self, instance):
        option = instance.question_option.all()
        data = super().to_representation(instance)
        data['options'] = QuestionOptionSerializer(
            option, many=True).data if option else None
        data['poll_instruction'] = instance.poll.poll_instruction
        return data


class PollListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Poll
        fields = '__all__'

    def to_representation(self, instance):
        user = self.context.get('request').user
        data = super().to_representation(instance)
        return data


class QuestionCreateSerializer(serializers.Serializer):
    poll_instruction = serializers.CharField(required=True)
    questions = serializers.ListSerializer(
        child=QuestionSerializer(), required=True)

    def validate(self, attrs):
        #     questions = attrs['questions']
        #     poll = self.context['poll']
        #     poll_type = poll.type
        #     question_type = []
        #     special_polls = ['CANDIDATE_POPULARITY', 'PARTY_POPULARITY',
        #                      'NEEDS_ASSESSMENT']  # analytical polls

        #     qs = Question.objects.filter(poll=poll)
        #     poll_questions = qs.exclude(poll=poll) if self.instance else qs
        #     if poll_questions.exists():
        #         raise serializers.ValidationError(
        #             {'questions': 'questions already set up for this poll'})
        #     if poll_type in special_polls:
        #         for question in questions:
        #             if question['type'] in special_polls:
        #                 question_type.append(question['type'])
        #         if poll.type not in question_type:
        #             raise serializers.ValidationError(
        #                 {'type': f'must contain a {poll_type} type'})
        #         elif len(question_type) > 1:
        #             raise serializers.ValidationError(
        #                 {'type': f'invalid questions'})  # todo improve error message
        return attrs

    def to_representation(self, instance):
        return QuestionSerializer(instance).data

    def create(self, validated_data):

        poll = self.context['poll']
        questions = validated_data['questions']
        poll_instruction = validated_data['poll_instruction']
        for question in questions:
            options = question.pop('options')
            if question['type'] == poll.type:
                question['required'] = True
            question_obj = PollQuestion.objects.create(
                **question, poll=poll)
            for option in options:
                PollQuestionOption.objects.create(
                    **option, question=question_obj)

        poll.poll_instruction = poll_instruction
        print("===========", poll)
        poll.save()
        return True

    # def update(self, instance, validated_data):
    #     """
    #     delete the question and recreate
    #     """
    #     poll = self.context['poll']
    #     poll_instruction = validated_data['poll_instruction']
    #     questions = Question.objects.filter(poll=poll)
    #     questions.delete() if questions else None
    #     questions = validated_data['questions']
    #     for question in questions:
    #         options = question.pop('options')
    #         if question['type'] == poll.type:
    #             question['required'] = True
    #         question_obj = Question.objects.create(**question, poll=poll)
    #         for option in options:
    #             QuestionOption.objects.create(**option, question=question_obj)
    #     poll.poll_instruction = poll_instruction
    #     poll.save()
    #     return True
