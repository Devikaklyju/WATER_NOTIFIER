import time
from plyer import notification

if __name__ == "__main__":
    
    notification.notify(
    title = "STOP WHATEVER YOU ARE DOING AND GO GRAB A GLASS OF WATER!!!",
    message  = "It's so important for you to get hydrated!\nA simple glass of water can help boost brain function by 14%.",
    app_icon = r"C:\Users\User\Desktop\drinking water notifier\icon.ico.ico",
    timeout=10
    )
    
