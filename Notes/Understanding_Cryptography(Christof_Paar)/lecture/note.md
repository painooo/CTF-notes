# Notes
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
