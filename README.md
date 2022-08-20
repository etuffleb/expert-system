# Expert-system

This project involves creating an expert system in proposal calculation. In other words, a program that can reason on a set of rules and initial facts to deduce other facts.

Implemented a backward-chaining inference engine. Rules and facts are given as a text file, the format of which is described in the appendix. A fact can be any uppercase alphabetical character. The program accepts one parameter, which is the input file. It contains a list of rules, then a list of initial facts, then a list of queries. For each of these queries, the program, given the facts and rules given, tells if the query is true, false, or undetermined.

## Symbols and rules of precedence
The following symbols are defined, in order of decreasing priority:
* __(__ and __)__ which are fairly obvious. Example : A + (B | C) => D
* __!__   which means NOT. Example : !B
* __+__   which means AND. Example : A + B
* __|__   which means OR. Example : A | B
* __ˆ__   which means XOR. Example : A ˆ B
* __=>__  which means "implies". Example : A + B => C
* __<=>__ which means "if and only if". Example : A + B <=> C

## Example
```bash
# Example of input file

# Rules and symbols
C => E # C implies E
A + B + C => D # A and B and C implies D
A | B => C # A or B implies C
A + !B => F # A and not B implies F
C | !G => H # C or not G implies H
V ^ W => X # V xor W implies X
A + B => Y + Z # A and B implies Y and Z
E + F => !V # E and F implies not V
A + B <=> C # A and B if and only if C
A + B <=> !C # A and B if and only if not C

# Initial facts
= ABG

# Queries
?GVX
```



