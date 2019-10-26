--creating some basic tables for the project


--adding people
insert into persons values("Chris", "Pontikes","1998-02-25","Markham, ON","123 69 Street","780-555-1234");
insert into persons values("Josh", "Derkson","1998-05-06","High Level, AB","420 69 Street","780-555-5678");
insert into persons values("Alex", "Rostron","1998-01-24","Edmonton, AB","69 420 Street","780-123-5555");
insert into persons values("Brighton", "Greet","1998-03-25","Edmonton, AB","69 69 Street","780-123-1234");
insert into persons values("Jacob", "Reckhard","1998-12-08","Edmonton, AB","404 404 Street","780-404-1234");

--adding users, Chris is the only officer
insert into users values(1, "lego", "o", "Chris", "Pontikes", "Edmonton");
insert into users values(2, "jesus", "a", "Josh", "Derkson", "Edmonton");
insert into users values(3, "yeet", "a", "Alex", "Rostron", "Edmonton");
insert into users values(4, "dnd", "a", "Brighton", "Greet", "Edmonton");
insert into users values(5, "password", "a", "Jacob", "Reckhard", "Edmonton");

--giving all of us cars
insert into vehicles values("U069", "Ford", "F150", 2015, "Red"); --Chris' Car
insert into vehicles values("U003", "Tank", "Panzer IV", 1944, "Green"); --Josh's TANK
insert into vehicles values("U420", "Honda", "Civic", 2020, "Black"); --Alex's car
insert into vehicles values("U078", "Mitsubishi", "Eclipse", 2007, "Grey"); --Speedwagon for Brighton
insert into vehicles values("U404", "Suzuki", "Car", 2005, "Blue"); --Jacob's car

--registering our cars so it is all legal, except Josh registered his tank waaay to long ago
insert into registrations values(20, "2019-10-04", "2020-10-04", "legoboi", "U069", "Chris", "Pontikes");
insert into registrations values(1, "1945-06-06", "1946-06-06", "TANK", "U003", "Josh", "Derkson");
insert into registrations values(22, "2020-01-01", "2021-01-01", "yeet420", "U420", "Alex", "Rostron");
insert into registrations values(23, "2019-02-04", "2020-02-04", "spdwgn1", "U078", "Brighton", "Greet");
insert into registrations values(24, "2019-05-20", "2020-05-20", "eror404", "U404", "Jacob", "Reckhard");