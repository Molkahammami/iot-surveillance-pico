import serial, requests, json, time

WOKWI_URL = 'rfc2217://localhost:4003'
NODE_RED = 'http://127.0.0.1:1880/wokwi'

while True:
    try:
        print("Connexion...")
        ser = serial.serial_for_url(WOKWI_URL, baudrate=115200, timeout=2)
        print("Connected!")
        while True:
            line = ser.readline().decode('utf-8').strip()
            if not line or '{' not in line:
                continue
            try:
                line2 = line.replace("'",'"').replace('False','false').replace('True','true')
                data = json.loads(line2)
                print(data)
                requests.post(NODE_RED, json=data, timeout=0.1)
            except Exception as e:
                print(f"Parse err: {e}")
    except KeyboardInterrupt:
        break
    except Exception as e:
        print(f"Reconnexion: {e}")
        time.sleep(3)