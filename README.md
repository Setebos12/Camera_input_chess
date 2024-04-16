# Camera_input_chess

# Introduction

"ChessCam" is  application that allows users to play chess using a camera. The program enables real-time interaction with a virtual chessboard by capturing moves through the camera and transmitting them to a Lichess  for online gameplay.
# Features

Interface for capturing chess moves using trained classes: program utilizes a trained model to identify chess moves.

Online gameplay: It transmits recognized moves to a Lichess account.


# Requirements


Computer with a webcam.
Lichess account with Personal API access tokens (Settings -> API access tokens -> External play -> Play games with board API)


Software:

Python environment.
Required libraries.
Installed models for chess piece recognition.


Implementation

ChessCam is implemented in Python, leveraging popular libraries such as OpenCV, TensorFlow, and PyTorch for image processing and machine learning tasks. The program seamlessly integrates with a Lichess account to provide a smooth multiplayer experience.
Example Usage

    Launch the ChessCam program on your computer.
    Position the camera to capture the chessboard or any surface where the game is played.
    Make a move on the chessboard.
    The program will capture and recognize the move, transmitting it to your Lichess account for online gameplay.
    Engage in multiplayer chess gameplay with other users on Lichess.
    Place the physical chessboard in front of the camera.
    Make a chess move by moving a piece on the chessboard.
    The program will automatically register your move and display it on the screen.
    Continue the game by making subsequent moves.
