class ArucoMarker:
    def __init__(self, marker_id, cX, cY):
        # Initialize the ArucoMarker instance with its ID and center coordinates
        self.id = marker_id
        self.cX = cX
        self.cY = cY

    def describe(self):
        # Method to print the marker's attributes
        print(f"Aruco Marker ID: {self.id}, Center X: {self.cX}, Center Y: {self.cY}")
