
# Unreal Engine Virtual Framework for Human-Robot Interaction

This is a framework for building virtual worlds for Human Robot Interaction using Unreal Engine (UE) and for testing the associated algorithms using Python which communicates with Unreal Engine in real-time. It provides templates for the robots NAO and Pepper and a sample human mesh. The robots camera can be accessed and its behavior can be controlled during runtime using Python. Commonly used functionality such as Movement, Speech, Posture (NAO Robot), Emotions (Human Only) etc is provided. A sample python script is provided.  

## How to Use it
The framework uses Unreal 4.26. The framework depends on several open source plugins to work properly or provide specific functionality. You are required to download and place the following plugins in the project directory.

UnrealCV:
https://github.com/unrealcv/unrealcv

Mindmaker AI:
https://github.com/krumiaa/MindMaker

Text to Speech:
https://github.com/yar3333/text-to-speech-ue4

Once configured, you can start by simply placing the robots and humans in an Unreal Engine level. Press the play button in the editor and run the sample python script simultaneously as well. You should be able to get the robot view inside Python cv2 and test computer vision algorithms as usual.
