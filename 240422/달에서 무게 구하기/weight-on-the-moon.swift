// let a = 13.0
// let b = 0.165
// let c = a * b
// print(String(format: "%.0f * %.6f = %.6f", a, b, c))

import Foundation
let weightOnEarth: Double = 13
let moonGravityRatio: Double = 0.165

let weightOnMoon = weightOnEarth * moonGravityRatio

print(String(format: "%.0f * %.6f = %.6f", weightOnEarth, moonGravityRatio, weightOnMoon))