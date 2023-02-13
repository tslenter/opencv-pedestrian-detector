## 1. opencv-pedestrian-detector
Early concept for a pedestrian detection using a Webcam Livestream.

## 2. How to run
Within the script you can find 2 functions. Uncomment the one which you like to try, and run the script: capture_functions.py

## 3. Example run function
#Use function(capture device) / usually 0 or 1
live_detection(1)

#Use function(image_file)
image_detection("example.jpg")

## 4. Example output
![alt text](https://github.com/tslenter/opencv-pedestrian-detector/blob/main/example_detection.jpg?raw=true)

## 5. How to use
It probably does not work out of the box. Please change the the values within:
explain (regions, _) = hog.detectMultiScale(image, winStride=(5,5,), padding=(20,20),scale=1.20)

Explanation:
The winStride argument specifies the step size in the x and y directions, respectively, for scanning the image. The padding argument is used to add padding around the image in order to detect partially visible objects. The scale argument is used to rescale the image prior to object detection. The function returns a list of rectangles (represented by the x, y, width, and height of the rectangles) that enclose the detected objects in the image. The rectangles are stored in the output argument regions.

## 6. License

"opencv-pedestrian-detector" is a free application that can be used to make livestream or image cartoon like.

Copyright (C) 2021 Tom Slenter

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program. If not, see <http://www.gnu.org/licenses/>.

For more information contact the author:

Name author: Tom Slenter

E-mail: info@remotesyslog.com
