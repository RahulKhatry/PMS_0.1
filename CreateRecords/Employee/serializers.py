from rest_framework import serializers
from models import EmployeeRecords


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmployeeRecords
        field = {'EName', 'emailID', 'HiringDate'}

