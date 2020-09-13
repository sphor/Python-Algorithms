"""
Description: Script that Clerks at Five Star Retro Video can use to calculate the total charge for a customer’s video rentals.

Pseudocode

     1. Significant constants
          new videos
          oldies
     2. The inputs are
          (Specifics to added by you)
     3. Computations:
          total charge = new videos + old video 
     4. The outputs are
          total charge

"""
newVideos = float(3.00)
oldies = float(2.00)
newVideosCount = int(input("Enter new video count "))
oldiesCount = int(input("Enter oldies count "))

totalCharge = newVideos*newVideosCount + oldies*oldiesCount
print("The total cost is $", totalCharge)
