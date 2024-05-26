TDS Booking Application
Overview

This project implements a backend API for a booking application using Django and Django REST Framework. The application caters to multiple user types: Admin, Studio Owner, and Customer. It includes functionalities such as studio management, reservation creation, cancellation, and viewing based on user roles.
Backend Development
Technologies Used

    Django
    Django REST Framework
    Simple Django REST Framework JWT

Setup and Installation

    Clone the repository: git clone <repository-url>
    Navigate to the project directory: cd tds-booking-application
    Create a virtual environment: python -m venv venv
    Activate the virtual environment:
        On Windows: venv\Scripts\activate
        On macOS and Linux: source venv/bin/activate
    Install dependencies: pip install -r requirements.txt
    Apply migrations: python manage.py migrate
    Run the development server: python manage.py runserver

User Model and Authentication

    Multiple user types are implemented using a custom user model.
    JWT-based authentication is used for user authentication and authorization.

Studio Management

    Studio owners can create, view, edit, and delete studios.
    Admins can view all studios.

Reservation Management

    Customers can create reservations for specific dates, times, and studios.
    Customers can cancel reservations within 15 minutes of booking.

Reservation Views

    Customers can view their own reservations with an option to cancel within 15 minutes.
    Studio owners can view all reservations for their studios.
    Admins can view all reservations for all studios.

Frontend Development
Technologies Used

    ReactJS
    React Router
    Axios
    Redux (optional)
    TypeScript (optional)
    React-hook-form
    yup

Setup and Installation

    Clone the repository: git clone <repository-url>
    Navigate to the frontend directory: cd tds-booking-application/frontend
    Install dependencies: npm install
    Run the development server: npm start

Views
Authentication Views

    Login Page: Form for users to log in with their credentials.
    Registration Page: Separate forms for studio owners and customers to register.

Studio Management Views

    Dashboard displaying a list of owned studios with options to create, view, edit, or delete (For Studio Owner).
    Studio Creation Form: Form for Studio Owner to create a new studio.

Reservation Views

    Reservation List Page:
        For Customers: Displaying their own reservations (studio name - date & time) with an option to cancel within 15 minutes.
        For Studio Owners: Displaying all reservations for their studios (studio name - customer name - date & time).
        For Admin: Displaying all reservations for all studios (studio name - customer name - date & time).

Additional Views

    Profile Page: Users can view and edit their profile information.
    Error Pages: Customized pages for 404, 500 errors, etc.

Communication with Backend

    Utilizes Axios to make HTTP requests to the backend API endpoints for user authentication, data retrieval, and manipulation.
    Handles JWT tokens for authentication and authorization. Tokens are securely stored in local storage or cookies and handles token expiry.

Styling

    Uses CSS frameworks like Bootstrap or Material-UI for consistent styling.
    Maintains responsiveness for different screen sizes.

Testing (Bonus)

    Implements unit tests for React components using tools like Jest and React Testing Library.

Documentation

    Provides documentation for setting up the frontend environment, installing dependencies, and running the application.
    Documents the UI components and their functionalities.
    Explains how the frontend communicates with the backend API and handles authentication.

Delivery

    GitHub repository link: https://github.com/NagahShinawy/tds
    Include any required instructions to run the code.

