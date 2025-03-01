from page_objects.base_page_objects import TodoPage
from playwright.sync_api import Page, expect
import pytest
import allure

TODO_NAMES = ["text Ola", "send Ola cat meme", "ask Ola abou her day"]

@pytest.fixture()
def todo_page(page: Page) -> TodoPage:
    return TodoPage(page)

def test_add_multiple_todos(todo_page: TodoPage) -> None:
    todo_page.open_todo_website()
    todo_page.click_todo_input_field()
    for todo_name in TODO_NAMES:
        todo_page.enter_todo_name(todo_name)
        todo_page.save_todo()
    todo_page.take_screen_shot("multiple todos added test")
    assert(len(todo_page.get_todos_completed_toggle_locators()) == len(TODO_NAMES))

def test_check_nth_todo_name(todo_page: TodoPage) -> None:
    todo_page.open_todo_website()
    todo_page.click_todo_input_field()
    for todo_name in TODO_NAMES:
        todo_page.enter_todo_name(todo_name)
        todo_page.save_todo()
    todo_page.take_screen_shot("check nth todo name")
    todo_locator = todo_page.get_todo_locator(TODO_NAMES[len(TODO_NAMES) - 1])
    expect(todo_locator).to_have_count(1)

def test_check_first_todo_name(todo_page: TodoPage) -> None:
    todo_page.open_todo_website()
    todo_page.click_todo_input_field()
    for todo_name in TODO_NAMES:
        todo_page.enter_todo_name(todo_name)
        todo_page.save_todo()
    todo_page.take_screen_shot("check nth todo name")
    todo_locator = todo_page.get_todo_locator(TODO_NAMES[0])
    expect(todo_locator).to_have_count(1)