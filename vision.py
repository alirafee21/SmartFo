from xml.dom.minidom import Text
from google.cloud import vision
import io

class TextRecognizer():
    def __init__(self) -> None:
        self.image = None

    def set_image(self, image: str) -> None:
        """ Sets the image to be used for recognition
        Args:
            string (image): _description_
        """
        
        self.image = image

    def remove_image(self, image: str) -> None:
        """
        removes the image 
        Args:
            string (image): _description_
        """
        self.image = None 

    def detect_text(self):
        """Detects text in the file."""
        client = vision.ImageAnnotatorClient()
        try: 
            with io.open(self.image, 'rb') as image_file:
                content = image_file.read()

            image = vision.Image(content=content)

            response = client.text_detection(image=image)
            texts = response.text_annotations
            print('Texts:')

            for text in texts:
                print('\n"{}"'.format(text.description))

                vertices = (['({},{})'.format(vertex.x, vertex.y)
                            for vertex in text.bounding_poly.vertices])

                print('bounds: {}'.format(','.join(vertices)))

            if response.error.message:
                raise Exception(
                    '{}\nFor more info on error messages, check: '
                    'https://cloud.google.com/apis/design/errors'.format(
                        response.error.message))
        except FileNotFoundError:
            print("Could not find file: {}".format(response.error.message))
if __name__ == '__main__':
    image1 = TextRecognizer()

    image1.set_image('C:\\Users\\rafee\\Pictures\\hudson.jpg')
    image1.detect_text()
