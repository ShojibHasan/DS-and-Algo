package main
import "fmt"

func main() {
	list := [18]int{11,22,33,44,55,66,77,88,99,111,122,133,144,155,166,177,188,199}
	target := 111
	var a int = binary_search(list,target)
	fmt.Println(a)
	
}

func binary_search(list[18] int,target int)int{
	low := 0
	high := len(list)
	for low<=high{
		mid := (low+high)/2
		guess := list[mid]

		if guess == target{
			return mid
		} else if guess > target{
			high = mid -1
		} else{
			low = mid +1
		}

	}
	return -1

}