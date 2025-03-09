from page_objects.base_page_objects import TodoPage
from playwright.sync_api import Page, expect
import pytest
import allure

TODO_NAMES = ["text Ola", "send Ola cat meme", "ask Ola about her day"]

@pytest.fixture()
def todo_page(page: Page) -> TodoPage:
    return TodoPage(page)

def test_complete_all_todos(todo_page: TodoPage) -> None:
    todo_page.open_todo_website()
    todo_page.click_todo_input_field()
    for todo_name in TODO_NAMES:
        todo_page.enter_todo_name(todo_name)
        todo_page.save_todo()
    todo_page.take_screen_shot("all todos completed - before")
    todo_page.get_all_todos_selected_as_completed()
    todo_page.display_completed_todos()
    todo_page.take_screen_shot("all todos completed - after")
    assert(len(todo_page.get_todos_completed_toggle_locators()) == len(TODO_NAMES))

def test_uncomplete_all_todos(todo_page: TodoPage) -> None:
    todo_page.open_todo_website()
    todo_page.click_todo_input_field()
    for todo_name in TODO_NAMES:
        todo_page.enter_todo_name(todo_name)
        todo_page.save_todo()
    todo_page.take_screen_shot("all todos uncompleted - before")
    todo_page.get_all_todos_selected_as_completed()
    todo_page.get_all_todos_selected_as_completed()
    todo_page.display_active_todos()
    todo_page.take_screen_shot("all todos uncompleted - after")
    assert(len(todo_page.get_todos_completed_toggle_locators()) == len(TODO_NAMES))

def test_complete_all_todos_with_one_todo_completed_before(todo_page: TodoPage) -> None:
    todo_page.open_todo_website()
    todo_page.click_todo_input_field()
    for todo_name in TODO_NAMES:
        todo_page.enter_todo_name(todo_name)
        todo_page.save_todo()
    todo_page.mark_todo_as_completed(1)
    todo_page.take_screen_shot("all todos completed before - one todo completed before")
    todo_page.get_all_todos_selected_as_completed()
    todo_page.display_completed_todos()
    todo_page.take_screen_shot("all todos completed after - one todo completed before")
    assert(len(todo_page.get_todos_completed_toggle_locators()) == len(TODO_NAMES))