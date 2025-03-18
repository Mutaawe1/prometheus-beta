import pytest
from src.dot_case_converter import to_dot_case

def test_camel_case_conversion():
    assert to_dot_case("helloWorld") == "hello.world"
    assert to_dot_case("camelCaseString") == "camel.case.string"

def test_snake_case_conversion():
    assert to_dot_case("hello_world") == "hello.world"
    assert to_dot_case("snake_case_string") == "snake.case.string"

def test_kebab_case_conversion():
    assert to_dot_case("hello-world") == "hello.world"
    assert to_dot_case("kebab-case-string") == "kebab.case.string"

def test_space_separated_conversion():
    assert to_dot_case("Hello World") == "hello.world"
    assert to_dot_case("Mixed Case String") == "mixed.case.string"

def test_mixed_case_conversion():
    assert to_dot_case("HelloWorld_Test") == "hello.world.test"
    assert to_dot_case("hello-World_Test Case") == "hello.world.test.case"

def test_empty_string():
    assert to_dot_case("") == ""

def test_single_word():
    assert to_dot_case("hello") == "hello"
    assert to_dot_case("HELLO") == "hello"

def test_all_uppercase():
    assert to_dot_case("HELLO_WORLD") == "hello.world"

def test_invalid_input():
    with pytest.raises(TypeError):
        to_dot_case(123)
    with pytest.raises(TypeError):
        to_dot_case(None)

def test_special_characters():
    assert to_dot_case("hello@world") == "hello.world"
    assert to_dot_case("hello world!") == "hello.world"