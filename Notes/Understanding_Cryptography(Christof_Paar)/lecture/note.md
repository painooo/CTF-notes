# Notes Day 1
- Cryptology
    1. Cryptography
        1. Symmetric Algorithms
        2. Asymmetric Algorithms
        3. Protocols
    2. Cryptanalysis
- One part of security is cryptography

- Symmetric Cryptography
    - Problem: Communicating over insecure channel
        - Party A: Alice
        - Party B: Bob
        - Opponent: Oscar
        - Problem:
            1. Alice -> X -> [Insecure Channel]
            2. [Insecure Channel] -> X -> Bob & Oscar
        - Solution: Use encryption
            1. Alice -> X -> [Encrypt] -> Y -> [Insecure Channel]
            2. [Insecure Channel] -> Y -> Oscar
            3. [Insecure Channel] -> Y -> [Decrypt] -> X -> Bob
    - [Encrypt] & [Decrypt] functions should be public to make sure they are secure through peer review
        - Because the functions are public; we use a key so that a message can't be decrypted without the key used to encrypt it
        - The key can be exchanged through a secure channel, 
    - **Never use an untested crypto algorithm**
    - Channel examples:
        - Internet
        - Airwaves: GSM, WiFi
        - ...
- **Notation:**
    - `x` = plaintext
    - `y` = ciphertext
    - `e` = encryption function
    - `d` = decryption function
    - `k` = key
    - `|k|` = keyspace (number of keys)

- Kerckhoffs' Principle [1883]
    - A cryptosystem is only secure when an attacker who knows all intricate details about the system (with exception to the key), cannot exploit its logic

- Substitution Cipher
    - Historical cipher (aka stupid cipher)
    - Operated on letters
    - Idea: replace every plaintext letter by a fixed ciphertext letter
    - Ex. 
        - A -> l
        - B -> d
        - C -> w
        - ...
    - ^
        - e(ABBA) -> lddl
    - Q: Is the cipher secure? Why? No
        1. Attack: Brute Force -> 26!: Keyspace is too large!
        2. Attack: Letter Frequency Attack -> Plaintext frequencies map onto ciphertext frequencies -> We can identify the key based on that information
- Types of Attacks:
    - **There are often many possible attack vectors**
    - Cryptanalysis
        - Classical
            - Brute Force -> Test all combinations
            - Analytical Attacks -> Observes what happens & finds a way to exploit behavior
        - Social Engineering
        - Implementation Attacks
            - Ex. Attacking the hardware the algorithm is implemented on & analyzing behavior
                - "Side-channel analysis"

# Notes Day 2
- Modular Arithmetic
    - Goal: Computation in finite sets
    - Visualizable in a circular motion
    - Definition of Modulo Operator (mod):
        - Let a, r, $m\in{Z}$, and m > 0
            - r -> remainder
            - m -> modulus
        - $a\equiv{r \mod m}$
        - If m divides (a - r), i.e m|(a-r) (aka m divides (a-r))
        - Ex) a = 13, m = 9
            - $13\equiv{r \mod 9}$
            - r = 4
            - Check: a - r -> (13 - 4) -> 9 -> 9|9 = True
    - Computation of the remainder
        - Given a, $m\in{Z}$
        - $a = qm + r$ (q = quotient aka how many times m fits in a)  
        - Ex) a = 42, m = 9
            - $42 = q9 + r$ -> $42 = 4(9) + r$ -> r = 6
            - Check: (42 - 6) -> 9|36 = True
        - But also:
            - $42 = 3(9) + r$ -> r = 15 // There are many remainders
            - Check: (42 - 15) -> 9|27 = True
        - But (there's more):
            - $42 = 5(9) + r$ -> r = -3 // There are many remainders **positive and negative**; **remainder is not unique**
            - Check: (42 - (-3)) -> 9|45 = True
    - Equivalence Classes
        - Ex) a = 12, m = 5
            - $12\equiv{2 \mod{5}}$ -> 5|(12-2)
            - $12\equiv{7..} -> 5|(12-7)
            - $12\equiv{-3..}$ -> 5|(12-(-3))
        - The set ({..., -3, 2, 7, 12, 17, ...}) forms an equivalence class modulo 5
        - All members of the class ^^^^^ behave equivalent modulo 5
        - Ex) All equivalence class 5 (trick demo)
            - 0: {..., -10, -5, 0, 5, 10, ...}A
            - 1: {..., -9, -4, 1, 6, 11, ...}B
            - 2: {..., -8, -3, 2, 7, 12, ...}C
            - 3: {..., -7, -2, 3, 8, 13, ...}D
            - 4: {.... -6, -1, 4, 9, 14, ...}E
            - Ex) 13 * 16 - 8 = 208 - 8 = 200 = $0\mod{5}$
                - D * B - D -> $3(1)-3\equiv{0..}$
                - 13 belongs in group D, 16 belongs in Group B, and 8 belongs in group D therefore 13 = 3, 16 = 1, and 8 = 3
                    - $13\equiv{3\mod5}$
                    - $16\equiv{1\mod5}$
                    - $8\equiv{3\mod5}$
                    - In each equivalent class, pick the smallest positive result
            - Ex) 8 * 6 - (-7) = 48 + 7 = 55 = $0\mod{5}$
                - D * B - D -> $3(1)-3\equiv{0..}$
        - > Application: ${3^8\mod7\equiv{?}}$
            - > *dumb* way: $3^8=6567\equiv{2\mod{7}}$
            - > *better* way: $3^8=3^4(3^4)=81(81)$ -> replace 81 by another element in modulo 7 equivalent class -> ($81\mod{7}$) -> $4(4) = 16\equiv{2\mod7}$
    - Rings: An Algebraic View on Modular Arithmetic
        - The "integer ring" $Z_m$ consists of..
            1. The set of $Z_m=\{0, 1, 2, .., m-1\}$
            2. Two operators: "+" and "\*" s.t (such that) for all $a,b,c,d\in{Z_m}$
                - $a+b\equiv{c\mod{m}}$
                - $a(b)\equiv{d..}$
        - **(Rest will be written in the textbook part of notes)**
