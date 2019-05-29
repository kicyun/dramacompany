drop table if exists users;
    create table users (
    id integer primary key autoincrement,
    email text not null,
    password text not null,
    is_driver boolean not null check (is_driver in (0,1))
);
