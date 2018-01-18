# NameError: (undefined variable)
def fun_name(f):
    try:
        cat = f + dog
    except NameError as e:
        print('Handling run-time error:', e)

fun_name(1)
