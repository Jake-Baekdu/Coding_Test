-- 코드를 입력하세요
SELECT hour(datetime) as 'hour', count(hour(datetime)) as count
from animal_outs
Where hour(datetime) between 9 and 19
group by hour
order by hour