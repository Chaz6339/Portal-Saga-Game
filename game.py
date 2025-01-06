""" 
Game to play 'Lost Rovers'. This is the file you edit.
To make more ppm files, open a gif or jpg in xv and save as ppm raw.
"""
from GUI.graphics import Point
from items import SparePart, ShipPiece, Portal
from planet import Planet
from planet import *
from mylist import *
from stack import *
import random
from myqueue import *
from task import *

class Game:
    SIZE = 15 # 15x15 squares in the map

    def __init__(self):
        # Your game needs instance fields for:
        # 1) a Planet instance. This is the current planet you are on. 
        #      It begins as a starting planet.
        # 2) a rover location of row and column. This is where you are 
        #       on the map.  The rover starts in an empty location on the map.
        self.planet = Planet(Game.SIZE)
        self.rover_row, self.rover_col = self.planet.getEmptyLocation()
        self.stack = LinkedStack()

        # TODO Part 3
        # Your game needs instance fields for:
        # 1) a List of items in your inventory
        self.inventory = MyList()
        # 2) a Queue of tasks to fix the broken ship pieces
        self.tasks = LinkedQueue() 
        self.taskMake()

    def taskMake(self):
        brokenDict = {"exhaust": 0, "engine": 0, "cabin": 0}
        for row_index in range(Game.SIZE):
            for col_index in range(Game.SIZE):
                var = self.planet.map[row_index][col_index]
                if var != None and var.getKind() == "ship" and var.getStatus() == "broken":
                    name = var.getName()
                    brokenDict[name] += 1

        for key in brokenDict:
            amount = brokenDict[key]
            for rep in range(amount):
                task = Task(key)

                partList = ["screw", "gear", "bagel", "lettuce", "cake"]
                randNum = random.randint(2, 4)
                for x in range(randNum):
                    randPart = random.randint(0, 4)
                    partName = partList[randPart]
                    randAmount = random.randint(1, 3)
                    task.addComponent(randAmount, partName)

                self.tasks.enqueue(task)

    def getRoverImage(self):
        """ 
        Called by GUI when screen updates.
        Returns image name (as a string) of the rover. 
		(Likely './Img/rover.ppm')
        """
        # Only edit this if you get your own rover image
        return "./Img/rover.ppm"

    def getRoverLocation(self):
        """ 
        Called by GUI when screen updates.
        Returns location (as a Point). 
        """
        # return Point(column, row) # backwards of what you expect
        #return self.roverLocation
        return Point(self.rover_col, self.rover_row)
        
    def getImage(self, point:Point):
        """
        Called by GUI when screen updates.
        Returns image name (as a string) or None for the 
		spare part, ship component, or portal at the given 
		point coordinates. (such as './Img/engine.ppm')
        """
        row = point.y # point is backwards of what you expect
        col = point.x
        point = self.planet.map[row][col]

        if point == None:  
            return None
        else:
            image = point.getImageName()
            return image

    def goUp(self):
        """
        Called by GUI when button clicked.
        If legal, moves rover. If the robot lands
        on a portal, it will teleport.
        """
        # If legal, moves rover
        if self.rover_row > 0:
            self.rover_row -= 1
            
        if self.planet.map[self.rover_row][self.rover_col] == None:
            pass
        elif self.planet.map[self.rover_row][self.rover_col].getKind() == "portal":
            self.teleport()
        else:
            pass

    def goDown(self):
        """
        Called by GUI when button clicked. 
        If legal, moves rover. If the robot lands
        on a portal, it will teleport. 
        """
        # If legal, moves rover
        if self.rover_row < Game.SIZE - 1:
            self.rover_row += 1

        # If the robot lands on a portal, teleport
        if self.planet.map[self.rover_row][self.rover_col] == None:
            pass
        elif self.planet.map[self.rover_row][self.rover_col].getKind() == "portal":
            self.teleport()
        else:
            pass

    def goLeft(self):
        """
        Called by GUI when button clicked. 
        If legal, moves rover. If the robot lands
        on a portal, it will teleport. 
        """
        # If legal, moves rover
        if self.rover_col > 0:
            self.rover_col -= 1 

        # If the robot lands on a portal, teleport
        if self.planet.map[self.rover_row][self.rover_col] == None:
            pass
        elif self.planet.map[self.rover_row][self.rover_col].getKind() == "portal":
            self.teleport()
        else:
            pass

    def goRight(self):
        """
        Called by GUI when button clicked. 
        If legal, moves rover. If the robot lands
        on a portal, it will teleport.
        """
        # If legal, moves rover
        if self.rover_col < Game.SIZE -1:
            self.rover_col += 1 

        # If the robot lands on a portal, teleport
        if self.planet.map[self.rover_row][self.rover_col] == None:
            pass
        elif self.planet.map[self.rover_row][self.rover_col].getKind() == "portal":
            self.teleport()
        else:
            pass

    def showWayBack(self):
        """
        Called by GUI when button clicked.
        Flash the portal leading towards home.
        """
        head = self.stack.peek()
        if head == None:
            pass
        else: 
            head.fl = True

    def getInventory(self):
        """
        Called by GUI when inventory updates.
        Returns entire inventory (as a string). 
		3 cake
		2 screws
		1 rug
	    """
        # TODO Part 3
        count_gear = 0
        count_bagel = 0
        count_lettuce = 0
        count_screw = 0
        count_cake = 0

        string = ""
        for i in range(len(self.inventory)):
            item = self.inventory[i]
            if item == 'gear':
                count_gear += 1
            if item == 'bagel':
                count_bagel += 1
            if item == 'lettuce':
                count_lettuce += 1
            if item == 'screw':
                count_screw += 1
            if item == 'cake':
                count_cake += 1

        if count_gear > 0:
            string += f"{count_gear} gear(s) \n"
        if count_bagel > 0:
            string += f"{count_bagel} bagel(s) \n"
        if count_lettuce > 0:
            string += f"{count_lettuce} lettuce \n"
        if count_screw > 0:
            string += f"{count_screw} screw(s) \n"
        if count_cake > 0:
            string += f"{count_cake} cake(s) \n"

        if len(self.inventory) > 0:
            string = string[0:len(string) - 2]

        return string 

    def pickUp(self):
        """
        Called by GUI when button clicked. 
		If rover is standing on a part (not a portal 
		or ship component), pick it up and add it
		to the inventory. 
        """
        # TODO Part 3

        if self.planet.map[self.rover_row][self.rover_col] == None:
            return
        if self.planet.map[self.rover_row][self.rover_col].getKind() == "part":
            partPicked = self.planet.map[self.rover_row][self.rover_col]
            self.planet.map[self.rover_row][self.rover_col] = None
            partString = partPicked.getName()
            self.inventory.insert(partString)
        

    def getCurrentTask(self):
        """ 
        Called by GUI when task updates.
        Returns top task (as a string). 
		'Fix the engine using 2 cake, 3 rugs' or
		'You win!' 
 	    """
        if len(self.tasks) == 0:
            return "You win!"
        peeked = self.tasks.peek()
        name = peeked.getName()
        getComp = peeked.getComponents()
        string = "Fix the " + name + " using"
        for key in getComp:
            amount = getComp[key]
            string += "\n" + str(amount) + " " + key
        return string

    def performTask(self):
        """ 
        Called by the GUI when button clicked.
        If necessary parts are in inventory, and rover
        is on the relevant broken ship piece, then fixes
        ship piece and removes parts from inventory. If
        we run out of tasks, we win. 
        """
        task = self.tasks.peek()
        name = task.getName()
        comp = task.getComponents()

        item = self.planet.map[self.rover_row][self.rover_col]
        if item != None and item.getKind() == "ship" and item.getStatus() == "broken" and item.getName() == name:
            for partN in comp:
                if self.inventory.count(partN) < comp[partN]:
                    return
            item.setStatus("working")

            for stuff in comp:
                amount = comp[stuff]
                for z in range(amount):
                    self.inventory.remove(stuff)
                    self.tasks.dequeue()

    def setRoverLocation(self, row, col):
        """Sets the location of the rover. Used for autgrader testing."""
        self.rover_row = row
        self.rover_col = col

    def teleport(self):
        """ 
        If you are standing on a portal you teleport.
        """
        col, row = self.rover_col, self.rover_row
        if self.planet.map[self.rover_row][self.rover_col] == None:
            pass
        elif self.planet.map[self.rover_row][self.rover_col].getKind() == "portal":
            oldPortal = self.planet.map[self.rover_row][self.rover_col]
            self.planet.setupWormhole(row, col)
            otherPortal = oldPortal.getOtherPortal()
            planet = otherPortal.getPlanet()
            location = otherPortal.getLocation()
            head = self.stack.peek()
            if head == None:
                self.stack.push(otherPortal)
            elif head == oldPortal:
                self.stack.pop()
            else:
                self.stack.push(otherPortal)
            self.planet = planet
            self.rover_row, self.rover_col = location[0], location[1]