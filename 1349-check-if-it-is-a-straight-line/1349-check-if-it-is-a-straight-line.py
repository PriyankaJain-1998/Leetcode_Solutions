class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        # slope = (coordinates[1][1]-coordinates[0][1])/(coordinates[1][0]-coordinates[0][0])
        # for i in range(2,len(coordinates)):
        #     x, y = coordinates[i][0], coordinates[i][1]
        #     temp_s = (coordinates[i][1]-coordinates[i-1][1])/(coordinates[i][0]-coordinates[i-1][0])
        #     if temp_s!=slope: return False
        # return True

        
        first_point = coordinates[0]
        second_point = coordinates[1]
        x1, y1 = first_point
        x2, y2 = second_point
        
        for point in coordinates[2:]:
            x, y = point
            if (x - x1) * (y2 - y1) != (y - y1) * (x2 - x1):
                return False
              
        return True
