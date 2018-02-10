def safe_pawns(pawns):
    # Creating base of safe diagonal positions
    base = {"a": "b", "b": ("a", "c"), "c": ("b", "d"), "d": ("c", "e"), 
            "e": ("d", "f"), "f": ("e", "g"), "g": ("f", "h"), "h": "g"}
    count = 0
    for i in pawns:
        for a in base[i[0]]:
            if (a + str(int(i[1]) - 1)) in pawns: 
                count += 1
                break
    return count

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert safe_pawns({"b4", "d4", "f4", "c3", "e3", "g5", "d2"}) == 6
    assert safe_pawns({"b4", "c4", "d4", "e4", "f4", "g4", "e5"}) == 1
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")