# Modular Arithmetic
<sub>These are notes mainly taken from Khan Academy's [Modular Arithmetic](https://www.khanacademy.org/computing/computer-science/cryptography/modarithmetic/a/what-is-modular-arithmetic) lesson</sub>
> Its simply the remainder of division between two integers 
- The modulo operator (`mod`) is used in these situations 

```
A
- = Q remainder R
B
A mod B = R

```
- In the above example, B is defined as the modulus
- Modulus can be defined as a clock, it'll repeat every the hour hits the modulus. [This](https://www.desmos.com/calculator/iqxgurpfxi) example shows it repeating every 3

## Congruence Modulo
```
A is congruent to B(mod C)
```
- Idea is something like 1 mod 5 is the same as 6 mod 5 which means they are in the same equivalance class
- 1 is congruent to 6(mod 5)
    - 1 mod 5 = 1
    - 6 mod 5 = 1
    - congruent -> same equivalance class
    - (mod 5) -> the operation applied to both A and B
    - congruence symbol in this case is then defined as 'congruence modulo C'
- Because they're in the same equivalance class, they mathematically are defined with the congruence symbol
- Let it be known that in this situation 6 mod 5 is different from 6(mod 5)

![Image](https://cdn.kastatic.org/ka-perseus-images/9d2e00eaac8813b125dc99cb00f8018bde25abd2.png)
<sub>From [Khan Academy](https://www.khanacademy.org/computing/computer-science/cryptography/modarithmetic/a/congruence-modulo)</sub>

- C represents the modulus
- "This means the difference between any two values in a slice is some multiple of C"
- [Slice Gen](../Scripts/CongruenceModulo.py)

## Equivalance relations
> Defines how we partition a set of values into equivalance classes
- In this sense congruence modulo C is an equivalance relation
- Because of that it has the following properties:
    - Reflexive: A is related to A
    - Symmetric: If A is related to B then B is related to A
    - Transitive: If A is related to B and B is related to C then A is related to C

## Quotient Remainder Theorem
- Used to prove certain properties of modular arithmetics
- A = B * Q + R
    - Q = quotient
    - R = remainder
        - 0 <= R < B
    - A/B

## Proeprties of Modular Arithmetic
- Addition:
    - (A+B) mod C = (A mod C + B mod C) mod C
        - Proof:
            - LHS = (A + B) mod C
                - A = C * Q1 + R1 # Quotient Remainder Theorem
                - B = C * Q2 + R2 # Quotient Remainder Theorem
                - LHS = (C * Q1 + R1 + C * Q2 + R2) mod C
                - C mod C = 0
                - LHS = (R1 + R2) mod C
            - RHS = (A mod C + B mod C) mod C
                - A mod C = R1
                - B mod C = R2
                - RHS = (R1 + R2) mod C
            - LHS = RHS
- Multiplication:
    - (A * B) mod C = (A mod C * B mod C) mod C
        - Proof
            - LHS = (A + B) mod C
                - A = C * Q1 + R1
                - B = C * Q2 + R2
                - LHS = ((C * Q1 + R1) * (C * Q2 + R2)) mod C
                - Distribute (Full example [here](https://www.khanacademy.org/computing/computer-science/cryptography/modarithmetic/a/modular-multiplication))
                - C mod C = 0
                - LHS = (R1 * R2) mod C
            - RHS = (A mod C * B mod C) mod C
                - A mod C = R1
                - B mod C = R2
                - RHS = (R1 * R2) mod C
            - LHS = RHS
- Exponentiation
    - A^B mod C = ((A mod C)^B) mod C
        - Same proof as multiplication
- Modular Exponentiation can be done really fast by pairing [Square and Multiply](./Square_And_Multiply.md) with the Modular property for exponentiation
    - This way, there are less steps required and the number is always reduced
    - [Script](../../Scripts/ModularExpo.py)

## Modular Inverse
- Ex) 1/8 * 8, for 1/8 8 is the inverse because multiplied together it equals 1
- Only numbers which are coprime to C have an inverse
    - If the GCD of the number and C = 1 then it's a coprime
    - GCD can be figured out with the [Euclidean Algorithm](Euclidean_Algorithm.md) 
	- A * B is congruent to 1 mod C
		- This falls under the '1' bucket and thus we need an A that is 1 past a multiple of C
		- The GCD is involved because if the two numbers share a factor then there is no possiblity for A to get 1 past any multiply of C
			- Ex) 2 mod 6
				- 2 * 1 = 2
				- 2 * 2 = 4
				- 2 * 3 = 6 (We hit a multiple)
				- 2 * 4 = 8
				- 2 * 5 = 10
				- 2 * 6 = 12 (We hit a multiple)
				- ...
				- GCD(2, 6) = 2
