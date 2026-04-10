SELECT datname,
       pid,
       usename,
       application_name,
       backend_start,
       xact_start,
       query_start,
       state_change,
       wait_event,
       state,
       query,
       backend_type
FROM pg_stat_activity
WHERE usename='postgres' AND datname='test';
SELECT pg_backend_pid();
SELECT * FROM pg_stat_activity;
ALTER USER postgres WITH PASSWORD 'c*@k%!h)y^xrf+pw~d$e';
SELECT * FROM pg_stat_ssl;