import math

def dgim(bitstream, K):
    N = 2 * K               # Timestamp wraparound window
    k = int(math.ceil(math.log2(N)))
    buckets = [[] for _ in range(k)]  # Buckets of different sizes
    timestamp = 0

    for bit in bitstream:
        timestamp = (timestamp + 1) % N
        
        # Remove old buckets (timestamps outside window)
        for i in range(k):
            buckets[i] = [t for t in buckets[i] if (timestamp - t) % N < K]
        
        if bit == '1':
            # Add new bucket of size 1
            buckets[0].append(timestamp)
            
            # Merge buckets: if more than two buckets of size 2^i, merge oldest pair
            for i in range(k - 1):
                while len(buckets[i]) > 2:
                    oldest = buckets[i].pop(0)
                    buckets[i + 1].append(oldest)

    # Print all buckets with their sizes and timestamps
    print("\nBuckets with size and timestamp:")
    for i in range(k):
        for ts in buckets[i]:
            print(f"Size: {2**i}, Timestamp: {ts}")

    # Estimate number of 1s
    count = 0
    # Find oldest timestamp bucket (smallest timestamp among the largest bucket size)
    oldest_ts = None
    oldest_size = 0
    for i in reversed(range(k)):
        if buckets[i]:
            oldest_ts = min(buckets[i])
            oldest_size = 2 ** i
            break

    for i in range(k):
        for ts in buckets[i]:
            if ts == oldest_ts:
                count += oldest_size / 2
            else:
                count += 2 ** i

    return int(count)

# Example Usage
K = int(input("Enter window size K: "))
bitstream = input("Enter binary stream: ").strip()
estimate = dgim(bitstream, K)
print(f"\nEstimated number of 1s in last {K} bits: {estimate}")
