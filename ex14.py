from sys import argv

script, user_name = argv
prompt = '> '

print(f"hey {user_name}. Im the {script}")
print("I'd like to ask you a few questions")
print(f"do you like me {user_name}")
likes = input(prompt)

print("where do you live")
lives = input(prompt)

print("what kind of computre do you have?")
computer = input(prompt)

print(f"""
        you said that you like me {likes}
        and that you have this type of computer {computer}
        and you live in {lives}
        """
        )
