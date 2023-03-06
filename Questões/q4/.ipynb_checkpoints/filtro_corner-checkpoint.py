#!/usr/bin/python
# -*- coding: utf-8 -*-

import cv2
import sys

if __name__ == "__main__":

        file = cv2.imread("cross.png")
    
        bgr = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR) 
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Display the resulting frame
        # cv2.imshow('frame',frame)
        cv2.imshow('frame', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # When everything done, release the capture
    cap.release()
    cv2.destroyAllWindows()

