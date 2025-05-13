# <mark> WORKCOHOL Solution Pvt Ltd Internship Project </mark>
# Software Engineers

## Doctor_appointment_booking_platform

## Team Leader : Santhosh Natarajan
## Co-Team Leader : Christy Dasan

### Project Description :
 #### A platform that allows patients to book appointments with doctors online. It includes features like search, booking, and management of healthcare appointments.


1. Frontend :
     * HTML
     * CSS
     * JavaScript
2. Database :
     * MYSQL
3. Backend :
     * Python Libraries
     * Django Framework
     * RestAPI
4. Version Control :
     * GIT&GITHUB
5. Code Editor :
      * Visual Studio

### <mark> Flow Chart </mark>
    A[User Opens Website] --> B{Is User Logged In?};
    B --> C{No};
    C --> D[User Registers/Logs In];
    D --> E{Successful Login?};
    E --> F{Yes};
    E --> B;
    B --> G{Yes};
    G --> H[User Views Doctor List/Calendar];
    H --> I[User Selects Doctor/Slot];
    I --> J[User Fills Appointment Form];
    J --> K[User Submits Form];
    K --> L{Is Form Valid?};
    L --> M{No};
    M --> J;
    L --> N{Yes};
    N --> O[Appointment Confirmation];
    O --> P[Appointment Saved to Database];

### <mark> Explanation of the Flowchart Elements: </mark> 

* A: User Opens Website: The process begins when a user accesses the platform.
* B: Is User Logged In?: The system checks the user's authentication status.
* C: No: If the user is not logged in, they are redirected to registration/login.
* D: User Registers/Logs In: The user creates a new account or logs in to an existing one.
* E: Successful Login?: The system validates the user's credentials.
* F: Yes: If the login is successful, the user proceeds to the appointment booking section.
* G: Yes: If the user is already logged in, they bypass the login process.
* H: User Views Doctor List/Calendar: The user can see available doctors, their schedules, or a calendar view.
* I: User Selects Doctor/Slot: The user chooses a specific doctor and time slot for the appointment.
* J: User Fills Appointment Form: The user provides necessary details like name, contact information, and reason for the visit.
* K: User Submits Form: The user submits the appointment booking request.
* L: Is Form Valid?: The system validates the form data (e.g., required fields, date/time format).
* M: No: If the form has errors, the user is prompted to correct them.
* N: Yes: If the form is valid, the appointment booking is confirmed.
* O: Appointment Confirmation: A confirmation message is displayed to the user.
* P: Appointment Saved to Database: The appointment details are stored in the database.
