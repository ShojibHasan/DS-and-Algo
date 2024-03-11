package main

import (
    "fmt"
    "math/big"
)

func main() {
    // Create big.Rat values for 22 and 7
    numerator := new(big.Rat).SetInt64(22)
    denominator := new(big.Rat).SetInt64(7)

    // Perform the division
    result := new(big.Rat).Quo(numerator, denominator)

    // Print the result with high precision
    fmt.Printf("%.1000f\n", new(big.Float).SetRat(result))
}