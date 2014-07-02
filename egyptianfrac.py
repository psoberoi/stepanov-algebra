# Egyptian fractions

def gcd(a, b):
  """Returns gcd of two intergers a and b.

  a and b are integers, and a, b != 0.

  """
  while b != 0:
    a, b = b, a % b
  return a

def reduce_fraction(a, b):
  """Reduce the fraction to the lowest terms.

  a and b are integers, b != 0. Returns a1, b1 such that
  a/b == a1/b1 and gcd(a1, b1) == 1.

  """
  assert b != 0
  d = gcd(a, b)
  return (a // d, b // d)

def egyptian_fraction_step(a, b):
  """Perform one step of egyptian fraction computation.

  Takes integers a and b such that 2 <= a < b
  Returns positive integers (n, a1, b1), such that a/b == 1/n + a1/b1
  and n is the smallest such integer.

  """
  # Let q and r be the quotient and remainder when dividing b by a.
  # i.e. qa + r = b. Then, as per the requirements:
  #
  #     1/(n-1)  >  a/b         >  1/n
  #  =>   n - 1  <  b/a         <  n
  #  =>   n - 1  <  (qa + r)/a  <  n
  #  =>   n - 1  <  q + r/a     <  n
  #
  # Therefore, n = q + 1. And,
  #
  #     a1/b1 = a/b - 1/n
  #           = (an - b) / bn
  #
  # Since a1 and b1 are the smallest such integers, we need to simplify
  # the fraction by dividing by the GCD of the numerator and the denominator.

  assert 2 <= a < b
  n = (b // a) + 1
  return (n, a * n - b, b * n)

def egyptian_fraction(a, b):
  """Convert a rational number to an egyptian fraction.

  Takes integers a and b such that 1 <= a < b.
  Returns a list lst of positive integers representing the egyptian fraction
  such that a/b == sum(1/x for x in lst)

  The numerator of the remaining fraction after each step is an - b.
  We have n = q + 1, and b = aq + r. r > 0 because if the while condition.
  Therefore,

     an - b = a(q + 1) - (aq + r)
            = aq + a - aq - r
            = a - r < a

  Each step reduces the numerator, and therefore the process must terminate.

  """
  assert 1 <= a < b
  lst = []
  while b % a != 0:
    n, a, b = egyptian_fraction_step(a, b)
    lst.append(n)
  lst.append(b // a)
  return lst

def add_unit_fraction((a, b), n):
  """Returns a tuple (a1, b1) such that a1/b1 == a/b + 1/n."""

  return (a * n + b, b * n)

def reduce_egyptian_fraction(lst):
  """Convert an egyptian fraction to a rational number.

  Takes a list lst of positive integers representing an egyptian fraction.
  Returns a tuple of positive integers (a, b) such that
  a/b == sum(1/x for x in lst) and gcd(a, b) == 1.

  """
  return reduce_fraction(*reduce(add_unit_fraction, lst, (0, 1)))
