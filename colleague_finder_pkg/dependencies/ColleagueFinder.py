import apriltag
import cv2
from ArucoMarker import ArucoMarker


class ColleagueFinder:
    def __init__(self):
        # Initialize the AprilTags detector options
        self.options = apriltag.DetectorOptions(families="tag16h5")
        self.detector = apriltag.Detector(self.options)

    def getColleagueInfo(self, frame):
        """
        Detects AprilTags in the given frame and returns a list of ArucoMarker objects.
        :param frame: Video frame in which AprilTags need to be detected.
        :return: List of ArucoMarker objects containing ID and center coordinates.
        """
        # Convert the frame to grayscale (AprilTag detection works on grayscale images)
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Detect the AprilTags in the frame
        results = self.detector.detect(gray)

        # List to hold detected ArucoMarker instances
        markers = []

        # Loop over the AprilTag detection results
        for r in results:
            # Get the tag ID and center coordinates
            tagID = r.tag_id
            (cX, cY) = (int(r.center[0]), int(r.center[1]))

            # Create an ArucoMarker instance for each detected tag
            marker = ArucoMarker(marker_id=tagID, cX=cX, cY=cY)

            # Add the marker to the list
            markers.append(marker)

        return markers