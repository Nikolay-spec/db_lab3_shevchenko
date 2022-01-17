select * from clubs;
create table clubscopy as select * from clubs; 
select * from clubscopy;


DO $$
DECLARE
    team_id     clubscopy.team_id%TYPE;
    team_logo   clubscopy.team_logo%TYPE;
	  team_name   clubscopy.team_name%TYPE;
	

BEGIN
    team_id := 10000;
	  team_logo := 'Script';
    team_name := 'Name';
	
    FOR counter IN 1..10
        LOOP
            INSERT INTO clubscopy(team_id, team_logo, team_name)
            VALUES (team_id + counter, team_logo || counter, team_name || counter);
        END LOOP;
END;
$$
