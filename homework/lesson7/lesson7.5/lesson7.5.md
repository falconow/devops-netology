### Задание 3
1. 
```buildoutcfg
package main

import "fmt"

func main() {
    fmt.Print("Enter a number: ")
    var input float64
    input= 40
    output := input / 0.3048 

    fmt.Printf("В %f м. - %f футов", input, output)    
}
```
2. 
```buildoutcfg
package main

import (
	"fmt"
)

func main() {
	x := []int{48, 96, 1, 68, 57, 82, 63, 70, 37, 34, 83, 27, 19, 97, 9, 17}
	small_value := 0
	for i, value := range x {
		if (i==0) {
			small_value=value			
		} else {
			if (value<small_value) {
				small_value=value
			}
		}
	}
	
	fmt.Println("Наименьшее значение:",small_value)
}

```