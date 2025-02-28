from drf_yasg.utils import swagger_auto_schema
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.core.cache import cache
from ..serializers import RegisterSerializer


class RegisterAPIView(APIView):
    @swagger_auto_schema(request_body=RegisterSerializer)
    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            phone = serializer.validated_data['phone']
            cached_data = cache.get(phone)

            if not cached_data:
                return Response(
                    {"success": False, "detail": "Telefon raqamingiz tasdiqlangan raqamga mos emas!"},
                    status=status.HTTP_400_BAD_REQUEST
                )

            phone_number = cached_data.get("phone_number")
            if str(phone_number) == str(phone):
                serializer.save()
                return Response(
                    {"success": True, "detail": "Siz muvafaqqiyatli ro'yxatdan o'tdingiz!"},
                    status=status.HTTP_201_CREATED
                )

            # Agar telefon raqam mos kelmasa, qo'shimcha javob qaytarish
            return Response(
                {"success": False, "detail": "Telefon raqamingiz mos kelmadi!"},
                status=status.HTTP_400_BAD_REQUEST
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
