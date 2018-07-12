require 'pp'
def merge(a, b)
  post_a = 0
  post_b = 0
  r = []
  c = 0
  m = (a.size + b.size) / 2
  remainder = (a.size + b.size) % 2
  m += 1 if remainder.zero?
  while true
    if a[post_a] <= b[post_b]
      r << a[post_a]
      post_a += 1
      c += 1
    else
      a, b = b, a
      post_a, post_b = post_b, post_a
    end
    break if post_a >= a.size || post_b >= b.size
    # pp "a = #{a}, post_a = #{post_a}"
    # pp "b = #{b}, post_b = #{post_b}"
    # pp "r = #{r}"
  end
  if post_a < a.size
    r += a[post_a..-1]
  end
  if post_b < b.size
    r += b[post_b..-1]
  end
  return r
end
