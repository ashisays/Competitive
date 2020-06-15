package main

import (
	"fmt"
	"sync"
)

// TreeNode class
type BSTTreeNode struct {
	key       int
	value     int
	leftNode  *BSTTreeNode
	rightNode *BSTTreeNode
}

// BinarySearchTree class
type BinarySearchTree struct {
	rootNode *BSTTreeNode
	lock     sync.RWMutex
}

func (tree *BinarySearchTree) InsertElement(key int, val int) {
	tree.lock.Lock()
	defer tree.lock.Unlock()
	var treeNode *BSTTreeNode
	treeNode = &BSTTreeNode{key, val, nil, nil}
	if tree.rootNode == nil {
		tree.rootNode = treeNode
	} else {
		insertTreeNode(tree.rootNode, treeNode)
	}
}

func insertTreeNode(rootNode *BSTTreeNode, newTreeNode *BSTTreeNode) {
	if newTreeNode.key < rootNode.key {
		if rootNode.leftNode == nil {
			rootNode.leftNode = newTreeNode
		} else {
			insertTreeNode(rootNode.leftNode, newTreeNode)
		}
	} else {
		if rootNode.rightNode == nil {
			rootNode.rightNode = newTreeNode
		} else {
			insertTreeNode(rootNode.rightNode, newTreeNode)
		}
	}
}

// MinNode method
func (tree *BinarySearchTree) MinNode() *int {
	tree.lock.Lock()
	defer tree.lock.Unlock()
	var treeNode *BSTTreeNode
	treeNode = tree.rootNode
	if treeNode == nil {
		return (*int)(nil)
	}
	for {
		if treeNode.leftNode == nil {
			return &treeNode.value
		}
		treeNode = treeNode.leftNode
	}
}

// MaxNode method
func (tree *BinarySearchTree) MaxNode() *int {
	tree.lock.RLock()
	defer tree.lock.RUnlock()
	var treeNode *BSTTreeNode
	treeNode = tree.rootNode
	if treeNode == nil {
		//nil instead of 0
		return (*int)(nil)
	}
	for {
		if treeNode.rightNode == nil {
			return &treeNode.value
		}
		treeNode = treeNode.rightNode
	}
}

// SearchNode method
func (tree *BinarySearchTree) SearchNode(key int) bool {
	tree.lock.RLock()
	defer tree.lock.RUnlock()
	return searchNode(tree.rootNode, key)
}

// searchNode method
func searchNode(treeNode *BSTTreeNode, key int) bool {
	if treeNode == nil {
		return false
	}
	if key < treeNode.key {
		return searchNode(treeNode.leftNode, key)
	}
	if key > treeNode.key {
		return searchNode(treeNode.rightNode, key)
	}
	return true
}

// InOrderTraverseTree method
func (tree *BinarySearchTree) RemoveNode(key int) {
	tree.lock.RLock()
	defer tree.lock.RUnlock()
	removeNode(tree.rootNode, key)
}

// removeNode method
// removeNode method
func removeNode(treeNode *BSTTreeNode, key int) *BSTTreeNode {
	if treeNode == nil {
		return nil
	}
	if key < treeNode.key {
		treeNode.leftNode = removeNode(treeNode.leftNode, key)
		return treeNode
	}
	if key > treeNode.key {
		treeNode.rightNode = removeNode(treeNode.rightNode, key)
		return treeNode
	}
	// key == node.key
	if treeNode.leftNode == nil && treeNode.rightNode == nil {
		treeNode = nil
		return nil
	}
	if treeNode.leftNode == nil {
		treeNode = treeNode.rightNode
		return treeNode
	}
	if treeNode.rightNode == nil {
		treeNode = treeNode.leftNode
		return treeNode
	}
	var leftmostrightNode *BSTTreeNode
	leftmostrightNode = treeNode.rightNode
	for {
		//find smallest value on the right side
		if leftmostrightNode != nil && leftmostrightNode.leftNode != nil {
			leftmostrightNode = leftmostrightNode.leftNode
		} else {
			break
		}
	}
	treeNode.key, treeNode.value = leftmostrightNode.key, leftmostrightNode.value
	treeNode.rightNode = removeNode(treeNode.rightNode, treeNode.key)
	return treeNode
}

// InOrderTraverseTree method
func (tree *BinarySearchTree) InOrderTraverseTree(function func(int)) {
	tree.lock.RLock()
	defer tree.lock.RUnlock()
	inOrderTraverseTree(tree.rootNode, function)
}

func inOrderTraverseTree(treeNode *BSTTreeNode, function func(int)) {
	if treeNode != nil {
		inOrderTraverseTree(treeNode.leftNode, function)
		function(treeNode.value)
		inOrderTraverseTree(treeNode.rightNode, function)
	}
}

// PreOrderTraverseTree method
func (tree *BinarySearchTree) PreOrderTraverseTree(function func(int)) {
	tree.lock.RLock()
	defer tree.lock.RUnlock()
	preOrderTraverseTree(tree.rootNode, function)
}

func preOrderTraverseTree(treeNode *BSTTreeNode, function func(int)) {
	if treeNode != nil {
		function(treeNode.value)
		preOrderTraverseTree(treeNode.rightNode, function)
		preOrderTraverseTree(treeNode.leftNode, function)
	}
}

// PostOrderTraverseTree method
func (tree *BinarySearchTree) PostOrderTraverseTree(function func(int)) {
	tree.lock.RLock()
	defer tree.lock.RUnlock()
	postOrderTraverseTree(tree.rootNode, function)
}

func postOrderTraverseTree(treeNode *BSTTreeNode, function func(int)) {
	if treeNode != nil {
		postOrderTraverseTree(treeNode.rightNode, function)
		postOrderTraverseTree(treeNode.leftNode, function)
		function(treeNode.value)
	}
}

// String method
func (tree *BinarySearchTree) String() {
	tree.lock.Lock()
	defer tree.lock.Unlock()
	fmt.Println("------------------------------------------------")
	stringify(tree.rootNode, 0)
	fmt.Println("------------------------------------------------")
}

// stringify method
func stringify(treeNode *BSTTreeNode, level int) {
	if treeNode != nil {
		format := ""
		for i := 0; i < level; i++ {
			format += " "
		}
		format += "----[ "
		level++
		stringify(treeNode.leftNode, level)
		fmt.Printf(format+"%d\n", treeNode.key)
		stringify(treeNode.rightNode, level)
	}
}

// main method
func main() {
	var tree *BinarySearchTree = &BinarySearchTree{}
	tree.InsertElement(8, 8)
	tree.InsertElement(3, 3)
	tree.InsertElement(10, 10)
	tree.InsertElement(1, 1)
	tree.InsertElement(6, 6)
	tree.InsertElement(12, 12)
	tree.InsertElement(2, 2)
	tree.InsertElement(11, 11)
	tree.InsertElement(4, 4)
	tree.String()
	tree.RemoveNode(2)
	tree.String()
	tree.RemoveNode(3)
	tree.String()
}
