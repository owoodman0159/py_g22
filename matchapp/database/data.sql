-- Preload Users
INSERT INTO User (name, email, gender, location, age)
VALUES ('Qiyi', 'qiyi@rotman.com', "Male", "761 Bay St", 18);

INSERT INTO User (name, email, gender, location, age)
VALUES ('Olivia', 'oliv@rotman.com',"Female", "761 Bay St", 18);

INSERT INTO User (name, email, gender, location, age)
VALUES ('Scott', 'scott@rotman.com',"Male", "761 Bay St", 18);

INSERT INTO User (name, email, gender, location, age)
VALUES ('Bella', 'bella@rotman.com', "Female", "761 Bay St",18);

INSERT INTO User (name, email, gender, location, age)
VALUES ('Jiwon', 'jiwon@rotman.com', "Female", "761 Bay St",18);


-- Preload Actions
INSERT INTO Actions (uid1, uid2, like)
VALUES (
    (SELECT uid FROM User WHERE name = 'Qiyi'),
    (SELECT uid FROM User WHERE name = 'Olivia'),
    TRUE
);

INSERT INTO Actions (uid1, uid2, like)
VALUES (
    (SELECT uid FROM User WHERE name = 'Qiyi'),
    (SELECT uid FROM User WHERE name = 'Scott'),
    TRUE
);
INSERT INTO Actions (uid1, uid2, like)
VALUES (
    (SELECT uid FROM User WHERE name = 'Qiyi'),
    (SELECT uid FROM User WHERE name = 'Bella'),
    TRUE
);

INSERT INTO Actions (uid1, uid2, like)
VALUES (
    (SELECT uid FROM User WHERE name = 'Qiyi'),
    (SELECT uid FROM User WHERE name = 'Jiwon'),
    TRUE
);


-- interest for Qiyi
INSERT INTO Interest (uid, interest) VALUES ((SELECT uid FROM User WHERE name = 'Qiyi'), 'Game');
INSERT INTO Interest (uid, interest) VALUES ((SELECT uid FROM User WHERE name = 'Qiyi'), 'Sleep');
INSERT INTO Interest (uid, interest) VALUES ((SELECT uid FROM User WHERE name = 'Qiyi'), 'Code');
INSERT INTO Interest (uid, interest) VALUES ((SELECT uid FROM User WHERE name = 'Qiyi'), 'Travel');
INSERT INTO Interest (uid, interest) VALUES ((SELECT uid FROM User WHERE name = 'Qiyi'), 'Read');