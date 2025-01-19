Creator "Craig Warner Jan 19 11:52:30 2025"
Version 1
graph
[
  directed 0
  title "Indirect Detect Test"
  node
  [
    id 0
    name "A-Victim"
  ]
  node
  [
    id 1
    name "B"
  ]
  node
  [
    id 2
    name "C"
  ]
  node
  [
    id 3
    name "D"
  ]
  node
  [
    id 4
    name "E-Malicious"
  ]
  edge
  [
    source 4
    target 1
  ]
  edge
  [
    source 4
    target 2
  ]
  edge
  [
    source 4
    target 3
  ]
  edge
  [
    source 1
    target 0
  ]
  edge
  [
    source 2
    target 0
  ]
  edge
  [
    source 3
    target 0
  ]
]