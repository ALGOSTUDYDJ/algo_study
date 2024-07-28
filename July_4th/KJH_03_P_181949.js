const readline = require('readline')
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
})

let input = []

rl.on('line', function (line) {
  input = [line]
}).on('close', function () {
  str = input[0]
  n = str.length

  for (let i = 0; i < n; i++) {
    const chr = str[i]

    if (chr === chr.toUpperCase()) {
      process.stdout.write(chr.toLowerCase())
    } else {
      process.stdout.write(chr.toUpperCase())
    }
  }
})
