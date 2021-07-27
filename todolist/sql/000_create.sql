drop table if exists list;

create table list(
    id serial primary key,
    td_text text not null,
    status boolean default false,
    deadline date
);

