import pytest

def main():
    pytest_args = ["-v", "."]
    exit_code = pytest.main(pytest_args)

    exit(exit_code)

if __name__ == "__main__":
    main()

