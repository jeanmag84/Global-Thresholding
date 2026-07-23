# Global-Thresholding
Global Thresholding using Opencv in Python
In this example, we will use an image of a galaxy; by default, OpenCV opens images in BGR rather than RGB.

<img width="640" height="480" alt="Figure_bgr" src="https://github.com/user-attachments/assets/e9060ddf-0dc2-4ea9-9b31-87e3c8cc6271" />

And then, after converting the image, we will have it in standard RGB format.
<img width="640" height="480" alt="Figure_rgb" src="https://github.com/user-attachments/assets/d4f0176c-db98-4282-8dc8-b3ce34931160" />

However, we are using global thresholding; for this, we need to convert the image to grayscale, since global thresholding only works with values ​​up to 255.

<img width="640" height="480" alt="Figure_gray" src="https://github.com/user-attachments/assets/abb7fbe7-be80-4213-852b-910584a2d9f1" />

Now that we have the grayscale image, we can apply global thresholding and examine the results.

<img width="640" height="480" alt="Figure_1" src="https://github.com/user-attachments/assets/33d8fbab-136d-4bd7-88b0-181c688f1f99" /><img width="640" height="480" alt="Figure_2" src="https://github.com/user-attachments/assets/322d1a3f-8032-4a0d-9480-3386d3715322" /> 

