from django.shortcuts import render, redirect
from .models import Applicant_details, Person
from employer.models import Job
from .models import Applied_jobs
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from rest_framework.decorators import api_view
from rest_framework.response import Response
from applicant.serializers import PersonSerializer, loginSerializer, RegisterSerializer
from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework import status
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from django.core.paginator import Paginator


# from django.contrib.auth.models import User
# all below are commented due to apis testing
#-------------------------------creatin api's with help of rest framework-----------------------------------------

#   User.objects.all() -------->[1,2,3,4]---->Quesyset
#   we cannot parse this queryset to the frontend so we have to serialize and convert it into json
#   it with the help of serializer  ...it is a class which converts python objects into json objects


# here we are creating API using  APIview class
class PersonAPI(APIView):
    
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]


    def get(self, request):

        print(request.user)
        person = Person.objects.all()
        try:
        # this is for pagination
            page_size = 2
            page = request.GET.get('page', 1)
            paginator = Paginator(person, page_size)
            print(paginator.page(page))
            serialize = PersonSerializer(paginator.page(page), many = True)
            return Response(serialize.data)

        except Exception as e:
            return Response({
                "status":"false",
                "message":"invalid page number !"
            })

    
    def post(self, request):
        return Response({'message' : 'This is a post request'}) 
    
    def put(self, request):
        return Response({'message' : 'This is a put request'}) 
    
    def patch(self, request):
        return Response({'message' : 'This is a patch request'}) 
    
    def delete(self, request):
        return Response({'message' : 'This is a delete request'}) 
    

# this api has been build to get the login details and check validate them
@api_view(['POST'])
def api_login(request):
    data = request.data
    serializer = loginSerializer(data = data)

    if serializer.is_valid():
        data = serializer.data
        return Response({'successfully validated the data' : data})
    else:
        return Response(serializer.errors)


class LoginAPI(APIView):
    def post(self, request):
        data = request.data
        serializer = loginSerializer(data = data)
        if not serializer.is_valid():
            return Response({'status':'False', 'message':serializer.errors}, status.HTTP_400_BAD_REQUEST)
        user = authenticate(username = data['username'], password = data['password'])
        if not user:
            return Response({'status':'False', 'message':'invalid credentails'}, status.HTTP_400_BAD_REQUEST)

        token, _ = Token.objects.get_or_create(user = user)
        print(token)
        return Response({ "status":"True",'meassage':'User login succesfully', 'token':str(token)},status.HTTP_201_CREATED)  


class RegisterAPI(APIView):
    def post(self, request):
        data = request.data
        serializer = RegisterSerializer(data = data)
        if not serializer.is_valid():
            return Response({
                "status":"false",
                'meassage':serializer.errors},
                status.HTTP_400_BAD_REQUEST)    
        serializer.save()
        return Response({ "status":"True",'meassage':'User created succesfully'},status.HTTP_201_CREATED)  

#tis is a api by  using decorator 
# @api_view(['GET','POST', 'PUT'])
# def view_jobs(request):
#         ''''This is ude of Docstring'''

#         data = Job.objects.all().values()
#         params = {'data':data}

#         if request.method == 'POST':
#             received_data = request.data
#             print(received_data)
#             print("YOU HIT A POST REQUEST")
#             return Response(params)
        
#         elif request.method == 'GET':
#             print(request.GET.get('search'))
#             print("YOU HIT A GET REQUEST")
#             return Response(params)
        
#         elif request.method == 'PUT':
#              print("YOU HIT A POST REQUEST")
#              return Response(params)
             
# writing an view api to push and get data in Person model

@api_view(['POST', 'GET', 'PUT', 'PATCH', 'DELETE'])
def person(request):
    '''this fcn populates the person model with (name,age)'''
        # data = request.data
        # person = Person()
        # person.name = data['name']
        # person.age = data['age']
        # person.save()----> we can do this in such a way we have to use srialix[zer to check that the data is valid or not]
    if request.method == 'POST':
        data = request.data
        serialize = PersonSerializer( data = data)
        if serialize.is_valid():
            serialize.save()
            return Response(serialize.data)
        else:
            return Response(serialize.errors)  

# put doesnt support partial update while patch supports partial update means in put if we want to update the age then we have to pass 
# all the data but in patch we have to pass only that field
    #     {
    #     "id": 1,------------------>have to pass only the id and updated field
    #     "age": 18
    # }
    #     {
    #     "id": 1,------------------>in out we have to pas al the data
    #     "name": "anoop",
    #     "age": 18
    # }

    elif request.method == 'PUT':
        data = request.data
        obj = Person.objects.get(id = data['id'])
        serialize = PersonSerializer(obj, data = data)
        if serialize.is_valid():
            serialize.save()
            return Response(serialize.data)
        else:
            return Response(serialize.errors)  
              
    elif request.method == 'PATCH':
        data = request.data
        obj = Person.objects.get(id = data['id'])
        serialize = PersonSerializer(obj, data = data, partial = True)
        if serialize.is_valid():
            serialize.save()
            return Response(serialize.data)
        else:
            return Response(serialize.errors)        

    elif request.method == 'GET':
        person = Person.objects.all()
        serialize = PersonSerializer(person, many = True)
        return Response(serialize.data)

        # params = {'person': person}
        # return Response(params)-------->this will not parsed to frontend and throw an error that your 
        #data is not in json format. to resolve this we have to serialize the queryset but it is also working with .values()
    else:
        data = request.data
        obj = Person.objects.get(id = data['id'])
        obj.delete()
        return Response({'message': 'person deleted succesfully!'})


# this is a modelviewset class which is used to handle all the 5 crud methods just in one class precisely
class PersonViewSet(viewsets.ModelViewSet):
    serializer_class = PersonSerializer
    queryset = Person.objects.all()

    def list(self, request):
        search = request.GET.get('search')
        queryset = self.queryset
        if search:
            queryset = queryset.filter(name__startswith = search)

        serialize = PersonSerializer(queryset, many = True)

        return Response({"status" : 200, "data" : serialize.data}, status = status.HTTP_204_NO_CONTENT)




# actual  jobportal project code
    
@login_required(login_url="/login/")
def applicant_details(request):
        user = User.objects.filter(username = request.user).all().values()
        print(user[0].get('email'))
        current_user_email = user[0].get('email')
        user1 = Applicant_details.objects.filter(applicant_email = current_user_email)
        print(user1)

        if not user1.exists():
            if request.method == "POST":
                ad = Applicant_details()
                
                ad.applicant_name = request.POST.get('name' , '')
                ad.applicant_email = request.POST.get('email' , '')
                ad.applicant_age = request.POST.get('age' , 0)
                ad.applicant_address = request.POST.get('address' , '')
                ad.applicant_education = request.POST.get('education' , '')
                ad.applicant_gender = request.POST.get('gender' , '')
                ad.applicant_no = request.POST.get('no' , 0)
                ad.applicant_skills = request.POST.get('skills' , '')
                ad.disability_type = request.POST.get('type' , '')

                ad.save()

            return render(request , "applicant_details.html")
        else:
             return redirect("/applicant/view_jobs/")
    

@login_required(login_url="/login/")
def view_jobs(request):
        data = Job.objects.all().values()
        params = {'data':data}
        return render(request , "view_jobs.html",params)





from applicant.forms import PDFFileForm
@login_required(login_url="/login/")
def apply_now(request ,  myid):

    data = Job.objects.filter(id = myid).values()
    print(data[0]['company_name'])
   
    if request.method == 'POST':
        form = PDFFileForm( request.POST, request.FILES )

        if form.is_valid():
            
            form.save()
            obj =  Applied_jobs.objects.last()
            obj.Applied_id = myid
            obj.company_name = data[0]['company_name']
            obj.save()
            return redirect('view_jobs')

    else:
        form = PDFFileForm()
    params = {'data' : data ,  'form': form , 'Applied_id' : myid}
    return render(request, 'apply_now.html', params)






@login_required(login_url="/login/")
def job_details(request, myid):
    data = Job.objects.filter(id = myid).values()
    params = {'data' : data}

    return render(request , 'job_details.html' , params)





