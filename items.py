""" 
Classes for items that appear in the map (except the rover).
Each class has a getKind() method which returns what sort of 
item it is as a String.
"""

class SparePart:
    def __init__(self, imageName):
        # Make the following instance fields
        # 1) The image name
        self.imageName = imageName

    def getImageName(self):
        # return the image name including the imagepath if any
        return self.imageName

    def getKind(self):
        return "part"
    
    def getName(self):
        """
        Return a string representation of the parts name.  
        """
        if self.imageName == "./Img/screw.ppm":
            return 'screw'
        if self.imageName == "./Img/gear.ppm":
            return 'gear'
        if self.imageName == "./Img/bagel.ppm":
            return 'bagel'
        if self.imageName == "./Img/lettuce.ppm":
            return 'lettuce'
        if self.imageName == "./Img/cake.ppm":
            return 'cake'
        else:
            raise Exception

class ShipPiece:
    def __init__(self, imageName, status):
        # Make the following instance fields
        # 1) The image name
        self.imageName = imageName
        # 2) Its status; is it broken or working?
        self.status = status

    def getImageName(self):
        # return the image name including the imagepath if any
        """
        Return a string representation of the parts name.  
        """
        if self.getName() == "cabin" and self.getStatus() == "broken":
            return "./Img/cabin_broken.ppm"
        if self.getName() == "cabin" and self.getStatus() == "working":
            return "./Img/cabin.ppm"
        if self.getName() == 'exhaust' and self.getStatus() == "broken":
            return "./Img/exhaust_broken.ppm"
        if self.getName() == 'exhaust' and self.getStatus() == "working":
            return "./Img/exhaust.ppm"
        if self.getName() == 'engine' and self.getStatus() == "broken":
            return "./Img/engine_broken.ppm"
        if self.getName() == 'engine' and self.getStatus() == "working":
            return "./Img/engine.ppm"
        
    def getKind(self):
        return "ship"
    
    def getStatus(self):
        """
        Return "broken" or "working"
        """
        if self.status == "broken":
            return "broken"
        elif self.status == "working":
            return "working"
        else:
            return "There was an error"

    def setStatus(self, status):
        """
        "working" or "broken"
        """
        self.status = status
        return self.status

    def getName(self):
        """
        Return a string representation of the parts name.  
        """
        if self.imageName == "./Img/cabin_broken.ppm" or self.imageName == "./Img/cabin.ppm":
            return 'cabin'
        if self.imageName == "./Img/exhaust_broken.ppm" or self.imageName == "./Img/exhaust.ppm":
            return 'exhaust'
        if self.imageName == "./Img/engine_broken.ppm" or self.imageName == "./Img/engine.ppm":
            return 'engine'


class Portal:
    def __init__(self, portalMap = None, portalLocation = None):
        # Make the following instance fields
        # 1) The current image name ("./Img/portal.ppm" or "./Img/portal_flashing.ppm")
        self.imageName = "./Img/portal.ppm"
        self.flashing = "./Img/portal_flashing.ppm"
        self.fl= False

        # 1) The map that this portal is on
        self.portalMap = portalMap
        # 2) The location [row, column] of this portal on this map
        self.portalLocation = portalLocation
        # 3) The portal at the other end of the wormhole (None if it isn't known yet)
        self.otherPortal = None 
        self.planet = None

    def getImageName(self):
        # return the image name including the imagepath if any
        if self.fl == True:
            return self.flashing
        else:
            return self.imageName

    def getKind(self):
        return "portal"
    
    def isConnected(self):
        """
        Is this portal connected to another portal? True/False.
        """
        if self.otherPortal == None:
            return False
        else:
            return True
        
    def setPlanet(self, planet):
        """
        A setter method to set the instance field thje planet is on. 
        """
        self.planet = planet

    def getPlanet(self):
        """
        A getter method to return the instance field the planet the portal is on. 
        """
        return self.planet
    
    def setLocation(self, row, col):
        """
        A setter method to set the instance field of the [row, col] location
        of the portal in its map. 
        """
        self.portalLocation = [row, col]

    def getLocation(self):
        """
        A getter method to return the instance field the [row, col] location
        of the portal in its map. 
        """
        return self.portalLocation
    
    def setOtherPortal(self, portal):
        """
        A setter method to set the instance field for the portal on the 
        other end of the wormhole. 
        """
        self.otherPortal = portal

    def getOtherPortal(self):
        """
        A getter method to return the instance field for the portal on the
        other end of the wormhole. 
        """
        return self.otherPortal