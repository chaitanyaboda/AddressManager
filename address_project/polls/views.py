from django.db.models import Count
from django.http import HttpResponse
from polls.models import Company
from polls.serializers import CompanySerializer, PinCodeSerializer
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response


def index(request):
    return HttpResponse("Hello, world. You're at the index.")


@api_view(['GET', 'POST'])
def company_list(request):
    """
    List all addresses, or create a new address for a company.
    """
    if request.method == 'GET':
        city = request.GET.get('city', None)  # To list all the companies in a certain city

        if city is None:
            companies = Company.objects.all()
            serializer = CompanySerializer(companies, many=True)
            return Response(serializer.data)
        else:
            try:
                companies = Company.objects.filter(city=city)
                serializer = CompanySerializer(companies, many=True)
                return Response(serializer.data)
            except Company.DoesNotExist:
                return Response(status=status.HTTP_404_NOT_FOUND)

    elif request.method == 'POST':
        serializer = CompanySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def pincode_list(request, min_count):
    """
    List all postal codes which have more than min_count of companies
    """
    if min_count is not None:
        companies = Company.objects.values('postal_code').annotate(  # resolves to group by
            total=Count('company_name')).filter(total__gt=min_count)
        serializer = PinCodeSerializer(companies, many=True)
        return Response(serializer.data)


@api_view(['GET', 'PUT', 'DELETE'])
def company_detail(request, name):
    """
    Retrieve, update or delete a company details based on its name.
    """
    try:
        company = Company.objects.get(company_name=name)
    except Company.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = CompanySerializer(company)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = CompanySerializer(company, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        company.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
