DROP SCHEMA IF EXISTS `Trade1` ;
CREATE SCHEMA IF NOT EXISTS `Trade1` default character set gbk;
USE `Trade1` ;

CREATE TABLE `Customers` (
   `CustomerID`   VARCHAR(5)   NOT NULL,
   `CompanyName`  VARCHAR(40)  NOT NULL,
   `ContactName`  VARCHAR(30),
   `ContactTitle` VARCHAR(30),
   `Address`      VARCHAR(60),
   `City`         VARCHAR(15),
   `Region`       VARCHAR(15),
   `PostalCode`   VARCHAR(10),
   `Country`      VARCHAR(15),
   `Phone`        VARCHAR(24),
   `Fax`          VARCHAR(24),
   PRIMARY KEY (`CustomerID`)
);

CREATE TABLE `Employees` (
   `EmployeeID`      MEDIUMINT UNSIGNED  NOT NULL AUTO_INCREMENT,
                    
   `LastName`        VARCHAR(20)     NOT NULL,
   `FirstName`       VARCHAR(10)      NOT NULL,
   `Title`           VARCHAR(30),  
   `TitleOfCourtesy` VARCHAR(25),  
   `BirthDate`       DATE,         
   `HireDate`        DATE,
   `Address`         VARCHAR(60),
   `City`            VARCHAR(15),
   `Region`          VARCHAR(15),
   `PostalCode`      VARCHAR(10),
   `Country`         VARCHAR(15),
   `HomePhone`       VARCHAR(24),
   `Extension`       VARCHAR(4),
   `Photo`           BLOB,                          
   `Notes`           TEXT                NOT NULL, 
   `ReportsTo`       MEDIUMINT UNSIGNED  NULL,  
                                               
   `PhotoPath`       VARCHAR(255),
   `Salary`          INT,
  
   PRIMARY KEY (`EmployeeID`),
   FOREIGN KEY (`ReportsTo`) REFERENCES `Employees` (`EmployeeID`)
);

CREATE TABLE `Suppliers` (
   `SupplierID`   SMALLINT UNSIGNED  NOT NULL AUTO_INCREMENT,
                                     -- [0, 65535]
   `CompanyName`  VARCHAR(40)        NOT NULL,
   `ContactName`  VARCHAR(30),
   `ContactTitle` VARCHAR(30),
   `Address`      VARCHAR(60),
   `City`         VARCHAR(15),
   `Region`       VARCHAR(15),
   `PostalCode`   VARCHAR(10),
   `Country`      VARCHAR(15),
   `Phone`        VARCHAR(24),
   `Fax`          VARCHAR(24),
   `HomePage`     TEXT,   
    PRIMARY KEY (`SupplierID`)
    
);

CREATE TABLE `Categories` (
   `CategoryID`   TINYINT UNSIGNED  NOT NULL AUTO_INCREMENT,
                  -- [0, 255]
   `CategoryName` VARCHAR(30)       NOT NULL,
                 
   `Description`  TEXT,   
   `Picture`      BLOB,      
   PRIMARY KEY  (`CategoryID`)
  
);



CREATE TABLE `Products` (
   `ProductID`       SMALLINT UNSIGNED       NOT NULL AUTO_INCREMENT,
   `ProductName`     VARCHAR(40)             NOT NULL,
   `SupplierID`      SMALLINT UNSIGNED       NOT NULL, 
   `CategoryID`      TINYINT UNSIGNED        NOT NULL,
   `QuantityPerUnit` VARCHAR(20),           
   `UnitPrice`       DECIMAL(10,2) UNSIGNED  DEFAULT 0,
   `UnitsInStock`    SMALLINT                DEFAULT 0,  
   `UnitsOnOrder`    SMALLINT UNSIGNED       DEFAULT 0,
   `ReorderLevel`    SMALLINT UNSIGNED       DEFAULT 0,
   `Discontinued`    BOOLEAN                 NOT NULL DEFAULT FALSE,
   PRIMARY KEY (`ProductID`),
  
   FOREIGN KEY (`CategoryID`) REFERENCES `Categories` (`CategoryID`),
   FOREIGN KEY (`SupplierID`) REFERENCES `Suppliers` (`SupplierID`)
);

CREATE TABLE `Shippers` (
   `ShipperID`   TINYINT UNSIGNED  NOT NULL AUTO_INCREMENT,
   `CompanyName` VARCHAR(40)       NOT NULL,
   `Phone`       VARCHAR(24),
   PRIMARY KEY (`ShipperID`)
);

CREATE TABLE `Orders` (
   `OrderID`        INT UNSIGNED        NOT NULL AUTO_INCREMENT,
                   
   `CustomerID`     VARCHAR(5),
   `EmployeeID`     MEDIUMINT UNSIGNED  NOT NULL,
   `OrderDate`      DATE,
   `RequiredDate`   DATE,
   `ShippedDate`    DATE,
   `ShipVia`        TINYINT UNSIGNED,
   `Freight`        DECIMAL(10,2) UNSIGNED  DEFAULT 0,
   `ShipName`       VARCHAR(40),
   `ShipAddress`    VARCHAR(60),
   `ShipCity`       VARCHAR(15),
   `ShipRegion`     VARCHAR(15),
   `ShipPostalCode` VARCHAR(10),
   `ShipCountry`    VARCHAR(15),
   PRIMARY KEY (`OrderID`),
  
   FOREIGN KEY (`CustomerID`) REFERENCES `Customers` (`CustomerID`),
   FOREIGN KEY (`EmployeeID`) REFERENCES `Employees` (`EmployeeID`),
   FOREIGN KEY (`ShipVia`)    REFERENCES `Shippers`  (`ShipperID`)
);

CREATE TABLE `Order Details` (
   `OrderID`   INT UNSIGNED           NOT NULL,
   `ProductID` SMALLINT UNSIGNED      NOT NULL,
   `UnitPrice` DECIMAL(8,2) UNSIGNED  NOT NULL DEFAULT 999999.99,
                                      -- max value as default
   `Quantity`  SMALLINT(2) UNSIGNED   NOT NULL DEFAULT 1,
   `Discount`  DOUBLE(8,0)            NOT NULL DEFAULT 0, 
   PRIMARY KEY (`OrderID`, `ProductID`),
   FOREIGN KEY (`OrderID`)   REFERENCES `Orders`   (`OrderID`),
   FOREIGN KEY (`ProductID`) REFERENCES `Products` (`ProductID`)
);


