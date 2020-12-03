# -*- coding: utf-8 -*-
"""
Created on Fri Nov 27 14:00:35 2020

@author: Camille
"""
#API for the record class
import _k4arecord
import sys
import ctypes
import platform

class pyKinectAzureRecord:

    def __init__(self,modulePath=None):
        if modulePath is None:
            if platform.system().lower() == 'linux':
                modulePath = r'/usr/lib/x86_64-linux-gnu/libk4a.so'
            else:
                modulePath = 'C:\\Program Files\\Azure Kinect SDK v1.4.0\\sdk\\windows-desktop\\amd64\\release\\bin\\k4arecord.dll'
        self.k4arecord = _k4arecord.k4arecord(modulePath)
        
        self.record_handle = _k4arecord.k4a_record_t()

    def record_create(self,filePath,device_handle,device_config):
        """Opens a new recording file for writing.

        Parameters:
        filePath: Path to the created file
        device_handle: device_handle obtained with device_open
        device_config: Handle of configuration obtained with device.config.current_config
            
        Returns:
        None
        
        Remarks:
        Streaming does not need to be started on the device at the time this function is called, but when it is started
        it should be started with the same configuration provided in \p device_config.
        
        When done with the recording call record_close
        """
        return _k4arecord.VERIFY(self.k4arecord.k4a_record_create(filePath,device_handle,device_config,self.record_handle),"Create recording failed!")
    
    def write_header(self):
        """Writes the recording header and metadata to file.

        Parameters:
        None
            
        Returns:
        None
        
        Remarks:
        This must be called before captures or any track data can be written.
        """
        return _k4arecord.VERIFY(self.k4arecord.k4a_record_write_header(self.record_handle),"Writing header failed!")
    
    def write_capture(self,capture_handle):
        """Writes a camera capture to file.

        Parameters:
        capture_handle: Handle to a capture obtained with k4a.capture_handle
            
        Returns:
        None
        
        Remarks:
        Captures must be written in increasing order of timestamp, and the file's header must already be written.
        k4a_record_write_capture() will write all images in the capture to the corresponding tracks in the recording file.
        If any of the images fail to write, other images will still be written before a failure is returned.
        """
        return _k4arecord.VERIFY(self.k4arecord.k4a_record_write_capture(self.record_handle,capture_handle),"Writing capture failed!")
    
    def record_close(self):
        """Closes a recording handle.

        Parameters:
        None
            
        Returns:
        None
        
        Remarks:
        If there is any unwritten data it will be flushed to disk before closing the recording.
        """
        return _k4arecord.VERIFY(self.k4arecord.k4a_record_close(self.record_handle),"Closing recording failed!")






    



