def main():
    try:
        a=int(input('Enter a valid number: '))
        print(a)
        return a

    except Exception as e:
        print(e)

    finally:
        print("i am inside finally.")

main()

#Finally is useful inside a function , let's say we try block is succeful and returns a value leavinf some neccessary code un-executed.
#To takle that we use fnally which gurrenties a execution of program even if return is hit.