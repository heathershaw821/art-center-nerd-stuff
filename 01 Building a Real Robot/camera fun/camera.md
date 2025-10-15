![Robo Vision](/images/robovision.png)


First we will begin by installing the necessary camera interface packages and rebooting

```bash
sudo apt update
sudo apt full-upgrade
sudo apt install git meson libcamera-dev libcamera-apps libjpeg-dev
sudo reboot
```

Once rebooted test to make sure the camera is working:

```bash
rpicam-still -o ~/test.jpg
```

Now let's install some packages for python to use our camera:

```bash
sudo apt install python3-picamera2 python3-opencv python3-flask
```

## Now we can play with the code in camera.py!!!!