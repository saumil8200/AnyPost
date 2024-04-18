from rest_framework import serializers
from posts.models import Post, Category, Comment
from users.models import Profile

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class CommentSerializer(serializers.ModelSerializer):
    replies = serializers.SerializerMethodField()
    def get_replies(self, obj):
        replies = obj.replies.all()
        serializer = CommentSerializer(replies ,many=True)
        return serializer.data

    class Meta:
        model = Comment
        fields = ['id', 'content', 'created', 'user', 'post', 'parent', 'replies']

class PostSerializer(serializers.ModelSerializer):
    owner = ProfileSerializer(many=False)
    category = CategorySerializer(many=False)
    comment = serializers.SerializerMethodField()
    liked_by = ProfileSerializer(many=True)
    def get_comment(self, obj):
        comments = obj.comments.all()
        serializer = CommentSerializer(comments ,many=True)
        return serializer.data

    class Meta:
        model = Post
        fields = '__all__'