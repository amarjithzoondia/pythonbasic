from django.shortcuts import render
from django.http import JsonResponse
from datetime import datetime

def permit_response(request):
    response_data = {
        "permitType": [
            {
                "permitTypeId": 1,
                "permitTypeTitle": "Hot Work Permit"
            },
            {
                "permitTypeId": 2,
                "permitTypeTitle": "Cold Work Permit"
            }
        ],
        "generalConditionsSection": [
            {
                "id": 101,
                "permitTypeId": 1,
                "title": "Fire extinguisher available?"
            },
            {
                "id": 102,
                "permitTypeId": 2,
                "title": "Is PPE mandatory?"
            }
        ],
        "certificateValiditySection": [
            {
                "id": 201,
                "permitTypeId": 1,
                "title": "Start Time"
            },
            {
                "id": 202,
                "permitTypeId": 1,
                "title": "Work End Time"
            }
        ],
        "deletedPermitIds": [],
        "deletedGeneralSectionsIds": [],
        "deletedCertificateValiditySection": []
    }

    return JsonResponse(response_data, json_dumps_params={'indent': 2})

