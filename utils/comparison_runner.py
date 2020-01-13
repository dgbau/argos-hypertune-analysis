import os, csv
import docker 
from docker_exec import trial_exec
from params import ga_params, ht_params

trial_count = 50
print("GA - 0")
for trial in range(trial_count):
    trial_exec(ga_params[0])
print("GA - 1")
for trial in range(trial_count):
    trial_exec(ga_params[1])
print("GA - 2")
for trial in range(trial_count):
    trial_exec(ga_params[2])

print("HT - 0")
for trial in range(trial_count):
    trial_exec(ht_params[0])
print("HT - 1")
for trial in range(trial_count):
    trial_exec(ht_params[1])
print("HT - 2")
for trial in range(trial_count):
    trial_exec(ht_params[2])