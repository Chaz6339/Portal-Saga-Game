import unittest
from game import Game
from items import SparePart, ShipPiece, Portal
from planet import Planet

class TestGame(unittest.TestCase):
    def testInit(self):
        """
        Test the initialization of the Game class.
        """
        # The below fails so you remember to replace it with a real test
        # Hint: you need to verify if the attributes are initialized as they should
        # Make a Game (don't call start())
        # Test that the instance fields are the correct types
        game = Game()
        self.assertIsInstance(game.planet, Planet)

    def testGoUp(self):
        """
        Test if you can go up, and if you can, does your ship go up on GUI. 
        """
        # The below fails so you remember to replace it with a real test
        # Hint: you need to verify the related attributes to check if they updated correctly
        # Make a Game
        # Set the rover location to a location of your choosing
        # (Don't set it where it will land on a portal. Remove the portal if needed)
        # Call the goUp() method of the game
        # Test the rover's new location to make sure it has indeed gone up.
        game = Game()
        game.planet.map[8][4] = None
        game.planet.map[8 - 1][4] = None # [row, y] [col, x]
        game.rover_row = 8 
        game.rover_col = 4
        game.goUp()
        self.assertEqual(game.rover_row, 7, "Row did not decrease.")
        self.assertEqual(game.rover_col, 4, "Column changed unexpectedly.")
        
    def testGoDown(self):
        """
        Test if you can go down, and if you can, does your ship go down on GUI. 
        """
        # The below fails so you remember to replace it with a real test
        # Hint: you need to verify the related attributes to check if they updated correctly

        game = Game()
        game.planet.map[8][4] = None
        game.planet.map[8 + 1][4] = None # [row, y] [col, x]
        game.rover_row = 8 
        game.rover_col = 4
        game.goDown()
        self.assertEqual(game.rover_row, 9, "Row did not Increase.")
        self.assertEqual(game.rover_col, 4, "Column changed unexpectedly.")
       
    def testGoLeft(self):
        """
        Test if you can go left, and if you can, does your ship go left on GUI. 
        """
        # The below fails so you remember to replace it with a real test
        # Hint: you need to verify the related attributes to check if they updated correctly
        # This is the same idea as goUp
        
        game = Game()
        game.planet.map[8][4] = None
        game.planet.map[8][4 - 1] = None # [row, y] [col, x]
        game.rover_row = 8 
        game.rover_col = 4
        game.goLeft()
        self.assertEqual(game.rover_row, 8, "Row changed unexpectedly")
        self.assertEqual(game.rover_col, 3, "Column did not decrease.")
        
    def testGoRight(self):
        """
        Test if you can go right, and if you can, does your ship go right on GUI. 
        """
        # The below fails so you remember to replace it with a real test
        # Hint: you need to verify the related attributes to check if they updated correctly
        game = Game()
        game.planet.map[8][4] = None
        game.planet.map[8][4 + 1] = None # [row, y] [col, x]
        game.rover_row = 8 
        game.rover_col = 4
        game.goRight()
        self.assertEqual(game.rover_row, 8, "Row changed unexpectedly")
        self.assertEqual(game.rover_col, 5, "Column did not increase.")

    def test_setup_wormhole(self):
        """
        Test that the portals fields are properly setup. 
        """
        game = Game()

        portal_location = game.planet.findAPortal()
        row, column = portal_location
        portal = game.planet.getPortal(row, column)
        game.planet.setupWormhole(row, column)
        OtherPortal = portal.getOtherPortal()

        self.assertTrue(portal.isConnected(), "Portal is not connected.")
        self.assertNotEqual(portal.getPlanet(), OtherPortal.getPlanet(), "Portal is not on different planet.")
        self.assertNotEqual(portal.getLocation(), OtherPortal.getLocation(), "Portal is connected to itself.")
        self.assertEqual(OtherPortal.getOtherPortal(), portal, "Destination of OtherPortal is not portal. ")
        self.assertEqual(portal.getOtherPortal(), OtherPortal, "Destination of portal is not OtherPortal.")

    def test_unconnected_teleport(self):
        """
        Test that it is a different planet and a different location. 
        """
        game = Game()
        portalLocation = game.planet.findAPortal()
        row, column = portalLocation
        portal = game.planet.getPortal(row, column)
        [game.rover_row, game.rover_col] = [row, column]
        game.teleport()

        self.assertNotEqual([game.rover_row, game.rover_col], [row, column], "Rover location didn't change when teleported.")
        self.assertNotEqual(portal.getPlanet(), game.planet, "Rover did not change planets after teleporting.")

    def test_connected_portal(self):
        """
        Test that it is a original planet and a original location. 
        """
        game = Game()
        portalLocation = game.planet.findAPortal()
        row, column = portalLocation
        portal = game.planet.getPortal(row, column)
        [game.rover_row, game.rover_col] = [row, column]
        game.teleport()
        game.teleport()

        self.assertEqual([game.rover_row, game.rover_col], [row, column], "The rover is not in it's original location.")
        self.assertEqual(portal.getPlanet(), game.planet, "The rover is not in it's original planet.")

    def test_show_way_back(self): # This is wrong and must be fixed. 
        """
        Test that the portal you are now on is flashing (use getImageName()). 
        """
        # Hint: you need to verify the related attributes to check if they updated correctly
        game = Game()

        portalLocation = game.planet.findAPortal()
        row, column = portalLocation
        [game.rover_row, game.rover_col] = [row, column]
        game.teleport()
        [row, column] = [game.rover_row, game.rover_col]
        game.showWayBack()
        currentPortal = game.planet.getPortal(row, column)
        self.assertEqual(currentPortal.getImageName(), "./Img/portal_flashing.ppm", "Portal is not flashing.")
        
    def testPickUp(self):
        # The below fails so you remember to replace it with a real test
        # Hint: you need to verify the related attributes to check if they updated correctly
        # TODO Part 3
        pass

    def testPerformTask(self):
        # The below fails so you remember to replace it with a real test
        # Hint: you need to verify the related attributes to check if they updated correctly
        # TODO Part 3
        pass

    # add more test functions for other methods you have added (except simple getter and setters methods)
    
if __name__ == '__main__':
    unittest.main()