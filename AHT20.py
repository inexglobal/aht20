from microbit import i2c,sleep
class AHT20:
    AHT20_ADDR = 0x38
    def __init__(self):
        self.data = bytearray(6)
    def read(self):
        try:
            i2c.write(self.AHT20_ADDR, b'\xAC\x33\x00')
            sleep(100)
            self.data = i2c.read(self.AHT20_ADDR, 6)
            if self.data[0] & 0x80:
                i2c.write(self.AHT20_ADDR, b'\xBE')
                sleep(100)
                return (-991, -991)
            h = ((self.data[1] << 12) | (self.data[2] << 4) | ((self.data[3] & 0xF0) >> 4)) / pow(2, 20) * 100.0;
            t = (((self.data[3] & 0x0F) << 16) | (self.data[4] << 8) | self.data[5]) / pow(2, 20) * 200.0 - 50.0;
            return (round(t, 2), round(h, 2))
        except:
            return (-992, -992)