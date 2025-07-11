from graphviz import Digraph

# Create a new directed graph
dot = Digraph(comment='E-Learn ER Diagram', format='png')

# Define nodes (entities)
dot.node('User', 'User\n- userId (PK)\n- userName\n- userEmail\n- password\n- role')
dot.node('Course', 'Course\n- courseId (PK)\n- instructorId (FK)\n- title\n- category\n- level\n- pricing')
dot.node('Lecture', 'Lecture\n- lectureId (PK)\n- courseId (FK)\n- title\n- videoUrl\n- freePreview')
dot.node('CourseProgress', 'CourseProgress\n- progressId (PK)\n- userId (FK)\n- courseId (FK)\n- completed')
dot.node('Order', 'Order\n- orderId (PK)\n- userId (FK)\n- courseId (FK)\n- paymentStatus')
dot.node('StudentCourses', 'StudentCourses\n- studentCoursesId (PK)\n- userId (FK)\n- courseId (FK)')
dot.node('Quiz', 'Quiz\n- quizId (PK)\n- courseId (FK)\n- questions')
dot.node('Certificate', 'Certificate\n- certificateId (PK)\n- userId (FK)\n- courseId (FK)\n- issueDate')

# Define relationships (edges)
dot.edges([
    ('User', 'StudentCourses'),
    ('Course', 'StudentCourses'),
    ('Course', 'Lecture'),
    ('User', 'CourseProgress'),
    ('Course', 'CourseProgress'),
    ('User', 'Order'),
    ('Course', 'Order'),
    ('Course', 'Quiz'),
    ('User', 'Certificate'),
    ('Course', 'Certificate')
])

# Render and display the ER diagram
dot.render('/mnt/data/e_learn_er_diagram', view=True)
'/mnt/data/e_learn_er_diagram.png'
