select inf.ITEM_ID, inf.ITEM_NAME, inf.RARITY
from ITEM_INFO inf
left join ITEM_TREE tre
on inf.ITEM_ID = tre.ITEM_ID
left join ITEM_INFO inf2
on inf2.ITEM_ID = tre.PARENT_ITEM_ID
where tre.PARENT_ITEM_ID is not null and inf2.RARITY = "RARE"
order by inf.ITEM_ID desc
