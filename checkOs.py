import platform

system = platform.system()
platform_info = platform.platform()

if system == "Windows":
    print(f"Current system is Windows: {platform_info}")
elif system == "Linux":
    print(f"Current system is Linux: {platform_info}")
else:
    print(f"Current system is not recognized as Windows or Linux: {platform_info}")
