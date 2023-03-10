import math


class matter:
    def __init__(self):
        self.charge = None
        self.volume = None
        self.density = None
        self.inst_velocity = None
        self.inst_speed = None
        self.mass = None
        self.velocity = None
        self.height = None
        self.gravitational_force = 9.81
        self.temp = 0
        self.gasConst = 8.314
        self.voltage = 0

    def setCharge(self, electrons):
        e = 1.602e-19
        q = electrons * e
        self.charge = q

    def setVolumeCube(self, length):
        self.volume = length ** 3

    def setVolumeCone(self, radius, height):
        V = (1 / 3) * math.pi * radius ^ 2 * height
        self.volume = V

    def setVolumeCylinder(self, radius, height):
        V = math.pi * radius ** 2 * height
        self.volume = V

    def setVolumeSphere(self, radius):
        volume = 4 / 3 * math.pi * radius ** 3
        self.volume = volume

    def setVolumeRectPrism(self, length, w, h):
        self.volume = length * w * h

    def setDensity(self, mass):
        if not self.volume:
            raise TypeError("Please set the volume of the object before attempting to set density.")
        else:
            self.density = mass / self.volume

    def setInstVelocity(self, x1, y1, z1, x2, y2, z2, t1, t2):
        if t2 == t1:
            raise ZeroDivisionError("Both times are exactly the same, this causes the program to divide by 0")
        vx = (x2 - x1) / (t2 - t1)
        vy = (y2 - y1) / (t2 - t1)
        vz = (z2 - z1) / (t2 - t1)
        self.inst_velocity = [vx, vy, vz]

    def setInstSpeed(self, x1, y1, z1, x2, y2, z2, t1, t2):
        vx = (x2 - x1) / (t2 - t1)
        vy = (y2 - y1) / (t2 - t1)
        vz = (z2 - z1) / (t2 - t1)
        speed = math.sqrt(vx ** 2 + vy ** 2 + vz ** 2)
        self.inst_speed = speed

    def setMass(self, mass):
        self.mass = mass

    def setVelocity(self, velocity):
        self.velocity = velocity

    def setHeight(self, height):
        self.height = height

    def setVolts(self, voltage):
        self.voltage = voltage

    def setLocalGravityForce(self, g):
        self.gravitational_force = g

    def setTemperature(self, temp):
        self.temp = temp

    def getKineticEnergy(self):
        if not self.velocity or not self.mass:
            return "You have not set either mass, velocity or both. Please do so before attempting to get KE"

        else:
            return 0.5 * self.mass * self.velocity ** 2  # joules

    def getGPE(self):
        if not self.mass or not self.height:
            return "You have not set either height, mass or both. Please do so before attempting to get GPE"
        return self.mass * self.gravitational_force * self.height  # joules

    def getWeight(self):
        return self.mass * self.gravitational_force

    def getCharge(self):
        if not self.charge:
            return "You have not defined set a charge"
        else:
            return self.charge

    def getVolume(self):
        if not self.volume:
            return "You have not set a volume; try setting one using one of the `setVolume` functions"
        else:
            return self.volume

    def getDensity(self):
        if not self.density:
            return "You have not set a density; try using the `setDensity(mass)` function to get started"
        else:
            return self.density

    def getInstVelocity(self):
        if not self.inst_velocity:
            return "You have not set an inst_velocity; try using the `setInstVelocity` function to get started"
        else:
            return self.inst_velocity

    def getInstSpeed(self):
        if not self.inst_speed:
            return "You have not set an inst_speed; try using the `setInstSpeed` function to get started"
        return self.inst_speed

    def getLocalGravity(self):
        return self.gravitational_force

    def getGasPressure(self, gas_density):
        # temp is in Kelvin
        return gas_density * self.gasConst * self.temp

    def getVolts(self):
        return self.voltage

    def returnConsts(self):
        return {'BOLTZMANN_CONSTANT': 1.380649e-23,
                'ELEMENTARY_CHARGE': 1.602176634e-19,
                'PERMITTIVITY_OF_VACUUM': 8.8541878128e-12,
                'MAGNETIC_CONSTANT': 1.25663706212e-6,
                'SPEED_OF_SOUND_IN_AIR': 343.2 }
    
