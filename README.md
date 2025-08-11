# Chicken UI Project
A project allowing the management of chicken records

This project originally, only had the requirement of having a simple CLI based menu system. You will find the main branch of this repository to be exaclty that, though you might also want to explore the other branches.

# Approach
This project was made with a focus on Object Oriented principles to help with maintainability and extensibility. The goal would be to create a program where new features could be added with minimal chnages to existing code. This would be done by employing modular design and abstraction, allowing the core logic to be isolated and re used accross different user interfaces.

As a result, the transition from a CLI to a Flask powered web app would need minimal chnages to the underlying code. The core business logic would be consistent, demonstrating the effectivness of such an approach.
Predicting all future requirements though, is inherently difficult. This would be seen with the implementation of a MySQL backend which would need more substantual changes, though the object oriented design mitigated the scope of such a rewrite. Most of the core logic and existing front-end implementations were unaffected, highlighting the benefits of a well structured and modular codebase.
