import io
from google.cloud import vision

def detect_faces(img):
    """Detects faces in an image."""
    vision_client = vision.Client()

    content = img.read()

    image = vision_client.image(content=content)

    faces = image.detect_faces()

    return faces


def detect_faces_uri(uri):
    """Detects faces in the file located in Google Cloud Storage or the web."""
    vision_client = vision.Client()
    image = vision_client.image(source_uri=uri)

    faces = image.detect_faces()

    return faces