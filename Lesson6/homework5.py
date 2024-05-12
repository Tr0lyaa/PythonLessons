my_list = ["яблоко", "банан", "апельсин", "ананас", "гранат", "мандарин"]
print("List:", my_list)
print("First element: " + my_list[0], "Last element: " + my_list[-1], sep="\n")
print("Sublist:", my_list[2:4])
my_list[2] = "груша"
print("Modified list: ", my_list, "\n" , sep="")

my_dict = {"Apple": "яблоко", "Banana": "Банан", "Orange": "Апельсин"}
print("Dictionary:", my_dict)
print("Translation:", my_dict[input("Введите слово для перевода: ")])
my_dict["Apple"] = "Яблоко"
my_dict.update({"Pineapple": "Ананас"})
print("Modified dictionary:", my_dict)
