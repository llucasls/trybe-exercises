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


# Memória
def get_info(entry):
    info_list = entry.split()
    return int(info_list[1])


command = ["head", "-5", "/proc/meminfo"]
memory_info = check_output(command).decode("UTF-8").split("\n")
mem_total = round(get_info(memory_info[0]) / 1024)
mem_free = round(get_info(memory_info[1]) / 1024)
mem_available = round(get_info(memory_info[2]) / 1024)
buffers = round(get_info(memory_info[3]) / 1024)
cached = round(get_info(memory_info[4]) / 1024)
mem_used = mem_total - mem_free - buffers - cached
memory_data = {
    "Memória total": mem_total,
    "Memória utilizada": mem_used,
    "Memória livre": mem_free,
    "Memória disponível": mem_available,
}


# Output
if __name__ == "__main__":
    for desired_name, desired_description in desired_cpu_information.items():
        for information in cpu_information:
            if information.lower().startswith(desired_name):
                information = information.split("  ")  # 2 blank spaces
                information = information[-1].strip()
                print(f"{desired_description}: {information}")

    for label, value in memory_data.items():
        print(f"{label}: {value} MB")
