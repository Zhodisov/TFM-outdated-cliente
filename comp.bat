cython --embed -3 add.pyx

call "%ProgramFiles(x86)%\Microsoft Visual Studio\2019\BuildTools\VC\Auxiliary\Build\vcvarsall.bat" x86

cl add.c /MD /I "%ProgramFiles(x86)%\Python39\include" /link "%ProgramFiles(x86)%\Python39\libs\python39.lib"  "%WindowsSdkDir%Lib\%WindowsSDKVersion%um\%VSCMD_ARG_HOST_ARCH%\User32.lib" "%WindowsSdkDir%Lib\%WindowsSDKVersion%um\%VSCMD_ARG_HOST_ARCH%\Kernel32.lib"
