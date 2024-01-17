
def do_connect():
    import network
    count = 0
    sta_if = network.WLAN(network.STA_IF)
    if not sta_if.isconnected():
        sta_if.active(False)
        print('connecting to network...')
        sta_if.active(True)
        sta_if.connect('iPhone','cavalloBlu')
        while not sta_if.isconnected():
            count += 1
            print ("tentativo n:", count)
            pass
    print('network config:', sta_if.ifconfig())
    
do_connect()