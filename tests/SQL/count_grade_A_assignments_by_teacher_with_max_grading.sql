-- Write query to find the number of grade A's given by the teacher who has graded the most assignments
WITH TeacherGradedCount AS (
    SELECT 
        teacher_id, 
        COUNT(*) AS graded_count
    FROM 
        assignments
    WHERE 
        state = 'GRADED'
    GROUP BY 
        teacher_id
),
TopTeacher AS (
    SELECT 
        teacher_id
    FROM 
        TeacherGradedCount
    ORDER BY 
        graded_count DESC    
)
SELECT 
    COUNT(*) AS grade_a_count
FROM 
    assignments
WHERE 
    teacher_id = (SELECT teacher_id FROM TopTeacher)
    AND grade = 'A';
