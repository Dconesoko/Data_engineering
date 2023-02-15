WITH base AS ( -- Count the number of medals won by each team in each event
SELECT event, team, COUNT(CASE WHEN medal IS NOT NULL THEN 1 END) AS num_medals
FROM olympics_athletes_events
WHERE year = 2016
GROUP BY 1, 2
),

-- rank teams by the number of medals won in each event
 team_rank AS (
SELECT *, ROW_NUMBER() OVER (PARTITION BY event ORDER BY event, num_medals DESC, team) AS fq
FROM base
WHERE num_medals != 0
),

-- select the gold, silver, and bronze medalist teams for each event
gold_team AS (
SELECT event, team AS gold_team, num_medals, FORMAT('%s with %s medals', team, num_medals) AS gold, fq
FROM team_rank 
WHERE fq = 1
),
silver_team AS (
SELECT event, team AS silver_team, num_medals, FORMAT('%s with %s medals', team, num_medals) AS silv, fq
FROM team_rank 
WHERE fq = 2
),
bronze_team AS (
SELECT event, team AS bronze_team, num_medals, FORMAT('%s with %s medals', team, num_medals) AS bronze, fq
FROM team_rank 
WHERE fq = 3
)

-- select statement to retrieve the medalist teams for each event, or "No team" if no team won a medal in the event
SELECT A.event, COALESCE(B.gold, 'No team') AS gold_medalist, COALESCE(C.silv, 'No team') AS silver_medalist, COALESCE(D.bronze, 'No team') AS bronze_medalist
FROM (
SELECT DISTINCT event
FROM olympics_athletes_events
WHERE year = 2016 AND medal IS NOT NULL
) AS A
LEFT JOIN gold_team AS B
ON A.event = B.event
LEFT JOIN silver_team AS C
ON A.event = C.event
LEFT JOIN bronze_team AS D
ON A.event = D.event;