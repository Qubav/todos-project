from page_objects.base_page_objects import TodoPage
from playwright.sync_api import Page, expect
import pytest
import allure

@pytest.fixture()
def todo_page(page: Page) -> TodoPage:
    return TodoPage(page)

def test_add_new_todo(todo_page: TodoPage) -> None:
    todo_page.open_todo_website()
    todo_page.click_todo_input_field()
    todo_page.enter_todo_name("text Ola")
    todo_page.save_todo()
    todo_locator = todo_page.get_todo_locator("text Ola")
    expect(todo_locator).to_have_count(1)