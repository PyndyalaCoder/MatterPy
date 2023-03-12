# MatterPy

MatterPy is a Python library that calculates various properties of matter, including charge, volume, density, instantaneous velocity and speed, mass, gravitational force, temperature, gas pressure, voltage, and more.

## To Install

```
  pip install MatterPy
```

## To Use

After <strong>installation</strong>, make sure to create an instance of the object. For example:

```python
  newtons_apple = matter()
```
After this, use the `set` functions to setup information. (These set methods take input, then use it to perform calculations, before storing it in a variable. This variable can be retrieved using the `get` methods that are shown later):

```
setCharge(electrons): Sets the charge of the object in Coulombs, based on the number of electrons provided as an argument.
setVolumeCube(length): Sets the volume of the object to a cube with side length length.
setVolumeCone(radius, height): Sets the volume of the object to a cone with base radius radius and height height.
setVolumeCylinder(radius, height): Sets the volume of the object to a cylinder with base radius radius and height height.
setVolumeSphere(radius): Sets the volume of the object to a sphere with radius radius.
setVolumeRectPrism(length, w, h): Sets the volume of the object to a rectangular prism with length length, width w, and height h.
setDensity(mass): Sets the density of the object, based on its mass and volume. Note that the volume must be set before calling this function.
setInstVelocity(x1, y1, z1, x2, y2, z2, t1, t2): Sets the instantaneous velocity of the object, based on its position at two different times.
setInstSpeed(x1, y1, z1, x2, y2, z2, t1, t2): Sets the instantaneous speed of the object, based on its position at two different times.
setMass(mass): Sets the mass of the object.
setVelocity(velocity): Sets the velocity of the object.
setHeight(height): Sets the height of the object.
setVolts(voltage): Sets the voltage of the object.
setLocalGravityForce(g): Sets the local gravitational force.
setTemperature(temp): Sets the temperature of the object.
setAtomicNumber(number)
setAtomicMass(mass)
setResistance(voltage, current)
setCapacitance(charge, voltage)
setHalfLife(life)
setSphereSurfaceArea(radius)
setCylinderSurfaceArea(radius, height)
setConeSurfaceArea(radius, height)
setRectSurfaceArea(length, width, height)
```

<br>
Here are some functions that you can use to retrieve information about your object:

```python
getCharge() # retrieves the charge of the object in Coulombs
getVolume() # retrieves the volume of the object in cubic meters
getDensity() # retrieves the density of the object in kilograms per cubic meter
getInstVelocity() # retrieves the instantaneous velocity of the object in meters per second
getInstSpeed() # retrieves the instantaneous speed of the object in meters per second
getLocalGravity() # retrieves the local gravitational force in meters per second squared
getGasPressure(gas_density) # retrieves the gas pressure in pascals, based on the gas density and temperature
getVolts() # retrieves the voltage of the object in volts
getKineticEnergy()
getDecayRate()
getNuclearBindingEnergy()
getResistance()
getSurfaceArea()
luminosity(radius)
getSchwarzschildFrequency()
getEscapeVelocity(radius)
getSchwarzschildRadius()
getCapacitance()
getWeight()
returnConsts() # returns physics constants
```
