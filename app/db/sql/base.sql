select
	*
from
	t_student ts
	left join
		t_students_attend_class tsac
			on ts.studentId =tsac.studentId
	left join
		t_classes tc
			on tsac.classId =tc.classId
where
    tc.gradeId in (2,3,4,5,6)
    and tc.schoolId =4404001




select
	*
from
	t_classes
where
    gradeId in (2,3,4,5,6)
    and schoolId =4404001




select
    tte.studentId ,tte.teacherId , tte.content ,tte.score, tte.subject, tte.week,14
from t_teacher_evaluation_2022_2023_2 tte
    left join t_student ts on tte.studentId =ts.studentId
    left join t_students_attend_class tsac on ts.studentId =tsac.studentId
    left join t_classes tc on tsac.classId = tc.classId
where
    tc.gradeId in (2,3,4,5,6)
    and tc.schoolId =4404001
    and tte.teacherId != '8a7dbfa2-f43a-4e54-b0c2-333e4e90f5e6'




select
    ttt.teacherId, ttt.teacherName, ttt.schoolId
from t_teachers ttt
    left join t_teach tt on ttt.teacherId =tt.teacherId
    left join t_classes tc on tt.classId = tc.classId
where
    tc.gradeId in (2,3,4,5,6)
    and tc.schoolId =4404001
    and tt.masterId in (0,1)
group by ttt.teacherId




select
    tt.teacherId, tt.classId
from t_teach tt
    left join t_classes tc on tt.classId = tc.classId
where
    tc.gradeId in (2,3,4,5,6)
    and tc.schoolId =4404001
    and tt.masterId in (0)
