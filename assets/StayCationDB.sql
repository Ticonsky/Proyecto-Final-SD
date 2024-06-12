drop database if exists staycation;
create database staycation;

use staycation;

-- User table creation
create table User (
    userId varchar(36) primary key default (replace(uuid(), '-', '')),
    userRole varchar(1) not null,
    name varchar(50) not null,
    email varchar(60) unique not null,
    hashedPassword varchar(64) not null, -- utilizar un hash SHA-256
    phone varchar(20) unique not null
);

-- Card table creation
create table Card (
    cardId varchar(36) primary key default (replace(uuid(), '-', '')),
    userId varchar(36) not null,
    cardNumber varchar(28) not null,
    cardOwner varchar(50) not null,
    dueDate varchar(5) not null,
    cvv varchar(5) not null, -- i.e: 07/28 
    balance int check(balance > 0),
    foreign key (userId) references User(userId)
);

-- Property Type table creation
create table PropertyType (
    propertyTypeId int primary key auto_increment,
    name varchar(50) unique not null,
    description varchar(200) not null
);

-- Property Addons table creation
create table PropertyAddon (
    propertyAddonId int primary key auto_increment,
    wifi boolean default false,
    kitchen boolean default false,
    parking boolean default false,
    staffService boolean default false,
    pool boolean default false,
    securityCameras boolean default false,
    laundry boolean default false,
    gym boolean default false
);

-- Property table creation
create table Property (
    propertyId varchar(36) primary key default (replace(uuid(), '-', '')),
    userId varchar(36) not null,
    propertyTypeId int not null,
    propertyAddonId int not null,
    location varchar(100) not null,
    guestsCapacity int check(guestsCapacity > 0),
    availableRooms int check(availableRooms > 0),
    availableBeds int check(availableBeds > 0),
    availableBaths int check(availableBaths > 0),
    media varchar(200) not null, -- Url
    name varchar(25) unique not null,
    description varchar(200) not null,
    price decimal(10,2) not null,
    foreign key (userId) references User(userId),
    foreign key (propertyTypeId) references PropertyType(propertyTypeId),
    foreign key (propertyAddonId) references PropertyAddon(propertyAddonId)
);
ALTER TABLE booking
ADD COLUMN ending_date TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP;

drop table staycation.Booking
-- Booking table creation
create table Booking (
    bookingId varchar(36) primary key default (replace(uuid(), '-', '')),
    propertyId varchar(36) not null,
    userId varchar(36) not null,
    startingDate timestamp default current_timestamp,
    foreign key (propertyId) references Property(propertyId),
    foreign key (userId) references User(userId)
);

-- Creación de tabla para Comentarios
create table Comment (
    commentId int primary key auto_increment,
    bookingId varchar(36) not null,
    userId varchar(36) not null,
    content varchar(500) not null,
    uploadDate timestamp default current_timestamp,
    rating int check (rating >= 0 and rating <= 5),
    foreign key (bookingId) references Booking(bookingId),
    foreign key (userId) references User(userId)
);

-- Creación de tabla para Facturas
create table Bill (
    billId int primary key auto_increment,
    bookingId varchar(36) not null,
    propertyId varchar(36) not null,
    userId varchar(36) not null,
    billStatus varchar(15) unique not null,
    foreign key (bookingId) references Booking(bookingId),
    foreign key (propertyId) references Property(propertyId),
    foreign key (userId) references User(userId)
);
