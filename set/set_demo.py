import time

# this is a list
ll = [i for i in range(1, 1025 * 32)]

result = False
start = time.time()
for el in ll:
    result = el in ll
end = time.time()
print("This is a list ", end - start)  # needed time for iteration: ~3.9302210807800293

############################################################

# this is a set
ss = set(ll)


start = time.time()
for el in ss:
    result = el in ss
end = time.time()
print("This is a set: ", end - start)  # needed time for iteration: ~0.0030007362365722656
