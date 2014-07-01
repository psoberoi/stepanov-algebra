# Egyptian fractions

def egyptian_fraction_step(a, b):
  """Perform one step of egyptian fraction computation.

  Takes integers a and b such that 2 <= a < b
  Returns integers (n, a1, b1), such that a/b == 1/n + a1/b1
  and n, a1, b1 are the smallest such integers.

  """
  # Let q and r be the quotient and remainder when dividing b by a.
  # i.e. qa + r = b. Then, as per the requirements:
  #
  #     1/(n-1)  >  a/b         >  1/n
  # =>    n - 1  <  b/a         <  n
  # =>    n - 1  <  (qa + r)/a  <  n
  # =>    n - 1  <  q + r/a     <  n
  #
  # Therefore, n = q + 1. And,
  #
  #     a1/b1 = a/b - 1/n
  #           = (an - b) / bn
  #
  # Since a1 and b1 are the smallest such integers, we need to simplify
  # the fraction by dividing by the GCD of the numerator and the denomiator.

  assert 2 <= a < b
  n = b // a + 1
  a1 = a * n - b
  b1 = b * n
  return (n, a1, b1)

def egyptian_fraction(a, b):
  """Return a list of integers corresponding to the egyptial fraction.

  Takes integers a and b such that 1 <= a < b.
  Returns a list lst of integers such that a/b == sum(1/x for x in lst)

  """
  assert 1 <= a < b
  lst = []
  while b % a != 0:
    n, a, b = egyptian_fraction_step(a, b)
    lst.append(n)
  lst.append(b // a)
  return lst

