DROP TABLE IF EXISTS cities;
CREATE TABLE cities
    ( id bigint NOT NULL AUTO_INCREMENT,
      name varchar(256) NOT NULL, region varchar(256) NOT NULL,
      creation_date timestamp DEFAULT CURRENT_TIMESTAMP NULL,
      PRIMARY KEY (id),
  CONSTRAINT cities_ix1 UNIQUE (name, region)) ENGINE=InnoDB DEFAULT CHARSET=latin1;

DROP TABLE IF EXISTS trips;

CREATE TABLE trips
    ( id bigint NOT NULL AUTO_INCREMENT, origin bigint NOT NULL,
      destination bigint NOT NULL,
      timestamp timestamp DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
      time bigint NOT NULL, text_time varchar(256) NOT NULL, PRIMARY KEY (id),
      INDEX Trips_fk1 (origin), INDEX Trips_fk2 (destination)) ENGINE=InnoDB DEFAULT CHARSET=latin1;

ALTER TABLE trips ADD CONSTRAINT Trips_fk2 FOREIGN KEY (destination) REFERENCES cities (id) ;
ALTER TABLE trips ADD CONSTRAINT Trips_fk1 FOREIGN KEY (origin) REFERENCES cities (id);