drop table if exists users;
    create table users (
    id integer primary key autoincrement,
    -- 이메일
    email text not null,
    -- 암호
    password text not null,
    -- 택시 기사 여부 (0 : 승객, 1 : 택시 기사)
    is_driver boolean not null check (is_driver in (0,1))
);


drop table if exists calls;
    create table calls (
    id integer primary key autoincrement,
    -- 승객 user id
    passenger integer not null,
    -- 승차 주소
    address text not null,
    -- 택시 기사 user id
    driver integer,
    -- 배차 요청 시간
    request_time text not null DEFAULT (datetime('now','localtime')),
    -- 배차 완료 시간
    dispatch_time text
);
