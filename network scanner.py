print("🔍 Jalal's Network Scanner 🚀")
ips = []

for i in range(3):
    ip = input("Enter device IP address: ")
    ips.append(ip)

print("\n📡 Devices Detected in Your Network:")
for ip in ips:
    print("🔗 " + ip)