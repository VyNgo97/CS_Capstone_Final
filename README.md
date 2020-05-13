# Mood Recognition Music Player

## A note about the data:

If you are planning to clone this repository and run the program yourself through the python scripts,
you'll have to download the facial emotion recognition data. You can download the data from this link:
https://www.kaggle.com/c/challenges-in-representation-learning-facial-expression-recognition-challenge/data
extract and name the data into the data folder and rename it ferData.

## How to install & use system:

> Make sure you have Docker installed on your device
> Use Docker pull to pull files
> Docker run files



## Device Registry API Usage

Respones will be in the form

```json
{
    "data": "Response data",
    "message": "Description of what happened"
}
```

Responses for expected value of our 'data field'

### List all devices

**Definitions**

`GET /devices`

**Response**

- `200 OK` on success

```json
[
{
    "identifier": "LED-arduino",
    "name": "LED Lights",
    "device_type": "lights",
    "controller_gateway": "192.168.0.4"
}
]
```

### Registering New Device

`POST /devices`

**Arguments required to register device**

-`"identifier":string` a globally unique identifier for device
-`"name":string` client side name for device
-`"device_type":string` type of device as understood by client
-`"controller_gateway":string` IP address of device's controller

**Response**

-`201 Created` on success

```json
{
    "identifier": "LED-arduino",
    "name": "LED Lights",
    "device_type": "lights",
    "controller_gateway": "192.168.0.4"
}
```

## Get device information

`GET /devices/<deviceId>

**Response**

-`404 Not Foound` if no device with target ID in registry
- `202 OK` on success

```json
{
    "identifier": "LED-arduino",
    "name": "LED Lights",
    "device_type": "lights",
    "controller_gateway": "192.168.0.4"
}
```

- `404 Not Found` if device doesn't exist
- `204 No Content` on success

#References:

The sources used to complete our project include:
https://towardsdatascience.com/real-time-face-recognition-an-end-to-end-project-b738bb0f7348
https://opencv.org/
https://github.com/omar178/Emotion-recognition/blob/master/models/_mini_XCEPTION.102-0.66.hdf5
