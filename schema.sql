drop table if exists users;
    create table users (
    id integer primary key autoincrement,
    email text not null,
    password text not null,
    is_driver boolean not null check (is_driver in (0,1))
);


drop table if exists requests:
    create table calls (
    id integer primary key autoincrement,
    passenger integer not null,
    address text not null,
    driver integer,
    request_time text not null DEFAULT (datetime('now','localtime')),
    dispatch_time text
);
