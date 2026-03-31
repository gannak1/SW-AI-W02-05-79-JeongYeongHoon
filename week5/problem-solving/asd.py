from cpuinfo import get_cpu_info

info = get_cpu_info()

print(info.keys())
print(info['flags'])