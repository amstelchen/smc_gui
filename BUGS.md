### Misc distros

```
$ smc-gui 
qt.qpa.plugin: From 6.5.0, xcb-cursor0 or libxcb-cursor0 is needed to load the Qt xcb platform plugin.
qt.qpa.plugin: Could not load the Qt platform plugin "xcb" in "" even though it was found.
This application failed to start because no Qt platform plugin could be initialized. Reinstalling the application may fix this problem.

Available platform plugins are: eglfs, vkkhrdisplay, offscreen, minimalegl, linuxfb, vnc, minimal, wayland-egl, wayland, xcb.

Abgebrochen
$
```

### MocaccinoOS

```
$ smc-gui 
MESA-LOADER: failed to open zink: /usr/lib64/dri/zink_dri.so: cannot open shared object file: No such file or directory (search paths /usr/lib64/dri, suffix _dri)
failed to load driver: zink
spectre-meltdown-checker GUI 0.1.2
Copyright (C) 2023, 2024, by Michael John
^C
```

```
$ uname -a
Linux moc 6.1.72-mocaccino #6.1.72-Mocaccino SMP PREEMPT_DYNAMIC Wed Jan 10 23:47:48 UTC 20 x86_64 AMD Ryzen 7 5700G with Radeon Graphics AuthenticAMD GNU/Linux
```

```
$ glxinfo | grep OpenGL
MESA-LOADER: failed to open zink: /usr/lib64/dri/zink_dri.so: cannot open shared object file: No such file or directory (search paths /usr/lib64/dri, suffix _dri)
failed to load driver: zink
OpenGL vendor string: Mesa
OpenGL renderer string: llvmpipe (LLVM 17.0.6, 256 bits)
OpenGL core profile version string: 4.5 (Core Profile) Mesa 23.3.3
OpenGL core profile shading language version string: 4.50
OpenGL core profile context flags: (none)
OpenGL core profile profile mask: core profile
OpenGL core profile extensions:
OpenGL version string: 4.5 (Compatibility Profile) Mesa 23.3.3
OpenGL shading language version string: 4.50
OpenGL context flags: (none)
OpenGL profile mask: compatibility profile
OpenGL extensions:
OpenGL ES profile version string: OpenGL ES 3.2 Mesa 23.3.3
OpenGL ES profile shading language version string: OpenGL ES GLSL ES 3.20
OpenGL ES profile extensions:
```

### openSUSE Tumbleweed

spectre-meltdown-checker comes packaged spectre-meltdown-checker.sh

### Void Linux

```
$ python3 -m pip install smc_gui-0.1.2-py3-none-any.whl
Defaulting to user installation because normal site-packages is not writeable
Processing ./smc_gui-0.1.2-py3-none-any.whl
Collecting pyside6>=6.2 (from smc-gui==0.1.2)
  Using cached PySide6-6.6.1-cp38-abi3-manylinux_2_28_x86_64.whl.metadata (5.3 kB)
INFO: pip is looking at multiple versions of smc-gui to determine which version is compatible with other requirements. This could take a while.
ERROR: Package 'smc-gui' requires a different Python: 3.12.2 not in '<3.12,>=3.8'
```

### elementary OS

```
$ smc-gui 
QApplication: invalid style override 'adwaita' passed, ignoring it.
	Available styles: Windows, Fusion
spectre-meltdown-checker GUI 0.1.2
Copyright (C) 2023, 2024, by Michael John
$ QT_STYLE_OVERRIDE="" smc-gui 
spectre-meltdown-checker GUI 0.1.2
Copyright (C) 2023, 2024, by Michael John
$ 
```