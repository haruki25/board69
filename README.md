# Random Sound Player with Key Logging
This is a Python script that plays a random sound from a list of sound files every time a key is pressed. The script uses the winsound and pynput modules to play sounds and detect key presses.

Usage
To run the script, simply execute the board69.py file with Python:
```
python board69.py
```

Once the script is running, every key press will trigger the playback of a random sound from the SOUNDS list. The script will also log every key press and sound played in a file named log.txt.

To stop the script, press the ESC key.

## Dependencies
The script depends on the following Python modules:

pynput
winsound
logging

You can install these modules using pip, the Python package manager:
```
pip install pynput
pip install logging
pip install winsound
```

### License
This script is licensed under the MIT License. See the LICENSE file for more information.
