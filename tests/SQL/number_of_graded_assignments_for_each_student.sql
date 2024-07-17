-- Write query to get number of graded assignments for each student:
SELECT 
    students.id AS student_id,
    COUNT(assignments.id) AS graded_assignments_count
FROM 
    students
JOIN 
    assignments ON students.id = assignments.student_id
WHERE 
    assignments.state = 'GRADED'
GROUP BY 
    students.id;