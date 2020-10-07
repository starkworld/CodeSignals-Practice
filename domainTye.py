def domainType(domains):
    ans = []
    for domain in domains:
        label = domain.split(".")[-1]
        if label == "com":
            ans.append("commercial")
        elif label == "org":
            ans.append("organization")
        elif label == "net":
            ans.append("network")
        elif label == "info":
            ans.append("information")
    return ans
