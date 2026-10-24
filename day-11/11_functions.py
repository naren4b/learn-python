# Day 11: functions and arguments


def total_price(price, quantity=1):
    return price * quantity


def count_labels(*labels):
    return len(labels)


def get_region(**attributes):
    return attributes.get("region", "unknown")


double = lambda value: value * 2

print(f"Total: {total_price(price=100, quantity=3):.2f}")
print(f"Labels: {count_labels('dev', 'test', 'prod')}")
print(f"Region: {get_region(name='api', region='eu-central-1')}")
print(f"Double: {double(4)}")
