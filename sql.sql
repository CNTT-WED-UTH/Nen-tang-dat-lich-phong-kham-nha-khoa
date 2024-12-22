-- Bảng bệnh nhân
CREATE TABLE Patients (
    PatientID INT AUTO_INCREMENT PRIMARY KEY,
    FullName VARCHAR(100) NOT NULL,
    DateOfBirth DATE NOT NULL,
    Gender ENUM('Male', 'Female', 'Other') NOT NULL,
    PhoneNumber VARCHAR(15) NOT NULL UNIQUE,
    Email VARCHAR(100) UNIQUE,
    Address VARCHAR(255)
);

-- Bảng nha sĩ
CREATE TABLE Dentists (
    DentistID INT AUTO_INCREMENT PRIMARY KEY,
    FullName VARCHAR(100) NOT NULL,
    Specialty VARCHAR(100),
    PhoneNumber VARCHAR(15) NOT NULL UNIQUE,
    Email VARCHAR(100) UNIQUE,
    YearsOfExperience INT,
    ClinicAddress VARCHAR(255)
);

-- Bảng dịch vụ nha khoa
CREATE TABLE Services (
    ServiceID INT AUTO_INCREMENT PRIMARY KEY,
    ServiceName VARCHAR(100) NOT NULL,
    Description TEXT,
    Price DECIMAL(10, 2) NOT NULL
);

-- Bảng lịch hẹn
CREATE TABLE Appointments (
    AppointmentID INT AUTO_INCREMENT PRIMARY KEY,
    PatientID INT NOT NULL,
    DentistID INT NOT NULL,
    ServiceID INT NOT NULL,
    AppointmentDate DATETIME NOT NULL,
    Status ENUM('Scheduled', 'Completed', 'Cancelled') DEFAULT 'Scheduled',
    Notes TEXT,
    FOREIGN KEY (PatientID) REFERENCES Patients(PatientID),
    FOREIGN KEY (DentistID) REFERENCES Dentists(DentistID),
    FOREIGN KEY (ServiceID) REFERENCES Services(ServiceID)
);

-- Bảng thanh toán
CREATE TABLE Payments (
    PaymentID INT AUTO_INCREMENT PRIMARY KEY,
    AppointmentID INT NOT NULL,
    PaymentDate DATETIME NOT NULL,
    Amount DECIMAL(10, 2) NOT NULL,
    PaymentMethod ENUM('Cash', 'Credit Card', 'Bank Transfer') NOT NULL,
    PaymentStatus ENUM('Pending', 'Completed', 'Failed') DEFAULT 'Pending',
    FOREIGN KEY (AppointmentID) REFERENCES Appointments(AppointmentID)
);
