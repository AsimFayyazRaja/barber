# barber

This is an implementation of GAN-based Image Compositing using Segmentation Masks (SIGGRAPH Asia 2021) for quick execution and updated requirements with code.
It also provides a flask server which can be directly hit and can be used as an API. 

## Example outputs
Given below are some of the generated outputs from the model. It generates a hair mask and then generates a new hairstyle with various olour schemes in a very appealing manner.

<img width="400" alt="image" src="https://user-images.githubusercontent.com/28213136/227770850-c94dfe7a-6688-4285-90f8-83c32b940f4d.png">

<img width="400" alt="image" src="https://user-images.githubusercontent.com/28213136/227770882-cfb6bb49-f753-428c-85c4-e9e7818dee72.png">


## Execution
- Install the requirements by pip3 install reqs.txt
- Execute the flask server like python app.py
- You can hit the POST request to get the output like this:

<img width="500" alt="image" src="https://user-images.githubusercontent.com/28213136/227771009-9a4a4196-2f08-46fa-a103-85383871da85.png">
