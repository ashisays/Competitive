package main

// KeyValue type
type KeyValue interface {
	LessThan(KeyValue) bool
	EqualTo(KeyValue) bool
}

// TreeNode class
type TreeNode struct {
	KeyValue     KeyValue
	BalanceValue int
	LinkedNodes  [2]*TreeNode
}

//opposite method
func opposite(nodeValue int) int {
	return 1 - nodeValue
}
