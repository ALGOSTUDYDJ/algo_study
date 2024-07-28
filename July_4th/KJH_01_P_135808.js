function solution(k, m, score) {
  var answer = 0

  // 점수를 내림차순으로 정렬
  score.sort((a, b) => b - a)

  // m개씩 묶어서 상자를 만든다.
  for (let i = 0; i + m <= score.length; i += m) {
    // 상자의 최소 점수
    let boxMinScore = score[i + m - 1]
    // 상자의 가격을 계산하여 총 이익에 더한다.
    answer += boxMinScore * m
  }

  return answer
}
