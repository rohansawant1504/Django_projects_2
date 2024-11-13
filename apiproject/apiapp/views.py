from .models import employee_data
from.serializers import EmpSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class emp(APIView):
    def get(self,r):
        edata = employee_data.objects.all()
        serdata = EmpSerializer(edata, many=True)
        return Response(serdata.data,status=status.HTTP_200_OK)

    def post(self,r):
        serobj = EmpSerializer(data=r.data)
        if serobj.is_valid():
            serobj.save()
            return Response(serobj.data, status=status.HTTP_201_CREATED)
        return Response(serobj.data, status=status.HTTP_400_BAD_REQUEST)

    def put(self,r,id):
        edata = employee_data.objects.get(emp_id=id)
        serdata = EmpSerializer(edata,data=r.data)
        if serdata.is_valid():
            serdata.save()
            return Response(serdata.data, status=status.HTTP_201_CREATED)
        return Response(serdata.data, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, r, id):
        edata = employee_data.objects.get(emp_id=id)
        edata.delete()
        return Response(status=status.HTTP_200_OK)