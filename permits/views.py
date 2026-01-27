from django.shortcuts import render
from django.http import JsonResponse

def permit_response(request):
    response_data = {
        "hasError": False,   # ← FIXED
        "errorCode": -1,
        "message": "Success",
        "response": {
            "deletedPermitIds": [],
            "deletedGeneralSectionsIds": [],
            "deletedCertificateValiditySection": [],

            "permitType": [
                {
                    "id": 1,
                    "title": "Hot Work Permit",
                    "updatedTime": "2026-01-27 10:30:00",
                    "version": 1.0
                },
                {
                    "id": 2,
                    "title": "Cold Work Permit",
                    "updatedTime": "2026-01-27 10:30:00",
                    "version": 1.0
                }
            ],

            "generalConditionsSection": [
                {
                    "id": 101,
                    "permitTypeId": 1,
                    "title": "Fire extinguisher available?",
                    "updatedTime": "2026-01-27 10:30:00"
                },
                {
                    "id": 102,
                    "permitTypeId": 2,
                    "title": "Is PPE mandatory?",
                    "updatedTime": "2026-01-27 10:30:00"
                }
            ],

            "certificateValiditySection": [
                {
                    "id": 201,
                    "permitTypeId": 1,
                    "title": "Start Time",
                    "updatedTime": "2026-01-27 10:30:00"
                },
                {
                    "id": 202,
                    "permitTypeId": 1,
                    "title": "Work End Time",
                    "updatedTime": "2026-01-27 10:30:00"
                }
            ]
        }
    }

    return JsonResponse(response_data, json_dumps_params={'indent': 2})
