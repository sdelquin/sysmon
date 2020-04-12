import hug
import psutil

MB = 1024 * 1024
GB = 1024 * MB


@hug.get('/')
def root():
    cpu_load = psutil.cpu_percent()
    cpu_freq = psutil.cpu_freq().current
    mem_available = psutil.virtual_memory().available / MB
    disk_available = psutil.disk_usage('/').free / GB
    return {
        'cpu_load': cpu_load,
        'cpu_freq': cpu_freq,
        'mem_available': mem_available,
        'disk_available': disk_available
    }
