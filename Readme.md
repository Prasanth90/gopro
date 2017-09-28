# Go Pro Hero 4 Session

## What does this repo does ?
- Stream the live feed of GopRo HERO4 Session to the browser (Chrome only).
- Capture screen shot during the live feed

## Browser
  - It will work only in Chrome Browser that too in Desktop only (Not in mobile)
  - Add the video plugin to chrome https://www.videoexpertsgroup.com/vxg-chrome-plugin/

## Camera:
  - Install the latest firmware
  - Set the Camera in the APP mode
  - Connect the computer to the Wifi network of the camera
  - Insert an SD card in the camera (Needed to store captured images)

## Server:
  - Install python 3.6
  - Install Mongodb > Version 3.4.5 (used to store the URLs of captures images)
  - Set pip in the Environment variable
 
```sh
  cd server
  pip install -r requirements.txt
  python gopro.py
```

## Client:

```sh
  $ cd bootstrapclient
  $ mongoose-free-6.9.exe
```

### See the live feed at [here](http://localhost:8080)