# Stay Cation: Comprehensive Backend Platform for Vacation Property Management
### Made by _Ticonsky_ && _Nous_

## Overview
Stay Cation is a backend platform designed to streamline the management of vacation properties. The platform caters to property owners, managers, and guests, providing features such as user registration, property management, bookings, comments, and billing. It integrates with the Google Maps API to enhance the user experience by providing property location visualization.

## Features
- **User Management**: Register, login, and manage user profiles.
- **Property Management**: Add, update, and delete property details, integrate Google Maps API for location.
- **Booking System**: Manage property bookings, ensure no date conflicts.
- **Comments**: Allow users to leave and view comments on properties.
- **Billing**: Generate and manage invoices for bookings.
- **Secure Payment Processing**: Handle payment details securely.


## Database Schema
The database schema includes the following entities:
- **User**: Represents property owners and travelers.
- **PropertyType**: Represents different types of properties.
- **PropertyAddon**: Represents additional features/services for properties.
- **Property**: Details of the properties listed by users.
- **Card**: Payment card information linked to users.
- **Booking**: Reservation details for properties.
- **Comment**: User comments and ratings for properties.
- **Bill**: Invoices generated for bookings.

## Methodology
The development of the Stay Cation platform followed a structured methodology to ensure the successful implementation of its features and functionalities. The key steps in the methodology are outlined below:
1. **Requirement Analysis**:
    - Identify the needs of property owners, managers, and guests.
    - Define user stories to capture the specific requirements and goals of each user type.
2. **System Design**:
    - Develop UML diagrams, including deployment, activity, sequence, and state diagrams, to visualize the system architecture.
    - Choose appropriate design patterns (MVC, Singleton, Factory) to ensure modularity, scalability, and maintainability.
3. **Implementation**:
    - Set up the development environment using MySQL, DBeaver, XAMPP, and Python.
    - Implement the core classes (User, Property, PropertyAddon, PropertyType, Booking, Comment, Bill, Card) based on the design specifications.
4. **Testing**:
    - Conduct unit tests to verify the functionality of individual components.
    - Perform integration tests to ensure functionality.

## Experiments and Results
### User Registration Tests
- Verified successful user registration and data storage.
- Valid and invalid data handling.
- Successful login functionality verification.

### Property Management Tests
- Addition, update, and deletion of properties.
- Correct display of properties owned by users.

### Booking Tests
- Property search and booking validation.
- Date conflict management.
- Booking details update and cancellation.

### Comment Tests
- Adding, editing, and deleting comments.
- Correct display of comments on property pages.

### Billing Tests
- Invoice generation and accuracy.
- Correct storage and retrieval of billing information.

### Preliminary Results
The system successfully handled user registrations, property management, bookings, comments, and billing. Integration with the Google Maps API significantly improved usability.

## Conclusion
Stay Cation provides a robust solution for vacation property management, leveraging modern technologies and design patterns to address real-life problems. The platform’s architecture ensures scalability and maintainability, making it a valuable tool for property owners, managers, and guests. Future work will focus on optimizing performance, enhancing security, and incorporating additional features based on user feedback.

## How to Run the Project
1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/Proyecto-Final-SD.git
    ```
2. Navigate to the project directory:
    ```bash
    cd Proyecto-Final-SD
    ```
3. Set up the environment and install dependencies:
    ```bash
    # Example using virtualenv and pip
    python3 -m venv venv
    source venv/bin/activate
    pip install -r requirements.txt
    ```
4. Configure the database connection in the appropriate configuration file.
5. Run the application:
    ```bash
    python src/Ticon/Manager.py
    ```

## Contributing
1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes.
4. Commit your changes (`git commit -m 'Add new feature'`).
5. Push to the branch (`git push origin feature-branch`).
6. Open a pull request.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments
Special thanks to Eng. Carlos Andrés Sierra, M.Sc., for his guidance and support throughout the project.

---

For any inquiries, please contact:
- **Juan Daniel Vanegas Mayorquin**: [jdvanegasm@udistrital.edu.co](mailto:jdvanegasm@udistrital.edu.co)
- **Josue Urrego Lopez**: [jurregol@udistrital.edu.co](mailto:jurregol@udistrital.edu.co)

---

© 2024 Universidad Distrital Francisco José de Caldas
