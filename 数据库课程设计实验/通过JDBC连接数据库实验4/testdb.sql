Create database Testdb default character set gbk;
use Testdb;

create table products(
	id int,
	category char(6),
	name varchar(20),
	quantity int,
	price float);

 insert into products values(1001,'�ֱ�','��ɫ�ֱ�',500,1.23);
        insert into products values(1002,'�ֱ�','��ɫ�ֱ�',800,1.25);
        insert into products values(1003,'�ֱ�','��ɫ�ֱ�',200,1.26);
insert into products values(1004,'�ֱ�','��ɫ�ֱ�',900,1.27);
insert into products values(1005,'Ǧ��','2BǦ��',1000,0.56);
insert into products values(1006,'Ǧ��','2HǦ��',600,0.58);
