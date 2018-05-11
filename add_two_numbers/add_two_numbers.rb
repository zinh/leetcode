class ListNode
  attr_accessor :val, :next
  def initialize(val)
    @val = val
    @next = nil
  end

  def to_i
    pointer = self
    number = ""
    while pointer
      number = pointer.val.to_s + number
      pointer = pointer.next
    end
    return number.to_i
  end

  def self.from_integer(num)
    digits = num.to_s.split('').reverse.map(&:to_i)
    head = ListNode.new(digits.first)
    digits[1..-1].reduce(head) do |memo, digit|
      newNode = ListNode.new(digit)
      memo.next = newNode
      newNode
    end
    head
  end
end

def add(l1, l2)
  pointer_1 = l1
  pointer_2 = l2
  result_pointer = nil
  head = nil
  memo = 0
  while pointer_1 && pointer_2
    a = pointer_1.val
    b = pointer_2.val
    pp [a, b, memo]
    newNode = ListNode.new((a + b + memo) % 10)
    memo = (a + b + memo) / 10
    if result_pointer.nil?
      result_pointer =  newNode
      head = newNode
    else
      result_pointer.next = newNode
      result_pointer = newNode
    end
    pointer_1 = pointer_1.next
    pointer_2 = pointer_2.next
  end
  remainding = pointer_1 || pointer_2
  if remainding
    result_pointer.next = remainding
    if memo > 0
      while remainding && (memo > 0)
        val = remainding.val
        remainding.val = (val + memo) % 10
        memo = (val + memo) / 10
        result_pointer = remainding
        remainding = remainding.next
      end
    end
  end
  if memo > 0
    result_pointer.next = ListNode.new(memo)
  end
  return head
end

puts add(ListNode.from_integer(73), ListNode.from_integer(29)).to_i
