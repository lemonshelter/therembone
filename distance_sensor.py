import time
import VL53L0X

class DistanceSensor:
    def __init__(self):
        # Create a VL53L0X object
        self.tof = VL53L0X.VL53L0X(i2c_bus=1,i2c_address=0x29)
        # I2C Address can change before tof.open()
        # tof.change_address(0x32)
        self.tof.open()
        # Start ranging
        self.tof.start_ranging(VL53L0X.Vl53l0xAccuracyMode.BETTER)
    
    def measure_distance(self):
        distance = self.tof.get_distance()
        if distance < 0:
            distance = 0
        print("Distance: {} mm".format(distance))
        return distance

    def stop_sensor(self):
        self.tof.stop_ranging()
        self.tof.close()
