from django.shortcuts import render
from django.http import JsonResponse
from datetime import datetime

def permit_response(request):
    # Construct the response data with the required wrapper
    response_data = {
        "hasError": False,
        "errorCode": -1,
        "message": "Success",
        "response": {
            "permitType": [
                {
                    "permitTypeId": 1,
                    "title": "Hot Work Permit",
                    "updatedTime": "2026-01-27 10:30:00",
                },
                {
                    "permitTypeId": 2,
                    "title": "Cold Work Permit",
                    "updatedTime": "2026-01-27 10:30:00",
                }
            ],
            "generalConditionsSection": [
                {
                    "id": 101,
                    "permitTypeId": 1,
                    "title": "Fire extinguisher available?",
                    "updatedTime": "2026-01-27 10:30:00"
                },
            ],
            "certificateValiditySection": [
                {
                    "id": 202,
                    "permitTypeId": 1,
                    "title": "Work End Time",
                    "updatedTime": "2026-01-27 10:30:00"
                }
            ],
            "deletedPermitIds": [],
            "deletedGeneralSectionsIds": [],
            "deletedCertificateValiditySection": []
        }
    }

    # Create the response object
    response = JsonResponse(response_data)
    
    # Fix for iOS Brotli issue:
    # Explicitly set Content-Encoding to 'identity' to tell proxies (like Render's edge) 
    # not to compress this specific response with Brotli or Gzip.
    response['Content-Encoding'] = 'identity'
    # 'no-transform' tells proxies/CDNs not to modify the response body (prevents auto-compression)
    response['Cache-Control'] = 'no-transform'
    
    return response
