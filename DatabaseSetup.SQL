CREATE DATABASE python_chitter;
\c python_chitter;
CREATE TABLE chitter_users(id SERIAL PRIMARY KEY, username VARCHAR(25), password TEXT);
CREATE TABLE peeps(username VARCHAR(25), peep VARCHAR(240), time TIMESTAMP);

CREATE DATABASE python_chitter_test;
\c python_chitter;
CREATE TABLE chitter_users(id SERIAL PRIMARY KEY, username VARCHAR(25), password TEXT);
CREATE TABLE peeps(username VARCHAR(25), peep VARCHAR(240), time TIMESTAMP);

