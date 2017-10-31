# @param {Integer[]} nums
# # @param {Integer} target
# # @return {Integer[]}
def two_sum(nums, target)
  nums_with_index = nums.map.with_index do |num, index|
    [num, index]
  end
  # sort
  sorted_nums = nums_with_index.sort{|a, b| a.first <=> b.first}
  # b-search
  sorted_nums.each_with_index do |(num, pos), index|
    search_val = target - num
    if (result = bsearch(sorted_nums, search_val, index + 1))
      return [pos, result.last].sort
    end
  end
end

def bsearch(arr, target, from)
  hi = arr.size - 1
  lo = from
  while hi >= lo
    mid = (hi + lo) / 2
    if arr[mid].first == target
      return arr[mid]
    elsif arr[mid].first > target
      hi = mid - 1
    else
      lo = mid + 1
    end
  end
  return nil
end
