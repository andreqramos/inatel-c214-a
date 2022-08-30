import pytest
from src.teacher_attending_time import TeacherAttendingTime


def get_source_sample():
    source = {
        'teacher_name': 'Christopher',
        'start_hour': '17:30',
        'period': 'full',
    }
    return source


class TestTeacherAttendingTimeTeacherName:

    def test_teacher_attending_time_teacher_name_equals_Christopher(self):
        source = get_source_sample()
        source['teacher_name'] = 'Christopher'
        teacher_attending_time = TeacherAttendingTime(**source)
        assert teacher_attending_time.teacher_name == 'Christopher'

    def test_teacher_attending_time_teacher_name_equals_Marcelo(self):
        source = get_source_sample()
        source['teacher_name'] = 'Marcelo'
        teacher_attending_time = TeacherAttendingTime(**source)
        assert teacher_attending_time.teacher_name == 'Marcelo'


class TestTeacherAttendingTimeStartHour:

    def test_teacher_attending_time_start_hour_equals_17_30(self):
        source = get_source_sample()
        source['start_hour'] = '17:30'
        teacher_attending_time = TeacherAttendingTime(**source)
        assert teacher_attending_time.start_hour == '17:30'

    def test_teacher_attending_time_start_hour_equals_19_00(self):
        source = get_source_sample()
        source['start_hour'] = '19:00'
        teacher_attending_time = TeacherAttendingTime(**source)
        assert teacher_attending_time.start_hour == '19:00'


class TestTeacherAttendingTimePeriod:

    def test_teacher_attending_time_period_equals_full(self):
        source = get_source_sample()
        source['period'] = 'full'
        teacher_attending_time = TeacherAttendingTime(**source)
        assert teacher_attending_time.period == 'full'

    def test_teacher_attending_time_period_equals_night(self):
        source = get_source_sample()
        source['period'] = 'night'
        teacher_attending_time = TeacherAttendingTime(**source)
        assert teacher_attending_time.period == 'night'


