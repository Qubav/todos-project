from page_objects.base_page_objects import TodoPage
from playwright.sync_api import Page, expect
import pytest
import allure

TODOS = ["text Ola", "send cat meme to Ola", "go to the gym"]
TODO_TO_DESTROY = 0

@pytest.fixture()
def todo_page(page: Page) -> TodoPage:
    return TodoPage(page)

def test_destroy_todo(todo_page: TodoPage) -> None:
    todo_page.open_todo_website()
    todo_page.click_todo_input_field()
    todo_page.enter_todo_name("text Ola")
    todo_page.save_todo()
    todo_page.take_screen_shot("todo before destroying")
    todo_page.hover_over_todo("text Ola")
    todo_page.destroy_todo()
    todo_locator = todo_page.get_todo_locator("text Ola")
    todo_page.take_screen_shot("todo after destroying")
    expect(todo_locator).to_have_count(0)