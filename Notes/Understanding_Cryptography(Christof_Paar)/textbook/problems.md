# Problems
> Each chapter has a section for chapters & this is where I store my answers (read the textbook to view the questions)
## Chapter 1
1. ```
lrvmnir bpr sumvbwvr jx bpr lmiwv yjeryrkbi jx qmbm wi
bpr xjvni mkd ymibrut jx irhx wi bpr riirkvr jx
ymbinlmtmipw utn qmumbr dj w ipmhh but bj rhnvwdmbr bpr
yjeryrkbi jx bpr qmbm mvvjudwko bj yt wkbrusurbmbwjk
lmird jk xjubt trmui jx ibndt
wb wi kjb mk rmit bmiq bj rashmwk rmvp yjeryrkb mkd wbi
iwokwxwvmkvr mkd ijyr ynib urymwk nkrashmwkrd bj ower m
vjyshrbr rashmkmbwjk jkr cjnhd pmer bj lr fnmhwxwrd mkd
wkiswurd bj invp mk rabrkb bpmb pr vjnhd urmvp bpr ibmbr
jx rkhwopbrkrd ywkd vmsmlhr jx urvjokwgwko ijnkdhrii
ijnkd mkd ipmsrhrii ipmsr w dj kjb drry ytirhx bpr xwkmh
mnbpjuwbt lnb yt rasruwrkvr cwbp qmbm pmi hrxb kj djnlb
bpmb bpr xjhhjcwko wi bpr sujsru msshwvmbwjk mkd
wkbrusurbmbwjk w jxxru yt bprjuwri wk bpr pjsr bpmb bpr
riirkvr jx jqwkmcmk qmumbr cwhh urymwk wkbmvb
```
    - Frequencies:
        A: 0.77%
        B: 10.53%
        C: 0.77%
        D: 3.56
        ... (not typing all of that, use dcode.fr)
    - 
```
BECAUSE THE PRACTICE OF THE BASIC MOVEMENTS OF KATA IS THE FOCUS AND MASTERY OF SELF IS THE ESSENCE OF MATSUBAYASHI RYU KARATE DO I SHALL TRY TO ELUCIDATE THE MOVEMENTS OF THE KATA ACCORDING TO MY INTERPRETATION BASED ON FORTY YEARS OF STUDY IT IS NOT AN EASY TASK TO EXPLAIN EACH MOVEMENT AND ITS SIGNIFICANCE AND SOME MUST REMAIN UNEXPLAINED TO GIVE A COMPLETE EXPLANATION ONE WOULD HAVE TO BE QUALIFIED AND INSPIRED TO SUCH AN EXTENT THAT HE COULD REACH THE STATE OF ENLIGHTENED MIND CAPABLE OF RECOGNIZING SOUNDLESS SOUND AND SHAPELESS SHAPE I DO NOT DEEM MYSELF THE FINAL AUTHORITY BUT MY EXPERIENCE WITH KATA HAS LEFT NO DOUBT THAT THE FOLLOWING IS THE PROPER APPLICATION AND INTERPRETATION I OFFER MY THEORIES IN THE HOPE THAT THE ESSENCE OF OKINAWAN KARATE WILL REMAIN INTACT
```
    - Shoshin Nagamine
2. `xultpaajcxitltlxaarpjhtiwtgxktghidhipxciwtvgtpilpitghlxiwiwtxgqadds`
    - 18 characters, `ifweallunitewewillcausetheriverstostainthegreatwaterswiththeirblood`
    - Tecumseh
3. - How long exhaustive search take?
    - 10000 ASIC can run in parallel
        - Each can check 5 * 10**8 keys per second thus 5 * 10**11 per second
        - 2**127 keys to check
        - Roughly 10**18 years to check. This is 10**8 more years than the age of the universe
    -  103.5yrs to wait for check to be 24 hrs 
4. Relation between password and key size (key in form of password)
    - 128^8 possible passwords (password w/ 8 characters)
    - 56 bits key length
    - (Roughly 5 bits per character) 40 bits key length
    - a. Roughly 19 characters b. Roughly 26 characters
5. Modular Arithmetic
    - $15*29\mod{13} = 15\mod{13} * 29\mod{13} = 2*3 = 6$ 
    - $2*29\mod{13} = 2*3 = 6$
    - $2*3\mod{13} = 2*3 = 6$
    - $-11*3\mod{13} = -11\mod{13} * 3\mod{13} = 2*3 = 6$
    - For each problem numbers like 15, 2, -11 or 29, 3 belong in the same equivalance class and so result in the same answer in the end
6. Compute
    - $\frac{1}{5}\mod{13} = \frac{1}{5}$
    - $\frac{1}{5}\mod{7} = \frac{1}{5}$
    - $3*\frac{2}{5}\mod{7} = 3 * \frac{2}{5} = \frac{6}{5}$
7. Consider ring $Z_4$
| + | 0 | 1 | 2 | 3 |
|---|---|---|---|---|
| 0 | 0 | 1 | 2 | 3 |
| 1 | 1 | 2 | 3 | 0 |
| 2 | 1 | 3 | 0 | 1 |
| 3 | 3 | 0 | 1 | 2 |

| * | 0 | 1 | 2 | 3 |
|---|---|---|---|---|
| 0 | 0 | 0 | 0 | 0 |
| 1 | 0 | 1 | 2 | 3 |
| 2 | 0 | 2 | 0 | 2 |
| 3 | 0 | 3 | 2 | 1 |

    - Consider $Z_5$
| + | 0 | 1 | 2 | 3 | 4 |
|---|---|---|---|---|---|
| 0 | 0 | 1 | 2 | 3 | 4 |
| 1 | 1 | 2 | 3 | 4 | 0 |
| 2 | 2 | 3 | 4 | 0 | 1 |
| 3 | 3 | 4 | 0 | 1 | 2 |
| 4 | 4 | 0 | 1 | 2 | 3 |

| * | 0 | 1 | 2 | 3 | 4 |
|---|---|---|---|---|---|
| 0 | 0 | 0 | 0 | 0 | 0 |
| 1 | 0 | 1 | 2 | 3 | 4 |
| 2 | 0 | 2 | 4 | 1 | 3 |
| 3 | 0 | 3 | 1 | 3 | 0 |
| 4 | 0 | 4 | 3 | 0 | 1 |

    - Consider $Z_6$
| + | 0 | 1 | 2 | 3 | 4 | 5 |
|---|---|---|---|---|---|---|
| 0 | 0 | 1 | 2 | 3 | 4 | 5 |
| 1 | 1 | 2 | 3 | 4 | 5 | 0 |
| 2 | 2 | 3 | 4 | 5 | 0 | 1 |
| 3 | 3 | 4 | 5 | 0 | 1 | 2 |
| 4 | 4 | 5 | 0 | 1 | 2 | 3 |
| 5 | 5 | 0 | 1 | 2 | 3 | 4 |

| * | 0 | 1 | 2 | 3 | 4 | 5 |
|---|---|---|---|---|---|---|
| 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| 1 | 0 | 1 | 2 | 3 | 4 | 5 |
| 2 | 0 | 2 | 4 | 0 | 2 | 4 |
| 3 | 0 | 3 | 0 | 3 | 0 | 3 |
| 4 | 0 | 4 | 2 | 0 | 4 | 2 |
| 5 | 0 | 5 | 4 | 3 | 2 | 1 |

    - Which elements in $Z_4$ & $Z_6$ don't have multiplicative inverses?
        - 4: 0, 2
        - 6: 0, 2, 3, 4
    - Why $Z_5$ all non-zero are multiplicative inverses?
        - Because 5 is a prime number and so only factors are 1 and 5
8. Multiplicative inverse of 5 in $Z_11, Z_12, Z_13$
    - 11: 9
    - 12: 5
    - 13: 8
    - Note: inverse depends completely on the ring
9. Compute x
    - $x=3^2\mod{13} = 3*3 = x = 9$ 
    - $x=7^2\mod{13} = 7*7 = x = 49$
    - $x=3^10\mod{13} -> 3^10 = 3^3 * 3^3 * 3^3 * 3^2\equiv{27 * 27 * 27 * 9=1*1*1*9\mod{13}} -> x\equiv{9\mod{13}}$
    - $x=7^100\mod{13} -> 7^100 = 7^10\mod{13} * 7^10\mod{13} * 7^10\mod{13} * ... = 4^10 = 4^2\mod{13} * 4^2\mod{13} * ... = 3^5 = 343 -> 343\equiv{9\mod{13}} -> x = 9$
    - $7^x=11\mod{13} -> x = 5 (bruteforced solution)$ // problem is known as discrete logarithm
10. Euler's phi function
    - phi(4): 2
    - phi(5): 4
    - phi(9): 6
    - phi(26): 12
11. falszztysyjzyjkywjrztyjztyynaryjkyswarztyegyyj (affine cipher: a = 7, b = 22)
    - "firstthesentenceandthentheevidencesaidthequeen"
    - Lewis Carroll
12. Extending Affine (added 3)
    - Encrypt: $e_k{x}=y\equiv{a*x+b\mod{29}}$
    - Decrypt: $d_k{y}=x\equiv{a^-1*(y-b)\mod{29}}$
    - Keyspace: 29 * 29 = 841
    - F R O D O
    - Comes from The Shire
13. Affack
    - If (x2-x1)%m = 1 then a equiv (f(x2) - f(x1)) % m
    - And b equiv y1 - a*x1 % m
14. Double encrypting
    - f(x) = 1x + 5 mod 26  does the same as g(h(x))
        - g(x) = 1x + 2 mod 26
        - h(x) = 1x + 3 mod 26
    - f3(x) = a1*a2*x + a2*b1 + b2
    - For a1 = 3, b1 = 5 & a2 = 11, b2 = 7: a3 = 33 & b3 = 62
    - No, effective key is not increased as we're still able to decrypt double with a single
