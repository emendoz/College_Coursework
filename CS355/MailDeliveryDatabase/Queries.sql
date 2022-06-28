use emendoza_cs355fl20;

#Query 1
SELECT t.Receipt_Number, Status, Tracking_Number, Street, City, State, ZIP_Code 
FROM Transport t
JOIN Mail m
ON t.Receipt_Number = m.Receipt_Number 
JOIN Person p 
ON p.Receipt_Number = t.Receipt_Number
JOIN Delivery_Worker d 
ON d.Receipt_Number = m.Receipt_Number
WHERE Status = 'IN TRANSIT'
     ORDER BY m.Receipt_Number;
     
# A query to show what mail type is set to 'Letter' (extra created query)
SELECT Status, m.Receipt_Number, Date_Recieved, Type, Price, Weight
FROM Mail m
JOIN Transport t ON t.Receipt_Number = m.Receipt_Number 
JOIN Delivery_Worker d ON d.Receipt_Number = t.Receipt_Number
JOIN Person p ON p.Receipt_Number = m.Receipt_Number 
WHERE Type = 'Letter'
GROUP BY m.Receipt_Number;
    
#Query 2
SELECT DISTINCT Type FROM Mail;

#Query 3
SELECT Receipt_Number AS Receipt From Mail
UNION
SELECT Receipt_Number AS Receipt FROM Person;

#Query 4
UPDATE Transport
SET status = 'MISSING'
WHERE Tracking_Number = 'PSJH21960143570';

#Query 5
CREATE OR REPLACE VIEW Status AS
SELECT Tracking_Number, Status, Estimated_Arrival_Time FROM Transport
ORDER BY Estimated_Arrival_Time DESC
LIMIT 2;
SELECT * FROM Status ORDER BY Tracking_Number;

#Query 6
CREATE OR REPLACE VIEW status_counts AS
SELECT Tracking_Number, COUNT(Tracking_Number) AS count, status FROM Transport 
GROUP BY Status;
DROP FUNCTION IF EXISTS stat_count;
DELIMITER //
CREATE FUNCTION stat_count(_status varchar(25)) RETURNS bigint BEGIN
DECLARE theCount bigint;
SELECT count INTO theCount FROM status_counts
WHERE status = _status; RETURN theCount;
END// DELIMITER ;
SELECT stat_count('DELIVERED');
