Q_ALL_STAFF_ALPHA = """
select personal || ' ' || family as name
from staff
order by family
"""

Q_COUNT_EXP_BY_STAFF = """
select staff_id, count(*) as num_experiments
from performed
group by staff_id
order by staff_id
"""

Q_MOST_RECENT_INVALIDATERS = """
select distinct staff.personal || ' ' || staff.family as name
from staff join invalidated
on staff.staff_id = invalidated.staff_id
where invalidated.rowid in (
    select rowid
    from invalidated
    where date = (
        select max(date) from invalidated
    )	
)
order by staff.family, staff.personal
"""
