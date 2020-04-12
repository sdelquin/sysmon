import hug
import psutil

MB = 1024 * 1024
GB = 1024 * MB


def get_stats():
    cpu_load = psutil.cpu_percent()
    cpu_freq = psutil.cpu_freq().current
    mem_available = psutil.virtual_memory().available / MB
    disk_available = psutil.disk_usage('/').free / GB
    return {
        'cpu_load': [cpu_load, '%'],
        'cpu_freq': [cpu_freq, 'MHz'],
        'mem_available': [mem_available, 'MB'],
        'disk_available': [disk_available, 'GB']
    }


@hug.get('/')
def root():
    return get_stats()
