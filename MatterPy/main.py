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
        self.resistance = None
        self.capacitance = None
        self.voltage = 0
        self.atomic_number = None
        self.half_life = None
        self.atomic_mass = None
        self.surface_area = None
        self.delta_temp = None
        self.spec_heat = None

    def setCharge(self, electrons):
        e = 1.602e-19
        q = electrons * e
        self.charge = q

    def setSphereSurfaceArea(self, radius):
        self.surface_area = 4 * math.pi * radius ** 2

    def setCylinderSurfaceArea(self, radius, height):
        self.surface_area = 2 * math.pi * radius * height + 2 * math.pi * radius ** 2

    def setConeSurfaceArea(self, radius, height):
        slant_height = math.sqrt(radius ** 2 + height ** 2)
        self.surface_area = math.pi * radius * slant_height + math.pi * radius ** 2

    def setRectSurfaceArea(self, length, width, height):
        self.surface_area = 2 * (length * width + length * height + width * height)

    def getSurfaceArea(self):
        if not self.surface_area:
            return "You have not set a surface area yet, use one of the funcs to set it"
        else:
            return self.surface_area

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
        
    def getGravityConst(self):
        # returns gravitational constant in m^3 kg^-1 s^-2.
        return 6.6743e-11
    
    def getLightSpeed(self):
        # returns speed of light in meters per second
        return 299792458

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

    @staticmethod
    def returnConsts():
        return {'BOLTZMANN_CONSTANT': 1.380649e-23,
                'ELEMENTARY_CHARGE': 1.602176634e-19,
                'PERMITTIVITY_OF_VACUUM': 8.8541878128e-12,
                'MAGNETIC_CONSTANT': 1.25663706212e-6,
                'SPEED_OF_SOUND_IN_AIR': 343.2}

    def setResistance(self, voltage, current):
        if current == 0:
            raise ZeroDivisionError("Current cannot be zero!")
        self.resistance = voltage / current

    def setCapacitance(self, charge, voltage):
        if voltage == 0:
            raise ZeroDivisionError("Voltage cannot be zero!")
        self.capacitance = charge / voltage

    def getResistance(self):
        if not self.resistance:
            return "You have not set resistance"
        return self.resistance

    def getCapacitance(self):
        if not self.capacitance:
            return "You have not set capacitance"
        return self.capacitance

    def setHalfLife(self, life):
        self.half_life = life

    def setAtomicNumber(self, number):
        self.atomic_number = number

    def getDecayRate(self):
        if not self.half_life:
            return "Set half life first"
        # Calculate the decay rate based on the half-life
        return math.log(2) / self.half_life

    def setAtomicMass(self, mass):
        self.atomic_mass = mass

    def getNuclearBindingEnergy(self):
        if not self.atomic_mass or not self.atomic_number:
            return "Set atomic_mass and self.atomic_number before trying to get nuclear binding energy"

        # Calculate the nuclear binding energy based on the atomic mass and number
        mass_defect = self.atomic_mass - (self.atomic_number * 1.00728)
        binding_energy = mass_defect * 931.5  # Conversion factor for MeV to atomic mass units
        return binding_energy

    def getSchwarzschildRadius(self):
        if not self.mass:
            return "You have not set mass. Please do that"
        """
        Calculates the Schwarzschild radius of an object given its mass.
        """
        G = 6.67430e-11  # gravitational constant
        c = 299792458  # speed of light
        rs = 2 * G * self.mass / (c ** 2)
        return rs

    def getEscapeVelocity(self, radius):
        if not self.mass:
            return "Set mass first"
        """
        Calculates the escape velocity of an object given its mass and radius.
        """
        G = 6.67430e-11  # gravitational constant
        ve = math.sqrt(2 * G * self.mass / radius)
        return ve

    def getSchwarzschildFrequency(self):
        if not self.mass:
            return "Mass needs to be set"
        """
        Calculates the Schwarzschild frequency of an object given its mass.
        """
        G = 6.67430e-11  # gravitational constant
        c = 299792458  # speed of light
        fs = (c ** 3) / (8 * math.pi * G * self.mass)
        return fs

    def luminosity(self, radius):
        if not self.temp:
            return "Temp needs to be set"
        """
        Calculates the luminosity of an object given its radius and temperature.
        """
        sigma = 5.670367e-8  # Stefan-Boltzmann constant
        L = 4 * math.pi * (radius ** 2) * sigma * (self.temp ** 4)
        return L
    
    def setSpecificHeatCapacity(cap):
        self.spec_heat = cap
    
    def setDeltaTemp(temp):
        self.delta_temp = temp
        
    def getHeatCapacity():
        if not self.delta_temp or not self.spec_heat or not self.mass:
            return "Some required consts are not defined"
        
        return self.mass * self.spec_heat * self.delta_temp
