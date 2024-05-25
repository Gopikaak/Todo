from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from api.serializers import Registration,User,Todoserializer
from rest_framework.viewsets import ViewSet,ModelViewSet
from work.models import Taskmodel
from rest_framework import status
from rest_framework import authentication,permissions




class Userregister(APIView):
    def post(self,request,*args,**kwargs):

        serializer=Registration(data=request.data)
        if serializer.is_valid():

            serializer.save()
            #creat 
        return Response(serializer.data)
    
class Todoviewsetview(ViewSet):

    authentication_classes=[authentication.TokenAuthentication]                        #basic authemtication aanengill oropravishyavum usernameum passwordum choykkum.
    permission_classes=[permissions.IsAuthenticated]                                   #tokenauthentication aanengill athonnum kodukkan

    def list(self,request,*args,**kwargs):
        qs=Taskmodel.objects.all()
        serializer=Todoserializer(qs,many=True)

        return Response(serializer.data,status=status.HTTP_200_OK)

    def create(self,request,*args,**kwargs):
        serializer=Todoserializer(data=request.data)

        if serializer.is_valid():
            serializer.save(user=request.user)

        return Response(serializer.data)
    
    def destroy(self,request,*args,**kwargs):
        id=kwargs.get('pk')
        qs=Taskmodel.objects.get(id=id)
        if qs.user==request.user:
            qs.delete()
            return Response({"message":"Todo object deleted"})
        
        else:
            # raise serializers.ValidationError("not allowed")
            return Response({"message":"not allowed"})
    
    def retrieve(self,request,*args,**kwargs):
        id=kwargs.get('pk')
        try:
           qs=Taskmodel.objects.get(id=id)
           serializer=Todoserializer(qs)

           return Response(serializer.data,status=status.HTTP_202_ACCEPTED)
        
        except:
            return Response({"message":"id doesnt exist"},status=status.HTTP_404_NOT_FOUND)
        

    
    def update(self,request,*args,**kwargs):
        id=kwargs.get('pk')
        qs=Taskmodel.objects.get(id=id)
        serializer=Todoserializer(data=request.data,instance=qs)

        if serializer.is_valid():
            serializer.save(user=request.user)

            return Response(serializer.data,status=status.HTTP_200_OK)
        
        else:
            return Response(serializer.errors,status=status.HTTP_304_NOT_MODIFIED)



class Todomodelviewset(ModelViewSet):
    queryset=Taskmodel.objects.all()
    serializer_class=Todoserializer
    authentication_classes=[authentication.TokenAuthentication]
    permission_classes=[permissions.IsAuthenticated]

    def perform_create(self, serializer):
        return serializer.save(user=self.request.user)
 
# router.register('todomodel',Todomodelviewset,basename='api')