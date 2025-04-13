import unittest

from typing import Literal, Dict

# Please take a look at the project's repo:
# https://github.com/lzrdGreen/uk-planning-permission-check

def _is_universal_category(site_category: str) -> bool:
    """
    Checks if the site category falls under the universal rules.

    Args:
        site_category (str): The category of the site (e.g., "2U1").

    Returns:
        bool: True if it's a universal category, False otherwise.
    """
    return site_category.startswith("2U")

def _check_other_conditions(
    is_highway_adjacent: bool = False,
    faces_listed_building: bool = False,
    height_above_2m: bool = False,
    is_listed_building_constraint: bool = False,
    is_article_2_3_land: bool = False,
    is_article_2_4_land: bool = False,
    is_article_4_directive: bool = False,
    is_aonb: bool = False,
    affects_tpo: bool = False,
    pd_rights_removed: bool = False,
    is_new_build_restriction: bool = False,
) -> bool:
    """
    Checks if any of the 'other' conditions requiring planning permission are met.

    Args:
        is_highway_adjacent (bool): True if adjacent to a highway.
        faces_listed_building (bool): True if facing a listed building.
        height_above_2m (bool): True if height is above 2 meters.
        is_listed_building_constraint (bool): True if it's a listed building.
        is_article_2_3_land (bool): True if it's Article 2(3) Land.
        is_article_2_4_land (bool): True if it's Article 2(4) Land.
        is_article_4_directive (bool): True if an Article 4 Directive applies.
        is_aonb (bool): True if within an Area of Outstanding Natural Beauty.
        affects_tpo (bool): True if works affect a Tree Preservation Order.
        pd_rights_removed (bool): True if permitted development rights were removed.
        is_new_build_restriction (bool): True if it's a new build with restrictions.

    Returns:
        bool: True if any condition is met, False otherwise.
    """
    return (
        is_highway_adjacent
        or faces_listed_building
        or height_above_2m
        or is_listed_building_constraint
        or is_article_2_3_land
        or is_article_2_4_land
        or is_article_4_directive
        or is_aonb
        or affects_tpo
        or pd_rights_removed
        or is_new_build_restriction
    )

# A scalable Python function to determine if planning permission is required
# for a fence, gate, or wall based on given rules.
def check_planning_permission(
    site_category: str,
    is_highway_adjacent: bool = False,
    faces_listed_building: bool = False,
    height_up_to_1m: bool = False,
    height_above_1m_to_2m: bool = False,
    height_above_2m: bool = False,
    is_listed_building_constraint: bool = False,
    is_article_2_3_land: bool = False,
    is_article_2_4_land: bool = False,
    is_article_4_directive: bool = False,
    is_aonb: bool = False,
    affects_tpo: bool = False,
    pd_rights_removed: bool = False,
    is_new_build_restriction: bool = False,
) -> Literal["Y", "N", "Unknown Category"]:
    """
    Determines if planning permission is required for a fence, gate, or wall based on simplified UK rules.

    Args:
        site_category (str): The category of the site (e.g., "2U1", "2A3").
        is_highway_adjacent (bool): True if adjacent to a highway used by vehicular traffic.
        faces_listed_building (bool): True if facing onto a property with a listed building.
        height_up_to_1m (bool): True if height is up to 1 meter.
        height_above_1m_to_2m (bool): True if height is above 1 meter and up to 2 meters.
        height_above_2m (bool): True if height is above 2 meters.
        is_listed_building_constraint (bool): True if the property itself is a listed building.
        is_article_2_3_land (bool): True if the land is designated as Article 2(3) Land.
        is_article_2_4_land (bool): True if the land is designated as Article 2(4) Land.
        is_article_4_directive (bool): True if an Article 4 Directive removes PD rights.
        is_aonb (bool): True if the location is within an Area of Outstanding Natural Beauty.
        affects_tpo (bool): True if works affect a Tree Preservation Order.
        pd_rights_removed (bool): True if permitted development rights were previously removed.
        is_new_build_restriction (bool): True if it's a new build property with restrictions.

    Returns:
        Literal["Y", "N", "Unknown Category"]: "Y" if permission is required, "N" if not,
                                                "Unknown Category" if the category is not recognized.
    """
    if not isinstance(site_category, str):
        raise TypeError("site_category must be a string.")

    # Validate boolean inputs
    boolean_inputs = [is_highway_adjacent, faces_listed_building, height_up_to_1m,
                      height_above_1m_to_2m, height_above_2m, is_listed_building_constraint,
                      is_article_2_3_land, is_article_2_4_land, is_article_4_directive,
                      is_aonb, affects_tpo, pd_rights_removed, is_new_build_restriction]
    for input_value in boolean_inputs:
        if not isinstance(input_value, bool):
            raise TypeError(f"All condition flags must be boolean, but got {type(input_value)}.")

    if _is_universal_category(site_category):
        return "Y"
    elif site_category.startswith("2A"):
        if _check_other_conditions(
            is_highway_adjacent,
            faces_listed_building,
            height_above_2m,
            is_listed_building_constraint,
            is_article_2_3_land,
            is_article_2_4_land,
            is_article_4_directive,
            is_aonb,
            affects_tpo,
            pd_rights_removed,
            is_new_build_restriction,
        ):
            return "Y"
        else:
            return "N"
    else:
        return "Unknown Category"


# A simplified set of rules and conditions to determine if planning permission is required for erecting a fence, gate, or wall
# It is represented as List of Dictionaries
# Each dictionary represents a row (excluding the header), and the keys are the column headers
# Even if the rules are hardcoded now, they can be made externally configurable (via JSON or YAML)  
set_of_rules = [
    {
        "Category": "2U1",
        "HighwayAdjacent": "y",
        "ListedBuildingFacing": "y",
        "HeightUpTo1m": "y",
        "HeightAbove1mTo2m": "y",
        "HeightAbove2m": "y",
        "ListedBuildingConstraint": "y",
        "Article2_3": "y",
        "Article2_4": "y",
        "Article4Directive": "y",
        "AONB": "y",
        "TPO": "y",
        "PDRemovedPrevious": "y",
        "NewBuildRestriction": "y",
        "PermissionRequired": "Yes"
    },
    {
        "Category": "2U2",
        "HighwayAdjacent": "y",
        "ListedBuildingFacing": "y",
        "HeightUpTo1m": "y",
        "HeightAbove1mTo2m": "y",
        "HeightAbove2m": "y",
        "ListedBuildingConstraint": "y",
        "Article2_3": "y",
        "Article2_4": "y",
        "Article4Directive": "y",
        "AONB": "y",
        "TPO": "y",
        "PDRemovedPrevious": "y",
        "NewBuildRestriction": "y",
        "PermissionRequired": "Yes"
    },
    {
        "Category": "2U3",
        "HighwayAdjacent": "y",
        "ListedBuildingFacing": "y",
        "HeightUpTo1m": "y",
        "HeightAbove1mTo2m": "y",
        "HeightAbove2m": "y",
        "ListedBuildingConstraint": "y",
        "Article2_3": "y",
        "Article2_4": "y",
        "Article4Directive": "y",
        "AONB": "y",
        "TPO": "y",
        "PDRemovedPrevious": "y",
        "NewBuildRestriction": "y",
        "PermissionRequired": "Yes"
    },
    {
        "Category": "2U4",
        "HighwayAdjacent": "y",
        "ListedBuildingFacing": "y",
        "HeightUpTo1m": "y",
        "HeightAbove1mTo2m": "y",
        "HeightAbove2m": "y",
        "ListedBuildingConstraint": "y",
        "Article2_3": "y",
        "Article2_4": "y",
        "Article4Directive": "y",
        "AONB": "y",
        "TPO": "y",
        "PDRemovedPrevious": "y",
        "NewBuildRestriction": "y",
        "PermissionRequired": "Yes"
    },
    {
        "Category": "2U5",
        "HighwayAdjacent": "y",
        "ListedBuildingFacing": "y",
        "HeightUpTo1m": "y",
        "HeightAbove1mTo2m": "y",
        "HeightAbove2m": "y",
        "ListedBuildingConstraint": "y",
        "Article2_3": "y",
        "Article2_4": "y",
        "Article4Directive": "y",
        "AONB": "y",
        "TPO": "y",
        "PDRemovedPrevious": "y",
        "NewBuildRestriction": "y",
        "PermissionRequired": "Yes"
    },
    {
        "Category": "2U6",
        "HighwayAdjacent": "y",
        "ListedBuildingFacing": "y",
        "HeightUpTo1m": "y",
        "HeightAbove1mTo2m": "y",
        "HeightAbove2m": "y",
        "ListedBuildingConstraint": "y",
        "Article2_3": "y",
        "Article2_4": "y",
        "Article4Directive": "y",
        "AONB": "y",
        "TPO": "y",
        "PDRemovedPrevious": "y",
        "NewBuildRestriction": "y",
        "PermissionRequired": "Yes"
    },
    {
        "Category": "2U7",
        "HighwayAdjacent": "y",
        "ListedBuildingFacing": "y",
        "HeightUpTo1m": "y",
        "HeightAbove1mTo2m": "y",
        "HeightAbove2m": "y",
        "ListedBuildingConstraint": "y",
        "Article2_3": "y",
        "Article2_4": "y",
        "Article4Directive": "y",
        "AONB": "y",
        "TPO": "y",
        "PDRemovedPrevious": "y",
        "NewBuildRestriction": "y",
        "PermissionRequired": "Yes"
    },
    {
        "Category": "2U8",
        "HighwayAdjacent": "y",
        "ListedBuildingFacing": "y",
        "HeightUpTo1m": "y",
        "HeightAbove1mTo2m": "y",
        "HeightAbove2m": "y",
        "ListedBuildingConstraint": "y",
        "Article2_3": "y",
        "Article2_4": "y",
        "Article4Directive": "y",
        "AONB": "y",
        "TPO": "y",
        "PDRemovedPrevious": "y",
        "NewBuildRestriction": "y",
        "PermissionRequired": "Yes"
    },
    {
        "Category": "2U9",
        "HighwayAdjacent": "y",
        "ListedBuildingFacing": "y",
        "HeightUpTo1m": "y",
        "HeightAbove1mTo2m": "y",
        "HeightAbove2m": "y",
        "ListedBuildingConstraint": "y",
        "Article2_3": "y",
        "Article2_4": "y",
        "Article4Directive": "y",
        "AONB": "y",
        "TPO": "y",
        "PDRemovedPrevious": "y",
        "NewBuildRestriction": "y",
        "PermissionRequired": "Yes"
    },
    {
        "Category": "2A1",
        "HighwayAdjacent": "y",
        "ListedBuildingFacing": "y",
        "HeightUpTo1m": "y",
        "HeightAbove1mTo2m": "y",
        "HeightAbove2m": "y",
        "ListedBuildingConstraint": "y",
        "Article2_3": "y",
        "Article2_4": "y",
        "Article4Directive": "y",
        "AONB": "y",
        "TPO": "y",
        "PDRemovedPrevious": "y",
        "NewBuildRestriction": "y",
        "PermissionRequired": "Yes"
    },
    {
        "Category": "2A2",
        "HighwayAdjacent": "y",
        "ListedBuildingFacing": "y",
        "HeightUpTo1m": "y",
        "HeightAbove1mTo2m": "y",
        "HeightAbove2m": "y",
        "ListedBuildingConstraint": "y",
        "Article2_3": "n",
        "Article2_4": "n",
        "Article4Directive": "n",
        "AONB": "n",
        "TPO": "n",
        "PDRemovedPrevious": "n",
        "NewBuildRestriction": "n",
        "PermissionRequired": "Yes"
    },
    {
        "Category": "2A3",
        "HighwayAdjacent": "y",
        "ListedBuildingFacing": "y",
        "HeightUpTo1m": "y",
        "HeightAbove1mTo2m": "y",
        "HeightAbove2m": "n",
        "ListedBuildingConstraint": "n",
        "Article2_3": "y",
        "Article2_4": "n",
        "Article4Directive": "n",
        "AONB": "n",
        "TPO": "n",
        "PDRemovedPrevious": "n",
        "NewBuildRestriction": "n",
        "PermissionRequired": "Yes"
    },
    {
        "Category": "2A4",
        "HighwayAdjacent": "y",
        "ListedBuildingFacing": "y",
        "HeightUpTo1m": "y",
        "HeightAbove1mTo2m": "n",
        "HeightAbove2m": "y",
        "ListedBuildingConstraint": "n",
        "Article2_3": "n",
        "Article2_4": "y",
        "Article4Directive": "n",
        "AONB": "n",
        "TPO": "n",
        "PDRemovedPrevious": "n",
        "NewBuildRestriction": "n",
        "PermissionRequired": "Yes"
    },
    {
        "Category": "2A5",
        "HighwayAdjacent": "n",
        "ListedBuildingFacing": "y",
        "HeightUpTo1m": "y",
        "HeightAbove1mTo2m": "y",
        "HeightAbove2m": "y",
        "ListedBuildingConstraint": "n",
        "Article2_3": "n",
        "Article2_4": "n",
        "Article4Directive": "y",
        "AONB": "n",
        "TPO": "n",
        "PDRemovedPrevious": "n",
        "NewBuildRestriction": "n",
        "PermissionRequired": "Yes"
    },
    {
        "Category": "2A6",
        "HighwayAdjacent": "n",
        "ListedBuildingFacing": "y",
        "HeightUpTo1m": "y",
        "HeightAbove1mTo2m": "y",
        "HeightAbove2m": "y",
        "ListedBuildingConstraint": "y",
        "Article2_3": "n",
        "Article2_4": "n",
        "Article4Directive": "n",
        "AONB": "n",
        "TPO": "n",
        "PDRemovedPrevious": "y",
        "NewBuildRestriction": "n",
        "PermissionRequired": "Yes"
    }
]
    
class TestPlanningPermission(unittest.TestCase):

    def test_universal_category(self):
        self.assertEqual(check_planning_permission('2U1'), 'Y')
        self.assertEqual(check_planning_permission('2U9'), 'Y')

    def test_other_category_no_conditions(self):
        self.assertEqual(check_planning_permission('2A3'), 'N')

    def test_other_category_single_condition(self):
        self.assertEqual(check_planning_permission('2A1', is_highway_adjacent=True), 'Y')
        self.assertEqual(check_planning_permission('2A4', is_listed_building_constraint=True), 'Y')
        self.assertEqual(check_planning_permission('2A6', height_above_2m=True), 'Y')

    def test_other_category_multiple_conditions(self):
        self.assertEqual(check_planning_permission('2A2', faces_listed_building=True, is_article_4_directive=True), 'Y')
        self.assertEqual(check_planning_permission('2A5', is_aonb=True, pd_rights_removed=True, is_new_build_restriction=True), 'Y')

    def test_unknown_category(self):
        self.assertEqual(check_planning_permission('2B1'), 'Unknown Category')

    def test_invalid_input_category_type(self):
        with self.assertRaises(TypeError):
            check_planning_permission(123)

    def test_invalid_input_boolean_type(self):
        with self.assertRaises(TypeError):
            check_planning_permission('2A1', is_highway_adjacent='yes')

if __name__ == '__main__':
        
    # --- Example Scenarios ---
    # Although we use unittest but printing out almost everything also works
    print("--- Universal Category Examples ---")
    print(f"Category 2U1: Permission Required? {check_planning_permission('2U1')}")
    print(f"Category 2U9: Permission Required? {check_planning_permission('2U9')}")
    print(f"Category 2U5 with other conditions: Permission Required? {check_planning_permission('2U5', is_highway_adjacent=True, height_above_2m=True)}")

    print("\n--- Other Categories (2A) Examples ---")
    print(f"Category 2A1, Adjacent to highway: Permission Required? {check_planning_permission('2A1', is_highway_adjacent=True)}")
    print(f"Category 2A2, Faces listed building: Permission Required? {check_planning_permission('2A2', faces_listed_building=True)}")
    print(f"Category 2A3, Height above 2m: Permission Required? {check_planning_permission('2A3', height_above_2m=True)}")
    print(f"Category 2A4, Listed building constraint: Permission Required? {check_planning_permission('2A4', is_listed_building_constraint=True)}")
    print(f"Category 2A5, Article 2(3) Land: Permission Required? {check_planning_permission('2A5', is_article_2_3_land=True)}")
    print(f"Category 2A6, No conditions met: Permission Required? {check_planning_permission('2A6')}")

    print("\n--- Other Categories (2A) - Multiple Conditions ---")
    print(f"Category 2A1, Highway adjacent AND Article 4 Directive: Permission Required? {check_planning_permission('2A1', is_highway_adjacent=True, is_article_4_directive=True)}")
    print(f"Category 2A3, Faces listed building AND AONB AND PD rights removed: Permission Required? {check_planning_permission('2A3', faces_listed_building=True, is_aonb=True, pd_rights_removed=True)}")
    print(f"Category 2A5, Height up to 1m AND no other constraints: Permission Required? {check_planning_permission('2A5', height_up_to_1m=True)}") # Should be 'N'

    print("\n--- Unknown Category ---")
    print(f"Category 2B1: Permission Required? {check_planning_permission('2B1')}")
    
    # Example Usage (Demonstrating Error Handling)
    print("--- Example Usage with Error Handling ---")
    try:
        result = check_planning_permission(123)
        print(f"Result: {result}")
    except TypeError as e:
        print(f"Error (Example): {e}")

    try:
        result = check_planning_permission("2A1", is_highway_adjacent="yes")
        print(f"Result: {result}")
    except TypeError as e:
        print(f"Error (Example): {e}")

    unittest.main()
    
    
    
# --- Example of using the function with a Pandas DataFrame ---
# import pandas as pd
#
# dat = {
#     'Category': ['2U1', '2A2', '2A3', '2A5'],
#     'HighwayAdjacent': [True, False, True, False],
#     'FacesListedBuilding': [True, True, False, False],
#     'HeightAbove2m': [True, False, True, False],
#     'IsListedBuildingConstraint': [True, False, False, False],
#     'Article2_3': [False, False, True, False],
#     'Article4Directive': [False, False, False, True],
#     'PermissionRequired_Expected': ['Y', 'Y', 'Y', 'Y'] # Expected outcomes for testing
# }
#
# df = pd.DataFrame(dat)
#
# def check_permission_df(row):
#     return check_planning_permission(
#         row['Category'],
#         is_highway_adjacent=row['HighwayAdjacent'],
#         faces_listed_building=row['FacesListedBuilding'],
#         height_above_2m=row['HeightAbove2m'],
#         is_listed_building_constraint=row['IsListedBuildingConstraint'],
#         is_article_2_3_land=row['Article2_3'],
#         is_article_4_directive=row['Article4Directive']
#         # Add other relevant columns here
#     )
#
# df['PermissionRequired_Calculated'] = df.apply(check_permission_df, axis=1)
#
# print(df)