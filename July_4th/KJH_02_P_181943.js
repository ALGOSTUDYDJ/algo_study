function solution(my_string, overwrite_string, s) {
  var answer = ''

  let n = overwrite_string.length
  answer = my_string.slice(0, s) + overwrite_string + my_string.slice(s + n)

  return answer
}
