# serializers.py
from rest_framework import serializers
from posts.models import Group, Post, Comment
from django.contrib.auth.models import User


class GroupSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Group
        fields = ('id', 'title', 'slug', 'description')


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'first_name', 'last_name')


class PostSerializer(serializers.ModelSerializer):
    author = UserSerializer(read_only=True)          # Вложенный автор (только чтение)
    # group = GroupSerializer(read_only=True)          # Вложенная группа (только чтение)
    # Поля для записи (по id)
    # author_id = serializers.PrimaryKeyRelatedField(
    #     queryset=User.objects.all(), source='author', read_only=True
    # )
    # group_id = serializers.PrimaryKeyRelatedField(
    #     queryset=Group.objects.all(), source='group', write_only=True, required=False, allow_null=True
    # )
    group = serializers.PrimaryKeyRelatedField(
        queryset=Group.objects.all(), required=False, allow_null=True
    )
 
    class Meta:
        model = Post
        fields = ('id', 'text', 'pub_date', 'author', 'author_id',
                  'image', 'group')
        read_only_fields = ('author', 'author_id')


class CommentSerializer(serializers.ModelSerializer):
    author = UserSerializer(read_only=True)
    post = serializers.PrimaryKeyRelatedField(read_only=True)
    # post_id = serializers.PrimaryKeyRelatedField(
    #     queryset=Post.objects.all(), source='post', write_only=True, required=False
    # )

    class Meta:
        model = Comment
        fields = ('id', 'author', 'post', 'text', 'created')