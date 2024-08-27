from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
from filesharer import FileSharer
import time

Builder.load_file('frontend.kv')

# This class can be used for the Webcam class


class CameraScreen(Screen):
    def start(self):
        """Starts the camera and changes the Camera Button text"""
        self.ids.camera.play = True
        self.ids.camera_button.text = "Stop Camera"
        self.ids.camera.texture = self.ids.camera._camera.texture

    def stop(self):
        """Stops the camera and changes the Camera Button text"""
        self.ids.camera.play = False
        self.ids.camera_button.text = "Start Camera"
        self.ids.camera.texture = None

    def capture(self):
        """Creates a filename with the current time and captures and saves a photo image in the filepath"""
        current_time = time.strftime('%Y%m%d-%H%M%S')
        self.filepath = f"images/{current_time}.png"
        self.ids.camera.export_to_png(self.filepath)

        self.manager.current = 'image_screen'
        self.manager.current_screen.ids.img.source = self.filepath


class ImageScreen(Screen):
    """Take the current saved phot and upload it to the web and share the link under the `Share the link` button"""

    def create_link(self):
        file_path = App.get_running_app().root.ids.camera_screen.filepath
        fileshare = FileSharer(filepath=file_path)
        url = fileshare.share()
        self.ids.link.text = url
        print(file_path)


class RootWidget(ScreenManager):
    pass


class MainApp(App):

    def build(self):
        return RootWidget()


MainApp().run()
