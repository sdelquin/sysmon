import hug
import psutil

MB = 1024 * 1024
GB = 1024 * MB


def get_stats():
    cpu_freq = psutil.cpu_freq()
    cpu_freq = {
        'current': cpu_freq.current,
        'max': -1,
        'units': 'MHz'
    }

    cpu_load = psutil.cpu_percent()
    cpu_load = {
        'current': cpu_load,
        'max': 100,
        'units': '%'
    }

    memory = psutil.virtual_memory()
    memory = {
        'current': (memory.total - memory.available) / MB,
        'max': memory.total / MB,
        'units': 'MB'
    }

    disk = psutil.disk_usage('/')
    disk = {
        'current': disk.used / GB,
        'max': disk.total / GB,
        'units': 'GB'
    }

    return {
        'cpu_freq': cpu_freq,
        'cpu_load': cpu_load,
        'memory': memory,
        'disk': disk
    }


@hug.get('/')
def root():
    return get_stats()
