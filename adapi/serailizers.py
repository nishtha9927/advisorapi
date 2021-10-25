from rest_framework import serializers
from rest_framework.fields import SerializerMethodField
from .models import advisordetail, usermodel, bookingdetail



class adminserializer(serializers.ModelSerializer):
    class Meta:
        model = advisordetail
        fields = ('name', 'imageurl')
        lookup_field = 'name'


class userserializer(serializers.ModelSerializer):
    class Meta:
        model = usermodel
        fields = ("name", "email", "password")


class userloginserializer(serializers.ModelSerializer):
    class Meta:
        model = usermodel
        fields = ("email", "password")


class bookingdetailserializer(serializers.ModelSerializer):
    advisor_name = serializers.SerializerMethodField(read_only=True)
    advisor_img_url = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = bookingdetail
        fields = '__all__'

    def get_advisor_name(self, obj):
        return obj.advisor_id.name

    def get_advisor_img_url(self, obj):
        return obj.advisor_id.imageurl
