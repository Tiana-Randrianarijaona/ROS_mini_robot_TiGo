class TrackerHelper():
    def __init__(self, focal_length = 10000,real_ball_radius = 100):
        self.focal_length = focal_length
        self.real_ball_radius = real_ball_radius

    # focal length finder function
    def setFocalLength(self,measured_distance, radius_in_frame):

        focal_length_value = (radius_in_frame * measured_distance) / self.real_ball_radius
        #return focal length.
        self.focal_length =  focal_length_value
    
    def getCoordinates(self, ball_radius_in_frame, center_y_in_frame):
        x = (self.real_ball_radius * self.focal_length)/ball_radius_in_frame
        y = (center_y_in_frame * x )/self.focal_length
        print(f"(x,y) = ({x},{y})")
        return (x,y)    

    def getDistance(self,radius_in_frame):
        return self.focal_length * self.real_ball_radius / radius_in_frame
    # def initializeFocalLength(self):
        
