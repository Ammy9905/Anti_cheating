from django.shortcuts import render
from django.http import JsonResponse
from .image import ImageCapture

# Initialize ImageCapture instance
capture = ImageCapture()

def start_camera(request):
    if request.method == 'GET':
        capture.start_camera()
        return JsonResponse({'message': 'Camera started.'})
    else:
        return JsonResponse({'error': 'Method not allowed'}, status=405)

def stop_camera(request):
    if request.method == 'GET':
        capture.stop_camera()
        return JsonResponse({'message': 'Camera stopped.'})
    else:
        return JsonResponse({'error': 'Method not allowed'}, status=405)

def capture_image(request):
    if request.method == 'GET':
        capture.save_image()
        return JsonResponse({'message': 'Image captured and saved.'})
    else:
        return JsonResponse({'error': 'Method not allowed'}, status=405)






