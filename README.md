# Minimal DJI Cloud API example

Minimal working example using DJI Cloud API.

## Setup

1. Install dependencies: `pip install -r ./requirements.txt`
2. Install docker and setup `emqx` (MQTT server)
    - `docker run -d --name emqx -p 1883:1883 -p 8083:8083 -p 8084:8084 -p 8883:8883 -p 18083:18083  emqx:5.0.20`
    - open http://localhost:18083/ to setup admin account l: `admin` p: `public`
    - create user account (I am not sure whether it is needed, you can use admin account)
3. Connect your DJI Smart Controller to the same local network your PC is in (in case of laptop I recommend creating local hotspot).
4. Set env variable `HOST_ADDR`, `USERNAME`, `PASSWORD` to your IP which will be visible for controller and run `./cloud_api.http.py`
5. Set env variable `HOST_ADDR` and run `./cloud_api_mqtt.py`


### Conecting the controller

1. Open DJI Pilot App
2. Go to `Cloud Service` -> `Other platforms`
3. Write url `http://HOST_ADDR:5000/login` and connect
4. Press Login.

Now app `cloud_api_mqtt.py` should show you some telemetry from drone

expected example:

```
📨Got msg: thing/product/1ZNBK7LC00AB/osd
🌍Status: Lat: 0 Lon: 0 height: 16.160583 att_head 10.4 att_pitch -0.4 att_roll 0.2
{'61-0-0': {'gimbal_pitch': 0,
            'gimbal_roll': 0,
            'gimbal_yaw': 117.8,
            'measure_target_altitude': 0,   
            'measure_target_distance': 4.2,
            'measure_target_error_state': 3,
            'measure_target_latitude': 0,
            'measure_target_longitude': 0,
            'payload_index': '61-0-0',
            'version': 1},
 'elevation': 0,
 'firmware_version': '03.31.0000',
 'gear': 1,
 'home_distance': 0,
 'horizontal_speed': 0,
 'longitude': 0,
 'mode_code': 0,
 'position_state': {'gps_number': 0,
                    'is_fixed': 0,
                    'quality': 0,
                    'rtk_number': 0},
 'storage': {'total': 24434700, 'used': 7723000},
 'total_flight_distance': 0,
 'total_flight_time': 0,
 'track_id': '',
 'vertical_speed': 0,
 'wind_direction': 0,
 'wind_speed': 0}
```