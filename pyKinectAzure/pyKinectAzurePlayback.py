# -*- coding: utf-8 -*-
"""
Created on Fri Nov 27 14:00:35 2020

@author: Camille
"""
#API for the record class
import _k4a
import _k4aplayback
import numpy as np
import cv2
import sys
import ctypes
from config import config
import platform

class pyKinectAzurePlayback:

    def __init__(self,modulePath=None):
        if modulePath is None:
            if platform.system().lower() == 'linux':
                modulePath = r'/usr/lib/x86_64-linux-gnu/libk4a.so'
            else:
                modulePath = 'C:\\Program Files\\Azure Kinect SDK v1.4.0\\sdk\\windows-desktop\\amd64\\release\\bin\\k4arecord.dll'
        self.k4aplayback = _k4aplayback.k4aplayback(modulePath)
        
        self.playback_handle = _k4aplayback.k4a_playback_t()
        self.calibration_handle =_k4a.k4a_calibration_t()
        self.config = _k4aplayback.k4a_record_configuration_t()
        # self.config = self.get_record_configuration()

    def playback_open(self,filePath):
        """Opens an existing recording file for reading.

        Parameters:
        filePath: Path to the recording file
            
        Returns:
        None
        
        Remarks:
        If successful, this contains a pointer to the recording handle. Caller must call k4a_playback_close() when
        finished with the recording.
        """
        return _k4aplayback.VERIFY(self.k4aplayback.k4a_playback_open(filePath,self.playback_handle),"Opening recording failed!")
    
    def get_calibration(self):
        """Get the camera calibration for Azure Kinect device used during recording. The output struct is used as input to all
        transformation functions.

        Parameters:
        None
            
        Returns:
        None
        
        Remarks:
        If successful, this contains a pointer to the recording handle. Caller must call k4a_playback_close() when
        finished with the recording.
        """
        return _k4aplayback.VERIFY(self.k4aplayback.k4a_playback_get_calibration(self.playback_handle,self.calibration_handle),"Failed to retrieve calibration!!")
    
    def get_record_configuration(self):
        """Get the device configuration used during recording.

        Parameters:
        device_config:location to write the device configuration
            
        Returns:
        None
        
        Remarks:
        If successful, this contains a pointer to the recording handle. Caller must call k4a_playback_close() when
        finished with the recording.
        """
        return _k4aplayback.VERIFY(self.k4aplayback.k4a_playback_get_record_configuration(self.playback_handle,self.config),"Failed to retrieve configuration!!")
    
    def get_next_capture(self,capture_handle):
        """Read the next capture in the recording sequence.

        Parameters:
        capture_handle: Handle to an empty capture to write into
            
        Returns:
        None
        
        Remarks:
        Capture objects returned by the playback API will always contain at least one image, but may have images missing if
        frames were dropped in the original recording. When calling k4a_capture_get_color_image(),
        k4a_capture_get_depth_image(), or k4a_capture_get_ir_image(), the image should be checked for NULL.
        """
        return self.k4aplayback.k4a_playback_get_next_capture(self.playback_handle,capture_handle)
    
    def get_recording_length(self):
        """Gets the last timestamp in a recording, relative to the start of the recording.

        Parameters:
        None
            
        Returns:
        time in usec
        
        Remarks:
        This function returns a file timestamp, not an absolute device timestamp, meaning it is relative to the start of the
        recording. This function is equivalent to the length of the recording.
        """
        return self.k4aplayback.k4a_playback_get_recording_length_usec(self.playback_handle)
    
    def set_color_conversion(self,color_format):
        """Set the image format that color captures will be converted to. By default the conversion format will be the same as
        the image format stored in the recording file, and no conversion will occur.

        Parameters:
        color_format : format to convert the record into
            
        Returns:
        time in usec
        
        Remarks:
        After the color conversion format is set, all \ref k4a_capture_t objects returned from the playback handle will have
        their color images converted to the \p target_format.
        
        Color format conversion occurs in the user-thread, so setting \p target_format to anything other than the format
        stored in the file may significantly increase the latency of \p k4a_playback_get_next_capture() and
        \p k4a_playback_get_previous_capture().
        """
        return _k4aplayback.VERIFY(self.k4aplayback.k4a_playback_set_color_conversion(self.playback_handle,color_format),"Failed to change color format!!")
    
    def playback_close(self):
        """Close the playback once we are done with it

        Parameters:
            
        Returns:
        None
        
        Remarks:
        If successful, this contains a pointer to the recording handle. Caller must call k4a_playback_close() when
        finished with the recording.
        """
        self.k4aplayback.k4a_playback_close(self.playback_handle)
    
    def transformation_depth_image_to_point_cloud(self, input_depth_image_handle, calibration_type, pyK4A):
        device_calibration = _k4a.k4a_calibration_t()
        
        # Get desired image format
        image_format = _k4a.K4A_IMAGE_FORMAT_CUSTOM
        width = pyK4A.image_get_width_pixels(input_depth_image_handle)
        height = pyK4A.image_get_height_pixels(input_depth_image_handle)
        stride = 6*width
        
        # Get the camera calibration
        self.get_calibration()
        
        # Set the transformation handle
        transformation_handle = pyK4A.transformation_create(self.calibration_handle)
        
        # Create the image handle        
        transformed_depth_image_handle = _k4a.k4a_image_t()
        pyK4A.image_create(image_format,width,height,stride,transformed_depth_image_handle)
        
        # Define from which camera perspective we do the calibration, 
        #calibration_type = 1 # 0= depth, 1 = color
        pyK4A.k4a.k4a_transformation_depth_image_to_point_cloud(transformation_handle,input_depth_image_handle,calibration_type,transformed_depth_image_handle)
        
        #Get image size
        image_size = pyK4A.image_get_size(transformed_depth_image_handle)
        #Get pointer to start of image data
        buffer_pointer = pyK4A.image_get_buffer(transformed_depth_image_handle)
        #retrieve image data and put it into an array
        buffer_array = np.ctypeslib.as_array(buffer_pointer,shape=(image_size,))
        #Reinterpret the array as a 3D array with type int16
        xyz_cloud = np.frombuffer(buffer_array, dtype=np.int16).reshape(height,width,3)
        
        # Close transformation 
        pyK4A.transformation_destroy(transformation_handle)
        
        return xyz_cloud






    



