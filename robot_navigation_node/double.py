import cv2

def main():
    # Open the default camera (usually the first camera found)
    cap = cv2.VideoCapture()

    # Check if the camera opened successfully
    if not cap.isOpened():
        print("Error: Couldn't open camera.")
        return

    while True:
        # Capture frame-by-frame
        ret, frame = cap.read()

        # If frame is read correctly ret is True
        if not ret:
            print("Error: Can't receive frame (stream end?). Exiting...")
            break

        # Display the frame
        cv2.imshow('Webcam', frame)

        # Check for user input to exit the loop
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release the capture when done
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
