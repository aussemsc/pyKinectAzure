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

class k4aplayback:

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
        K4ARECORD_EXPORT k4a_result_t k4a_playback_open(const char *path, 
                                                         k4a_playback_t *playback_handle);
        """
        
        self.k4a_playback_open = dll.k4a_playback_open
        self.k4a_playback_open.restype = k4a_result_t
        self.k4a_playback_open.argtypes = (ctypes.POINTER(ctypes.c_char), \
                                          ctypes.POINTER(k4a_playback_t),)
        
        """
        K4ARECORD_EXPORT k4a_buffer_result_t k4a_playback_get_raw_calibration(k4a_playback_t playback_handle,
                                                                      uint8_t *data,
                                                                      size_t *data_size);
        """
        self.k4a_playback_get_raw_calibration = dll.k4a_playback_get_raw_calibration
        self.k4a_playback_get_raw_calibration.restype = k4a_buffer_result_t
        self.k4a_playback_get_raw_calibration.argtypes = (k4a_playback_t, \
                                                        ctypes.POINTER(ctypes.c_uint), \
                                                        ctypes.POINTER(ctypes.c_size_t))
            
        """
        K4ARECORD_EXPORT k4a_result_t k4a_playback_get_calibration(k4a_playback_t playback_handle,
                                                           k4a_calibration_t *calibration);
        """
        self.k4a_playback_get_calibration = dll.k4a_playback_get_calibration
        self.k4a_playback_get_calibration.restype = k4a_result_t
        self.k4a_playback_get_calibration.argtypes = (k4a_playback_t, \
                                                     ctypes.POINTER(k4a_calibration_t))
            
        """
        K4ARECORD_EXPORT k4a_result_t k4a_playback_get_record_configuration(k4a_playback_t playback_handle,
                                                                    k4a_record_configuration_t *config);
        """
        self.k4a_playback_get_record_configuration = dll.k4a_playback_get_record_configuration
        self.k4a_playback_get_record_configuration.restype = k4a_result_t
        self.k4a_playback_get_record_configuration.argtypes = (k4a_playback_t, \
                                                              ctypes.POINTER(k4a_record_configuration_t))
            
        """
        K4ARECORD_EXPORT bool k4a_playback_check_track_exists(k4a_playback_t playback_handle, const char *track_name);
        """
        self.k4a_playback_check_track_exists = dll.k4a_playback_check_track_exists
        self.k4a_playback_check_track_exists.restype = ctypes.c_bool
        self.k4a_playback_check_track_exists.argtypes = (k4a_playback_t, \
                                                        ctypes.POINTER(ctypes.c_char))
        
        """
        K4ARECORD_EXPORT size_t k4a_playback_get_track_count(k4a_playback_t playback_handle);
        """
        self.k4a_playback_get_track_count = dll.k4a_playback_get_track_count
        self.k4a_playback_get_track_count.restype = ctypes.c_size_t
        self.k4a_playback_get_track_count.argtypes = (k4a_playback_t,)
        
        """
        K4ARECORD_EXPORT k4a_buffer_result_t k4a_playback_get_track_name(k4a_playback_t playback_handle,
                                                                 size_t track_index,
                                                                 char *track_name,
                                                                 size_t *track_name_size);
        """
        self.k4a_playback_get_track_name = dll.k4a_playback_get_track_name
        self.k4a_playback_get_track_name.restype = k4a_buffer_result_t
        self.k4a_playback_get_track_name.argtypes = (k4a_playback_t, \
                                                    ctypes.c_size_t, \
                                                    ctypes.POINTER(ctypes.c_char), \
                                                    ctypes.POINTER(ctypes.c_size_t),)
            
        """
        K4ARECORD_EXPORT bool k4a_playback_track_is_builtin(k4a_playback_t playback_handle, const char *track_name);
        """
        self.k4a_playback_track_is_builtin = dll.k4a_playback_track_is_builtin
        self.k4a_playback_track_is_builtin.restype = ctypes.c_bool
        self.k4a_playback_track_is_builtin.argtypes = (k4a_playback_t, \
                                                      ctypes.POINTER(ctypes.c_char),)
            
        """
        K4ARECORD_EXPORT k4a_result_t k4a_playback_track_get_video_settings(k4a_playback_t playback_handle,
                                                                    const char *track_name,
                                                                    k4a_record_video_settings_t *video_settings);
        """
        self.k4a_playback_track_get_video_settings = dll.k4a_playback_track_get_video_settings
        self.k4a_playback_track_get_video_settings.restype = k4a_result_t
        self.k4a_playback_track_get_video_settings.argtypes = (k4a_playback_t, \
                                                            ctypes.POINTER(ctypes.c_char), \
                                                            ctypes.POINTER(k4a_record_video_settings_t),)
            
        """
        K4ARECORD_EXPORT k4a_buffer_result_t k4a_playback_track_get_codec_id(k4a_playback_t playback_handle,
                                                                     const char *track_name,
                                                                     char *codec_id,
                                                                     size_t *codec_id_size);
        """
        self.k4a_playback_track_get_codec_id = dll.k4a_playback_track_get_codec_id
        self.k4a_playback_track_get_codec_id.restype = k4a_buffer_result_t
        self.k4a_playback_track_get_codec_id.argtypes = (k4a_playback_t, \
                                                            ctypes.POINTER(ctypes.c_char), \
                                                            ctypes.POINTER(ctypes.c_char), \
                                                            ctypes.POINTER(ctypes.c_size_t),)
            
        """
        K4ARECORD_EXPORT k4a_buffer_result_t k4a_playback_track_get_codec_context(k4a_playback_t playback_handle,
                                                                          const char *track_name,
                                                                          uint8_t *codec_context,
                                                                          size_t *codec_context_size);
        """
        self.k4a_playback_track_get_codec_context = dll.k4a_playback_track_get_codec_context
        self.k4a_playback_track_get_codec_context.restype = k4a_buffer_result_t
        self.k4a_playback_track_get_codec_context.argtypes = (k4a_playback_t, \
                                                            ctypes.POINTER(ctypes.c_char), \
                                                            ctypes.POINTER(ctypes.c_uint8), \
                                                            ctypes.POINTER(ctypes.c_size_t),)
        
        """
        K4ARECORD_EXPORT k4a_buffer_result_t k4a_playback_get_tag(k4a_playback_t playback_handle,
                                                          const char *name,
                                                          char *value,
                                                          size_t *value_size);
        """
        self.k4a_playback_get_tag = dll.k4a_playback_get_tag
        self.k4a_playback_get_tag.restype = k4a_buffer_result_t
        self.k4a_playback_get_tag.argtypes = (k4a_playback_t, \
                                              ctypes.POINTER(ctypes.c_char), \
                                            ctypes.POINTER(ctypes.c_char), \
                                            ctypes.POINTER(ctypes.c_size_t),)
            
        """
        K4ARECORD_EXPORT k4a_result_t k4a_playback_set_color_conversion(k4a_playback_t playback_handle,
                                                                k4a_image_format_t target_format);
        """
        self.k4a_playback_set_color_conversion = dll.k4a_playback_set_color_conversion
        self.k4a_playback_set_color_conversion.restype = k4a_result_t
        self.k4a_playback_set_color_conversion.argtypes = (k4a_playback_t, \
                                                           k4a_image_format_t)
            
        """
        K4ARECORD_EXPORT k4a_buffer_result_t k4a_playback_get_attachment(k4a_playback_t playback_handle,
                                                                 const char *file_name,
                                                                 uint8_t *data,
                                                                 size_t *data_size);
        """
        self.k4a_playback_get_attachment = dll.k4a_playback_get_attachment
        self.k4a_playback_get_attachment.restype = k4a_buffer_result_t
        self.k4a_playback_get_attachment.argtypes = (k4a_playback_t, \
                                                ctypes.POINTER(ctypes.c_char), \
                                                ctypes.POINTER(ctypes.c_uint8), \
                                                ctypes.POINTER(ctypes.c_size_t),)
            
        """
        K4ARECORD_EXPORT k4a_stream_result_t k4a_playback_get_next_capture(k4a_playback_t playback_handle,
                                                                   k4a_capture_t *capture_handle);
        """
        self.k4a_playback_get_next_capture = dll.k4a_playback_get_next_capture
        self.k4a_playback_get_next_capture.restype = k4a_stream_result_t
        self.k4a_playback_get_next_capture.argtypes = (k4a_playback_t, \
                                                      ctypes.POINTER(k4a_capture_t))
        
        """
        K4ARECORD_EXPORT k4a_stream_result_t k4a_playback_get_previous_capture(k4a_playback_t playback_handle,
                                                                       k4a_capture_t *capture_handle);
        """
        self.k4a_playback_get_previous_capture = dll.k4a_playback_get_previous_capture
        self.k4a_playback_get_previous_capture.restype = k4a_stream_result_t
        self.k4a_playback_get_previous_capture.argtypes = (k4a_playback_t, \
                                                           ctypes.POINTER(k4a_capture_t))
            
        """
        K4ARECORD_EXPORT k4a_stream_result_t k4a_playback_get_next_imu_sample(k4a_playback_t playback_handle,
                                                                      k4a_imu_sample_t *imu_sample);
        """
        self.k4a_playback_get_next_imu_sample = dll.k4a_playback_get_next_imu_sample
        self.k4a_playback_get_next_imu_sample.restype = k4a_stream_result_t
        self.k4a_playback_get_next_imu_sample.argtypes = (k4a_playback_t, \
                                                        ctypes.POINTER(k4a_imu_sample_t))
            
        """
        K4ARECORD_EXPORT k4a_stream_result_t k4a_playback_get_previous_imu_sample(k4a_playback_t playback_handle,
                                                                          k4a_imu_sample_t *imu_sample);
        """
        self.k4a_playback_get_previous_imu_sample = dll.k4a_playback_get_previous_imu_sample
        self.k4a_playback_get_previous_imu_sample.restype = k4a_stream_result_t
        self.k4a_playback_get_previous_imu_sample.argtypes = (k4a_playback_t, \
                                                        ctypes.POINTER(k4a_imu_sample_t))
         
        """
        K4ARECORD_EXPORT k4a_stream_result_t k4a_playback_get_next_data_block(k4a_playback_t playback_handle,
                                                                      const char *track_name,
                                                                      k4a_playback_data_block_t *data_block_handle);
        """
        self.k4a_playback_get_next_data_block = dll.k4a_playback_get_next_data_block
        self.k4a_playback_get_next_data_block.restype = k4a_stream_result_t
        self.k4a_playback_get_next_data_block.argtypes = (k4a_playback_t, \
                                                        ctypes.POINTER(ctypes.c_char), \
                                                        ctypes.POINTER(k4a_playback_data_block_t),)
        
        """
        K4ARECORD_EXPORT k4a_stream_result_t k4a_playback_get_previous_data_block(k4a_playback_t playback_handle,
                                                                          const char *track_name,
                                                                          k4a_playback_data_block_t *data_block_handle);
        """
        self.k4a_playback_get_previous_data_block = dll.k4a_playback_get_previous_data_block
        self.k4a_playback_get_previous_data_block.restype = k4a_stream_result_t
        self.k4a_playback_get_previous_data_block.argtypes = (k4a_playback_t, \
                                                        ctypes.POINTER(ctypes.c_char), \
                                                        ctypes.POINTER(k4a_playback_data_block_t),)
        
        """
        K4ARECORD_EXPORT uint64_t
        k4a_playback_data_block_get_device_timestamp_usec(k4a_playback_data_block_t data_block_handle);
        """
        self.k4a_playback_data_block_get_device_timestamp_usec = dll.k4a_playback_data_block_get_device_timestamp_usec
        self.k4a_playback_data_block_get_device_timestamp_usec.restype = ctypes.c_uint64
        self.k4a_playback_data_block_get_device_timestamp_usec.argtypes = (k4a_playback_data_block_t,)
        
        """
        K4ARECORD_EXPORT size_t k4a_playback_data_block_get_buffer_size(k4a_playback_data_block_t data_block_handle);
        """
        self.k4a_playback_data_block_get_buffer_size = dll.k4a_playback_data_block_get_buffer_size
        self.k4a_playback_data_block_get_buffer_size.restype = ctypes.c_size_t
        self.k4a_playback_data_block_get_buffer_size.argtypes = (k4a_playback_data_block_t,)
        
        """
        K4ARECORD_EXPORT uint8_t *k4a_playback_data_block_get_buffer(k4a_playback_data_block_t data_block_handle);
        """
        self.k4a_playback_data_block_get_buffer = dll.k4a_playback_data_block_get_buffer
        self.k4a_playback_data_block_get_buffer.restype = ctypes.POINTER(ctypes.c_uint8)
        self.k4a_playback_data_block_get_buffer.argtypes = (k4a_playback_data_block_t,)
        
        """
        K4ARECORD_EXPORT void k4a_playback_data_block_release(k4a_playback_data_block_t data_block_handle);
        """
        self.k4a_playback_data_block_release = dll.k4a_playback_data_block_release
        self.k4a_playback_data_block_release.restype = None
        self.k4a_playback_data_block_release.argtypes = (k4a_playback_data_block_t,)
        
        """
        K4ARECORD_EXPORT k4a_result_t k4a_playback_seek_timestamp(k4a_playback_t playback_handle,
                                                          int64_t offset_usec,
                                                          k4a_playback_seek_origin_t origin);
        """
        self.k4a_playback_seek_timestamp = dll.k4a_playback_seek_timestamp
        self.k4a_playback_seek_timestamp.restype = k4a_result_t
        self.k4a_playback_seek_timestamp.argtypes = (k4a_playback_t, \
                                                    ctypes.c_int64, \
                                                    k4a_playback_seek_origin_t,)
            
        """
        K4ARECORD_EXPORT uint64_t k4a_playback_get_recording_length_usec(k4a_playback_t playback_handle);
        """
        self.k4a_playback_get_recording_length_usec = dll.k4a_playback_get_recording_length_usec
        self.k4a_playback_get_recording_length_usec.restype = ctypes.c_uint64
        self.k4a_playback_get_recording_length_usec.argtypes = (k4a_playback_t,)
        
        """
        K4ARECORD_DEPRECATED_EXPORT uint64_t k4a_playback_get_last_timestamp_usec(k4a_playback_t playback_handle);
        """
        self.k4a_playback_get_last_timestamp_usec = dll.k4a_playback_get_last_timestamp_usec
        self.k4a_playback_get_last_timestamp_usec.restype = ctypes.c_uint64
        self.k4a_playback_get_last_timestamp_usec.argtypes = (k4a_playback_t,)
        
        """
        K4ARECORD_EXPORT void k4a_playback_close(k4a_playback_t playback_handle);
        """
        self.k4a_playback_close = dll.k4a_playback_close
        self.k4a_playback_close.restype = None
        self.k4a_playback_close.argtypes = (k4a_playback_t,)
        
def VERIFY(result, error):
    if result != K4A_RESULT_SUCCEEDED:
        print(error)
        traceback.print_stack()
        sys.exit(1)