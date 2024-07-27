select distinct staff.personal || ' ' || staff.family
from staff join invalidated
on staff.staff_id = invalidated.staff_id
where invalidated.rowid in (
    select rowid
    from invalidated
    where date = (
        select max(date) from invalidated
    )	
);
