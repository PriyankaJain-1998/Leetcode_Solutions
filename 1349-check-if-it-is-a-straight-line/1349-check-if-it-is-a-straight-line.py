class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        # slope = (coordinates[1][1]-coordinates[0][1])/(coordinates[1][0]-coordinates[0][0])
        # for i in range(2,len(coordinates)):
        #     x, y = coordinates[i][0], coordinates[i][1]
        #     temp_s = (coordinates[i][1]-coordinates[i-1][1])/(coordinates[i][0]-coordinates[i-1][0])
        #     if temp_s!=slope: return False
        # return True

 
        x1, y1 = coordinates[0][0],coordinates[0][1]
        x2, y2 = coordinates[1][0],coordinates[1][1]
        y_coord, x_coord = (y2 - y1), (x2 - x1)
        for point in coordinates[2:]:
            x, y = point
            if (x - x1) * y_coord != (y - y1) * x_coord:
                return False
              
        return True
