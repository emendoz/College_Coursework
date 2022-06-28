use emendoza_cs355fl20;

DROP TABLE IF EXISTS Delivery_Worker;
DROP TABLE IF EXISTS Warehouse;
DROP TABLE IF EXISTS Transport;
DROP TABLE IF EXISTS Person;
DROP TABLE IF EXISTS Mail;

CREATE TABLE Mail (
    Receipt_Number varchar(6),
    Date_Recieved datetime NOT NULL,
    Type varchar(30),
    Price numeric(6,2) NOT NULL,
    Weight varchar(15) NOT NULL, 
    PRIMARY KEY(Receipt_Number)
);

CREATE TABLE Person (
    Postal_Account_ID varchar(5),
    Name varchar(50) NOT NULL,
    Phone_Number char(12) CHECK(Phone_Number REGEXP '[0-9]{3}-[0-9]{3}-[0-9]{4}'),
    Receipt_Number varchar(6),
    PRIMARY KEY(Postal_Account_ID),
    UNIQUE(Postal_Account_ID, Name),
    FOREIGN KEY(Receipt_Number) 
    REFERENCES Mail(Receipt_Number)
        ON DELETE CASCADE
        ON UPDATE CASCADE
);

CREATE TABLE Transport(
    Tracking_Number varchar(15),
    Status varchar(20) NOT NULL,
    Street varchar(30) NOT NULL,
    City varchar(28) NOT NULL,
    State char(2) CHECK (State in ('AK', 'AL', 'AR', 'AS', 'AZ', 'CA', 'CO', 'CT', 'DC', 'DE', 
    'FL', 'GA', 'GU', 'HI', 'IA', 'ID', 'IL', 'IN', 'KS', 'KY',
    'LA', 'MA', 'MD', 'ME', 'MI', 'MN', 'MO', 'MP', 'MS', 'MT',
    'NC', 'ND', 'NE', 'NH', 'NJ', 'NM', 'NV', 'NY', 'OH', 'OK',
    'OR', 'PA', 'PR', 'RI', 'SC', 'SD', 'TN', 'TX', 'UM', 'UT', 
    'VA', 'VI', 'VT', 'WA', 'WI', 'WV', 'WY')),
    ZIP_Code varchar(5) NOT NULL,
    Estimated_Arrival_Time datetime,
    Receipt_Number varchar(6), 
    UNIQUE(Tracking_Number),
    PRIMARY KEY(Tracking_Number),
    FOREIGN KEY (Receipt_Number) 
    REFERENCES Mail(Receipt_Number)
        ON DELETE CASCADE
        ON UPDATE CASCADE
);

CREATE TABLE Warehouse(
    Warehouse_Number varchar(5),
    Name varchar(30) NOT NULL,
    Street varchar(30) NOT NULL,
    City varchar(28) NOT NULL,
    State char(2) CHECK (State in ('AK', 'AL', 'AR', 'AS', 'AZ', 'CA', 'CO', 'CT', 'DC', 'DE',
    'FL', 'GA', 'GU', 'HI', 'IA', 'ID', 'IL', 'IN', 'KS', 'KY',
    'LA', 'MA', 'MD', 'ME', 'MI', 'MN', 'MO', 'MP', 'MS', 'MT',
    'NC', 'ND', 'NE', 'NH', 'NJ', 'NM', 'NV', 'NY', 'OH', 'OK',
    'OR', 'PA', 'PR', 'RI', 'SC', 'SD', 'TN', 'TX', 'UM', 'UT', 
    'VA', 'VI', 'VT', 'WA', 'WI', 'WV', 'WY')),
    ZIP_Code varchar(5) NOT NULL,
    PRIMARY KEY(Warehouse_Number)
);

CREATE TABLE Delivery_Worker(
    Employee_ID varchar(5),
    Name varchar(50),
    Receipt_Number varchar(6),
    Warehouse_Number varchar(5), 
    PRIMARY KEY(Employee_ID),
    UNIQUE KEY(Name),
    FOREIGN KEY (Receipt_Number) 
    REFERENCES Mail(Receipt_Number)
        ON DELETE CASCADE
        ON UPDATE CASCADE,
    FOREIGN KEY (Warehouse_Number) 
    REFERENCES Warehouse(Warehouse_Number)
        ON DELETE CASCADE
        ON UPDATE CASCADE
);

# Population of Data
INSERT INTO Mail (Receipt_Number, Date_Recieved, Type, Price, Weight) VALUES 
('LD1097','2020-09-05 11:24:09','Letter','0.00','0 lbs');
INSERT INTO Mail VALUES ('SE2308','2020-12-14 05:24:45','Priority Mail Express 
Package','30.00','4.5 lbs');
INSERT INTO Mail VALUES ('HK9301','2021-01-13 12:12:05','Letter','0.00','0.5 lbs');
INSERT INTO Mail VALUES ('PA0394','2019-05-11 09:21:00','Priority Mail Express 
Package','25.00','2 lbs');

INSERT INTO Person (Postal_Account_ID, Name, Phone_Number, Receipt_Number) VALUES 
('1','Roger Banks','109-240-1923','SE2308');
INSERT INTO Person VALUES ('5','Maggie Thurtle','282-389-0886','LD1097');
INSERT INTO Person VALUES ('29','Rani Pelon','262-737-8391','HK9301');
INSERT INTO Person VALUES ('15','Elli Wilton','642-952-9285','PA0394');

INSERT INTO Transport (Tracking_Number, Status, Street, City, State, ZIP_Code, 
Estimated_Arrival_Time, Receipt_Number) VALUES ('PKLA12908234019','IN 
TRANSIT','8455 Pardee Drive','Oakland','CA','94621','2020-11-21 
09:07:11','LD1097');
INSERT INTO Transport VALUES ('LDJM89720127395','DELIVERED','180 Napolean 
Street','San Francisco','CA','94124','2020-12-14 05:24:45','SE2308');
INSERT INTO Transport VALUES ('PSJH21960143570','IN TRANSIT','1402 20th 
Avenue','Queens','NY','11356','2021-01-13 12:12:05','HK9301');
INSERT INTO Transport VALUES ('SLFM92758250638','DELIVERED','300 Maspeth 
Avenue','Brooklyn','NY','11211','2019-05-11 09:21:00','PA0394');

INSERT INTO Warehouse (Warehouse_Number, Name, Street, City, State, ZIP_Code) 
VALUES ('0','USPS','180 Napolean Street','San Francisco','CA','94124');
INSERT INTO Warehouse VALUES ('12','FedEx','8455 Pardee 
Drive','Oakland','CA','94621');
INSERT INTO Warehouse VALUES ('02','USPS','1402 20th 
Avenue','Queens','NY','11356');
INSERT INTO Warehouse VALUES ('67','FedEx','300 Maspeth 
Avenue','Brooklyn','NY','11211');

INSERT INTO Delivery_Worker (Employee_ID, Name, Receipt_Number, Warehouse_Number) 
VALUES ('F0972','Martin Kansi','SE2308','12');
INSERT INTO Delivery_Worker VALUES ('A2912','Patril Fathom','LD1097','0');
INSERT INTO Delivery_Worker VALUES ('M1905','Mitchel Kallen','HK9301','02');
INSERT INTO Delivery_Worker VALUES ('A0485','Patterson Finkle','PA0394','67');
