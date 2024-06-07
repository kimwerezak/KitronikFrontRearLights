// Turns off all LEDs by grouping them, chaning the rgb to 0,0,0
// You must show your color once it has been set.
let All_LED = Kitronik_Move_Motor.createMoveMotorZIPLED(4)
All_LED.setColor(Kitronik_Move_Motor.colors(Kitronik_Move_Motor.ZipLedColors.Black))
All_LED.show()
// LEDs are regrouped into front lights and back lights.
// The range parameter indicates which LED to start with and the number
// of consecutive LED's in that group (includeing the first).
let Front_LED = All_LED.range(0, 2)
let Back_LED = All_LED.range(2, 2)
// This will continually run as long as the robot is on.  
// When the light sensor on the microbit reads less than 100, then
// the front LEDs will turn white and the back LEDs will turn red, otherwise
// they will turn off.  This is to mimic the automatic lights on a vehicle. 
while (true) {
    if (input.lightLevel() < 100) {
        Front_LED.setColor(Kitronik_Move_Motor.colors(Kitronik_Move_Motor.ZipLedColors.White))
        Front_LED.setBrightness(50)
        Front_LED.show()
        Back_LED.setColor(Kitronik_Move_Motor.colors(Kitronik_Move_Motor.ZipLedColors.Red))
        Back_LED.setBrightness(50)
        Back_LED.show()
    } else {
        Front_LED.setColor(Kitronik_Move_Motor.colors(Kitronik_Move_Motor.ZipLedColors.Black))
        Front_LED.show()
        Back_LED.setColor(Kitronik_Move_Motor.colors(Kitronik_Move_Motor.ZipLedColors.Black))
        Back_LED.show()
    }
    
}
