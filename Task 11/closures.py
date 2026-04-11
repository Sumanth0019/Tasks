def outer():
    message = "how are you?"

    def inner():
        print(message)

    return inner

func = outer()
func()