"""Parse an SSH auth log for failed logins and flag likely brute-force source IPs."""

with open("sample_auth.log") as f:
    counts = {}
    for line in f:
        if "Failed password" in line and "from " in line:
            ip = line.split("from ")[1].split(" port")[0]
            counts[ip] = counts.get(ip, 0) + 1

ranked = sorted(counts.items(), key=lambda pair: pair[1], reverse=True)
for ip, count in ranked:
    if count >= 5:
        print(f"[WARNING]: The following IP: {ip} has failed {count} attempts")
