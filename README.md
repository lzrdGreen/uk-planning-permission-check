# uk-planning-permission-check

The task:
"Welcome to the PlanningHub Code Challenge!

Please provide pseudo or Python code for the given diagram. Your code should determine whether planning permission is required (Y) or not required (N) for a fence, gate, or wall in various scenarios.

If the site falls under the universal category, which should be checked first, planning permission is required. If the site is not in one of the universal categories, other conditions will establish if planning permission is required. Some examples might not require a planning permission and some will require planning permission if multiple conditions are met.

We are keen to understand if you can independently write a scalable code for this type of task. 

We will be scoring your work based on the following criteria:

Diligence: Please ensure you cover all given scenarios including these with multiple variables.
Ability to write code in a structured and readable way: As you will work in a team, it is critical that your code can be easily navigated and modified by other users.
You are welcome to use online tools for writing the code, but please work independently without input from other engineers.
We are looking for scalable, diligent and complete solutions and if you want to impress, please do!
Please let us know which parts of the challenge you found difficult and which parts were easy."

## UK Planning Permission Check (Simplified)

This Python script (`planning_permission.py`) provides a simplified function to determine if planning permission is likely required for erecting a fence, gate, or wall in the UK, based on a set of basic rules and conditions.

## How to Run

1.  **Download the script:** Download the `planning_permission.py` file and save it to your local machine.
2.  **Open your terminal or command prompt.**
3.  **Navigate to the directory** where you saved the `planning_permission.py` file.
4.  **Run the script using the Python interpreter:**

    ```bash
    python planning_permission.py
    ```

    This will execute the script and display the results of several example scenarios and the output of unit tests.

## What it Does

The script defines a function `check_planning_permission` that takes a site category and various boolean flags representing different conditions (e.g., adjacency to a highway, presence of a listed building, height of the structure, etc.). It returns:

* `"Y"` if planning permission is likely required.
* `"N"` if planning permission is likely not required (based on the simplified rules).
* `"Unknown Category"` if the provided site category is not recognized.

The script also includes:

* Helper functions (`_is_universal_category`, `_check_other_conditions`) to organize the rule logic.
* A set of example scenarios demonstrating the function's usage with different inputs.
* Unit tests (using the `unittest` module) to verify the correctness of the `check_planning_permission` function.
* Basic error handling for invalid input types.

## Important Notes

* **Simplified Rules:** Please be aware that this script implements a **highly simplified** version of the UK planning permission rules. Real-world regulations are much more complex and can vary significantly based on local authorities, specific circumstances, and other factors not covered here.
* **Not Legal Advice:** The output of this script should **not** be considered legal advice. Always consult official planning guidance from your local planning authority or a qualified professional for accurate and definitive information.
* **No External Dependencies:** This script relies only on the standard Python library and has no external dependencies.

## Further Development (Optional)

This script could be extended to:

* Incorporate more detailed planning rules and regulations.
* Load rules from external data sources (e.g., CSV, JSON, YAML) for easier configuration and updates.
* Provide more context-specific information based on location or other parameters (though this would significantly increase complexity).
* Be integrated into a larger application or web service via API.
