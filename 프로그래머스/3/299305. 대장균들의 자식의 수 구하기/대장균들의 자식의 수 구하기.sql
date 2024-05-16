
select e1.ID, IFNULL(e2.CHILD_COUNT, 0) as CHILD_COUNT
from ECOLI_DATA e1
left join (select PARENT_ID, count(*) as CHILD_COUNT
          from ECOLI_DATA
          group by PARENT_ID) e2
on e1.ID = e2.PARENT_ID
