# 🔍 Airbnb Project - Core Concepts

This document lists the key objects and concepts used in the Airbnb-like roommate finder project. Each concept is categorized into **Object**, **Context**, and **Information** relevant to its use.

| **Object**         | **Context**                          | **Information**                                                                 |
|--------------------|--------------------------------------|----------------------------------------------------------------------------------|
| **User**           | Authentication                       | Name, email, password, login state, preference (veg/non-veg, gender, religion)  |
| **City**           | City Selection Page                  | City name, number of listings, selected city ID                                  |
| **Listing**        | Property Listing Page                | Title, description, rent, photos, availability, occupancy type (single/double)  |
| **Filter**         | Sidebar Filters                      | Gender, food preference, religious preference, occupancy type                   |
| **Authentication** | Login / Register Page                | Email, password validation, auth tokens                                          |
| **Roommate Match** | Matching Algorithm / Filter Logic    | Compatibility score, preferences matching, exclusion rules                       |
| **UI Components**  | Across All Pages                     | Buttons, cards, modals, search bar, tabs                                        |
| **Navigation**     | Routing Between Pages                | Current path, route guards, params (like `/city/mumbai`)                        |
| **Review**         | Listing Review Section               | User rating, review text, timestamp                                              |
| **Bookmark**       | Saved Listings Feature (Optional)    | User ID, listing ID, save state                                                 |

---

 _Location: `docs/concepts.md` in the project root_
