import resource
# Create a large list
large_list = [i for i in range(100000)]
# Print memory usage before deleting the list

print(f"Memory usage before deleting: {resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1000:.2f} MB")
# Delete the list
del large_list
# Print memory usage after deleting the list
print(f"Memory usage after deleting: {resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1000:.2f} MB")