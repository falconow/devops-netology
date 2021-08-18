### Задание 1
***
>  Установил golang
```buildoutcfg
root@vagrant:~# apt install golang
root@vagrant:~# go version
go version go1.13.8 linux/amd64

```

### Задание 2
***
> Ознакомился с интерактивной консолью https://tour.golang.org/. Все понятно и просто 
> объясняется, понравилось что можно сразу посмотреть как теория выглядит на практике.

### Задание 3
***
- Задача 1
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
- Задача 2 
```buildoutcfg
package main

import (
	"fmt"
)

func main() {
	x := []int{48, 96, 12, 68, 57, 82, 63, 70, 37, 34, 83, 27, 19, 97, 9, 17}
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
	
	fmt.Println("Список значений:",x)
	fmt.Println("Наименьшее значение в списке:",small_value)
}
```
- Задача 3 
```buildoutcfg
package main

import (
	"fmt"
)

func main() {
	for i := 1; i<=100; i++ {
		if (i % 3 == 0) {
			fmt.Println(i)	
		}		
	}
}
```

