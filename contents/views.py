from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from .models import Content,Rating
from .serializers import ContentSerializer
from django.db.models import Avg  
from django.db.models import Q
from django.shortcuts import get_object_or_404



class GetAllContents(APIView):
    permission_classes=(IsAuthenticatedOrReadOnly,)
    def get(self,request):
        contents = Content.objects.all()
        contents_serializer = ContentSerializer(contents,many = True)
        return Response(data=contents_serializer.data,status=200)


class RateContent(APIView):
    permission_classes=(IsAuthenticatedOrReadOnly,)
    def get(self,request,content_id):
        content = get_object_or_404(Content, pk=content_id)
        content_serializer = ContentSerializer(instance=content)
        return Response(content_serializer.data,status=200)
    
    def post(self,request,content_id):
        content = get_object_or_404(Content, pk=content_id)
        rate = request.data['rate']

        if rate < 0 or rate > 5 :
            return Response({'msg':'not valid please enter between 0 and 5'},status=400)

        if Rating.objects.filter(Q(user = request.user)&Q(content__id = content_id)).exists():
            user_rate = Rating.objects.get(Q(user = request.user)&Q(content__id = content_id))
            user_rate.rate = rate
            user_rate.save()

            avg_rate = Rating.objects.filter(content__id = content_id).aggregate(Avg("rate"))
            content.rate = avg_rate['rate__avg']
            content.save()

        else:
            rate_obj = Rating()
            rate_obj.rate = rate
            rate_obj.save()
            rate_obj.user.add(request.user)
            rate_obj.content.add(content)
            rate_obj.save()

            avg_rate = Rating.objects.filter(content__id = content_id).aggregate(Avg("rate"))
            content.rate = avg_rate['rate__avg']
            content.save()


        return Response({'msg':'ok'},status=200)

        