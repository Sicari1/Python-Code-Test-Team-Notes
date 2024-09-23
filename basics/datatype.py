# data type은 'tuple' 이런식이 아니라 그냥 tuple 그 자체이다.
type((1,2)) == tuple ==> True
type((1,2)) == 'tuple' ==> False
