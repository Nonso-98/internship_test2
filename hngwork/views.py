from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status 
from django .db. models import Q

from .models import Profile
from .serializer import ProfileSerializer, ProfileListSerializer  
from .services import externalAPIservice

class ProfileCreateView(APIView):  # Capital 'P' matches your urls.py

    def post(self, request):
        name = request.data.get("name")

        if not name:
            return Response(
                {"status": "error", "message": "Name is required"},
                status=status.HTTP_400_BAD_REQUEST
            )

        if not isinstance(name, str):
            return Response(
                {"status": "error", "message": "Invalid type"},
                status=status.HTTP_422_UNPROCESSABLE_ENTITY
            )

        name = name.lower()

        # Idempotency check
        existing = Profile.objects.filter(name=name).first()
        if existing:
            return Response({
                "status": "success",
                "message": "Profile already exists",
                "data": ProfileSerializer(existing).data
            }, status=status.HTTP_200_OK)

        try:
            gender_data = ExternalAPIService.get_gender(name)
            age_data = ExternalAPIService.get_age(name)
            country_data = ExternalAPIService.get_country(name)

        except Exception as e:
            return Response({"status": "error", "message": str(e)},
                status=status.HTTP_502_BAD_GATEWAY
            )

        profile = Profile.objects.create(
            name=name,
            **gender_data,
            **age_data,
            **country_data
        )

        return Response({ "status": "success", "data": ProfileSerializer(profile).data}, status=status.HTTP_201_CREATED)


class ProfileDetailView(APIView):

    def get(self, request, id):
        try:
            profile = Profile.objects.get(id=id)
        except Profile.DoesNotExist:
            return Response(
                {"status": "error", "message": "Profile not found"},
                status=status.HTTP_404_NOT_FOUND
            )

        return Response({
            "status": "success",
            "data": ProfileSerializer(profile).data
        })


class ProfileListView(APIView):

    def get(self, request):
        gender = request.GET.get("gender")
        country_id = request.GET.get("country_id")
        age_group = request.GET.get("age_group")

        queryset = Profile.objects.all()

        if gender:
            queryset = queryset.filter(gender__iexact=gender)

        if country_id:
            queryset = queryset.filter(country_id__iexact=country_id)

        if age_group:
            queryset = queryset.filter(age_group__iexact=age_group)

        serializer = ProfileListSerializer(queryset, many=True)

        return Response({
            "status": "success",
            "count": queryset.count(),
            "data": serializer.data
        })


class ProfileDeleteView(APIView):

    def delete(self, request, id):
        try:
            profile = Profile.objects.get(id=id)
        except Profile.DoesNotExist:
            return Response( {"status": "error", "message": "Profile not found"}, status=status.HTTP_404_NOT_FOUND
            )

        profile.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
