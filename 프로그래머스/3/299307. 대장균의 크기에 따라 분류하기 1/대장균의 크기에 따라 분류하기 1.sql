select ID, 
        case 
        WHEN SIZE_OF_COLONY > 1000 then 'HIGH'
        WHEN SIZE_OF_COLONY > 100 then 'MEDIUM'
        ELSE 'LOW'
        END as SIZE
from ECOLI_DATA
order by ID;
