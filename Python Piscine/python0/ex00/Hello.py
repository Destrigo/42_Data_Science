ft_list = ["Hello", "tata!"]
ft_tuple = ("Hello", "toto!")
ft_set = {"Hello", "tutu!"}
ft_dict = {"Hello": "titi!"}


ft_list[1] = "World"

ft_tupletmp = list(ft_tuple)
ft_tupletmp[1] = "Netherlands!"
ft_tuple = tuple(ft_tupletmp)

ft_set = {"Amsterdam!", "Hello"}

ft_dict.Hello = "Codam!"

print(ft_list)
print(ft_tuple)
print(ft_set)
print(ft_dict)
