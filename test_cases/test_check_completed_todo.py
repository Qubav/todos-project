from page_objects.base_page_objects import TodoPage
from playwright.sync_api import Page, expect
import pytest
import allure

@pytest.fixture()
def todo_page(page: Page) -> TodoPage:
    return TodoPage(page)

def test_completed_todo_in_all_view(todo_page: TodoPage) -> None:
    todo_page.open_todo_website()
    todo_page.click_todo_input_field()
    todo_page.enter_todo_name("go to Grocery store")
    todo_page.save_todo()
    todo_page.mark_todo_as_completed()
    todo_page.display_all_todos()
    todo_page.take_screen_shot("completed todo in display all view")
    todo_locator = todo_page.get_todo_locator("go to Grocery store")
    expect(todo_locator).to_have_count(1)

def test_completed_todo_in_active_view(todo_page: TodoPage) -> None:
    todo_page.open_todo_website()
    todo_page.click_todo_input_field()
    todo_page.enter_todo_name("take Max for a walk")
    todo_page.save_todo()
    todo_page.mark_todo_as_completed()
    todo_page.display_active_todos()
    todo_page.take_screen_shot("completed todo in display active view")
    todo_locator = todo_page.get_todo_locator("take Max for a walk")
    expect(todo_locator).to_have_count(0)

def test_completed_todo_in_display_completed_view(todo_page: TodoPage) -> None:
    todo_page.open_todo_website()
    todo_page.click_todo_input_field()
    todo_page.enter_todo_name("get hudrated")
    todo_page.save_todo()
    todo_page.mark_todo_as_completed()
    todo_page.display_completed_todos()
    todo_page.take_screen_shot("completed todo in display completed view")
    todo_locator = todo_page.get_todo_locator("get hudrated")
    expect(todo_locator).to_have_count(1)

def test_completed_todo_in_display_completed_view_twice_clicked(todo_page: TodoPage) -> None:
    todo_page.open_todo_website()
    todo_page.click_todo_input_field()
    todo_page.enter_todo_name("get hudrated")
    todo_page.save_todo()
    todo_page.mark_todo_as_completed()
    todo_page.display_completed_todos()
    todo_page.take_screen_shot("completed todo in display completed view - twice completed test case - after first click")
    todo_page.mark_todo_as_completed()
    todo_page.take_screen_shot("completed todo in display completed view - twice completed test case - after second click")
    todo_locator = todo_page.get_todo_locator("get hudrated")
    expect(todo_locator).to_have_count(0)