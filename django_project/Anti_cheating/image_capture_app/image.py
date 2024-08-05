import os
import cv2

class ImageCapture:
    def __init__(self):
        self.cap = None
        self.is_camera_open = False
        self.is_capture_started = False
        self.image = None
        self.save_folder = 'captured_images'

        # Create save folder if it doesn't exist
        if not os.path.exists(self.save_folder):
            os.makedirs(self.save_folder)

    def start_camera(self):
        if not self.is_camera_open:
            self.cap = cv2.VideoCapture(0)
            self.is_camera_open = True
            print("Camera opened. Press SPACE to capture an image, or ESC to exit.")

        while self.is_camera_open:
            ret, frame = self.cap.read()
            cv2.imshow('Camera Feed', frame)

            key = cv2.waitKey(1)
            if key == 27:  # ESC key to exit
                self.stop_camera()
            elif key == 32:  # SPACE key to capture image
                self.image = frame.copy()
                self.is_capture_started = True
                print("Image captured. Press SPACE to capture another image, or ESC to exit.")
                self.save_image()

    def stop_camera(self):
        if self.is_camera_open:
            self.cap.release()
            cv2.destroyAllWindows()
            self.is_camera_open = False
            self.is_capture_started = False
            print("Camera closed.")

    def save_image(self):
        if self.is_capture_started:
            image_path = os.path.join(self.save_folder, 'captured_image.png')
            cv2.imwrite(image_path, self.image)
            print(f"Image saved: {image_path}")
        else:
            print("No image captured yet.")

    def get_image(self):
        if self.is_capture_started:
            return self.image
        else:
            print("No image captured yet.")
            return None

if __name__ == "__main__":
    capture = ImageCapture()
    capture.start_camera()

    # Example usage to get captured image:
    # captured_image = capture.get_image()



