select count(f.ID) as FISH_COUNT
from FISH_INFO f
left join FISH_NAME_INFO f_n
on f.FISH_TYPE  = f_n.FISH_TYPE
where f_n.FISH_NAME = "BASS" or  f_n.FISH_NAME = "SNAPPER"