---Script rédigé par Anne Legrand en août 2020 pour la base de données db_DjangoPhoto.sqlite
---destinée à la réalisation de l'application Python pour la fin du module
---dispensé aux M2-TNAH par Thibault CLérice

BEGIN TRANSACTION;

CREATE TABLE IF NOT EXISTS `user` (
	`user_id`	integer NOT NULL PRIMARY KEY AUTOINCREMENT,
	`user_nom`	TINYTEXT NOT NULL,
	`user_login`	VARCHAR ( 45 ) NOT NULL,
	`user_email`	TINYTEXT NOT NULL,
	`user_motdepasse`	VARCHAR ( 100 ) NOT NULL,
	`user_type`	TEXT DEFAULT 'user'
);

DROP TABLE IF EXISTS `authorship`;
CREATE TABLE IF NOT EXISTS `authorship` (
	`authorship_id`	integer NOT NULL PRIMARY KEY AUTOINCREMENT,
	`authorship_user_id`	integer NOT NULL,
	`authorship_image_id`	integer NOT NULL,
	`authorship_date`	DATETIME DEFAULT current_timestamp,
	FOREIGN KEY(authorship_user_id) REFERENCES user(user_id),
	FOREIGN KEY(authorship_image_id) REFERENCES image(id)
);

CREATE TABLE IF NOT EXISTS Image (
	id	INTEGER PRIMARY KEY AUTOINCREMENT,
	titre TEXT NOT NULL,
	chemin TEXT NOT NULL,
	date TEXT NOT NULL,
	nom_photographe TEXT NOT NULL,
	description TEXT NOT NULL,
	source TEXT NOT NULL,
	tag TEXT NOT NULL,
	orientation TEXT NOT NULL,
	image_valid	TINYTEXT DEFAULT 'y'
);

CREATE TABLE IF NOT EXISTS tag_img (
	tag_mot TEXT NOT NULL PRIMARY KEY
);

INSERT INTO `tag` (
	`tag_mot`) 
VALUES 
("quintette"),
("musicien"),
("famille"),
("portrait"),
("autre")
;

CREATE TABLE IF NOT EXISTS orientation_img (
	orientation_type TEXT NOT NULL PRIMARY KEY
);

INSERT INTO `orientation` (
	`orientation_type`) 
VALUES 
("portrait"),
("paysage")
;


COMMIT;

BEGIN TRANSACTION;

INSERT or IGNORE INTO Image (titre, chemin, date, nom_photographe,description,source,tag,orientation) VALUES ('Django en famille', '<img src="/static/img/002.jpg">', 'circa 1920','', 'Django en famille. De gauche à droite : sa mère, dite Negros (la deuxième), Django (le septième).', 'BnF / Fonds Ch. Delaunay, Boîte 71, page 3', 'famille', 'paysage');
INSERT or IGNORE INTO Image (titre, chemin, date, nom_photographe,description,source,tag,orientation) VALUES ('Django adolescent au banjo', '<img src="/static/img/003.jpg">', 'circa 1923','', 'Django adolescent au banjo. ', 'BnF / Fonds Ch. Delaunay, Boîte 71, page 4', 'banjo', 'portrait');
INSERT or IGNORE INTO Image (titre, chemin, date, nom_photographe,description,source,tag,orientation) VALUES ('Django adolescent avec un Borsalino', '<img src="/static/img/004.jpg">', 'circa 1931','', 'Django adolescent avec un Borsalino.', 'BnF / Fonds Ch. Delaunay, Boîte 71, page 5', 'adolescent', 'portrait');
INSERT or IGNORE INTO Image (titre, chemin, date, nom_photographe,description,source,tag,orientation) VALUES ('Django à Toulon', '<img src="/static/img/010.jpg">', '1931','Emile Savitry', 'A Toulon, Django Reinhardt, les bras levés, et de droite à gauche, Joseph Reinhardt et Emile Savitry qui réalise la photo avec un déclencheur automatique.', 'Paco Savitry / S. Malexis', 'Savitry', 'paysage');
INSERT or IGNORE INTO Image (titre, chemin, date, nom_photographe,description,source,tag,orientation) VALUES ('L orchestre de Guerino à la Boîte à Matelots, à Paris', '<img src="/static/img/017.jpg">', 'circa 1933','Studio Bonnet', 'L orchestre de Guerino à la Boîte à Matelots, à Paris. De gauche à droite : Pierre Ferret (g), Lucien Galopain (g), Sylvio Schmidt (v), Guerino (acc), Christian Fauré (cb), Django Reinhardt, Meneghi Guerino (g).', 'BnF / Fonds Ch. Delaunay,Boîte 71, page 8', 'Guerino', 'paysage');
INSERT or IGNORE INTO Image (titre, chemin, date, nom_photographe,description,source,tag,orientation) VALUES ('Avec Jean Sablon au Bourget', '<img src="/static/img/029.jpg">', 'circa 1934','', 'Jean Sablon, Alec Siniavine, André Ekyan et Django Reinhardt au Bourget devant un avion Hillman s Airways en partance pour Londres.', 'Archives Jean Sablon', 'Sablon', 'paysage');
INSERT or IGNORE INTO Image (titre, chemin, date, nom_photographe,description,source,tag,orientation) VALUES ('Première photographie officielle du Quintette du HCF', '<img src="/static/img/042.jpg">', 'hiver 1934-1935','', 'Première photographie officielle du Quintette du HCF par Juliette Lasserre. De gauche à droite : Assis : Stéphane Grappelli (vl), Roger Chaput (g), Django Reinhardt, Joseph Reinhardt (g). Debouts : Louis Vola (cb)  et le chanteur Bert Marshall. Cette photo est dédicacée à Jean Sablon par Grappelli et Django.', 'Archives Jean Sablon', 'Quintette', 'paysage');
INSERT or IGNORE INTO Image (titre, chemin, date, nom_photographe,description,source,tag,orientation) VALUES ('Quintette du HCF avec Pierre Nourry', '<img src="/static/img/043.jpg">', 'circa 1937','', 'Quintette du HCF avec Pierre Nourry. De gauche à droite : Assis : Roger Chaput (g), Louis Vola (cb), Joseph Reinhardt (g). Debouts : Django Reinhardt, Pierre Nourry (fondateur du Quintette du HCF) et Stéphane Grappelli.', 'Archives Pierre Nourry', 'Quintette', 'portrait');
INSERT or IGNORE INTO Image (titre, chemin, date, nom_photographe,description,source,tag,orientation) VALUES ('Quintette du HCF avec Pierre Nourry', '<img src="/static/img/044.jpg">', 'vers 1937','Studio Tronchet', 'Quintette du HCF avec Pierre Nourry vers 1937. De gauche à droite : Assis : Roger Chaput (g), Louis Vola avec un jouet (cb), Joseph Reinhardt (g). Debouts : Django Reinhardt, Pierre Nourry (fondateur du Quintette du HCF) et Stéphane Grappelli.', 'BnF / Fonds Ch. Delaunay, Boîte 71, page 10', 'Quintette', 'portrait');
INSERT or IGNORE INTO Image (titre, chemin, date, nom_photographe,description,source,tag,orientation) VALUES ('Le Quintette du HCF au Big Apple, rue Pigalle', '<img src="/static/img/061.jpg">', 'Été 1937','', 'Le Quintette du HCF au Big Apple, rue Pigalle. De gauche à droite : Django Reinhardt, Joseph Reinhardt (g) cachant en partie Gusti Malha (g), Louis Vola (cb), Stéphane Grappelli (vl) et Anne de Crépy (soeur de Pierre Nourry).', 'BnF / Fonds Ch. Delaunay, Boîte 71, page 14', 'Quintette', 'paysage');
INSERT or IGNORE INTO Image (titre, chemin, date, nom_photographe,description,source,tag,orientation) VALUES ('Le Quintette du HCF à la gare d Anvers, Belgique', '<img src="/static/img/073.jpg">', 'novembre 1937','', 'Le Quintette du HCF à la gare d Anvers, Belgique. De gauche à droite : Louis Vola (avec le cigare), Naguine, Gusti Malha, Django Reinhardt, Hans Philippi (Suisse installé à Anvers, Président du Jazz Club d Anvers), Charles Delaunay, inconnu et Stéphane Grappelli (fumant une cigarette).', 'BnF / Fonds Ch. Delaunay, Boîte 71, page 15 c ou cote cliché reproduit : NQ-D-006873', 'Quintette', 'paysage');
INSERT or IGNORE INTO Image (titre, chemin, date, nom_photographe,description,source,tag,orientation) VALUES ('Django Reinhardt dans le train à la gare d Anvers, Belgique', '<img src="/static/img/074.jpg">', 'novembre 1937','Hans Philippi', 'Charles Delaunay, Naguine et Django Reinhardt dans le train à la gare d Anvers, Belgique. Novembre 1937.', 'BnF / Fonds Ch. Delaunay, Boîte 71, page 15 a', 'Naguine', 'paysage');
INSERT or IGNORE INTO Image (titre, chemin, date, nom_photographe,description,source,tag,orientation) VALUES ('Le Quintette du HCF à Londres dans les studios Decca', '<img src="/static/img/078.jpg">', 'janvier 1938','', 'Le Quintette du HCF à Londres dans les studios Decca. De gauche à droite : Stéphane Grappelli (vl), Eugène Vées, (g), Roger Grasset (cb), Django Reinhardt et Joseph Reinhardt (g).', 'BnF / Fonds Ch. Delaunay, Boîte 71, page 16 ou cote cliché reproduit : NB-A-095004', 'Quintette', 'portrait');
INSERT or IGNORE INTO Image (titre, chemin, date, nom_photographe,description,source,tag,orientation) VALUES ('Django Reinhardt à Stockholm', '<img src="/static/img/080.jpg">', 'février 1939','', 'Django Reinhardt et Stéphane Grappelli à Stockholm.', 'BnF / Fonds Ch. Delaunay, Boîte 71, page 17 a', 'Grappelli', 'paysage');
INSERT or IGNORE INTO Image (titre, chemin, date, nom_photographe,description,source,tag,orientation) VALUES ('Inauguration des locaux du Hot Club de France et de Jazz Hot au 14 rue Chaptal, Paris Ixe', '<img src="/static/img/082.jpg">', '1er avril 1939','', 'Inauguration des locaux du Hot Club de France et de Jazz Hot au 14 rue Chaptal, Paris IXe. Au centre, Duke Ellington. A gauche, Rex Stewart (tp), Django Reinhardt. A droite, Louis Vola (cb), Max Geldray (har). En haut, Joseph Reinhardt (g) et Salvador Nepus (har). 1er avril 1939.', 'BnF / Fonds Ch. Delaunay, Boîte 71, page 17 b ou cote cliché reproduit : 99-B-157251', 'Hot Club de France', 'portrait');
INSERT or IGNORE INTO Image (titre, chemin, date, nom_photographe,description,source,tag,orientation) VALUES ('Jam-Session dans la cave du Hot Club de France ', '<img src="/static/img/083.jpg">', '1er avril 1939','', 'Jam-Session dans la cave du Hot Club de France : Django Reinhardt au piano, Joseph à la contrebasse, Pierre Fouad à la batterie, Alix Combelle au sax ténor, Hubert Rostaing à la clarinette, Christian Bellest (trompette à gauche) et Pierre Allier (trompette à droite). ', 'Archives Hubert Rostaing', 'Hot Club de France', 'portrait');
INSERT or IGNORE INTO Image (titre, chemin, date, nom_photographe,description,source,tag,orientation) VALUES ('Django, Michael Carr et Stéphane Grappelli', '<img src="/static/img/084.jpg">', 'circa 1939','', 'Django et le compositeur anglais Michael Carr et Stéphane Grappelli avant la Seconde Guerre mondiale. ', 'Archives Hubert Rostaing', 'Michael Carr', 'portrait');
INSERT or IGNORE INTO Image (titre, chemin, date, nom_photographe,description,source,tag,orientation) VALUES ('Django présente son nouveau Quintette du Hot Club de France ', '<img src="/static/img/085.jpg">', 'octobre 1940','Marcel Arthaud', 'Django présente son nouveau Quintette du Hot Club de France avec la chanteuse Josette Daydé au cinéma Normandie, avenue des Champs-Élysées, Paris :  Django (g), Hubert Rostaing (cl), Francis Luca (cb). Ici pas de chanteuse sur la photo.', 'Musée Niepce/ Collection Marcel Arthaud, Album 7 : Jazz - musique classique – littérature, Jazz 901', 'Quintette', 'portrait');
INSERT or IGNORE INTO Image (titre, chemin, date, nom_photographe,description,source,tag,orientation) VALUES ('Django présente son nouveau Quintette du Hot Club de France ', '<img src="/static/img/086.jpg">', 'octobre 1940','Marcel Arthaud', 'Django présente son nouveau Quintette du Hot Club de France avec la chanteuse Josette Daydé au cinéma Normandie, avenue des Champs-Élysées, Paris : Hubert Rostaing (cl), Joseph Reinhardt (g), Pierre Fouad (dm), Django (g), Francis Luca (cb). ', 'Musée Niepce/ Collection Marcel Arthaud, Album 7 : Jazz - musique classique – littérature, Jazz 902', 'Quintette', 'portrait');
INSERT or IGNORE INTO Image (titre, chemin, date, nom_photographe,description,source,tag,orientation) VALUES ('Django, Babik et Negros au Bourget', '<img src="/static/img/203.jpg">', '1949','Michel Descamps / Paris Match / Scoop', 'Babik jouant de la guitare avec son père Django à l extérieur de la Roulotte au Bourget. La mère de Django, Negros est à l intérieur et les regarde.', 'Scoop, M0174840', 'Babik', 'portrait');
INSERT or IGNORE INTO Image (titre, chemin, date, nom_photographe,description,source,tag,orientation) VALUES ('Django Reinhardt à l Aquarium de New York.', '<img src="/static/img/267.jpg">', 'novembre 1946','William P. Gottlieb ', 'Django Reinhardt jouant sur une guitare Gibson à l Aquarium de New York.', 'Library of Congress, LC-GLB23- 0733 ', 'New York', 'portrait');

