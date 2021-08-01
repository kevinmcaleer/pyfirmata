# PyFirmata
# Or how to control Arduino's using Python

To clone this use:
`git clone https://www.github.com/kevinmcaleer/pyfirmata`

## To Install PyFirmata
First, create a new virutal environment, I do this on a Mac using:
`python3 -m venv venv`

Next, install the pyfirmata library using:
`pip install pyfirmata`

now you can import it into your code using
`from pyfirmata import Arduino`

and then you can setup a board:
`board = Arduino('com3')` - where com3 is the name of the serial device, on unix computers this will be something like `/dev/usb-serial01`