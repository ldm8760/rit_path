import code
from University import University

def testFunc():
    print("xyz123")


def main():
    uni = University.load_courses("data.csv")
    q = quit

    allowed_locals = {
        'uni': uni,         # Add the `uni` object (the loaded courses)
        'test_func': testFunc,  # Add the specific function
        'q': q
    }
    print("\nType commands to interact with the data.")
    code.interact(local=allowed_locals)
    

if __name__ == "__main__":
    main()