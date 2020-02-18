DELIMITER $$
CREATE DEFINER=`adriana`@`%` FUNCTION `Distance`(

        lat1 FLOAT, lon1 FLOAT,
        lat2 FLOAT, lon2 FLOAT
     ) RETURNS decimal(10,2)
    NO SQL
    DETERMINISTIC
BEGIN

    RETURN DEGREES(ACOS(
              COS(RADIANS(lat1)) *
              COS(RADIANS(lat2)) *
              COS(RADIANS(lon2) - RADIANS(lon1)) +
              SIN(RADIANS(lat1)) * SIN(RADIANS(lat2))
            ));
END$$
DELIMITER ;