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
    

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.connect("192.168.0.193", 1883, 60)

root = Tk()
root.title("Breadnet Wire")
root.geometry("400x200")

btn = Button(root, text="Connect to MQTT", command=client.loop_start).pack()
btn2 = Button(root, text="MegaLights OFF", command=megaoff).pack()
btn3 = Button(root, text="MegaLights ON", command=megaon).pack()
btn4 = Button(root, text="Exit Program", command=root.quit).pack()
btn5 = Button(root, text="Ping Phone", command=phoneping).pack()

lbl2 = Label(root, font=('calibri', 16, 'bold'))
lbl2.pack(anchor='center')

root.mainloop()