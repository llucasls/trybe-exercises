#!/usr/bin/env python

from subprocess import check_output


# Processador
cpu_information = check_output("lscpu").decode("UTF-8").split("\n")
desired_cpu_information = {
    "model name": "Modelo",
    "cpu(s)": "Cores",
    "cpu mhz": "Velocidade (MHz)",
    "l1d": "Cache L1d",
    "l1i": "Cache L1i",
    "l2": "Cache L2",
    "l3": "Cache L3",
}
for desired_name, desired_description in desired_cpu_information.items():
    for information in cpu_information:
        if information.lower().startswith(desired_name):
            information = information.split("  ")  # 2 blank spaces
            information = information[-1].strip()
            print(f"{desired_description}: {information}")


# Memória

def get_info(entry):
    info_list = entry.split(" ")
    spaces = 0
    for value in info_list:
        if value == "":
            spaces += 1
    for index in range(spaces):
        info_list.remove("")
    return int(info_list[1])


command = ["head", "-5", "/proc/meminfo"]
memory_info = check_output(command).decode("UTF-8").split("\n")
mem_total = get_info(memory_info[0])
mem_free = get_info(memory_info[1])
mem_available = get_info(memory_info[2])
buffers = get_info(memory_info[3])
cached = get_info(memory_info[4])
mem_used = mem_total - mem_free - buffers - cached
memory_data = {
    "Memória total": round(mem_total / 1024),
    "Memória utilizada": round(mem_used / 1024),
    "Memória livre": round(mem_free / 1024),
    "Memória disponível": round(mem_available / 1024),
}
for label, value in memory_data.items():
    print(f"{label}: {value} MB")
