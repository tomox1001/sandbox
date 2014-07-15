#!/usr/bin/env python
# -*- coding: utf-8 -*-

def main():
    name = input("お名前は？ ")
    age = input("何歳は？ ")
    print("こんにちは。%sさん(%d歳)" % (name, int(age)))

if __name__ == "__main__":
    main()
