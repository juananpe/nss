select staff_id, count(*)
from performed
group by staff_id;
