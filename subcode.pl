studies(alice, math).
studies(bob, physics).
studies(charlie, history).
studies(alice, chemistry).
studies(bob, math).
studies(diana, history).

% Predicate to represent a teacher teaching a subject.
% Format: teaches(teacher_name, subject_name).
teaches(mr_davis, math).
teaches(mrs_evans, physics).
teaches(mr_williams, history).
teaches(mr_davis, chemistry).

% Predicate to represent a subject's code.
% Format: subject_code(subject_name, code).
subject_code(math, 'MATH101').
subject_code(physics, 'PHYS201').
subject_code(history, 'HIST101').
subject_code(chemistry, 'CHEM301').












% Here are some example queries you could run in a Prolog interpreter:

% To find which subject Alice studies:
% ?- studies(alice, Subject).

% To find who studies History:
% ?- studies(Student, history).

% To find which teacher teaches math:
% ?- teaches(Teacher, math).

% To find the code for the physics subject:
% ?- subject_code(physics, Code).

% To find which students are taught by Mr. Davis (using a rule):
% ?- teaches(mr_davis, Subject), studies(Student, Subject).

% To find the subject code for the subject Bob studies (using a rule):
% ?- studies(bob, Subject), subject_code(Subject, Code).