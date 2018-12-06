def find_discounted(prices):
    if not prices:
        return ''
    prices = [int(char) for char in prices.split(' ')]
    discounted = []
    seen_nums = {}
    for num in prices:
        key = num * 0.75
        if seen_nums.get(key, 0) > 0:
            discounted.append(int(key))
            seen_nums[key] -= 1
            continue
        if seen_nums.get(num):
            seen_nums[num] += 1
        else:
            seen_nums[num] = 1
    discounted = ' '.join([str(num) for num in discounted])
    return discounted


print(find_discounted("9 9 12 12 12 15 16 20"))
