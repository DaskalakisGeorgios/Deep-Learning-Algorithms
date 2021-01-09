import jetson.inference
import jetson_utils_python

# Loading the detection model
net = jetson.inference.detectNet("ssd-mobilenet-v2", threshold=0.5) 
#ssd-mobilenet------ pretrained model.
#Opening the camera stream
camera = jetson.utils.gstCamera(1280,720, '/dev/video0')   

#Create a video output interface with the videoOutput object and create a main loop that will run until the user exits.
display=jetson.utils.glDisplay()
while display.IsOpen():
# main loop will go here

    img, width, height = camera.CaptureRGBA() #This goes with gstreamer
    detections=net.Detect(img, width, height)
    display.RenderOnce(img, width, height) #καθιστώ
    display.SetTitle("Object Detection | Network {:.0f} FPS".format(net.GetNetworkFPS()))
#Finally we'll visualize the results with OpenGL and update the title of the window to display the current peformance.
#The Render() function will automatically flip the backbuffer and present the image on-screen.
