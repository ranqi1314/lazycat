#提前创库news和表sina_news

create table sina_news(
	id int not null auto_increment primary key,
	title varchar(100),
	send_time varchar(100),
	author varchar(20),
	url varchar(100)
);