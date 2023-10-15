unique_hosts = set()

with open('mbox.txt', 'r') as file:
    for line in file:
     
     if line.startswith("From:"):
            parts = line.split()
            if len(parts) > 1:
                email = parts[1]
                host = email.split('@')[1]
                unique_hosts.add(host)

print("Unique host names:")
for host in unique_hosts:
    print(host)
print("Total hosts printed:", len(unique_hosts))
