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

    memory_usage = psutil.virtual_memory()
    memory_usage = {
        'current': memory_usage.used / MB,
        'max': memory_usage.total / MB,
        'units': 'MB'
    }

    disk_usage = psutil.disk_usage('/')
    disk_usage = {
        'current': disk_usage.used / GB,
        'max': disk_usage.total / GB,
        'units': 'GB'
    }

    return {
        'cpu_freq': cpu_freq,
        'cpu_load': cpu_load,
        'memory_usage': memory_usage,
        'disk_usage': disk_usage
    }


@hug.get('/')
def root():
    return get_stats()
