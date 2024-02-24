user_word = input("Digite a palavra que deseja checar:\n\nR: ").lower()

user_word = "".join([i for i in user_word if i.isalpha()])

print(user_word)

# b a n a n a

palindrome = []

for i in range(1, len(user_word)+1):
    palindrome.append(user_word[-i])



palindrome_str = "".join(palindrome)

if user_word == palindrome_str:
    print("Essa palavra é um palíndromo.")

else:
    print("Essa palavra não é um palíndromo.")