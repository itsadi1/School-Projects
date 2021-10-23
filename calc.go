package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
)

func main() {
	var (x , y int
	 z string)
	for z != "exit"{
		number1, number2, number3 := Input(x, y)
		z = number3
		add, sub, mul, div := Calc(number1, number2)
		Display(add, sub, mul, div)
}
}

func Input(x, y int) (out1 int64, out2 int64, out3 string) {
	a1 := bufio.NewScanner(os.Stdin)
	fmt.Print("Enter first number: ")
	a1.Scan()
	n1, _ := strconv.ParseInt(a1.Text(), 10, 64)
	b1 := bufio.NewScanner(os.Stdin)
	fmt.Print("Enter second number: ")
	b1.Scan()
	n2, _ := strconv.ParseInt(b1.Text(), 10, 64)
	out1 = n1
	out2 = n2
	out3 = a1.Text()
	return
}

func Calc(number1, number2 int64) (add, sub, mul, div int) {
	add = int(number1 + number2)
	sub = int(number1 - number2)
	mul = int(number1 * number2)
	div = int(number1 / number2)
	return
}

func Display(add, sub, mul, div int) {
	fmt.Println("\nAddition", add)
	fmt.Println("Subtraction", sub)
	fmt.Println("Multiplication", mul)
	fmt.Println("Division", div)
}
