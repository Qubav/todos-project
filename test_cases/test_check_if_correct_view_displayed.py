from page_objects.base_page_objects import TodoPage
from playwright.sync_api import Page, expect
import pytest
import allure

@pytest.fixture()
def todo_page(page: Page) -> TodoPage:
    return TodoPage(page)

def test_display_all_view(todo_page: TodoPage) -> None:
    todo_page.open_todo_website()
    todo_page.click_todo_input_field()
    todo_page.enter_todo_name("text Ola")
    todo_page.save_todo()
    todo_page.display_all_todos()
    expect(todo_page.get_all_button_selected_locator()).to_have_count(1)

def test_display_completed_view(todo_page: TodoPage) -> None:
    todo_page.open_todo_website()
    todo_page.click_todo_input_field()
    todo_page.enter_todo_name("text Ola")
    todo_page.save_todo()
    todo_page.display_active_todos()
    expect(todo_page.get_active_button_selected_locator()).to_have_count(1)

def test_display_active_view(todo_page: TodoPage) -> None:
    todo_page.open_todo_website()
    todo_page.click_todo_input_field()
    todo_page.enter_todo_name("text Ola")
    todo_page.save_todo()
    todo_page.display_completed_todos()
    expect(todo_page.get_completed_button_selected_locator()).to_have_count(1)