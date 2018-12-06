def next_smaller(n):
    nums = [int(char) for char in list(str(n))]
    seen = []
    nums_lookup = {}
    magnitude = len(nums)
    if magnitude < 2:
        return -1
    ix = magnitude - 1
    current_num = nums[ix]
    while ix > 0:
        if not nums_lookup.get(current_num, None):
            nums_lookup[current_num] = ix
            seen.append(current_num)
        ix -= 1
        current_num = nums[ix]
        for num in seen:
            if current_num > num:
                nums.pop(nums_lookup[num])
                nums = nums[0:ix] + [num] + sorted([current_num] + nums[ix + 1:], reverse=True)
                num_to_str = ''.join(str(num) for num in nums).lstrip('0')
                return int(num_to_str) if len(num_to_str) == magnitude else -1
    return -1
