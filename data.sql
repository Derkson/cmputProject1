--creating some basic tables for the project


--adding people
insert into persons values("Chris", "Pontikes","1998-02-25","Markham, ON","123 69 Street","780-555-1234");
insert into persons values("Josh", "Derkson","1998-05-06","High Level, AB","420 69 Street","780-555-5678");
insert into persons values("Alex", "Rostron","1998-01-24","Edmonton, AB","69 420 Street","780-123-5555");
insert into persons values("Brighton", "Greet","1998-03-25","Edmonton, AB","69 69 Street","780-123-1234");
insert into persons values("Jacob", "Reckhard","1998-12-08","Edmonton, AB","404 404 Street","780-404-1234");


--now we gotta register parents (boi)
insert into persons values("Mother", "Pontikes", "1964-03-05", "Ticonderoga", "123 69 street", "780-555-5555");
insert into persons values("Father", "Pontikes", "1965-11-04", "Edmonton", "123 69 street", "780-123-2222");
insert into persons values("Mama", "Derkson", "0789-03-30", "Constantinople", "Ye olde home", "780-444-4444");
insert into persons values("Papa", "Derkson", "0777-04-12", "Pangea", "Ye Older home", "780-111-1111");
insert into persons values("Mom", "Rostron", "1980-07-21", "Edmonton", "11243 58ave", "780-333-3456");
insert into persons values("Doctor", "Rostron", "1980-09-22", "Edmonton", "11243 58ave", "780-444-1234");


--we were now registered at birth, so there is proof on paper that we exist
insert into births values(1, "Chris", "Pontikes", "1998-02-28", "Markham, ON", "M", "Father", "Pontikes", "Mother", "Pontikes");
insert into births values(2, "Josh", "Derkson", "1012-05-30", "Transylvania", "M", "Papa", "Derkson", "Mama", "Derkson");
insert into births values(6, "Alex", "Rostron", "1998-01-28", "Edmonton, AB", "M", "Doctor", "Rostron", "Mom", "Rostron");

--adding users, Chris is the only officer
insert into users values("U100", "lego", "o", "Chris", "Pontikes", "Edmonton");
insert into users values("U007", "jesus", "a", "Josh", "Derkson", "Edmonton");
insert into users values("U420", "yeet", "a", "Alex", "Rostron", "Edmonton");
insert into users values("U069", "dnd", "a", "Brighton", "Greet", "Edmonton");
insert into users values("U404", "password", "a", "Jacob", "Reckhard", "Edmonton");

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

--need to add some tickets now
insert into tickets values(1, 20, 69, "dumb bastard", "2017-11-12" );
insert into tickets values(2, 20, 420, "drunk boi", "2019-07-09");
insert into tickets values(3, 22, 100, "swearing in Christian Minecraft server", "2019-11-01");
insert into tickets values(4, 22, 69, "yeeting too hard on a longboard", "2019-11-01");
