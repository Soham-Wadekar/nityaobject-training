# KIWI NG Documentation

## Overview

**KIWI NG** is a powerful tool for building **Linux system images**. It supports a wide range of image formats including:

- Virtual machine images (QEMU/KVM, VMWare, etc.)
- Live ISO images (like bootable CDs/DVDs)
- Cloud images (like AWS AMIs)
- Disk images for bare-metal systems

KIWI NG is mainly used by Linux distributions like **openSUSE** and **SUSE Linux Enterprise** to create and manage OS images in an automated and repeatable way.

---

## What is KIWI NG?

- **KIWI NG** is the **next-generation** version of the older **KIWI** tool.
- It's written in **Python** and maintained by the openSUSE Project.
- It allows developers and system administrators to define an entire operating system image using simple configuration files.

---

## Key Use Cases

- Creating bootable USB or ISO images
- Building virtual machine images for QEMU/KVM, VMware, etc.
- Generating minimal cloud images (e.g., for AWS, Azure)
- Creating reproducible custom Linux systems (e.g., routers, kiosks, embedded)

---

## Installation
- Create a python virtual environment and clone the kiwi repository inside it

```python
# Create a python virtual environment
python -m venv kiwi-env

# Clone the kiwi git repository inside
git clone https://github.com/OSInside/kiwi

```
