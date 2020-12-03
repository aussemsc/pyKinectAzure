# -*- coding: utf-8 -*-
"""
Created on Wed Nov 25 12:38:45 2020

@author: Camille
"""

import ctypes
# from _k4atypes import *

class _handle_k4a_playback_t(ctypes.Structure):
    _fields_= [
        ("_rsvd", ctypes.c_size_t),
    ]
k4a_playback_t = ctypes.POINTER(_handle_k4a_playback_t)

class _handle_k4a_record_t(ctypes.Structure):
    _fields_= [
        ("_rsvd", ctypes.c_size_t),
    ]
k4a_record_t = ctypes.POINTER(_handle_k4a_record_t)
class _handle_k4a_playback_data_block_t(ctypes.Structure):
    _fields_= [
        ("_rsvd", ctypes.c_size_t),
    ]
k4a_playback_data_block_t = ctypes.POINTER(_handle_k4a_playback_data_block_t)

K4A_TRACK_NAME_COLOR = "COLOR"
K4A_TRACK_NAME_DEPTH = "DEPTH"
K4A_TRACK_NAME_IR = "IR"
K4A_TRACK_NAME_IMU = "IMU"

#class k4a_stream_result_t(CtypeIntEnum)
k4a_stream_result_t = ctypes.c_int
K4A_STREAM_RESULT_SUCCEEDED = 0
K4A_STREAM_RESULT_FAILED = 1
K4A_STREAM_RESULT_EOF = 2

# class k4a_playback_seek_origin_t(CtypeIntEnum)
k4a_playback_seek_origin_t = ctypes.c_int32
K4A_PLAYBACK_SEEK_BEGIN = 0
K4A_PLAYBACK_SEEK_END = 1
K4A_PLAYBACK_SEEK_DEVICE_TIME = 2


class _k4a_record_configuration_t(ctypes.Structure):
    _fields_= [
        ("color_format", ctypes.c_int),
		("color_resolution", ctypes.c_int),
		("depth_mode", ctypes.c_int),
		("camera_fps", ctypes.c_int),
        ("color_track_enabled", ctypes.c_bool),
        ("depth_track_enabled", ctypes.c_bool),
        ("ir_track_enabled", ctypes.c_bool),
        ("imu_track_enabled", ctypes.c_bool),
        ("depth_delay_off_color_usec", ctypes.c_int32),
		("wired_sync_mode", ctypes.c_int),
		("subordinate_delay_off_master_usec", ctypes.c_uint32),
		("disable_streaming_indicator", ctypes.c_bool),
        ]
k4a_record_configuration_t = _k4a_record_configuration_t

class _k4a_record_video_settings_t(ctypes.Structure):
    _fields_= [
        ("width", ctypes.c_uint64),
        ("height", ctypes.c_uint64),
        ("frame_rate", ctypes.c_uint64),
        ]
k4a_record_video_settings_t = _k4a_record_video_settings_t

class _k4a_record_subtitle_settings_t(ctypes.Structure):
    _fields_= [
        ("high_freq_data", ctypes.c_bool),
        ]
k4a_record_subtitle_settings_t = _k4a_record_subtitle_settings_t

