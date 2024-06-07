#Turns off all LEDs by grouping them, chaning the rgb to 0,0,0
#You must show your color once it has been set.
All_LED = Kitronik_Move_Motor.create_move_motor_zipled(4)
All_LED.set_color(Kitronik_Move_Motor.colors(Kitronik_Move_Motor.ZipLedColors.BLACK))
All_LED.show()

#LEDs are regrouped into front lights and back lights.
#The range parameter indicates which LED to start with and the number
#of consecutive LED's in that group (includeing the first).
Front_LED = All_LED.range(0, 2)
Back_LED = All_LED.range(2, 2)

#This will continually run as long as the robot is on.  
#When the light sensor on the microbit reads less than 100, then
#the front LEDs will turn white and the back LEDs will turn red, otherwise
#they will turn off.  This is to mimic the automatic lights on a vehicle. 
while True:
    
    if input.light_level() < 100:
        
        Front_LED.set_color(Kitronik_Move_Motor.colors(Kitronik_Move_Motor.ZipLedColors.WHITE))
        Front_LED.set_brightness(50)
        Front_LED.show()
        
        Back_LED.set_color(Kitronik_Move_Motor.colors(Kitronik_Move_Motor.ZipLedColors.RED))
        Back_LED.set_brightness(50)
        Back_LED.show()
    
    else:
        
        Front_LED.set_color(Kitronik_Move_Motor.colors(Kitronik_Move_Motor.ZipLedColors.BLACK))
        Front_LED.show()
        
        Back_LED.set_color(Kitronik_Move_Motor.colors(Kitronik_Move_Motor.ZipLedColors.BLACK))
        Back_LED.show()