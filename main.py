import serial
import time


COM_PORT = 'COM3'  
BAUD_RATE = 9600    

def send_sms(phone_number, message):
    try:
        with serial.Serial(COM_PORT, BAUD_RATE, timeout=1) as modem:
            time.sleep(1)  
            
            
            modem.write(b'AT+CMGF=1\r')
            time.sleep(1)
            print("Set SMS mode to text")
            
           
            modem.write(f'AT+CMGS="{phone_number}"\r'.encode())
            time.sleep(1)
            print("Recipient's phone number set")
            
            
            modem.write(message.encode() + b'\x1A')  
            time.sleep(3)  
            print("Message sent successfully!")
    
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    recipient_number = input("Enter the recipient's phone number (with country code): ")
    message = input("Enter the message you want to send: ")
    send_sms(recipient_number, message)
