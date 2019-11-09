Create database Testdb default character set gbk;
use Testdb;

create table products(
	id int,
	category char(6),
	name varchar(20),
	quantity int,
	price float);

 insert into products values(1001,'¸Ö±Ê','ºìÉ«¸Ö±Ê',500,1.23);
        insert into products values(1002,'¸Ö±Ê','À¶É«¸Ö±Ê',800,1.25);
        insert into products values(1003,'¸Ö±Ê','ºÚÉ«¸Ö±Ê',200,1.26);
insert into products values(1004,'¸Ö±Ê','°×É«¸Ö±Ê',900,1.27);
insert into products values(1005,'Ç¦±Ê','2BÇ¦±Ê',1000,0.56);
insert into products values(1006,'Ç¦±Ê','2HÇ¦±Ê',600,0.58);
