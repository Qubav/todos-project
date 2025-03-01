from playwright.sync_api import  Page, Locator
from environment import URL
import allure

class TodoPage:

    def __init__(self, page: Page) -> None:
        self.page = page
        self.url = URL
        self.todo_input_field = "input.new-todo"
        self.button_active = "a[href='#/active']"
        self.button_all = "a[href='#/all']"
        self.button_completed = "a[href='#/completed']"
        self.todo_locating = "label"
        self.button_destroy = "button.destroy"
        self.completed_toggle_locating = "input.toggle"
        self.todos_left_displayed_number_locating = "strong"
        self.selected_button_all = "a.selected[href='#/all']"
        self.selected_button_completed = "a.selected[href='#/completed']"
        self.selected_button_active = "a.selected[href='#/active']"

    def open_todo_website(self) -> None:
        self.page.goto(self.url)

    def click_todo_input_field(self) -> None:
        self.page.locator(self.todo_input_field).click()
    
    def enter_todo_name(self, todo_name: str) -> None:
        self.page.locator(self.todo_input_field).fill(todo_name)
    
    def save_todo(self) -> None:
        self.page.locator(self.todo_input_field).press(key="Enter")

    def display_all_todos(self) -> None:
        self.page.locator(self.button_all).click()
    
    def display_completed_todos(self) -> None:
        self.page.locator(self.button_completed).click()
    
    def display_active_todos(self) -> None:
        self.page.locator(self.button_active).click()
    
    def hover_over_todo(self, todo_name: str) -> None:
        self.page.locator(self.todo_locating, has_text=todo_name).hover()
    
    def destroy_todo(self) -> None:
        self.page.locator(self.button_destroy).click()
    
    def get_todo_locator(self, todo_name: str) -> Locator:
        return self.page.locator(self.todo_locating, has_text=todo_name)
    
    def get_todos_completed_toggle_locators(self) -> list[Locator]:
        return self.page.locator(self.completed_toggle_locating).all()

    def take_screen_shot(self, screenshot_name: str) -> None:
        self.page.screenshot(path="screenshots/" + screenshot_name + ".png")
    
    def get_all_button_selected_locator(self) -> Locator:
        return self.page.locator(self.selected_button_all)
    
    def get_active_button_selected_locator(self) -> Locator:
        return self.page.locator(self.selected_button_active)
    
    def get_completed_button_selected_locator(self) -> Locator:
        return self.page.locator(self.selected_button_completed)