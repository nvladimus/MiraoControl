# MiraoControl
Control of Mirao52e deformable mirror (DM)

The code includes 
* control of Thorlabs WFS sensor, 
* measurement of DM response matrix, 
* SVD pseudo-inversion of the DM response matrix
* Open and closed-loop flattening of the DM surface, measured by the WFS sensor using a collimated HeNe 633 nm laser

Drivers of from your Mirao52e instllation DVD should be copied into `/lib/x64` and `/lib/x86` sub-folders (64-bit or 32-bit, respectively). 
The bitness (64 or 32) of your Python distribution *must* match the bitness of Thorlabs WFS and Mirao DM drivers you use. 
Both devices come with x32 and x64 drivers.
