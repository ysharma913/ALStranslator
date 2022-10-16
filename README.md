## ASL translator

# Inspiration
We wanted to do something with Machine Learning that benefits the community! We decided on ASL detection and provide a means to learn it for anyone interested.

#What it does
Our project allows users to take pictures of their ASL signs with their webcam, which then goes to our AI that detects what sign it was and if it was accurate. This essentially works as a functioning quiz where the user would be asked sign a certain letter of the alphabet, take a picture from the webcam, cross-check with our AI, and assess how well the user did.

#How we built it
We decided to build the AI with a neural network trained on a dataset of ASL hand signs. Since the dataset consisted of small images of hand signs, when testing the AI afterwards with our own images, we needed downscale the image to size that the AI was used to seeing to make it work. Once on the web end side, we decided to use Vanilla JS and use the webcam-easy.js module for picture capturing. We used php server-side to be able to save the webcam picture to the local server. On top of this, we used flask as python back-end to call the Neural Network classifier and obtain the result of the picture.

#Challenges we ran into
We ran into a few challenges when developing the web-end portion. We kept running into ajax request errors with GET/POST requests. Additionally, when implementing flask alongside the php server, we had a few issues connecting the backend to our project.

#Accomplishments that we're proud of
We're definitely proud of the Neural Network we were able to train that can detect a handsign for an ASL alphabet character with a pretty good accuracy.

#What we learned
We learned a lot on the web-end side of things, especially with setting up servers and how to deal with cross origin requests.

#What's next for ASL Translator
The next steps for ASL Translator is to expand the learning/quizzing portion to be able to test words and sentences. This would be done by allowing the neural network to now take in short videos and detect what is being said. This would prove a little more challenging depending on the speed of different people's handsigns; however, we think being able to take it to this level would greatly increase the impact of this project.
