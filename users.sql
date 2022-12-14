drop table if exists users;
    create table users (
    emailId text PRIMARY key,
    password text not null,
    noOfsearches integer DEFAULT 0
);