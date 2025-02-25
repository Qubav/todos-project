from playwright.sync_api import  Page, Locator
from environment import URL

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