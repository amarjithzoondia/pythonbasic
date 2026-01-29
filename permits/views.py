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
                    "permitTypeId": 3,
                    "title": "Height Work Certificate",
                    "updatedTime": "2026-01-24 16:20:56",
                    "image": ""
                },
                {
                    "permitTypeId": 2,
                    "title": "Height Work Certificate",
                    "updatedTime": "2026-01-24 16:21:00",
                    "image": "https://rotgdevbkt.s3.ap-south-1.amazonaws.com/permits/images111_36e29.png"
                },
                {
                    "permitTypeId": 1,
                    "title": "Hot Work Certificates",
                    "updatedTime": "2026-01-24 16:21:03",
                    "image": "https://rotgdevbkt.s3.ap-south-1.amazonaws.com/permits/250*250_f0b76.jpeg"
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
