#Pseudocode for Control module of software

class point(valuepassed, anglepassed):
    """
    Class used for storing points in polar coordinates.
    Angle is in respect to the front of the device.
    """
    self.value = valuepassed
    self.angle = anglepassed
    
    def getCartesian()
        """
        Returns the cartesian coordinates of the point.
        """
        return (x, y)

class Map(listofcartesianpoints = []):
    """
    Class used to store list of points in cartesian coordinates, where the device is an origin.
    """

    def createMap(listofcartesianpoints)
        """
        Creates a proper map with straight walls from given list.
        """
        return mappedPoints

    def getQImage(scale = 0) //TODO decide on default value based on the size of the screen
        """
        Returns scaled QImage of the map
        """
        return mapImage



class Control():
    """
    One-instance class that handles processing of data and hardware interaction.
    """

    def getLidar():
        """
        Obtains single value of measurement from LIDAR sensor
        """
        return value_from_LIDARsensor

    def moveMotorBynStep(stepnum):
        """
        Moves motor by number of basic steps
        """
        return angle_moved_by

    def getDistance(samplesize=10)
        """
        takes n = 10 ( //TODO specify appropiate number)
        measurements and averages them.
        Returns the averaged distance.
        """
        l = []
        for it in range(samplesize):
            l[it] = getLidar()
        
        averagedist = sum(l) / samplesize
        return averagedist

    

