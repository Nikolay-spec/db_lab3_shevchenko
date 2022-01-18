select * from clubs;
create table clubscopy as select * from clubs; 
select * from clubscopy;


DO $$
DECLARE
    team_id     clubscopy.team_id%TYPE;
	team_name   clubscopy.team_name%TYPE;
	

BEGIN
    team_id := 10000;
    team_name := 'Name';
	
    FOR counter IN 1..10
        LOOP
            INSERT INTO clubscopy(team_id, team_name)
            VALUES (team_id + counter, team_name || counter);
        END LOOP;
END;
$$
