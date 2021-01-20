import Main
from Main import Setup

settings = Main.CurrentSetup()
settings.Set_Device(Setup.Get_Device())

print(settings.Get_Device())
