  
# Mirao 52e ERROR codes:
# Error codes (status)
errors = {}
errors[0] = 'MRO_OK, No error'
errors[1] = 'MRO_UNKNOWN_ERROR'
errors[2] = 'MRO_DEVICE_NOT_OPENED_ERROR, mirao 52-e is not opened.'
errors[3] = 'MRO_DEFECTIVE_DEVICE_ERROR, mirao 52-e has been identified as defective.'
errors[4] = 'MRO_DEVICE_ALREADY_OPENED_ERROR, mirao 52-e is already opened.'
errors[5] = 'MRO_DEVICE_IO_ERROR, a communication error has been detected.'
errors[6] = 'MRO_DEVICE_LOCKED_ERROR, a temperature overheat or an excess of current has lead mirao 52-e to a protection state.'
errors[7] = 'MRO_DEVICE_DISCONNECTED_ERROR'
errors[8] = 'MRO_DEVICE_DRIVER_ERROR, an internal driver malfunction'
errors[9] = 'MRO_FILE_EXISTS_ERROR, the file to write already exists and its not allowed to overwrite it.'
errors[10] = 'MRO_FILE_FORMAT_ERROR, the considered file is corrupted or has not a valid file format.'
errors[11] = 'MRO_FILE_IO_ERROR, an error has been detected while reading/writing a file.'
errors[12] = 'MRO_INVALID_COMMAND_ERROR, there are two possibilities: \
(1) A least one of the values of the command is out of specification (value > 1.0 or value < -1.0).\
(2) The sum of the absolute values of the command values is greater than 25.0.'
errors[13] = 'MRO_NULL_POINTER_ERROR, a null pointer has been identified as a parameter which cannot be null.'
errors[14] = 'MRO_OUT_OF_BOUNDS_ERROR, this happens when an index parameter is out of its possible values.'
errors[15] = 'MRO_OPERATION_ONGOING_ERROR, operation already in progress. The requested operation cannot be performed due to a synchronization lock.'
errors[16] = 'MRO_SYSTEM_ERROR, An error has been detected while calling the operating system.'
errors[17] = 'MRO_UNAVAILABLE_DATA_ERROR, The requested data is unavailable.\
This can be due to the call of an unavailable functionality or a functionality that needs monitoring to be enabled.'
errors[18] = 'MRO_UNDEFINED_VALUE_ERROR, The requested value is not available. Ex: request of an undefined stock command value.'
errors[19] = 'MRO_OUT_OF_SPECIFICATIONS_ERROR, The value, which is not an index, is out of allowed values.'
errors[20] = 'MRO_FILE_FORMAT_VERSION_ERROR, The file format version is not supported. \
The version of the MRO file format is not handled by this mirao 52-e API.'
errors[21] = 'MRO_USB_INVALID_HANDLE, This error implies either an operating system error or an internal driver error.'
errors[22] = 'MRO_USB_DEVICE_NOT_FOUND, mirao 52-e cannot be found among the USB ports. There may be several possibilities:\
(1) The device is not connected to the computer or the connection is defective, \
(2) The USB port is not correctly installed in the operating system,\
(3) The mirao 52-e device is not turned ON, \
(4) The mirao 52-e device is already opened by another process, \
(5) The mirao 52-e device is defective.'
errors[23] = 'MRO_USB_DEVICE_NOT_OPENED, Internal driver not opened. This error implies an operating system error.'
errors[24] = 'MRO_USB_IO_ERROR, Internal driver IO error. The internal driver encountered a problem for reading from \
or writing to the hardware device.'
errors[25] = 'MRO_USB_INSUFFICIENT_RESOURCES, There are insufficient system resources to perform the requested operation.'
errors[26] = 'MRO_USB_INVALID_BAUD_RATE, The configuration of the connection speed is not supported.'
errors[27] = 'MRO_USB_NOT_SUPPORTED, A functionnality is not supported by the internal driver. \
Implies an operating system error perhaps due to a bad USB driver version.'
errors[28] = 'MRO_FILE_IO_EACCES, Permission denied. A file cannot be accessed due to a permission denied error.'
errors[29] = 'MRO_FILE_IO_EAGAIN, No more processes. An attempt to create a new process failed.'
errors[30] = 'MRO_FILE_IO_EBADF, Bad file number. An invalid internal file descriptor has been used. This is an operating system error.'
errors[31] = 'MRO_FILE_IO_EINVAL, An internal invalid argument has been used with a file IO function. This is an operating system error.'
errors[32] = 'MRO_FILE_IO_EMFILE, Too many opened files. The maximum number of open files allowed by the operating system has been reached.'
errors[33] = 'MRO_FILE_IO_ENOENT, No such file or directory. The considered file or directory does not exists.'
errors[34] = 'MRO_FILE_IO_ENOMEM, Not enough memory. The operation requested cannot be performed because the process is out of memory.'
errors[35] = 'MRO_FILE_IO_ENOSPC, No space left on device. A file cannot be written because the hard drive lacks of space.'

def read_Mirao_commandFile(path, driver):
    '''
    Reads 52 double values from .MRO file using Mirao52e.dll API. 
    Run 
        import ctypes 
        driver = ctypes.windll.mirao52e 
    to open driver (dll) session.
    '''
    import ctypes
    import numpy as np
    import os
    byref = ctypes.byref
    status  = ctypes.c_int32() 
    path = path.replace('/', '\\')
    Cpath = ctypes.c_char_p(path)
    cmd = np.zeros(52,dtype = np.float64)
    if os.path.exists(path):
        assert driver.mro_readCommandFile(Cpath,cmd.ctypes.data,byref(status)), errors[status.value]
    else:
        print('Error: command file not found')
    return cmd
    
def DM_voltage_to_map(v):
    """
    Reshape the 52-long vector v into 2D matrix representing the actual DM aperture.
    Corners of the matrix are set to None for plotting.
    Parameters:
    v - double array of length 52
    
    Returns:
    output: 8x8 ndarray of doubles.
    -------
    Author: Nikita Vladimirov
    """
    import numpy as np
    M = np.zeros((8,8))
    M[:,:] = None
    M[2:6,0] = v[:4]
    M[1:7,1] = v[4:10]
    M[:,2] = v[10:18]
    M[:,3] = v[18:26]
    M[:,4] = v[26:34]
    M[:,5] = v[34:42]
    M[1:7,6] = v[42:48]
    M[2:6,7] = v[48:52]
    return M