from django.shortcuts import render
from django.http import JsonResponse
from datetime import datetime

def permit_response(request):
    # Construct the response data to match exactly what iOS expects
    response_data = {
        "errorCode": -1,
        "hasError": False,
        "message": "Success",
        "response": {
            "certificateValiditySection": [
                {
                    "id": 202,
                    "permitTypeId": 1,
                    "title": "Work End Time",
                    "updatedTime": "2026-01-27 10:30:00"
                }
            ],
            "deletedCertificateValiditySection": [],
            "deletedGeneralSectionsIds": [],
            "deletedPermitIds": [],
            "generalConditionsSection": [
                {
                    "id": 101,
                    "permitTypeId": 1,
                    "title": "Fire extinguisher available?",
                    "updatedTime": "2026-01-27 10:30:00"
                }
            ],
            "permitType": [
                {
                    "permitTypeId": 1,
                    "title": "Hot Work Permit",
                    "updatedTime": "2026-01-27 10:30:00",
                    "version": "1.2"
                },
                {
                    "permitTypeId": 2,
                    "title": "Cold Work Permit",
                    "updatedTime": "2026-01-27 10:30:00",
                    "version": "1"
                }
            ]
        }
    }

    # Create the response object
    response = JsonResponse(response_data)
    
    # Fix for iOS Brotli/Compression issues
    response['Content-Encoding'] = 'identity'
    response['Cache-Control'] = 'no-transform'
    
    return response
