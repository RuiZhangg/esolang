# esolang ![](https://github.com/ruizhangg/esolang/workflows/tests/badge.svg)

A simple esolang for experimenting with different syntax and semantics of programming languages.

Usage example:
```
python3 esolang
esolang> (1*2)+3+4*(5-6)
1
esolang> a=2; a+a?a:a*a
4
esolang> a=0; for i in range(10) {a = a + i}; a
45
esolang> f = lambda a: {c = 0;b=a-3;for i in range(b){a%(i+2)?c=c+1:c=c};c?print(a):};g = lambda d:{for j in range(d-3) {f(j+3)}}; g(30)
3
5
7
11
13
17
19
23
29
esolang> 
```