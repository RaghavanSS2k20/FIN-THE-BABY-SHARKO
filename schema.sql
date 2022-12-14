drop Table if EXISTS users;
create table users(
    id INTEGER primary key autoincrement,
    username text not null,
    password text not null
);