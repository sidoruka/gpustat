"""
The gpustat module.
"""

# isort: skip_file
from .core import GPUStat, GPUStatCollection
from .core import new_query, gpu_count, is_available
from .cli import print_gpustat, main


__all__ = (
    'GPUStat',
    'GPUStatCollection',
    'new_query',
    'gpu_count',
    'is_available',
    'print_gpustat',
    'main',
)
