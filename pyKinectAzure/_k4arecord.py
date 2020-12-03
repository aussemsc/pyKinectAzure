# -*- coding: utf-8 -*-
"""
Created on Wed Nov 25 12:33:00 2020

@author: Camille
"""
import ctypes
import sys
from _k4arecordtypes import *
from _k4atypes import *
import traceback

class k4arecord:

    def __init__(self,modulePath):
        try: 
            dll = ctypes.CDLL(modulePath)

        except Exception as e:

            if e.winerror == 193:
                print("Failed to load library. \n\nChange the module path to the 32 bit version.")
                sys.exit(1)

            print(e, "\n\nFailed to lad Windows library. Trying to load Linux library...\n")

            try:
                dll = ctypes.CDLL('k4arecord.so')
            except Exception as ee:
                print("Failed to load library", ee)
                sys.exit(1)
        """
        K4ARECORD_EXPORT k4a_result_t k4a_record_create(const char *path,
                                                k4a_device_t device,
                                                const k4a_device_configuration_t device_config,
                                                k4a_record_t *recording_handle);
        """
        self.k4a_record_create = dll.k4a_record_create
        self.k4a_record_create.restype = k4a_result_t
        self.k4a_record_create.argtypes = (ctypes.POINTER(ctypes.c_char), \
                                        k4a_device_t, \
                                        k4a_device_configuration_t, \
                                        ctypes.POINTER(k4a_record_t))
            
        """
        K4ARECORD_EXPORT k4a_result_t k4a_record_add_tag(k4a_record_t recording_handle, const char *name, const char *value);
        """
        self.k4a_record_add_tag = dll.k4a_record_add_tag
        self.k4a_record_add_tag.restype = k4a_result_t
        self.k4a_record_add_tag.argtypes = (k4a_record_t, \
                                        ctypes.POINTER(ctypes.c_char), \
                                        ctypes.POINTER(ctypes.c_char),)
            
        """
        K4ARECORD_EXPORT k4a_result_t k4a_record_add_imu_track(k4a_record_t recording_handle);
        """
        self.k4a_record_add_imu_track = dll.k4a_record_add_imu_track
        self.k4a_record_add_imu_track.restype = k4a_result_t
        self.k4a_record_add_imu_track.argtypes = (k4a_record_t,)
        
        """
        K4ARECORD_EXPORT k4a_result_t k4a_record_add_attachment(const k4a_record_t recording_handle,
                                                        const char *attachment_name,
                                                        const uint8_t *buffer,
                                                        size_t buffer_size);
        """
        self.k4a_record_add_attachment = dll.k4a_record_add_attachment
        self.k4a_record_add_attachment.restype = k4a_result_t
        self.k4a_record_add_attachment.argtypes = (k4a_record_t, \
                                                ctypes.POINTER(ctypes.c_char), \
                                                ctypes.POINTER(ctypes.c_uint8), \
                                                ctypes.c_size_t)
            
        """
        K4ARECORD_EXPORT k4a_result_t k4a_record_add_custom_video_track(const k4a_record_t recording_handle,
                                                                const char *track_name,
                                                                const char *codec_id,
                                                                const uint8_t *codec_context,
                                                                size_t codec_context_size,
                                                                const k4a_record_video_settings_t *track_settings);
        """
        self.k4a_record_add_custom_video_track = dll.k4a_record_add_custom_video_track
        self.k4a_record_add_custom_video_track.restype = k4a_result_t
        self.k4a_record_add_custom_video_track.argtypes = (k4a_record_t, \
                                                        ctypes.POINTER(ctypes.c_char), \
                                                        ctypes.POINTER(ctypes.c_char), \
                                                        ctypes.POINTER(ctypes.c_uint8), \
                                                        ctypes.c_size_t, \
                                                        ctypes.POINTER(k4a_record_video_settings_t),)
            
        """
        K4ARECORD_EXPORT k4a_result_t
        k4a_record_add_custom_subtitle_track(const k4a_record_t recording_handle,
                                     const char *track_name,
                                     const char *codec_id,
                                     const uint8_t *codec_context,
                                     size_t codec_context_size,
                                     const k4a_record_subtitle_settings_t *track_settings);
        """
        self.k4a_record_add_custom_subtitle_track = dll.k4a_record_add_custom_subtitle_track
        self.k4a_record_add_custom_subtitle_track.restype = k4a_result_t
        self.k4a_record_add_custom_subtitle_track.argtypes = (k4a_record_t, \
                                                        ctypes.POINTER(ctypes.c_char), \
                                                        ctypes.POINTER(ctypes.c_char), \
                                                        ctypes.POINTER(ctypes.c_uint8), \
                                                        ctypes.c_size_t, \
                                                        ctypes.POINTER(k4a_record_video_settings_t),)
    
        """
        K4ARECORD_EXPORT k4a_result_t k4a_record_write_header(k4a_record_t recording_handle);
        """
        self.k4a_record_write_header = dll.k4a_record_write_header
        self.k4a_record_write_header.restype = k4a_result_t
        self.k4a_record_write_header.argtypes = (k4a_record_t,)
        
        """
        K4ARECORD_EXPORT k4a_result_t k4a_record_write_capture(k4a_record_t recording_handle, k4a_capture_t capture_handle);
        """
        self.k4a_record_write_capture = dll.k4a_record_write_capture
        self.k4a_record_write_capture.restype = k4a_result_t
        self.k4a_record_write_capture.argtypes = (k4a_record_t, k4a_capture_t)
        
        """
        K4ARECORD_EXPORT k4a_result_t k4a_record_write_imu_sample(k4a_record_t recording_handle, k4a_imu_sample_t imu_sample);
        """
        self.k4a_record_write_imu_sample = dll.k4a_record_write_imu_sample
        self.k4a_record_write_imu_sample.restype = k4a_result_t
        self.k4a_record_write_imu_sample.argtypes = (k4a_record_t, k4a_imu_sample_t)
        
        """
        K4ARECORD_EXPORT k4a_result_t k4a_record_write_custom_track_data(const k4a_record_t recording_handle,
                                                                 const char *track_name,
                                                                 uint64_t device_timestamp_usec,
                                                                 uint8_t *custom_data,
                                                                 size_t custom_data_size);
        """
        self.k4a_record_write_custom_track_data = dll.k4a_record_write_custom_track_data
        self.k4a_record_write_custom_track_data.restype = k4a_result_t
        self.k4a_record_write_custom_track_data.argtypes = (k4a_record_t, \
                                                        ctypes.POINTER(ctypes.c_char), \
                                                        ctypes.c_uint64, \
                                                        ctypes.POINTER(ctypes.c_uint8), \
                                                        ctypes.c_size_t)
        
        """
        K4ARECORD_EXPORT k4a_result_t k4a_record_flush(k4a_record_t recording_handle);
        """
        self.k4a_record_flush = dll.k4a_record_flush
        self.k4a_record_flush.restype = k4a_result_t
        self.k4a_record_flush.argtypes = (k4a_record_t,)
        
        """
        K4ARECORD_EXPORT void k4a_record_close(k4a_record_t recording_handle);
        """
        self.k4a_record_close = dll.k4a_record_close
        self.k4a_record_close.restype = None
        self.k4a_record_close.argtypes = (k4a_record_t,)
        
def VERIFY(result, error):
    if result != K4A_RESULT_SUCCEEDED:
        print(error)
        traceback.print_stack()
        sys.exit(1)