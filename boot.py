from machine import Pin, PWM

def do_connect():
    import network
    sta_if = network.WLAN(network.STA_IF)
    if not sta_if.isconnected():
        print('connecting to network...')
        sta_if.active(True)
        sta_if.connect('Kanga Banga', 'puddingpie')
        while not sta_if.isconnected():
            pass
    print('network config:', sta_if.ifconfig())

# flash led while network is initializing
led = Pin(13, Pin.OUT)
ledPWM = PWM(led)
ledPWM.freq(1)
ledPWM.duty(512)

# initialize network
do_connect()

# turn led 'on' at a low brightness
ledPWM.freq(10000)
ledPWM.duty(255)