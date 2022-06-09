import math

def find_substring(str1, pattern):
  
  chars = {}
  for char in pattern:
    if char not in chars:
      chars[char] = 0
    chars[char] += 1
  
  window_start = 0
  curr_string = ''
  min_string = ''
  min_string_len = math.inf

  curr_chars = {}
  for window_end in range(len(str1)):

    right_char = str1[window_end]
    curr_string += right_char
    if right_char not in chars:
      continue

    if right_char not in curr_chars:
      curr_chars[right_char] = 0
    curr_chars[right_char] += 1
    
    while curr_chars[right_char] > chars[right_char]:
      curr_string = curr_string[1:]
      curr_chars[str1[window_start]] -= 1
      window_start += 1

    if curr_string[0] not in chars:
      curr_string = curr_string[1:]

    if chars == curr_chars:
      if min_string_len > len(curr_string):
        min_string = curr_string
        min_string_len = len(min_string)

  return min_string

def main():
  print(find_substring("aabdec", "abc"))
  print(find_substring("aabdec", "abac"))
  print(find_substring("abdbca", "abc"))
  print(find_substring("adcad", "abc"))

main()