CREATE  VIEW V_users_commenters
    AS 
    select dt.* , uu.username commenter_username, uu.id commenter_id,
-- calculate distance
uu.address__geo__lat commenter_lat, uu.address__geo__lng commenter_lng,
 distance(poster_lat, poster_lng, uu.address__geo__lat, uu.address__geo__lng) distance
from users uu inner join
(
SELECT p.userid poster_id, u.username poster_username, u.address__geo__lat poster_lat, u.address__geo__lng poster_lng,
 pc.email commenter_email, count(0) nr_of_times_commented  
FROM posts p, post_comments pc, users u  
where p.id = pc.postId
and p.userId = u.id
-- and p.userid = 21
group by p.userid , pc.email 
having count(0) >= 3
) as dt 
on uu.email = dt.commenter_email
order by nr_of_times_commented desc
