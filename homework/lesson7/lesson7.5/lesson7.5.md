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