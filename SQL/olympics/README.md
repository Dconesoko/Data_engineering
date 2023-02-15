## PROBLEM STATEMENT
 :bomb: **Find the top 3 medal-winning teams by counting the total number of medals
for each event in the Rio De Janeiro 2016 olympics. In case there is a tie, 
order the countries by name in descending order.Output the event name along
with the top 3 teams as the 'gold team', 'silver team', and 'bronze team',
with the team name and the total medals under each column in format "{team} 
with {number of medals} medals".Replace NULLs with "No Team" string.**

<img src="https://github.com/Dconesoko/Data_engineering/blob/dev/SQL/olympics/Capture.PNG?raw=true" width="70%">

### Solution

```sql
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
```

### Output data
<img src="https://github.com/Dconesoko/Data_engineering/blob/dev/SQL/olympics/Solution.PNG?raw=true" width="70%">
