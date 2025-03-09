from page_objects.base_page_objects import TodoPage
from playwright.sync_api import Page, expect
import pytest
import allure

TODO_NAMES = ["text Ola", "send Ola cat meme", "ask Ola about her day"]

@pytest.fixture()
def todo_page(page: Page) -> TodoPage:
    return TodoPage(page)

def test_clear_completed_when_all_todos_are_completed(todo_page: TodoPage) -> None:
    todo_page.open_todo_website()
    todo_page.click_todo_input_field()
    for todo_name in TODO_NAMES:
        todo_page.enter_todo_name(todo_name)
        todo_page.save_todo()
    todo_page.get_all_todos_selected_as_completed()
    todo_page.display_completed_todos()
    todo_page.take_screen_shot("test clear completed - all todos completed - before clicking button")
    todo_page.click_clear_completed_button()
    todo_page.take_screen_shot("test clear completed - all todos completed - after clicking button")
    assert(len(todo_page.get_todos_completed_toggle_locators()) == 0)

def test_clear_completed_when_only_one_todo_is_completed_checking_number_of_todos(todo_page: TodoPage) -> None:
    todo_page.open_todo_website()
    todo_page.click_todo_input_field()
    for todo_name in TODO_NAMES:
        todo_page.enter_todo_name(todo_name)
        todo_page.save_todo()
    todo_page.mark_todo_as_completed(1)
    todo_page.take_screen_shot("test clear completed - one todo completed - before clicking button - len")
    todo_page.click_clear_completed_button()
    todo_page.take_screen_shot("test clear completed - one todo completed - after clicking button - len")
    assert(len(todo_page.get_todos_completed_toggle_locators()) == len(TODO_NAMES) - 1)

def test_clear_completed_when_only_one_todo_is_completed_checking_whether_correct_todo_was_cleared(todo_page: TodoPage) -> None:
    todo_page.open_todo_website()
    todo_page.click_todo_input_field()
    for todo_name in TODO_NAMES:
        todo_page.enter_todo_name(todo_name)
        todo_page.save_todo()
    todo_page.mark_todo_as_completed(1)
    todo_page.take_screen_shot("test clear completed - one todo completed - before clicking button - name")
    todo_page.click_clear_completed_button()
    todo_page.take_screen_shot("test clear completed - one todo completed - after clicking button - name")
    todo_locator = todo_page.get_todo_locator(TODO_NAMES[1])
    expect(todo_locator).to_have_count(0)