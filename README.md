# spectre-meltdown-checker GUI

### A simple GUI for spectre-meltdown-checker

*Meltdown* and *Spectre* are two significant security vulnerabilities that rocked the technology world when they were disclosed in early 2018. Both vulnerabilities affect the majority of modern microprocessors, including those made by Intel, AMD, and ARM.

Meltdown primarily targets Intel processors, while Spectre affects a wider range of chips, including those from AMD and ARM. These vulnerabilities exploit the fundamental design flaws in modern processors that allow malicious programs to access sensitive data in the computer's memory.

**spectre-meltdown-checker** is a shell script written and maintained by Stéphane Lesimple to assess your system's resilience against the several transient execution CVEs that were published since early 2018, and give you guidance as to how to mitigate them.

**spectre-meltdown-checker GUI** ist just a simple frontend for *spectre-meltdown-checker*.

#### Installation

Steps assume that `python` (>= 3.8) and `pip` are already installed.

Install dependencies (see sections below)

Then, run:

    $ pip install smc-gui

Install directly from ``github``:

    $ pip install git+https://github.com/amstelchen/smc_gui#egg=smc_gui

When completed, run it with:

    $ smc-gui

#### Dependencies

None, except [spectre-meltdown-checker](https://github.com/speed47/spectre-meltdown-checker).

**smc-gui** is tested to work on the following distributions:

- Debian 11.3 or newer 
- Ubuntu, Kubuntu, Xubuntu, Pop!_OS 20.04 or newer
- Linux Mint 21 or newer
- LMDE 6 or newer
- MX Linux 23 or newer
- Arch Linux (or any Arch based distribution like Manjaro, ArcoLinux, Garuda Linux, ...)
- Void Linux 
- Artix Linux
- openSUSE Tumbleweed
- Zorin OS 16.3 or newer
- EndeavourOS
- elementary OS
- Fedora 37 Workstation or newer 
- Slackware 64 14.2 and 15.0
- Gentoo Linux, MocaccinoOS

#### Reporting bugs

If you encounter any bugs or incompatibilities, __please report them [here](https://github.com/amstelchen/smc_gui/issues/new)__.

#### Enabling logging/debugging

```
$ smc-gui DEBUG
spectre-meltdown-checker GUI 0.1.2
Copyright (C) 2023, 2024, by Michael John
DEBUG:Reading /tmp/smc_output_nohw.txt...
DEBUG:Spectre and Meltdown mitigation detection tool v0.46
Kernel is Linux 6.7.3-arch1-1 #1 SMP PREEMPT_DYNAMIC Thu, 01 Feb 2024 10:30:35 +0000 x86_64
CPU is AMD Ryzen 7 5700G with Radeon Graphics

DEBUG:CVE-2017-5753 found in file.
DEBUG:CVE-2017-5715 found in file.
DEBUG:CVE-2017-5754 found in file.
DEBUG:CVE-2018-3640 found in file.
DEBUG:CVE-2018-3639 found in file.
DEBUG:CVE-2018-3615 found in file.
DEBUG:CVE-2018-3620 found in file.
DEBUG:CVE-2018-3646 found in file.
DEBUG:CVE-2018-12126 found in file.
DEBUG:CVE-2018-12130 found in file.
DEBUG:CVE-2018-12127 found in file.
DEBUG:CVE-2019-11091 found in file.
DEBUG:CVE-2019-11135 found in file.
DEBUG:CVE-2018-12207 found in file.
DEBUG:CVE-2020-0543 found in file.
DEBUG:CVE-2023-20593 found in file.
DEBUG:There were a total of 16 CVEs found in the file.
DEBUG:CVE-2017-5753 selected.
```

#### Licences

*smc-gui* is licensed under the [GPLv2](LICENSE) license.

<a href="https://www.flaticon.com/free-icons/computer" title="computer Icons">Computer Icons created by Freepik - Flaticon</a>
