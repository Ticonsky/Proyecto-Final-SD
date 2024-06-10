
- **assets/**: Contains any assets used in the project (images, etc.).
- **src/**: Contains the source code of the project.
- **Poster SD.pdf**: Poster presentation of the project.
- **README.md**: This file.
- **Technical_report_SD.pdf**: Detailed technical report of the project.

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

## Relational Algebra Queries
### For Guests
1. **Search properties by location and date**:
    ```sql
    σ_{location = 'desired location'}(Property) ⋈ σ_{startingDate ≤ 'desired start date' ∧ startingDate ≥ 'desired end date'}(Booking)
    ```
2. **View property details**:
    ```sql
    π_{name, description, media, propertyAddonId}(Property) ⋈ π_{propertyAddonId, wifi, kitchen, parking, staffService, pool, securityCameras, laundry, gym}(PropertyAddon)
    ```
3. **Book a property**:
    ```sql
    INSERT INTO Booking(bookingId, propertyId, userId, startingDate)
    ```
4. **Pay for booking**:
    ```sql
    INSERT INTO Bill(billId, bookingId, propertyId, userId, billStatus)
    ```
5. **Leave a review**:
    ```sql
    INSERT INTO Comment(commentId, bookingId, userId, content, uploadDate, rating)
    ```

### For Hosts
1. **List a new property**:
    ```sql
    INSERT INTO Property(propertyId, userId, propertyTypeId, propertyAddonId, location, guestsCapacity, availableRooms, availableBeds, availableBaths, media, name, description, price)
    ```
2. **Manage property listings**:
    ```sql
    UPDATE Property SET column = value WHERE propertyId = 'propertyId'
    ```
3. **View and manage bookings**:
    ```sql
    π_{bookingId, startingDate}(σ_{propertyId = 'propertyId'}(Booking))
    ```
4. **Receive payments for bookings**:
    ```sql
    π_{billId, billStatus}(σ_{propertyId = 'propertyId'}(Bill))
    ```
5. **Respond to reviews**:
    ```sql
    INSERT INTO Comment(commentId, bookingId, userId, content, uploadDate, rating)
    ```

### Additional Queries
1. **List all properties in a location**:
    ```sql
    σ_{location = 'desired location' ∧ guestsCapacity > 0 ∧ availableRooms > 0 ∧ availableBeds > 0 ∧ availableBaths > 0}(Property)
    ```
2. **Find bookings by a specific traveler**:
    ```sql
    π_{bookingId, propertyId, startingDate}(σ_{userId = 'userId'}(Booking))
    ```
3. **Get all reviews for a property**:
    ```sql
    π_{rating, content}(σ_{propertyId = 'propertyId'}(Comment ⋈ Booking))
    ```

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
    python src/main.py
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

## Acknowledgements
Special thanks to Eng. Carlos Andrés Sierra, M.Sc., for his guidance and support throughout the project.

---

For any inquiries, please contact:
- **Juan Daniel Vanegas Mayorquin**: [jdvanegasm@udistrital.edu.co](mailto:jdvanegasm@udistrital.edu.co)
- **Josue Urrego Lopez**: [jurregol@udistrital.edu.co](mailto:jurregol@udistrital.edu.co)

---

© 2024 Universidad Distrital Francisco José de Caldas
