# TodoMVC Automated Testing  

The project was created to automate the testing of the [TodoMVC](https://todomvc.com/) application using **Playwright** and **pytest**. The tests cover key functionalities of the app, ensuring that todos behave correctly in various scenarios.  

## **Technologies Used:**  
- **Playwright** – for end-to-end testing  
- **pytest** – for test execution  

## **Tested Features:**  

1. **Adding new todos** – Verifies that new tasks can be successfully added.  
2. **Displaying selected views** – Checks if the "All," "Active," and "Completed" views display the correct todos.  
3. **Todo behavior on "Completed" button click** – Ensures that marking a todo as completed updates its state correctly.  
4. **Displayed completed and uncompleted todos in each view** – Confirms that only relevant todos are shown in their respective filters.  
5. **"Complete All" button functionality** – Tests whether all todos can be marked as completed at once.  
6. **"Clear All Completed" option** – Ensures that completed todos are removed when using this feature.  
7. **Todo deletion** – Verifies that individual todos can be successfully removed.  
8. **Editing todo content** – Checks if modifying an existing todo updates its text properly.  

## **Screenshots for Test Verification:**  

During the test execution, screenshots are taken at various stages to allow verification of what is visible in the browser at the time of testing. These screenshots help to confirm that the application behaves as expected during each test case.  

Below, I will provide screenshots for a few selected test cases to demonstrate the process and expected behavior.  

Each test case ensures that the TodoMVC app functions correctly across different scenarios, improving reliability and usability. 

## Test Case: Clear completed - one completed todo ##
Before clicking **Claer completed button**:
![test clear completed - one todo completed - before clicking button - name](https://github.com/user-attachments/assets/99400f9e-67ca-4196-83b4-d4b7434980a2)
After clicking **Claer completed button**:
![test clear completed - one todo completed - after clicking button - name](https://github.com/user-attachments/assets/53c931a4-941b-4a6e-9c28-3d7fef5f996a)

## Test Case: Select all as completed ##
Before clicking **Select all as completed**:
![all todos completed - before](https://github.com/user-attachments/assets/695ee636-340a-4ecb-8811-c092c9a5b0ba)
After clicking **Select all as completed**:
![all todos completed - after](https://github.com/user-attachments/assets/a9798149-9d4c-43ea-996d-8fce7e311fdc)
