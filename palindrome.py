

#determinar si es palindromo o non
# ana   sí es palindromo
# cesar   no es palindromo


def is_palindrome (string: str) -> bool:
    string = string.replace("", "").lower()
    return string == string[::-1]

def run():
    print(is_palindrome("ana"))

if __name__ == '__main__':
    run()





