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

## Real-World Planning Permission (Key Considerations)

Please note that the rules implemented in this script are a simplification. In reality, UK planning permission for fences, gates, and walls is governed by factors such as (based on a Perplexity search):

* **Height Restrictions:** Planning permission is generally required if the structure exceeds 1 metre in height when adjacent to a highway or footpath, or 2 metres in other locations.
* **Listed Buildings and Conservation Areas:** Planning permission is usually required for any fence, gate, or wall work on listed buildings or within their grounds. In conservation areas, stricter rules may apply.
* **Alterations and Maintenance:** You typically don't need permission to alter, maintain, or take down an existing structure if its height isn't increased.
* **Other Restrictions:** Permitted development rights can be removed in certain areas. Structures shouldn't enclose land in a way that changes its use.

**Source:** Perplexity Search (UK planning permission rules for gate, wall, fence, or other)

**It is crucial to consult your local planning authority for accurate and specific advice related to your situation.** This script provides a basic illustration and should not be used for making real-world planning decisions.

## Perplexity output:
In the UK, planning permission rules for gates, walls, fences, and similar structures are governed by permitted development rights. Here are the key guidelines:

- **Height Restrictions**:
  - Planning permission is required if the structure exceeds **1 metre in height** when adjacent to a highway used by vehicles or a footpath.
  - For other locations, the height limit is **2 metres** without planning permission[1][2][3].

- **Listed Buildings and Conservation Areas**:
  - If your property is a **listed building** or within its curtilage, planning permission is required regardless of height.
  - In **conservation areas**, additional restrictions may apply, and you may need consent even for taking down existing structures[2][3][5].

- **Alterations and Maintenance**:
  - You do not need planning permission to alter, maintain, or take down an existing fence, wall, or gate as long as its height is not increased[2][5][6].

- **Other Restrictions**:
  - Permitted development rights may be removed in certain areas due to **Article Four Directions** or specific planning conditions.
  - Structures must not enclose land that changes its use (e.g., converting agricultural land to private garden requires permission)[6].

Always consult your local planning authority for specific advice tailored to your property and area.

Citations:
[1] Fences - Gates - Walls - Permitted Development - TownPlanning.info https://www.townplanning.info/permitted-development/fences-gates-walls/
[2] Do I need planning permission to construct a fence, wall or gate? https://www.hastings.gov.uk/planning/need/fencewallgate/
[3] Walls and fences - Chelmsford City Council https://www.chelmsford.gov.uk/planning-and-building-control/planning-advice-and-permissions/check-if-you-need-planning-permission/walls-and-fences/
[4] Do driveway gates need planning permission? https://charltonsgates.com/do-driveway-gates-need-planning-permission/
[5] Do I need Planning Permission for Fences, Gates and Garden Walls? https://www.drawingandplanning.com/do-i-need-planning-permission/i-need-planning-permission-fences-gates-gardens/
[6] Gates, fences, walls and other means of enclosure - Planning Aid https://www.planningaid.co.uk/hc/en-us/articles/203210521-Gates-fences-walls-and-other-means-of-enclosure
[7] Planning Permission - Fences, gates and garden walls https://www.planningportal.co.uk/permission/common-projects/fences-gates-and-garden-walls/planning-permission/
[8] The Town and Country Planning (General Permitted Development ... https://www.legislation.gov.uk/uksi/2015/596/schedule/2/part/2/crossheading/class-a-gates-fences-walls-etc