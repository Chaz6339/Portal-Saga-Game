from items import SparePart, ShipPiece, Portal
import random 


class Planet:
    def __init__(self, size = 15, starting = True):
        # Make the following instance fields
        # 1) The map is a size x size 2D Python list
        self.size = size
        self.starting = starting
        self.map = []
        for x in range(self.size):
            row = []
            for y in range(self.size):
                row.append(None)
            self.map.append(row)

        # If its the starting planet
        # Setup the starting map (when starting is True)
        # It has spaceship components, spare parts, and wormholes
        if self.starting == True:
            cabin = ShipPiece("./Img/cabin.ppm", "broken")
            cabinLoc = self.getEmptyLocation()
            row, col = cabinLoc
            self.map[row][col] = cabin
            exhaust = ShipPiece("./Img/exhaust.ppm", "broken")
            exhaustLoc = self.getEmptyLocation()
            row, col = exhaustLoc
            self.map[row][col] = exhaust
            engine = ShipPiece("./Img/engine.ppm", "broken")
            engineLoc = self.getEmptyLocation()
            row, col = engineLoc
            self.map[row][col] = engine
            engine2 = ShipPiece("./Img/engine.ppm", "broken")
            engine2Loc = self.getEmptyLocation()
            row, col = engine2Loc
            self.map[row][col] = engine2
            exhaust2 = ShipPiece("./Img/exhaust.ppm", "broken")
            exhaust2Loc = self.getEmptyLocation()
            row, col = exhaust2Loc
            self.map[row][col] = exhaust2

            screw = SparePart("./Img/screw.ppm")
            gear = SparePart("./Img/gear.ppm")
            bagel = SparePart("./Img/bagel.ppm")
            lettuce = SparePart("./Img/lettuce.ppm")
            cake = SparePart("./Img/cake.ppm")

            items = [screw, gear, bagel, lettuce, cake]
          
            for i in range(4):
                max = (len(items) - 1)
                randomNum = random.randint(0, max)
                item = items[randomNum]
                itemLoc = self.getEmptyLocation()
                row, col = itemLoc
                self.map[row][col] = item
                items.remove(item)

            items = [screw, gear, bagel, lettuce, cake]

            for i in range(random.randint(0, 5)):
                randomNum = random.randint(0, max)
                item = items[randomNum]
                itemLoc = self.getEmptyLocation()
                row, col = itemLoc
                self.map[row][col] = item
                
            for i in range (random.randint(2, 10)):     
                row, col = self.getEmptyLocation()
                self.map[row][col] = Portal()

        # If its not the starting planet
        # Setup a map for a planet that isn't the starting Planet
        # It has spare parts and wormholes
        if starting != True:
            screw = SparePart("./Img/screw.ppm")
            gear = SparePart("./Img/gear.ppm")
            bagel = SparePart("./Img/bagel.ppm")
            lettuce = SparePart("./Img/lettuce.ppm")
            cake = SparePart("./Img/cake.ppm")

            items = [screw, gear, bagel, lettuce, cake]
          
            for i in range(3):
                max = (len(items)-1)
                randomNum = random.randint(0, max)
                item = items[randomNum]
                itemLoc = self.getEmptyLocation()
                row, col = itemLoc
                self.map[row][col] = item
                items.remove(item)

            items = [screw, gear, bagel, lettuce, cake]

            for i in range(random.randint(0, 5)):
                randomNum = random.randint(0, max)
                item = items[randomNum]
                itemLoc = self.getEmptyLocation()
                row, col = itemLoc
                self.map[row][col] = item

            for i in range (random.randint(2, 10)):
                row, col = self.getEmptyLocation()

                self.map[row][col] = Portal()

       # Examples of making all three items on a planet
       # x = SparePart("./Img/screw.ppm") 
       # y = ShipPiece("./Img/cabin.ppm", "working")
       # z = Portal()

    def getEmptyLocation(self):
        """
        Finds an empty location on the map. 
        """
        # Optional method, but helpful for Part 1
        # Find an empty place in the map
        # Return its location as a list [row,col]
        empty = False
        while empty == False:
            col= random.randint(0, self.size - 1)
            row = random.randint(0, self.size - 1)
            if self.map[row][col] == None:
                empty = True
        
        empty_location = [row, col]
        return empty_location
    
    def isPortal(self, row, column):
        """
        Are these row, column coordinates a portal? Returns True/False. 
        """
        if self.map[row][column] == None:
            return False  
        elif self.map[row][column].getKind() == "portal":
            return True
        else:
            return False

    def getPortal(self, row, column):
        """
        Return the Portal at coordinates [row, col] or return None.
        """
        if self.map[row][column] == None:
            return None
        elif self.map[row][column].getKind() == "portal":
            return self.map[row][column]
        else:
            return None

    def findAPortal(self):
        """
        Return the location [row, col] of some unconnected portal. 
        """
        for x in range(self.size):
            for y in range(self.size):
                item = self.map[x][y]
                if item == None:
                    pass
                else: 
                    if item.getKind() == "portal":
                        if item.isConnected() == False:
                            return [x, y]

    def setupWormhole(self, row, column): # Double check w Prof.
        """
        Make sure the wormhole is ready to go at coordinates [row, column].
        """
        if self.map[row][column] == None:
            return -1
        elif self.map[row][column].getKind() != "portal":
            return -1
        elif self.map[row][column].getKind() == "portal":
            portalcoords = row, column 
        
        if self.map[row][column].isConnected() == True:
            return 
        else:
            planet = Planet()
            findP = planet.findAPortal() 
            newPortal = planet.getPortal(findP[0], findP[1])
            self.map[row][column].setPlanet(self) # Setting a planet on a portal in the current map
            self.map[row][column].setLocation(row, column) # Setting a location
            self.map[row][column].setOtherPortal(newPortal)

            newPortal.setPlanet(planet)
            newPortal.setLocation(findP[0], findP[1])
            newPortal.setOtherPortal(self.map[row][column])
        