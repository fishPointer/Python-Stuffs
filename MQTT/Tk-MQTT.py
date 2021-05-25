from tkinter import *
import paho.mqtt.client as mqtt

global payload
payload = ''

def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    client.subscribe("/corn/#")
    client.subscribe("/phone/#")

def on_message(client, userdata, msg):
    global payload
    payload = (msg.topic+" "+str(msg.payload))
    #print(payload)
    lbl2.config(text = payload)

def megaoff():
    client.publish("/corn/color/relay", "1")

def megaon():
    client.publish("/corn/color/relay", "0")

def phoneping():
    client.publish("/phone/ping", "1")
    
def submitcolors():
    r = horizontal.get()
    g = horizontal2.get()
    b = horizontal3.get()
    client.publish("/corn/color/r", r)
    client.publish("/corn/color/g", g)
    client.publish("/corn/color/b", b)

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.connect("192.168.0.193", 1883, 60)

root = Tk()
root.title("Breadnet Wire")
root.geometry("400x400")

btn = Button(root, text="Connect to MQTT", command=client.loop_start).pack()
btn2 = Button(root, text="MegaLights OFF", command=megaoff).pack()
btn3 = Button(root, text="MegaLights ON", command=megaon).pack()
btn4 = Button(root, text="Exit Program", command=root.quit).pack()
btn5 = Button(root, text="Ping Phone", command=phoneping).pack()

lbl2 = Label(root, font=('calibri', 16, 'bold'))
lbl2.pack(anchor='center')


lbl_r = Label(root, text="Red").pack()
horizontal = Scale(root, from_=0, to=255, orient=HORIZONTAL)
horizontal.pack()

lbl_g = Label(root, text="Green").pack()
horizontal2 = Scale(root, from_=0, to=255, orient=HORIZONTAL)
horizontal2.pack()

lbl_b = Label(root, text="Blue").pack()
horizontal3 = Scale(root, from_=0, to=255, orient=HORIZONTAL)
horizontal3.pack()

btn_rgb = Button(root, text="Submit Colors", command=submitcolors).pack()



root.mainloop()