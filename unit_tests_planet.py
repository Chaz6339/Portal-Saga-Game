import unittest
from planet import Planet
from items import SparePart, ShipPiece, Portal

class TestPlanet(unittest.TestCase):

    def testInstanceFields(self):
        """
        Test that the instance fields of Planet, size, starting, and map are initialized correctly.
        """
        
        # Make a starting Planet
        planet = Planet(15, True) #size, map, and starting

        # Test the type of each instance field
        self.assertIsInstance(planet.size, int, "Attribute size is not an integer.") 
        self.assertIsInstance(planet.starting, bool, "Attribute starting is not a boolean.") 
        self.assertIsInstance(planet.map, list, "Attribute map is not a list.") 
    
    def testShipPieces(self): # exhaust, exhaust2, engine, engine2, cabin, total greater then 5
        """
        Test the number of ship components in the planet's map.
        At least five different ship pieces, which are rnadomized every map. 
        """

        # The below fails so you remember to replace it with a real test
        
        # Make a starting Planet
        planet = Planet(15, True)
        # Test the number of ship components to make sure there are enough
        # and they have the correct variety (broken, etc)
        
        pieceTotal = 0
        for row in range(len(planet.map)):
            for col in range(len(planet.map[0])):
                if type(planet.map[row][col]) == ShipPiece and planet.map[row][col].status == "broken":
                    pieceTotal += 1
        
        self.assertGreater(pieceTotal, 4, "There are not enough ship pieces.")
        
    def testSpareParts(self):
        """
        Test the number of ship spare parts in the planet's map.
        At least four different spare parts, which are rnadomized every map. 
        """
        sparetotal = []
        for count in range(4):
            planet = Planet(15, True)
            partTotal = 0
            differentTotal = []

            for row in range(len(planet.map)):
                for col in range(len(planet.map[0])):
                    if type(planet.map[row][col]) == SparePart:
                        partTotal += 1
                    if type(planet.map[row][col]) == SparePart and planet.map[row][col].imageName not in differentTotal:
                        differentTotal.append(planet.map[row][col])

            self.assertGreater(partTotal, 3, "There are not enough spare parts.")
            self.assertGreater(len(differentTotal), 2, "There are not enough different spare parts.")

            sparetotal.append(partTotal)

        uniqueCounts = []
        for count in sparetotal:
            if count not in uniqueCounts:
                uniqueCounts.append(count)

        self.assertGreater(len(set(uniqueCounts)), 1, "All planets have the same number of spare parts.") 

        # Make a starting Planet
        # Test the number of spare parts to make sure there are enough
        # Also test that multiple sorts of spare parts are represented
        # Make second, third, and fourth starting Planets
        # Get the number of spare parts of each
        
    def testPortals(self):
        """
        Test the number of portals in the planet's map.
        At least two portals. 
        """
        sparetotal = []
        for count in range(4):
            planet = Planet(15, True)
            portalTotal = 0

            for row in range(len(planet.map)):
                for col in range(len(planet.map[0])):
                    if type(planet.map[row][col]) == Portal:
                        portalTotal += 1

            self.assertGreater(portalTotal, 1, "There are not enough portals.")
            sparetotal.append(portalTotal)

        uniqueCounts = []
        for count in sparetotal:
            if count not in uniqueCounts:
                uniqueCounts.append(count)

        self.assertGreater(len(set(uniqueCounts)), 1, "All planets have the same number of portals.") 

        # Test the number of portals to make sure there are enough, at least 2
        # Make second, third, and fourth starting Planets
        # Get the number of portals of each
        # Test that they do not all have the same number of portals.
    
if __name__ == '__main__':
    unittest.main()
