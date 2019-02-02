#import antigravity

import numpy

def parallax():
    ui = input('What are you solving for? Distance, Baseline, or Angle: ')
    ui = ui.upper()
    if ui == 'DISTANCE':
        print('baseline is 1 on Earth')
        baseline = float(input('Baseline(AU):'))
        angle = float(input('Angle(arcseconds):'))
        distance = baseline / angle
        distance = str(distance)
        distance = distance + ' parsecs'
        return distance
    elif ui == 'BASELINE':
        distance = float(input('Distance(parsecs):'))
        angle = float(input('Angle(arcseconds):'))
        baseline = distance * angle
        baseline = str(baseline)
        baseline = baseline + ' AU'
        return baseline
    elif ui == 'ANGLE':
        distance = float(input('Distance(parsecs):'))
        print('baseline is 1 on Earth')
        baseline = float(input('Baseline(AU):'))
        angle = baseline / distance
        angle = str(angle)
        angle = angle + ' arcseconds'
        return angle

############

def distanceModulus():
    ui = input('What are you solving for? Absolute Magnitude, Apparent Magnitude, or Distance: ')
    ui = ui.upper()
    if ui == 'ABSOLUTE MAGNITUDE':
        apparentMagnitude = float(input('Apparent Magnitude: '))
        distance = float(input('Distance(parsecs): '))
        distance = distance - 5
        distance = numpy.log10(distance)
        absoluteMagnitude = (-5 * distance) / apparentMagnitude
        return absoluteMagnitude

#############

def hubblesLaw():
    ui = input('What are you solving for? Recessional Velocity, or Distance: ')
    ui = ui.upper()
    hubbleConstant = 70
    if ui == 'RECESSIONAL VELOCITY':
        distance = float(input('Distance(Mpc): '))
        recessionalVelocity = hubbleConstant * distance
        recessionalVelocity = str(recessionalVelocity)
        recessionalVelocity = recessionalVelocity + ' km/s'
        return recessionalVelocity
    elif ui == 'DISTANCE':
        recessionalVelocity = float(input('Recessional Velocity(km/s): '))
        distance = recessionalVelocity / hubbleConstant
        distance = str(distance)
        distance = distance + ' Mpc'
        return distance


###################
def kelvinWavelength():
    ui = input('What are you solving for? Max Wavelength, or Temperature: ')
    ui = ui.upper()
    constant = .00293
    if ui == 'MAX WAVELENGTH':
        temperature = float(input('Temperature(K): '))
        maxWavelength = constant / temperature
        maxWavelength = str(maxWavelength)
        maxWavelength = maxWavelength + ' m'
        return maxWavelength
    if ui == 'TEMPERATURE':
        maxWavelength = float(input('Max Wavelength(m): '))
        temperature = constant / maxWavelength
        temperature = str(temperature)
        temperature = temperature + ' K'
        return temperature

#################

def apparentBrightness():
    ui = input('What are you solving for? Apparent Brightness, Luminosity, or Distance: ')
    ui = ui.upper()
    if ui == 'APPARENT BRIGHTNESS':
        luminosity = float(input('Luminosity(W): '))
        distance = float(input('Distance(m): '))
        apparentBrightness = luminosity / (4 * numpy.pi * (distance ** 2))
        apparentBrightness = str(apparentBrightness)
        apparentBrightness = apparentBrightness + ' W/m^2'
        return apparentBrightness
    elif ui == 'LUMINOSITY':
        apparentBrightness = float(input('Apparent Brightness(W/m^2): '))
        distance = float(input('Distance(m): '))
        luminosity = 4 * numpy.pi * (distance ** 2) * apparentBrightness
        luminosity = str(luminosity)
        luminosity = luminosity + ' W'
        return luminosity
    elif ui == 'DISTANCE':
        apparentBrightness = float(input('Apparent Brightness(W/m^2): '))
        luminosity = float(input('Luminosity(W): '))
        distance = (luminosity / (4 * numpy.pi * apparentBrightness)) ** .5
        distance = str(distance)
        distance = distance + ' m'
        return distance


##################################################
##################################################


with open('formulas') as f:
    for line in f:
        print(line.strip())
ui = input('What formula would you like to use: ')
ui = ui.upper()

if ui == 'PARALLAX':
    answer = parallax()
elif ui == 'DISTANCE MODULUS':
    answer = distanceModulus()
elif ui == 'HUBBLES LAW':
    answer = hubblesLaw()
elif ui == 'KELVIN-WAVELENGTH':
    answer = kelvinWavelength()
elif ui == 'APPARENT BRIGHTNESS':
    answer = apparentBrightness()
print(answer)
