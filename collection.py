#수정됨
import pymssql

from diskUsage import getDiskSpace
from startDay import getStartDay
from totalRows import getTotalRows
from patientCount import getPatientCount
from waveRows import getWaveRows
from waveTrand import getWaveTrand
from patientMonthly import getPatientMonthly
from patientDaily import getPatientDaily
from waveType import getWaveType


def get_data():
    with pymssql.connect(host='10.5.99.80',
                         user='labuser', password='foqdbwj202012#$') as conn:
        with conn.cursor() as cur:
            data = {
                'storage': getDiskSpace(),
                'day_count': getStartDay(cur),
                'total_rows': getTotalRows(cur),
                'total_patients': getPatientCount(cur),
                'wave_rows': getWaveRows(cur),
                'wave_trand': getWaveTrand(cur),
                'patient_monthly': getPatientMonthly(cur),
                'patient_daily': getPatientDaily(cur),
                'wave_type': getWaveType(cur)
            }

    return data
