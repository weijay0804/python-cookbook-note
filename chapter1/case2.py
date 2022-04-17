"""

    拆解任意長度的序列

"""

user_record = ("Dave", "dave@example.com", "012-3456-78", "012-456-78")

name, email, *phone_num = user_record

def do_foo(x ,y):
    print("foo", x, y)

def do_bar(s):
    print("bar", s)

if __name__ == "__main__":
    print(name)
    print(email)
    print(phone_num)

    record = [
        ("foo", 1, 2),
        ("bar", "hello"),
        ("foo", 5, 6)
    ]

    for tag, *args in record:
        if tag == "foo":
            do_foo(*args)
        
        elif tag == "bar":
            do_bar(*args)