import math
import os

from ctypes import *
from datetime import *
from enum import *

parent = os.path.dirname(__file__)
nativelib = f'{parent}\\caaplus.dll'
try:
	_aaplus = CDLL(nativelib)
except:
	raise Exception(f'The expected native library was not found at: {nativelib}')

class Months(IntEnum):
	January = 1
	February = 2
	March = 3
	April = 4
	May = 5
	June = 6
	July = 7
	August = 8
	September = 9
	October = 10
	November = 11
	December = 12

class AA2DCoordinate(Structure):
	_fields_ = [
		('X', c_double),
		('Y', c_double)
	]

class AA3DCoordinate(Structure):
	_fields_ = [
		('X', c_double),
		('Y', c_double),
		('Z', c_double)
	]

class AAPlus:
	@staticmethod
	def Version():
		_func = _aaplus.CAAPlus_Version
		_func.argtypes = []
		_func.restype = c_char_p
		return _func().decode(encoding='ascii')

	@staticmethod
	def VersionNumber():
		_func = _aaplus.CAAPlus_VersionNumber
		_func.argtypes = []
		_func.restype = c_int
		return _func()


class AAAberration:
	@staticmethod
	def EarthVelocity(JD: float, bHighPrecision: bool):
		_func = _aaplus.CAAAberration_EarthVelocity
		_func.argtypes = [c_double, c_byte]
		_func.restype = AA3DCoordinate
		return _func(JD, bHighPrecision)

	@staticmethod
	def EclipticAberration(Alpha: float, Delta: float, JD: float, bHighPrecision: bool):
		_func = _aaplus.CAAAberration_EclipticAberration
		_func.argtypes = [c_double, c_double, c_double, c_byte]
		_func.restype = AA2DCoordinate
		return _func(Alpha, Delta, JD, bHighPrecision)

	@staticmethod
	def EquatorialAberration(Lambda: float, Beta: float, JD: float, bHighPrecision: bool):
		_func = _aaplus.CAAAberration_EquatorialAberration
		_func.argtypes = [c_double, c_double, c_double, c_byte]
		_func.restype = AA2DCoordinate
		return _func(Lambda, Beta, JD, bHighPrecision)


class AAAngularSeparation:
	@staticmethod
	def Separation(Alpha1: float, Delta1: float, Alpha2: float, Delta2: float):
		_func = _aaplus.CAAAngularSeparation_Separation
		_func.argtypes = [c_double, c_double, c_double, c_double]
		_func.restype = c_double
		return _func(Alpha1, Delta1, Alpha2, Delta2)

	@staticmethod
	def PositionAngle(Alpha1: float, Delta1: float, Alpha2: float, Delta2: float):
		_func = _aaplus.CAAAngularSeparation_PositionAngle
		_func.argtypes = [c_double, c_double, c_double, c_double]
		_func.restype = c_double
		return _func(Alpha1, Delta1, Alpha2, Delta2)

	@staticmethod
	def DistanceFromGreatArc(Alpha1: float, Delta1: float, Alpha2: float, Delta2: float, Alpha3: float, Delta3: float):
		_func = _aaplus.CAAAngularSeparation_DistanceFromGreatArc
		_func.argtypes = [c_double, c_double, c_double, c_double, c_double, c_double]
		_func.restype = c_double
		return _func(Alpha1, Delta1, Alpha2, Delta2, Alpha3, Delta3)

	@staticmethod
	def SmallestCircle(Alpha1: float, Delta1: float, Alpha2: float, Delta2: float, Alpha3: float, Delta3: float):
		_func = _aaplus.CAAAngularSeparation_SmallestCircle
		_func.argtypes = [c_double, c_double, c_double, c_double, c_double, c_double, POINTER(c_byte)]
		_func.restype = c_double
		_bType1 = c_byte()
		_res = _func(Alpha1, Delta1, Alpha2, Delta2, Alpha3, Delta3, byref(_bType1))
		return { 'SmallestCircle': _res, 'bType': bool(_bType1.value) }


class AABinaryStar:
	class AABinaryStarDetails(Structure):
		_fields_ = [
			('r', c_double),
			('Theta', c_double),
			('Rho', c_double),
			('x', c_double),
			('y', c_double),
		]

	@staticmethod
	def Calculate(t: float, P: float, T: float, e: float, a: float, i: float, omega: float, w: float):
		_func = _aaplus.CAABinaryStar_Calculate
		_func.argtypes = [c_double, c_double, c_double, c_double, c_double, c_double, c_double, c_double]
		_func.restype = AABinaryStar.AABinaryStarDetails
		return _func(t, P, T, e, a, i, omega, w)

	@staticmethod
	def ApparentEccentricity(e: float, i: float, w: float):
		_func = _aaplus.CAABinaryStar_ApparentEccentricity
		_func.argtypes = [c_double, c_double, c_double]
		_func.restype = c_double
		return _func(e, i, w)


class AACoordinateTransformation:
	@staticmethod
	def Equatorial2Ecliptic(Alpha: float, Delta: float, Epsilon: float):
		_func = _aaplus.CAACoordinateTransformation_Equatorial2Ecliptic
		_func.argtypes = [c_double, c_double, c_double]
		_func.restype = AA2DCoordinate
		return _func(Alpha, Delta, Epsilon)

	@staticmethod
	def Ecliptic2Equatorial(Lambda: float, Beta: float, Epsilon: float):
		_func = _aaplus.CAACoordinateTransformation_Ecliptic2Equatorial
		_func.argtypes = [c_double, c_double, c_double]
		_func.restype = AA2DCoordinate
		return _func(Lambda, Beta, Epsilon)

	@staticmethod
	def Equatorial2Horizontal(LocalHourAngle: float, Delta: float, Latitude: float):
		_func = _aaplus.CAACoordinateTransformation_Equatorial2Horizontal
		_func.argtypes = [c_double, c_double, c_double]
		_func.restype = AA2DCoordinate
		return _func(LocalHourAngle, Delta, Latitude)

	@staticmethod
	def Horizontal2Equatorial(A: float, h: float, Latitude: float):
		_func = _aaplus.CAACoordinateTransformation_Horizontal2Equatorial
		_func.argtypes = [c_double, c_double, c_double]
		_func.restype = AA2DCoordinate
		return _func(A, h, Latitude)

	@staticmethod
	def Equatorial2Galactic(Alpha: float, Delta: float):
		_func = _aaplus.CAACoordinateTransformation_Equatorial2Galactic
		_func.argtypes = [c_double, c_double]
		_func.restype = AA2DCoordinate
		return _func(Alpha, Delta)

	@staticmethod
	def Galactic2Equatorial(l: float, b: float):
		_func = _aaplus.CAACoordinateTransformation_Galactic2Equatorial
		_func.argtypes = [c_double, c_double]
		_func.restype = AA2DCoordinate
		return _func(l, b)

	@staticmethod
	def DegreesToRadians(Degrees: float):
		_func = _aaplus.CAACoordinateTransformation_DegreesToRadians
		_func.argtypes = [c_double]
		_func.restype = c_double
		return _func(Degrees)

	@staticmethod
	def RadiansToDegrees(Radians: float):
		_func = _aaplus.CAACoordinateTransformation_RadiansToDegrees
		_func.argtypes = [c_double]
		_func.restype = c_double
		return _func(Radians)

	@staticmethod
	def RadiansToHours(Radians: float):
		_func = _aaplus.CAACoordinateTransformation_RadiansToHours
		_func.argtypes = [c_double]
		_func.restype = c_double
		return _func(Radians)

	@staticmethod
	def HoursToRadians(Hours: float):
		_func = _aaplus.CAACoordinateTransformation_HoursToRadians
		_func.argtypes = [c_double]
		_func.restype = c_double
		return _func(Hours)

	@staticmethod
	def HoursToDegrees(Hours: float):
		_func = _aaplus.CAACoordinateTransformation_HoursToDegrees
		_func.argtypes = [c_double]
		_func.restype = c_double
		return _func(Hours)

	@staticmethod
	def DegreesToHours(Degrees: float):
		_func = _aaplus.CAACoordinateTransformation_DegreesToHours
		_func.argtypes = [c_double]
		_func.restype = c_double
		return _func(Degrees)

	@staticmethod
	def PI():
		_func = _aaplus.CAACoordinateTransformation_PI
		_func.argtypes = []
		_func.restype = c_double
		return _func()

	@staticmethod
	def MapTo0To360Range(Degrees: float):
		_func = _aaplus.CAACoordinateTransformation_MapTo0To360Range
		_func.argtypes = [c_double]
		_func.restype = c_double
		return _func(Degrees)

	@staticmethod
	def MapToMinus90To90Range(Degrees: float):
		_func = _aaplus.CAACoordinateTransformation_MapToMinus90To90Range
		_func.argtypes = [c_double]
		_func.restype = c_double
		return _func(Degrees)

	@staticmethod
	def MapTo0To24Range(HourAngle: float):
		_func = _aaplus.CAACoordinateTransformation_MapTo0To24Range
		_func.argtypes = [c_double]
		_func.restype = c_double
		return _func(HourAngle)

	@staticmethod
	def MapTo0To2PIRange(Angle: float):
		_func = _aaplus.CAACoordinateTransformation_MapTo0To2PIRange
		_func.argtypes = [c_double]
		_func.restype = c_double
		return _func(Angle)

	@staticmethod
	def DMSToDegrees(Degrees: float, Minutes: float, Seconds: float, bPositive: bool):
		_func = _aaplus.CAACoordinateTransformation_DMSToDegrees
		_func.argtypes = [c_double, c_double, c_double, c_byte]
		_func.restype = c_double
		return _func(Degrees, Minutes, Seconds, bPositive)
	
	@staticmethod
	def Degrees2DMS(Degrees: float, DegDelim: str = '°', MinDelim: str = '′', SecDelim: str = '″', FracDelim: str = '.'):
		'''
		Formats decimal degrees as a DMS string with customizable separator characters
		'''
		IsNegative = False
		if Degrees < 0:
			Degrees = -Degrees
			IsNegative = True

		WholeDeg = math.trunc(Degrees)
		DDD = f'{WholeDeg:02}'

		Minutes = (Degrees - WholeDeg) * 60
		WholeMin = math.trunc(Minutes)
		MM = f'{WholeMin:02}'

		Seconds = (Minutes - WholeMin) * 60
		WholeSec = math.trunc(Seconds)
		SS = f'{WholeSec:02}'

		Fracs = (Seconds - WholeSec) * 1000
		WholeFracs = math.trunc(Fracs)

		res = f'{DDD}{DegDelim}{MM}{MinDelim}{SS}{FracDelim}{WholeFracs}{SecDelim}'
		if IsNegative:
			res = f'-{res}'

		return res
	
	@staticmethod
	def Hours2HMS(Hours: float, HourDelim: str = ':', MinDelim: str = ':'):
		'''
		Formats decimal hours as a HMS string with customizable separator characters
		'''
		assert Hours >= 0

		WholeHour = math.trunc(Hours)
		HH = f'{WholeHour:02}'

		Minutes = (Hours - WholeHour) * 60
		WholeMin = math.trunc(Minutes)
		MM = f'{WholeMin:02}'

		Seconds = (Minutes - WholeMin) * 60
		WholeSec = math.trunc(Seconds)
		SS = f'{WholeSec:02}'

		return f'{HH}{HourDelim}{MM}{MinDelim}{SS}'


class AADate:
	def __init__(self, Year: int, Month: int, Day: float, Hour: float, Minute: float, Second: float, IsGregorian: bool):
		self.__ptr = self.__Create(Year, Month, Day, Hour, Minute, Second, IsGregorian)
		self.__year = Year
		self.__month = Month
		self.__day = Day
		self.__hour = Hour
		self.__minute = Minute
		self.__second = Second

	def __del__(self):
		self.__Destroy()

	class DOW(IntEnum):
		SUNDAY = 0
		MONDAY = 1
		TUESDAY = 2
		WEDNESDAY = 3
		THURSDAY = 4
		FRIDAY = 5
		SATURDAY = 6

	class AACalendarDate(Structure):
		_fields_ = [
			('Year', c_long),
			('Month', c_long),
			('Day', c_long),
		]

	@staticmethod
	def DateToJD(Year: int, Month: int, Day: float, bGregorianCalendar: bool):
		_func = _aaplus.CAADate_DateToJD
		_func.argtypes = [c_long, c_long, c_double, c_byte]
		_func.restype = c_double
		return _func(Year, Month, Day, bGregorianCalendar)

	@staticmethod
	def IsLeap(Year: int, bGregorianCalendar: bool):
		_func = _aaplus.CAADate_IsLeap
		_func.argtypes = [c_long, c_byte]
		_func.restype = c_byte
		return _func(Year, bGregorianCalendar)

	@staticmethod
	def DayOfYearToDayAndMonth(DayOfYear: int, bLeap: bool):
		_func = _aaplus.CAADate_DayOfYearToDayAndMonth
		_func.argtypes = [c_long, c_byte, POINTER(c_long), POINTER(c_long)]
		_func.restype = None
		_DayOfMonth = c_long()
		_Month = c_long()
		_func(DayOfYear, bLeap, byref(_DayOfMonth), byref(_Month))
		return { 'DayOfMonth': _DayOfMonth.value, 'Month': _Month.value }

	@staticmethod
	def JulianToGregorian(Year: int, Month: int, Day: int):
		_func = _aaplus.CAADate_JulianToGregorian
		_func.argtypes = [c_long, c_long, c_long]
		_func.restype = AADate.AACalendarDate
		return _func(Year, Month, Day)

	@staticmethod
	def GregorianToJulian(Year: int, Month: int, Day: int):
		_func = _aaplus.CAADate_GregorianToJulian
		_func.argtypes = [c_long, c_long, c_long]
		_func.restype = AADate.AACalendarDate
		return _func(Year, Month, Day)

	@staticmethod
	def INT(value: float):
		_func = _aaplus.CAADate_INT
		_func.argtypes = [c_double]
		_func.restype = c_long
		return _func(value)

	@staticmethod
	def AfterPapalReform(Year: int, Month: int, Day: float):
		_func = _aaplus.CAADate_AfterPapalReform
		_func.argtypes = [c_long, c_long, c_double]
		_func.restype = c_byte
		return _func(Year, Month, Day)

	@staticmethod
	def AfterPapalReform_2(JD: float):
		_func = _aaplus.CAADate_AfterPapalReform_2
		_func.argtypes = [c_double]
		_func.restype = c_byte
		return _func(JD)

	@staticmethod
	def DayOfYear(JD: float, Year: int, bGregorianCalendar: bool):
		_func = _aaplus.CAADate_DayOfYear
		_func.argtypes = [c_double, c_long, c_byte]
		_func.restype = c_double
		return _func(JD, Year, bGregorianCalendar)

	@staticmethod
	def DaysInMonth(Month: int, bLeap: bool):
		_func = _aaplus.CAADate_DaysInMonth
		_func.argtypes = [c_long, c_byte]
		_func.restype = c_long
		return _func(Month, bLeap)

	def __Create(self, Year: int, Month: int, Day: float, Hour: float, Minute: float, Second: float, IsGregorian: bool):
		_func = _aaplus.CAADate_Create
		_func.argtypes = [c_long, c_long, c_double, c_double, c_double, c_double, c_byte]
		_func.restype = c_void_p
		return _func(Year, Month, Day, Hour, Minute, Second, IsGregorian)

	def __Get(self):
		_func = _aaplus.CAADate_Get
		_func.argtypes = [c_void_p, POINTER(c_long), POINTER(c_long), POINTER(c_long), POINTER(c_long), POINTER(c_long), POINTER(c_double)]
		_func.restype = None
		_year = c_long()
		_month = c_long()
		_day = c_long()
		_hour = c_long()
		_minute = c_long()
		_second = c_double()
		_func(self.__ptr, byref(_year), byref(_month), byref(_day), byref(_hour), byref(_minute), byref(_second))
		self.__year = _year.value
		self.__month = _month.value
		self.__day = _day.value
		self.__hour = _hour.value
		self.__minute = _minute.value
		self.__second = _second.value

	def __Set(self, Year: int, Month: int, Day: float, Hour: float, Minute: float, Second: float, IsGregorian: bool):
		_func = _aaplus.CAADate_Set
		_func.argtypes = [c_void_p, c_long, c_long, c_double, c_double, c_double, c_double, c_byte]
		_func.restype = None
		_func(self.__ptr, Year, Month, Day, Hour, Minute, Second, IsGregorian)

	def __DayOfWeek(self):
		_func = _aaplus.CAADate_DayOfWeek
		_func.argtypes = [c_void_p]
		_func.restype = AADate.DOW
		return _func(self.__ptr)
	
	def __DaysInYear(self):
		_func = _aaplus.CAADate_DaysInYear
		_func.argtypes = [c_void_p]
		_func.restype = c_long
		return _func(self.__ptr)
	
	def __FractionalYear(self):
		_func = _aaplus.CAADate_FractionalYear
		_func.argtypes = [c_void_p]
		_func.restype = c_double
		return _func(self.__ptr)
	
	def __InGregorianCalendar(self):
		_func = _aaplus.CAADate_InGregorianCalendar
		_func.argtypes = [c_void_p]
		_func.restype = c_byte
		return _func(self.__ptr)
	
	def __Leap(self):
		_func = _aaplus.CAADate_Leap
		_func.argtypes = [c_void_p]
		_func.restype = c_byte
		return _func(self.__ptr)
	
	def __SetInGregorianCalendar(self, IsGregorian: bool):
		_func = _aaplus.CAADate_SetInGregorianCalendar
		_func.argtypes = [c_void_p, c_byte]
		_func.restype = None
		_func(self.__ptr, IsGregorian)

	def __Julian(self):
		_func = _aaplus.CAADate_Julian
		_func.argtypes = [c_void_p]
		_func.restype = c_double
		return _func(self.__ptr)
	
	def __Destroy(self):
		_func = _aaplus.CAADate_Destroy
		_func.argtypes = [c_void_p]
		_func.restype = None
		_func(self.__ptr)

	def Get(self):
		self.__Get()
		return {'Year': self.__year, 'Month': self.__month, 'Day': self.__day, 'Hour': self.__hour, 'Minute': self.__minute, 'Second': self.__second}
	
	def Set(self, Year: int, Month: int, Day: float, Hour: float, Minute: float, Second: float, IsGregorian: bool):
		self.__Set(Year, Month, Day, Hour, Minute, Second, IsGregorian)

	def DayOfWeek(self):
		return AADate.DOW(self.__DayOfWeek()).name
	
	def DaysInYear(self):
		return self.__DaysInYear()
	
	def FractionalYear(self):
		return self.__FractionalYear()
	
	def InGregorianCalendar(self):
		return bool(self.__InGregorianCalendar())
	
	def Leap(self):
		return bool(self.__Leap())
	
	def SetInGregorianCalendar(self, IsGregorian: bool):
		self.__SetInGregorianCalendar(IsGregorian)

	def Julian(self):
		return self.__Julian()
	
	@staticmethod
	def JDToDateParts(JD: float, IsGregorian: bool):
		_func = _aaplus.CAADate_JDToDateParts
		_func.argtypes = [c_double, c_byte, POINTER(c_long), POINTER(c_long), POINTER(c_long), POINTER(c_long), POINTER(c_long), POINTER(c_double)]
		_func.restype = None
		_year = c_long()
		_month = c_long()
		_day = c_long()
		_hour = c_long()
		_minute = c_long()
		_second = c_double()
		_func(JD, IsGregorian, byref(_year), byref(_month), byref(_day), byref(_hour), byref(_minute), byref(_second))
		return {'Year': _year.value, 'Month': _month.value, 'Day': _day.value, 'Hour': _hour.value, 'Minute': _minute.value, 'Second': _second.value}
	
	@staticmethod
	def DateTimeUTC2JD(dt: datetime, IsGregorian: bool = True):
		'''
		Converts Python datetime in UTC to Julian Day number
		'''
		assert dt.tzinfo == timezone.utc
		delta = timedelta(hours = dt.hour, minutes = dt.minute, seconds = dt.second)
		return AADate.DateToJD(dt.year, dt.month, dt.day + delta.total_seconds() / 86400, IsGregorian)
	
	@staticmethod
	def TT2DateTimeUTC(TimeTT: float):
		'''
		Converts Julian Day number in TT timeframe to Python datetime
		'''
		TimeUTC = AADynamicalTime.TT2UTC(TimeTT)
		res = AADate.JDToDateParts(TimeUTC, True)
		return datetime(year = int(res['Year']), month = int(res['Month']), day = int(res['Day']), hour = int(res['Hour']), minute = int(res['Minute']), second = int(res['Second']), tzinfo = timezone.utc)
	
	@staticmethod
	def DateTimeUTC2TT(dt: datetime, IsGregorian: bool = True):
		'''
		Converts Python datetime in UTC timeframe to TT timeframe JD number
		'''
		return AADynamicalTime.UTC2TT(AADate.DateTimeUTC2JD(dt, IsGregorian))


class AADiameters:
	@staticmethod
	def SunSemidiameterA(Delta: float):
		_func = _aaplus.CAADiameters_SunSemidiameterA
		_func.argtypes = [c_double]
		_func.restype = c_double
		return _func(Delta)

	@staticmethod
	def MercurySemidiameterA(Delta: float):
		_func = _aaplus.CAADiameters_MercurySemidiameterA
		_func.argtypes = [c_double]
		_func.restype = c_double
		return _func(Delta)

	@staticmethod
	def VenusSemidiameterA(Delta: float):
		_func = _aaplus.CAADiameters_VenusSemidiameterA
		_func.argtypes = [c_double]
		_func.restype = c_double
		return _func(Delta)

	@staticmethod
	def MarsSemidiameterA(Delta: float):
		_func = _aaplus.CAADiameters_MarsSemidiameterA
		_func.argtypes = [c_double]
		_func.restype = c_double
		return _func(Delta)

	@staticmethod
	def JupiterEquatorialSemidiameterA(Delta: float):
		_func = _aaplus.CAADiameters_JupiterEquatorialSemidiameterA
		_func.argtypes = [c_double]
		_func.restype = c_double
		return _func(Delta)

	@staticmethod
	def JupiterPolarSemidiameterA(Delta: float):
		_func = _aaplus.CAADiameters_JupiterPolarSemidiameterA
		_func.argtypes = [c_double]
		_func.restype = c_double
		return _func(Delta)

	@staticmethod
	def SaturnEquatorialSemidiameterA(Delta: float):
		_func = _aaplus.CAADiameters_SaturnEquatorialSemidiameterA
		_func.argtypes = [c_double]
		_func.restype = c_double
		return _func(Delta)

	@staticmethod
	def SaturnPolarSemidiameterA(Delta: float):
		_func = _aaplus.CAADiameters_SaturnPolarSemidiameterA
		_func.argtypes = [c_double]
		_func.restype = c_double
		return _func(Delta)

	@staticmethod
	def UranusSemidiameterA(Delta: float):
		_func = _aaplus.CAADiameters_UranusSemidiameterA
		_func.argtypes = [c_double]
		_func.restype = c_double
		return _func(Delta)

	@staticmethod
	def NeptuneSemidiameterA(Delta: float):
		_func = _aaplus.CAADiameters_NeptuneSemidiameterA
		_func.argtypes = [c_double]
		_func.restype = c_double
		return _func(Delta)

	@staticmethod
	def MercurySemidiameterB(Delta: float):
		_func = _aaplus.CAADiameters_MercurySemidiameterB
		_func.argtypes = [c_double]
		_func.restype = c_double
		return _func(Delta)

	@staticmethod
	def VenusSemidiameterB(Delta: float):
		_func = _aaplus.CAADiameters_VenusSemidiameterB
		_func.argtypes = [c_double]
		_func.restype = c_double
		return _func(Delta)

	@staticmethod
	def MarsSemidiameterB(Delta: float):
		_func = _aaplus.CAADiameters_MarsSemidiameterB
		_func.argtypes = [c_double]
		_func.restype = c_double
		return _func(Delta)

	@staticmethod
	def JupiterEquatorialSemidiameterB(Delta: float):
		_func = _aaplus.CAADiameters_JupiterEquatorialSemidiameterB
		_func.argtypes = [c_double]
		_func.restype = c_double
		return _func(Delta)

	@staticmethod
	def JupiterPolarSemidiameterB(Delta: float):
		_func = _aaplus.CAADiameters_JupiterPolarSemidiameterB
		_func.argtypes = [c_double]
		_func.restype = c_double
		return _func(Delta)

	@staticmethod
	def SaturnEquatorialSemidiameterB(Delta: float):
		_func = _aaplus.CAADiameters_SaturnEquatorialSemidiameterB
		_func.argtypes = [c_double]
		_func.restype = c_double
		return _func(Delta)

	@staticmethod
	def SaturnPolarSemidiameterB(Delta: float):
		_func = _aaplus.CAADiameters_SaturnPolarSemidiameterB
		_func.argtypes = [c_double]
		_func.restype = c_double
		return _func(Delta)

	@staticmethod
	def UranusSemidiameterB(Delta: float):
		_func = _aaplus.CAADiameters_UranusSemidiameterB
		_func.argtypes = [c_double]
		_func.restype = c_double
		return _func(Delta)

	@staticmethod
	def NeptuneSemidiameterB(Delta: float):
		_func = _aaplus.CAADiameters_NeptuneSemidiameterB
		_func.argtypes = [c_double]
		_func.restype = c_double
		return _func(Delta)

	@staticmethod
	def PlutoSemidiameterB(Delta: float):
		_func = _aaplus.CAADiameters_PlutoSemidiameterB
		_func.argtypes = [c_double]
		_func.restype = c_double
		return _func(Delta)

	@staticmethod
	def ApparentAsteroidDiameter(Delta: float, d: float):
		_func = _aaplus.CAADiameters_ApparentAsteroidDiameter
		_func.argtypes = [c_double, c_double]
		_func.restype = c_double
		return _func(Delta, d)

	@staticmethod
	def GeocentricMoonSemidiameter(Delta: float):
		_func = _aaplus.CAADiameters_GeocentricMoonSemidiameter
		_func.argtypes = [c_double]
		_func.restype = c_double
		return _func(Delta)

	@staticmethod
	def ApparentSaturnPolarSemidiameterA(Delta: float, B: float):
		_func = _aaplus.CAADiameters_ApparentSaturnPolarSemidiameterA
		_func.argtypes = [c_double, c_double]
		_func.restype = c_double
		return _func(Delta, B)

	@staticmethod
	def ApparentSaturnPolarSemidiameterB(Delta: float, B: float):
		_func = _aaplus.CAADiameters_ApparentSaturnPolarSemidiameterB
		_func.argtypes = [c_double, c_double]
		_func.restype = c_double
		return _func(Delta, B)

	@staticmethod
	def TopocentricMoonSemidiameter(DistanceDelta: float, Delta: float, H: float, Latitude: float, Height: float):
		_func = _aaplus.CAADiameters_TopocentricMoonSemidiameter
		_func.argtypes = [c_double, c_double, c_double, c_double, c_double]
		_func.restype = c_double
		return _func(DistanceDelta, Delta, H, Latitude, Height)

	@staticmethod
	def AsteroidDiameter(H: float, A: float):
		_func = _aaplus.CAADiameters_AsteroidDiameter
		_func.argtypes = [c_double, c_double]
		_func.restype = c_double
		return _func(H, A)


class AADynamicalTime:
	@staticmethod
	def SetUserDefinedDeltaT(pProc):
		_func = _aaplus.CAADynamicalTime_SetUserDefinedDeltaT
		return _func(pProc)

	@CFUNCTYPE(c_double, c_double)
	def SampleCallback(JD: float):
		print('This is just an example! Do not use this in production!')
		return 0.0

	@staticmethod
	def DeltaT(JD: float):
		_func = _aaplus.CAADynamicalTime_DeltaT
		_func.argtypes = [c_double]
		_func.restype = c_double
		return _func(JD)

	@staticmethod
	def CumulativeLeapSeconds(JD: float):
		_func = _aaplus.CAADynamicalTime_CumulativeLeapSeconds
		_func.argtypes = [c_double]
		_func.restype = c_double
		return _func(JD)

	@staticmethod
	def TT2UTC(JD: float):
		_func = _aaplus.CAADynamicalTime_TT2UTC
		_func.argtypes = [c_double]
		_func.restype = c_double
		return _func(JD)

	@staticmethod
	def UTC2TT(JD: float):
		_func = _aaplus.CAADynamicalTime_UTC2TT
		_func.argtypes = [c_double]
		_func.restype = c_double
		return _func(JD)

	@staticmethod
	def TT2TAI(JD: float):
		_func = _aaplus.CAADynamicalTime_TT2TAI
		_func.argtypes = [c_double]
		_func.restype = c_double
		return _func(JD)

	@staticmethod
	def TAI2TT(JD: float):
		_func = _aaplus.CAADynamicalTime_TAI2TT
		_func.argtypes = [c_double]
		_func.restype = c_double
		return _func(JD)

	@staticmethod
	def TT2UT1(JD: float):
		_func = _aaplus.CAADynamicalTime_TT2UT1
		_func.argtypes = [c_double]
		_func.restype = c_double
		return _func(JD)

	@staticmethod
	def UT12TT(JD: float):
		_func = _aaplus.CAADynamicalTime_UT12TT
		_func.argtypes = [c_double]
		_func.restype = c_double
		return _func(JD)

	@staticmethod
	def UT1MinusUTC(JD: float):
		_func = _aaplus.CAADynamicalTime_UT1MinusUTC
		_func.argtypes = [c_double]
		_func.restype = c_double
		return _func(JD)


class AAEarth:
	@staticmethod
	def EclipticLongitude(JD: float, bHighPrecision: bool):
		_func = _aaplus.CAAEarth_EclipticLongitude
		_func.argtypes = [c_double, c_byte]
		_func.restype = c_double
		return _func(JD, bHighPrecision)

	@staticmethod
	def EclipticLatitude(JD: float, bHighPrecision: bool):
		_func = _aaplus.CAAEarth_EclipticLatitude
		_func.argtypes = [c_double, c_byte]
		_func.restype = c_double
		return _func(JD, bHighPrecision)

	@staticmethod
	def RadiusVector(JD: float, bHighPrecision: bool):
		_func = _aaplus.CAAEarth_RadiusVector
		_func.argtypes = [c_double, c_byte]
		_func.restype = c_double
		return _func(JD, bHighPrecision)

	@staticmethod
	def SunMeanAnomaly(JD: float):
		_func = _aaplus.CAAEarth_SunMeanAnomaly
		_func.argtypes = [c_double]
		_func.restype = c_double
		return _func(JD)

	@staticmethod
	def Eccentricity(JD: float):
		_func = _aaplus.CAAEarth_Eccentricity
		_func.argtypes = [c_double]
		_func.restype = c_double
		return _func(JD)

	@staticmethod
	def EclipticLongitudeJ2000(JD: float, bHighPrecision: bool):
		_func = _aaplus.CAAEarth_EclipticLongitudeJ2000
		_func.argtypes = [c_double, c_byte]
		_func.restype = c_double
		return _func(JD, bHighPrecision)

	@staticmethod
	def EclipticLatitudeJ2000(JD: float, bHighPrecision: bool):
		_func = _aaplus.CAAEarth_EclipticLatitudeJ2000
		_func.argtypes = [c_double, c_byte]
		_func.restype = c_double
		return _func(JD, bHighPrecision)


class AAEaster:
    class AAEasterDetails(Structure):
        _fields_ = [
            ('Month', c_long),
            ('Day', c_long)
        ]

    @staticmethod
    def Calculate(nYear: int, GregorianCalendar: bool = True):
        '''
        Calculates Easter for the given year and returns the Easter month and day.
        '''
        _calc = _aaplus.CAAEaster_Calculate
        _calc.argtypes = [c_int, c_byte]
        _calc.restype = AAEaster.AAEasterDetails
        return _calc(nYear, GregorianCalendar)


class AAEclipses:
	class AASolarEclipseDetails(Structure):
		_fields_ = [
			('Flags', c_uint),
			('TimeOfMaximumEclipse', c_double),
			('F', c_double),
			('u', c_double),
			('gamma', c_double),
			('GreatestMagnitude', c_double),
		]

	class AALunarEclipseDetails(Structure):
		_fields_ = [
			('bEclipse', c_byte),
			('TimeOfMaximumEclipse', c_double),
			('F', c_double),
			('u', c_double),
			('gamma', c_double),
			('PenumbralRadii', c_double),
			('UmbralRadii', c_double),
			('PenumbralMagnitude', c_double),
			('UmbralMagnitude', c_double),
			('PartialPhaseSemiDuration', c_double),
			('TotalPhaseSemiDuration', c_double),
			('PartialPhasePenumbraSemiDuration', c_double),
		]

	@staticmethod
	def CalculateSolar(k: float):
		_func = _aaplus.CAAEclipses_CalculateSolar
		_func.argtypes = [c_double]
		_func.restype = AAEclipses.AASolarEclipseDetails
		return _func(k)

	@staticmethod
	def CalculateLunar(k: float):
		_func = _aaplus.CAAEclipses_CalculateLunar
		_func.argtypes = [c_double]
		_func.restype = AAEclipses.AALunarEclipseDetails
		return _func(k)


class AAEclipticalElements:
	class AAEclipticalElementDetails(Structure):
		_fields_ = [
			('i', c_double),
			('w', c_double),
			('omega', c_double),
		]

	@staticmethod
	def Calculate(i0: float, w0: float, omega0: float, JD0: float, JD: float):
		_func = _aaplus.CAAEclipticalElements_Calculate
		_func.argtypes = [c_double, c_double, c_double, c_double, c_double]
		_func.restype = AAEclipticalElements.AAEclipticalElementDetails
		return _func(i0, w0, omega0, JD0, JD)

	@staticmethod
	def FK4B1950ToFK5J2000(i0: float, w0: float, omega0: float):
		_func = _aaplus.CAAEclipticalElements_FK4B1950ToFK5J2000
		_func.argtypes = [c_double, c_double, c_double]
		_func.restype = AAEclipticalElements.AAEclipticalElementDetails
		return _func(i0, w0, omega0)


class AAElementsPlanetaryOrbit:
	@staticmethod
	def MercuryMeanLongitude(JD: float):
		_func = _aaplus.CAAElementsPlanetaryOrbit_MercuryMeanLongitude
		_func.argtypes = [c_double]
		_func.restype = c_double
		return _func(JD)

	@staticmethod
	def MercurySemimajorAxis(JD: float):
		_func = _aaplus.CAAElementsPlanetaryOrbit_MercurySemimajorAxis
		_func.argtypes = [c_double]
		_func.restype = c_double
		return _func(JD)

	@staticmethod
	def MercuryEccentricity(JD: float):
		_func = _aaplus.CAAElementsPlanetaryOrbit_MercuryEccentricity
		_func.argtypes = [c_double]
		_func.restype = c_double
		return _func(JD)

	@staticmethod
	def MercuryInclination(JD: float):
		_func = _aaplus.CAAElementsPlanetaryOrbit_MercuryInclination
		_func.argtypes = [c_double]
		_func.restype = c_double
		return _func(JD)

	@staticmethod
	def MercuryLongitudeAscendingNode(JD: float):
		_func = _aaplus.CAAElementsPlanetaryOrbit_MercuryLongitudeAscendingNode
		_func.argtypes = [c_double]
		_func.restype = c_double
		return _func(JD)

	@staticmethod
	def MercuryLongitudePerihelion(JD: float):
		_func = _aaplus.CAAElementsPlanetaryOrbit_MercuryLongitudePerihelion
		_func.argtypes = [c_double]
		_func.restype = c_double
		return _func(JD)

	@staticmethod
	def VenusMeanLongitude(JD: float):
		_func = _aaplus.CAAElementsPlanetaryOrbit_VenusMeanLongitude
		_func.argtypes = [c_double]
		_func.restype = c_double
		return _func(JD)

	@staticmethod
	def VenusSemimajorAxis(JD: float):
		_func = _aaplus.CAAElementsPlanetaryOrbit_VenusSemimajorAxis
		_func.argtypes = [c_double]
		_func.restype = c_double
		return _func(JD)

	@staticmethod
	def VenusEccentricity(JD: float):
		_func = _aaplus.CAAElementsPlanetaryOrbit_VenusEccentricity
		_func.argtypes = [c_double]
		_func.restype = c_double
		return _func(JD)

	@staticmethod
	def VenusInclination(JD: float):
		_func = _aaplus.CAAElementsPlanetaryOrbit_VenusInclination
		_func.argtypes = [c_double]
		_func.restype = c_double
		return _func(JD)

	@staticmethod
	def VenusLongitudeAscendingNode(JD: float):
		_func = _aaplus.CAAElementsPlanetaryOrbit_VenusLongitudeAscendingNode
		_func.argtypes = [c_double]
		_func.restype = c_double
		return _func(JD)

	@staticmethod
	def VenusLongitudePerihelion(JD: float):
		_func = _aaplus.CAAElementsPlanetaryOrbit_VenusLongitudePerihelion
		_func.argtypes = [c_double]
		_func.restype = c_double
		return _func(JD)

	@staticmethod
	def EarthMeanLongitude(JD: float):
		_func = _aaplus.CAAElementsPlanetaryOrbit_EarthMeanLongitude
		_func.argtypes = [c_double]
		_func.restype = c_double
		return _func(JD)

	@staticmethod
	def EarthSemimajorAxis(JD: float):
		_func = _aaplus.CAAElementsPlanetaryOrbit_EarthSemimajorAxis
		_func.argtypes = [c_double]
		_func.restype = c_double
		return _func(JD)

	@staticmethod
	def EarthEccentricity(JD: float):
		_func = _aaplus.CAAElementsPlanetaryOrbit_EarthEccentricity
		_func.argtypes = [c_double]
		_func.restype = c_double
		return _func(JD)

	@staticmethod
	def EarthInclination(JD: float):
		_func = _aaplus.CAAElementsPlanetaryOrbit_EarthInclination
		_func.argtypes = [c_double]
		_func.restype = c_double
		return _func(JD)

	@staticmethod
	def EarthLongitudePerihelion(JD: float):
		_func = _aaplus.CAAElementsPlanetaryOrbit_EarthLongitudePerihelion
		_func.argtypes = [c_double]
		_func.restype = c_double
		return _func(JD)

	@staticmethod
	def MarsMeanLongitude(JD: float):
		_func = _aaplus.CAAElementsPlanetaryOrbit_MarsMeanLongitude
		_func.argtypes = [c_double]
		_func.restype = c_double
		return _func(JD)

	@staticmethod
	def MarsSemimajorAxis(JD: float):
		_func = _aaplus.CAAElementsPlanetaryOrbit_MarsSemimajorAxis
		_func.argtypes = [c_double]
		_func.restype = c_double
		return _func(JD)

	@staticmethod
	def MarsEccentricity(JD: float):
		_func = _aaplus.CAAElementsPlanetaryOrbit_MarsEccentricity
		_func.argtypes = [c_double]
		_func.restype = c_double
		return _func(JD)

	@staticmethod
	def MarsInclination(JD: float):
		_func = _aaplus.CAAElementsPlanetaryOrbit_MarsInclination
		_func.argtypes = [c_double]
		_func.restype = c_double
		return _func(JD)

	@staticmethod
	def MarsLongitudeAscendingNode(JD: float):
		_func = _aaplus.CAAElementsPlanetaryOrbit_MarsLongitudeAscendingNode
		_func.argtypes = [c_double]
		_func.restype = c_double
		return _func(JD)

	@staticmethod
	def MarsLongitudePerihelion(JD: float):
		_func = _aaplus.CAAElementsPlanetaryOrbit_MarsLongitudePerihelion
		_func.argtypes = [c_double]
		_func.restype = c_double
		return _func(JD)

	@staticmethod
	def JupiterMeanLongitude(JD: float):
		_func = _aaplus.CAAElementsPlanetaryOrbit_JupiterMeanLongitude
		_func.argtypes = [c_double]
		_func.restype = c_double
		return _func(JD)

	@staticmethod
	def JupiterSemimajorAxis(JD: float):
		_func = _aaplus.CAAElementsPlanetaryOrbit_JupiterSemimajorAxis
		_func.argtypes = [c_double]
		_func.restype = c_double
		return _func(JD)

	@staticmethod
	def JupiterEccentricity(JD: float):
		_func = _aaplus.CAAElementsPlanetaryOrbit_JupiterEccentricity
		_func.argtypes = [c_double]
		_func.restype = c_double
		return _func(JD)

	@staticmethod
	def JupiterInclination(JD: float):
		_func = _aaplus.CAAElementsPlanetaryOrbit_JupiterInclination
		_func.argtypes = [c_double]
		_func.restype = c_double
		return _func(JD)

	@staticmethod
	def JupiterLongitudeAscendingNode(JD: float):
		_func = _aaplus.CAAElementsPlanetaryOrbit_JupiterLongitudeAscendingNode
		_func.argtypes = [c_double]
		_func.restype = c_double
		return _func(JD)

	@staticmethod
	def JupiterLongitudePerihelion(JD: float):
		_func = _aaplus.CAAElementsPlanetaryOrbit_JupiterLongitudePerihelion
		_func.argtypes = [c_double]
		_func.restype = c_double
		return _func(JD)

	@staticmethod
	def SaturnMeanLongitude(JD: float):
		_func = _aaplus.CAAElementsPlanetaryOrbit_SaturnMeanLongitude
		_func.argtypes = [c_double]
		_func.restype = c_double
		return _func(JD)

	@staticmethod
	def SaturnSemimajorAxis(JD: float):
		_func = _aaplus.CAAElementsPlanetaryOrbit_SaturnSemimajorAxis
		_func.argtypes = [c_double]
		_func.restype = c_double
		return _func(JD)

	@staticmethod
	def SaturnEccentricity(JD: float):
		_func = _aaplus.CAAElementsPlanetaryOrbit_SaturnEccentricity
		_func.argtypes = [c_double]
		_func.restype = c_double
		return _func(JD)

	@staticmethod
	def SaturnInclination(JD: float):
		_func = _aaplus.CAAElementsPlanetaryOrbit_SaturnInclination
		_func.argtypes = [c_double]
		_func.restype = c_double
		return _func(JD)

	@staticmethod
	def SaturnLongitudeAscendingNode(JD: float):
		_func = _aaplus.CAAElementsPlanetaryOrbit_SaturnLongitudeAscendingNode
		_func.argtypes = [c_double]
		_func.restype = c_double
		return _func(JD)

	@staticmethod
	def SaturnLongitudePerihelion(JD: float):
		_func = _aaplus.CAAElementsPlanetaryOrbit_SaturnLongitudePerihelion
		_func.argtypes = [c_double]
		_func.restype = c_double
		return _func(JD)

	@staticmethod
	def UranusMeanLongitude(JD: float):
		_func = _aaplus.CAAElementsPlanetaryOrbit_UranusMeanLongitude
		_func.argtypes = [c_double]
		_func.restype = c_double
		return _func(JD)

	@staticmethod
	def UranusSemimajorAxis(JD: float):
		_func = _aaplus.CAAElementsPlanetaryOrbit_UranusSemimajorAxis
		_func.argtypes = [c_double]
		_func.restype = c_double
		return _func(JD)

	@staticmethod
	def UranusEccentricity(JD: float):
		_func = _aaplus.CAAElementsPlanetaryOrbit_UranusEccentricity
		_func.argtypes = [c_double]
		_func.restype = c_double
		return _func(JD)

	@staticmethod
	def UranusInclination(JD: float):
		_func = _aaplus.CAAElementsPlanetaryOrbit_UranusInclination
		_func.argtypes = [c_double]
		_func.restype = c_double
		return _func(JD)

	@staticmethod
	def UranusLongitudeAscendingNode(JD: float):
		_func = _aaplus.CAAElementsPlanetaryOrbit_UranusLongitudeAscendingNode
		_func.argtypes = [c_double]
		_func.restype = c_double
		return _func(JD)

	@staticmethod
	def UranusLongitudePerihelion(JD: float):
		_func = _aaplus.CAAElementsPlanetaryOrbit_UranusLongitudePerihelion
		_func.argtypes = [c_double]
		_func.restype = c_double
		return _func(JD)

	@staticmethod
	def NeptuneMeanLongitude(JD: float):
		_func = _aaplus.CAAElementsPlanetaryOrbit_NeptuneMeanLongitude
		_func.argtypes = [c_double]
		_func.restype = c_double
		return _func(JD)

	@staticmethod
	def NeptuneSemimajorAxis(JD: float):
		_func = _aaplus.CAAElementsPlanetaryOrbit_NeptuneSemimajorAxis
		_func.argtypes = [c_double]
		_func.restype = c_double
		return _func(JD)

	@staticmethod
	def NeptuneEccentricity(JD: float):
		_func = _aaplus.CAAElementsPlanetaryOrbit_NeptuneEccentricity
		_func.argtypes = [c_double]
		_func.restype = c_double
		return _func(JD)

	@staticmethod
	def NeptuneInclination(JD: float):
		_func = _aaplus.CAAElementsPlanetaryOrbit_NeptuneInclination
		_func.argtypes = [c_double]
		_func.restype = c_double
		return _func(JD)

	@staticmethod
	def NeptuneLongitudeAscendingNode(JD: float):
		_func = _aaplus.CAAElementsPlanetaryOrbit_NeptuneLongitudeAscendingNode
		_func.argtypes = [c_double]
		_func.restype = c_double
		return _func(JD)

	@staticmethod
	def NeptuneLongitudePerihelion(JD: float):
		_func = _aaplus.CAAElementsPlanetaryOrbit_NeptuneLongitudePerihelion
		_func.argtypes = [c_double]
		_func.restype = c_double
		return _func(JD)

	@staticmethod
	def MercuryMeanLongitudeJ2000(JD: float):
		_func = _aaplus.CAAElementsPlanetaryOrbit_MercuryMeanLongitudeJ2000
		_func.argtypes = [c_double]
		_func.restype = c_double
		return _func(JD)

	@staticmethod
	def MercuryInclinationJ2000(JD: float):
		_func = _aaplus.CAAElementsPlanetaryOrbit_MercuryInclinationJ2000
		_func.argtypes = [c_double]
		_func.restype = c_double
		return _func(JD)

	@staticmethod
	def MercuryLongitudeAscendingNodeJ2000(JD: float):
		_func = _aaplus.CAAElementsPlanetaryOrbit_MercuryLongitudeAscendingNodeJ2000
		_func.argtypes = [c_double]
		_func.restype = c_double
		return _func(JD)

	@staticmethod
	def MercuryLongitudePerihelionJ2000(JD: float):
		_func = _aaplus.CAAElementsPlanetaryOrbit_MercuryLongitudePerihelionJ2000
		_func.argtypes = [c_double]
		_func.restype = c_double
		return _func(JD)

	@staticmethod
	def VenusMeanLongitudeJ2000(JD: float):
		_func = _aaplus.CAAElementsPlanetaryOrbit_VenusMeanLongitudeJ2000
		_func.argtypes = [c_double]
		_func.restype = c_double
		return _func(JD)

	@staticmethod
	def VenusInclinationJ2000(JD: float):
		_func = _aaplus.CAAElementsPlanetaryOrbit_VenusInclinationJ2000
		_func.argtypes = [c_double]
		_func.restype = c_double
		return _func(JD)

	@staticmethod
	def VenusLongitudeAscendingNodeJ2000(JD: float):
		_func = _aaplus.CAAElementsPlanetaryOrbit_VenusLongitudeAscendingNodeJ2000
		_func.argtypes = [c_double]
		_func.restype = c_double
		return _func(JD)

	@staticmethod
	def VenusLongitudePerihelionJ2000(JD: float):
		_func = _aaplus.CAAElementsPlanetaryOrbit_VenusLongitudePerihelionJ2000
		_func.argtypes = [c_double]
		_func.restype = c_double
		return _func(JD)

	@staticmethod
	def EarthMeanLongitudeJ2000(JD: float):
		_func = _aaplus.CAAElementsPlanetaryOrbit_EarthMeanLongitudeJ2000
		_func.argtypes = [c_double]
		_func.restype = c_double
		return _func(JD)

	@staticmethod
	def EarthInclinationJ2000(JD: float):
		_func = _aaplus.CAAElementsPlanetaryOrbit_EarthInclinationJ2000
		_func.argtypes = [c_double]
		_func.restype = c_double
		return _func(JD)

	@staticmethod
	def EarthLongitudeAscendingNodeJ2000(JD: float):
		_func = _aaplus.CAAElementsPlanetaryOrbit_EarthLongitudeAscendingNodeJ2000
		_func.argtypes = [c_double]
		_func.restype = c_double
		return _func(JD)

	@staticmethod
	def EarthLongitudePerihelionJ2000(JD: float):
		_func = _aaplus.CAAElementsPlanetaryOrbit_EarthLongitudePerihelionJ2000
		_func.argtypes = [c_double]
		_func.restype = c_double
		return _func(JD)

	@staticmethod
	def MarsMeanLongitudeJ2000(JD: float):
		_func = _aaplus.CAAElementsPlanetaryOrbit_MarsMeanLongitudeJ2000
		_func.argtypes = [c_double]
		_func.restype = c_double
		return _func(JD)

	@staticmethod
	def MarsInclinationJ2000(JD: float):
		_func = _aaplus.CAAElementsPlanetaryOrbit_MarsInclinationJ2000
		_func.argtypes = [c_double]
		_func.restype = c_double
		return _func(JD)

	@staticmethod
	def MarsLongitudeAscendingNodeJ2000(JD: float):
		_func = _aaplus.CAAElementsPlanetaryOrbit_MarsLongitudeAscendingNodeJ2000
		_func.argtypes = [c_double]
		_func.restype = c_double
		return _func(JD)

	@staticmethod
	def MarsLongitudePerihelionJ2000(JD: float):
		_func = _aaplus.CAAElementsPlanetaryOrbit_MarsLongitudePerihelionJ2000
		_func.argtypes = [c_double]
		_func.restype = c_double
		return _func(JD)

	@staticmethod
	def JupiterMeanLongitudeJ2000(JD: float):
		_func = _aaplus.CAAElementsPlanetaryOrbit_JupiterMeanLongitudeJ2000
		_func.argtypes = [c_double]
		_func.restype = c_double
		return _func(JD)

	@staticmethod
	def JupiterInclinationJ2000(JD: float):
		_func = _aaplus.CAAElementsPlanetaryOrbit_JupiterInclinationJ2000
		_func.argtypes = [c_double]
		_func.restype = c_double
		return _func(JD)

	@staticmethod
	def JupiterLongitudeAscendingNodeJ2000(JD: float):
		_func = _aaplus.CAAElementsPlanetaryOrbit_JupiterLongitudeAscendingNodeJ2000
		_func.argtypes = [c_double]
		_func.restype = c_double
		return _func(JD)

	@staticmethod
	def JupiterLongitudePerihelionJ2000(JD: float):
		_func = _aaplus.CAAElementsPlanetaryOrbit_JupiterLongitudePerihelionJ2000
		_func.argtypes = [c_double]
		_func.restype = c_double
		return _func(JD)

	@staticmethod
	def SaturnMeanLongitudeJ2000(JD: float):
		_func = _aaplus.CAAElementsPlanetaryOrbit_SaturnMeanLongitudeJ2000
		_func.argtypes = [c_double]
		_func.restype = c_double
		return _func(JD)

	@staticmethod
	def SaturnInclinationJ2000(JD: float):
		_func = _aaplus.CAAElementsPlanetaryOrbit_SaturnInclinationJ2000
		_func.argtypes = [c_double]
		_func.restype = c_double
		return _func(JD)

	@staticmethod
	def SaturnLongitudeAscendingNodeJ2000(JD: float):
		_func = _aaplus.CAAElementsPlanetaryOrbit_SaturnLongitudeAscendingNodeJ2000
		_func.argtypes = [c_double]
		_func.restype = c_double
		return _func(JD)

	@staticmethod
	def SaturnLongitudePerihelionJ2000(JD: float):
		_func = _aaplus.CAAElementsPlanetaryOrbit_SaturnLongitudePerihelionJ2000
		_func.argtypes = [c_double]
		_func.restype = c_double
		return _func(JD)

	@staticmethod
	def UranusMeanLongitudeJ2000(JD: float):
		_func = _aaplus.CAAElementsPlanetaryOrbit_UranusMeanLongitudeJ2000
		_func.argtypes = [c_double]
		_func.restype = c_double
		return _func(JD)

	@staticmethod
	def UranusInclinationJ2000(JD: float):
		_func = _aaplus.CAAElementsPlanetaryOrbit_UranusInclinationJ2000
		_func.argtypes = [c_double]
		_func.restype = c_double
		return _func(JD)

	@staticmethod
	def UranusLongitudeAscendingNodeJ2000(JD: float):
		_func = _aaplus.CAAElementsPlanetaryOrbit_UranusLongitudeAscendingNodeJ2000
		_func.argtypes = [c_double]
		_func.restype = c_double
		return _func(JD)

	@staticmethod
	def UranusLongitudePerihelionJ2000(JD: float):
		_func = _aaplus.CAAElementsPlanetaryOrbit_UranusLongitudePerihelionJ2000
		_func.argtypes = [c_double]
		_func.restype = c_double
		return _func(JD)

	@staticmethod
	def NeptuneMeanLongitudeJ2000(JD: float):
		_func = _aaplus.CAAElementsPlanetaryOrbit_NeptuneMeanLongitudeJ2000
		_func.argtypes = [c_double]
		_func.restype = c_double
		return _func(JD)

	@staticmethod
	def NeptuneInclinationJ2000(JD: float):
		_func = _aaplus.CAAElementsPlanetaryOrbit_NeptuneInclinationJ2000
		_func.argtypes = [c_double]
		_func.restype = c_double
		return _func(JD)

	@staticmethod
	def NeptuneLongitudeAscendingNodeJ2000(JD: float):
		_func = _aaplus.CAAElementsPlanetaryOrbit_NeptuneLongitudeAscendingNodeJ2000
		_func.argtypes = [c_double]
		_func.restype = c_double
		return _func(JD)

	@staticmethod
	def NeptuneLongitudePerihelionJ2000(JD: float):
		_func = _aaplus.CAAElementsPlanetaryOrbit_NeptuneLongitudePerihelionJ2000
		_func.argtypes = [c_double]
		_func.restype = c_double
		return _func(JD)


class AAElliptical:
	class Object(IntEnum):
		SUN = 0
		MERCURY = 1
		VENUS = 2
		MARS = 3
		JUPITER = 4
		SATURN = 5
		URANUS = 6
		NEPTUNE = 7

	class AAEllipticalObjectElements(Structure):
		_fields_ = [
			('a', c_double),
			('e', c_double),
			('i', c_double),
			('w', c_double),
			('omega', c_double),
			('JDEquinox', c_double),
			('T', c_double),
		]

	class AAEllipticalPlanetaryDetails(Structure):
		_fields_ = [
			('ApparentGeocentricEclipticalLongitude', c_double),
			('ApparentGeocentricEclipticalLatitude', c_double),
			('ApparentGeocentricDistance', c_double),
			('ApparentLightTime', c_double),
			('ApparentGeocentricRA', c_double),
			('ApparentGeocentricDeclination', c_double),
			('TrueGeocentricRectangularEcliptical', AA3DCoordinate),
			('TrueHeliocentricEclipticalLongitude', c_double),
			('TrueHeliocentricEclipticalLatitude', c_double),
			('TrueHeliocentricDistance', c_double),
			('TrueGeocentricEclipticalLongitude', c_double),
			('TrueGeocentricEclipticalLatitude', c_double),
			('TrueGeocentricDistance', c_double),
			('TrueLightTime', c_double),
			('TrueGeocentricRA', c_double),
			('TrueGeocentricDeclination', c_double),
		]

	class AAEllipticalObjectDetails(Structure):
		_fields_ = [
			('HeliocentricRectangularEquatorial', AA3DCoordinate),
			('HeliocentricRectangularEcliptical', AA3DCoordinate),
			('HeliocentricEclipticLongitude', c_double),
			('HeliocentricEclipticLatitude', c_double),
			('TrueGeocentricRA', c_double),
			('TrueGeocentricDeclination', c_double),
			('TrueGeocentricDistance', c_double),
			('TrueGeocentricLightTime', c_double),
			('AstrometricGeocentricRA', c_double),
			('AstrometricGeocentricDeclination', c_double),
			('AstrometricGeocentricDistance', c_double),
			('AstrometricGeocentricLightTime', c_double),
			('Elongation', c_double),
			('PhaseAngle', c_double),
		]

	@staticmethod
	def DistanceToLightTime(Distance: float):
		_func = _aaplus.CAAElliptical_DistanceToLightTime
		_func.argtypes = [c_double]
		_func.restype = c_double
		return _func(Distance)

	@staticmethod
	def Calculate(JD: float, object: Object, bHighPrecision: bool = True):
		_func = _aaplus.CAAElliptical_Calculate
		_func.argtypes = [c_double, c_int, c_byte]
		_func.restype = AAElliptical.AAEllipticalPlanetaryDetails
		return _func(JD, object.value, bHighPrecision)

	@staticmethod
	def SemiMajorAxisFromPerihelionDistance(q: float, e: float):
		_func = _aaplus.CAAElliptical_SemiMajorAxisFromPerihelionDistance
		_func.argtypes = [c_double, c_double]
		_func.restype = c_double
		return _func(q, e)

	@staticmethod
	def MeanMotionFromSemiMajorAxis(a: float):
		_func = _aaplus.CAAElliptical_MeanMotionFromSemiMajorAxis
		_func.argtypes = [c_double]
		_func.restype = c_double
		return _func(a)

	@staticmethod
	def Calculate_2(JD: float, elements: AAEllipticalObjectElements, bHighPrecision: bool = True):
		_func = _aaplus.CAAElliptical_Calculate_2
		_func.argtypes = [c_double, POINTER(AAElliptical.AAEllipticalObjectElements), c_byte]
		_func.restype = AAElliptical.AAEllipticalObjectDetails
		return _func(JD, byref(elements), bHighPrecision)

	@staticmethod
	def InstantaneousVelocity(r: float, a: float):
		_func = _aaplus.CAAElliptical_InstantaneousVelocity
		_func.argtypes = [c_double, c_double]
		_func.restype = c_double
		return _func(r, a)

	@staticmethod
	def VelocityAtPerihelion(e: float, a: float):
		_func = _aaplus.CAAElliptical_VelocityAtPerihelion
		_func.argtypes = [c_double, c_double]
		_func.restype = c_double
		return _func(e, a)

	@staticmethod
	def VelocityAtAphelion(e: float, a: float):
		_func = _aaplus.CAAElliptical_VelocityAtAphelion
		_func.argtypes = [c_double, c_double]
		_func.restype = c_double
		return _func(e, a)

	@staticmethod
	def LengthOfEllipse(e: float, a: float):
		_func = _aaplus.CAAElliptical_LengthOfEllipse
		_func.argtypes = [c_double, c_double]
		_func.restype = c_double
		return _func(e, a)

	@staticmethod
	def CometMagnitude(g: float, delta: float, k: float, r: float):
		_func = _aaplus.CAAElliptical_CometMagnitude
		_func.argtypes = [c_double, c_double, c_double, c_double]
		_func.restype = c_double
		return _func(g, delta, k, r)

	@staticmethod
	def MinorPlanetMagnitude(H: float, delta: float, G: float, r: float, PhaseAngle: float):
		_func = _aaplus.CAAElliptical_MinorPlanetMagnitude
		_func.argtypes = [c_double, c_double, c_double, c_double, c_double]
		_func.restype = c_double
		return _func(H, delta, G, r, PhaseAngle)


class AAELP2000:
	class ELP2000MainProblemCoefficient(Structure):
		_fields_ = [
			('m_I', c_int * 4),
			('m_A', c_double),
			('m_B', c_double * 6),
		]

	class ELP2000EarthTidalMoonRelativisticSolarEccentricityCoefficient(Structure):
		_fields_ = [
			('m_IZ', c_int),
			('m_I', c_int * 4),
			('m_O', c_double),
			('m_A', c_double),
			('m_P', c_double),
		]

	class ELP2000PlanetPertCoefficient(Structure):
		_fields_ = [
			('m_ip', c_int * 11),
			('m_theta', c_double),
			('m_O', c_double),
			('m_P', c_double),
		]

	@staticmethod
	def EclipticLongitude(JD: float):
		_func = _aaplus.CAAELP2000_EclipticLongitude
		_func.argtypes = [c_double]
		_func.restype = c_double
		return _func(JD)

	@staticmethod
	def EclipticLongitude_2(pT: list, nTSize: int):
		_func = _aaplus.CAAELP2000_EclipticLongitude_2
		_func.argtypes = [c_double * nTSize, c_int]
		_func.restype = c_double
		return _func(pT, nTSize)

	@staticmethod
	def EclipticLatitude(JD: float):
		_func = _aaplus.CAAELP2000_EclipticLatitude
		_func.argtypes = [c_double]
		_func.restype = c_double
		return _func(JD)

	@staticmethod
	def EclipticLatitude_2(pT: list, nTSize: int):
		_func = _aaplus.CAAELP2000_EclipticLatitude_2
		_func.argtypes = [c_double * nTSize, c_int]
		_func.restype = c_double
		return _func(pT, nTSize)

	@staticmethod
	def RadiusVector(JD: float):
		_func = _aaplus.CAAELP2000_RadiusVector
		_func.argtypes = [c_double]
		_func.restype = c_double
		return _func(JD)

	@staticmethod
	def RadiusVector_2(pT: list, nTSize: int):
		_func = _aaplus.CAAELP2000_RadiusVector_2
		_func.argtypes = [c_double * nTSize, c_int]
		_func.restype = c_double
		return _func(pT, nTSize)

	@staticmethod
	def EclipticRectangularCoordinates(JD: float):
		_func = _aaplus.CAAELP2000_EclipticRectangularCoordinates
		_func.argtypes = [c_double]
		_func.restype = AA3DCoordinate
		return _func(JD)

	@staticmethod
	def EclipticRectangularCoordinatesJ2000(JD: float):
		_func = _aaplus.CAAELP2000_EclipticRectangularCoordinatesJ2000
		_func.argtypes = [c_double]
		_func.restype = AA3DCoordinate
		return _func(JD)

	@staticmethod
	def EquatorialRectangularCoordinatesFK5(JD: float):
		_func = _aaplus.CAAELP2000_EquatorialRectangularCoordinatesFK5
		_func.argtypes = [c_double]
		_func.restype = AA3DCoordinate
		return _func(JD)

	@staticmethod
	def MoonMeanMeanLongitude(pT: list, nTSize: int):
		_func = _aaplus.CAAELP2000_MoonMeanMeanLongitude
		_func.argtypes = [c_double * nTSize, c_int]
		_func.restype = c_double
		return _func(pT, nTSize)

	@staticmethod
	def MoonMeanMeanLongitude_2(JD: float):
		_func = _aaplus.CAAELP2000_MoonMeanMeanLongitude_2
		_func.argtypes = [c_double]
		_func.restype = c_double
		return _func(JD)

	@staticmethod
	def MeanLongitudeLunarPerigee(pT: list, nTSize: int):
		_func = _aaplus.CAAELP2000_MeanLongitudeLunarPerigee
		_func.argtypes = [c_double * nTSize, c_int]
		_func.restype = c_double
		return _func(pT, nTSize)

	@staticmethod
	def MeanLongitudeLunarPerigee_2(JD: float):
		_func = _aaplus.CAAELP2000_MeanLongitudeLunarPerigee_2
		_func.argtypes = [c_double]
		_func.restype = c_double
		return _func(JD)

	@staticmethod
	def MeanLongitudeLunarAscendingNode(pT: list, nTSize: int):
		_func = _aaplus.CAAELP2000_MeanLongitudeLunarAscendingNode
		_func.argtypes = [c_double * nTSize, c_int]
		_func.restype = c_double
		return _func(pT, nTSize)

	@staticmethod
	def MeanLongitudeLunarAscendingNode_2(JD: float):
		_func = _aaplus.CAAELP2000_MeanLongitudeLunarAscendingNode_2
		_func.argtypes = [c_double]
		_func.restype = c_double
		return _func(JD)

	@staticmethod
	def MeanHeliocentricMeanLongitudeEarthMoonBarycentre(pT: list, nTSize: int):
		_func = _aaplus.CAAELP2000_MeanHeliocentricMeanLongitudeEarthMoonBarycentre
		_func.argtypes = [c_double * nTSize, c_int]
		_func.restype = c_double
		return _func(pT, nTSize)

	@staticmethod
	def MeanHeliocentricMeanLongitudeEarthMoonBarycentre_2(JD: float):
		_func = _aaplus.CAAELP2000_MeanHeliocentricMeanLongitudeEarthMoonBarycentre_2
		_func.argtypes = [c_double]
		_func.restype = c_double
		return _func(JD)

	@staticmethod
	def MeanLongitudeOfPerihelionOfEarthMoonBarycentre(pT: list, nTSize: int):
		_func = _aaplus.CAAELP2000_MeanLongitudeOfPerihelionOfEarthMoonBarycentre
		_func.argtypes = [c_double * nTSize, c_int]
		_func.restype = c_double
		return _func(pT, nTSize)

	@staticmethod
	def MeanLongitudeOfPerihelionOfEarthMoonBarycentre_2(JD: float):
		_func = _aaplus.CAAELP2000_MeanLongitudeOfPerihelionOfEarthMoonBarycentre_2
		_func.argtypes = [c_double]
		_func.restype = c_double
		return _func(JD)

	@staticmethod
	def MoonMeanSolarElongation(pT: list, nTSize: int):
		_func = _aaplus.CAAELP2000_MoonMeanSolarElongation
		_func.argtypes = [c_double * nTSize, c_int]
		_func.restype = c_double
		return _func(pT, nTSize)

	@staticmethod
	def MoonMeanSolarElongation_2(JD: float):
		_func = _aaplus.CAAELP2000_MoonMeanSolarElongation_2
		_func.argtypes = [c_double]
		_func.restype = c_double
		return _func(JD)

	@staticmethod
	def SunMeanAnomaly(pT: list, nTSize: int):
		_func = _aaplus.CAAELP2000_SunMeanAnomaly
		_func.argtypes = [c_double * nTSize, c_int]
		_func.restype = c_double
		return _func(pT, nTSize)

	@staticmethod
	def SunMeanAnomaly_2(JD: float):
		_func = _aaplus.CAAELP2000_SunMeanAnomaly_2
		_func.argtypes = [c_double]
		_func.restype = c_double
		return _func(JD)

	@staticmethod
	def MoonMeanAnomaly(pT: list, nTSize: int):
		_func = _aaplus.CAAELP2000_MoonMeanAnomaly
		_func.argtypes = [c_double * nTSize, c_int]
		_func.restype = c_double
		return _func(pT, nTSize)

	@staticmethod
	def MoonMeanAnomaly_2(JD: float):
		_func = _aaplus.CAAELP2000_MoonMeanAnomaly_2
		_func.argtypes = [c_double]
		_func.restype = c_double
		return _func(JD)

	@staticmethod
	def MoonMeanArgumentOfLatitude(pT: list, nTSize: int):
		_func = _aaplus.CAAELP2000_MoonMeanArgumentOfLatitude
		_func.argtypes = [c_double * nTSize, c_int]
		_func.restype = c_double
		return _func(pT, nTSize)

	@staticmethod
	def MoonMeanArgumentOfLatitude_2(JD: float):
		_func = _aaplus.CAAELP2000_MoonMeanArgumentOfLatitude_2
		_func.argtypes = [c_double]
		_func.restype = c_double
		return _func(JD)

	@staticmethod
	def MercuryMeanLongitude(T: float):
		_func = _aaplus.CAAELP2000_MercuryMeanLongitude
		_func.argtypes = [c_double]
		_func.restype = c_double
		return _func(T)

	@staticmethod
	def VenusMeanLongitude(T: float):
		_func = _aaplus.CAAELP2000_VenusMeanLongitude
		_func.argtypes = [c_double]
		_func.restype = c_double
		return _func(T)

	@staticmethod
	def MarsMeanLongitude(T: float):
		_func = _aaplus.CAAELP2000_MarsMeanLongitude
		_func.argtypes = [c_double]
		_func.restype = c_double
		return _func(T)

	@staticmethod
	def JupiterMeanLongitude(T: float):
		_func = _aaplus.CAAELP2000_JupiterMeanLongitude
		_func.argtypes = [c_double]
		_func.restype = c_double
		return _func(T)

	@staticmethod
	def SaturnMeanLongitude(T: float):
		_func = _aaplus.CAAELP2000_SaturnMeanLongitude
		_func.argtypes = [c_double]
		_func.restype = c_double
		return _func(T)

	@staticmethod
	def UranusMeanLongitude(T: float):
		_func = _aaplus.CAAELP2000_UranusMeanLongitude
		_func.argtypes = [c_double]
		_func.restype = c_double
		return _func(T)

	@staticmethod
	def NeptuneMeanLongitude(T: float):
		_func = _aaplus.CAAELP2000_NeptuneMeanLongitude
		_func.argtypes = [c_double]
		_func.restype = c_double
		return _func(T)


class AAELPMPP02:
	class Correction(IntEnum):
		Nominal = 0
		LLR = 1
		DE405 = 2
		DE406 = 3

	@staticmethod
	def EclipticLongitude(JD: float, correction: Correction):
		_func = _aaplus.CAAELPMPP02_EclipticLongitude
		_func.argtypes = [c_double, c_int, POINTER(c_double)]
		_func.restype = c_double
		_pDerivative = c_double()
		return _func(JD, correction.value, byref(_pDerivative))

	@staticmethod
	def EclipticLongitude_2(pT: list, nTSize: int, correction: Correction):
		_func = _aaplus.CAAELPMPP02_EclipticLongitude_2
		_func.argtypes = [c_double * nTSize, c_int, c_int, POINTER(c_double)]
		_func.restype = c_double
		_pDerivative = c_double()
		return _func(pT, nTSize, correction.value, byref(_pDerivative))

	@staticmethod
	def EclipticLatitude(JD: float, correction: Correction):
		_func = _aaplus.CAAELPMPP02_EclipticLatitude
		_func.argtypes = [c_double, c_int, POINTER(c_double)]
		_func.restype = c_double
		_pDerivative = c_double()
		return _func(JD, correction.value, byref(_pDerivative))

	@staticmethod
	def EclipticLatitude_2(pT: list, nTSize: int, correction: Correction):
		_func = _aaplus.CAAELPMPP02_EclipticLatitude_2
		_func.argtypes = [c_double * nTSize, c_int, c_int, POINTER(c_double)]
		_func.restype = c_double
		_pDerivative = c_double()
		return _func(pT, nTSize, correction.value, byref(_pDerivative))

	@staticmethod
	def RadiusVector(JD: float, correction: Correction):
		_func = _aaplus.CAAELPMPP02_RadiusVector
		_func.argtypes = [c_double, c_int, POINTER(c_double)]
		_func.restype = c_double
		_pDerivative = c_double()
		return _func(JD, correction.value, byref(_pDerivative))

	@staticmethod
	def RadiusVector_2(pT: list, nTSize: int, correction: Correction):
		_func = _aaplus.CAAELPMPP02_RadiusVector_2
		_func.argtypes = [c_double * nTSize, c_int, c_int, POINTER(c_double)]
		_func.restype = c_double
		_pDerivative = c_double()
		return _func(pT, nTSize, correction.value, byref(_pDerivative))

	@staticmethod
	def EclipticRectangularCoordinates(JD: float, correction: Correction):
		_func = _aaplus.CAAELPMPP02_EclipticRectangularCoordinates
		_func.argtypes = [c_double, c_int, POINTER(AA3DCoordinate)]
		_func.restype = AA3DCoordinate
		_pDerivative = AA3DCoordinate()
		return _func(JD, correction.value, byref(_pDerivative))

	@staticmethod
	def EclipticRectangularCoordinates_2(pT: list, nTSize: int, correction: Correction):
		_func = _aaplus.CAAELPMPP02_EclipticRectangularCoordinates_2
		_func.argtypes = [c_double * nTSize, c_int, c_int, POINTER(AA3DCoordinate)]
		_func.restype = AA3DCoordinate
		_pDerivative = AA3DCoordinate()
		return _func(pT, nTSize, correction.value, byref(_pDerivative))

	@staticmethod
	def EclipticRectangularCoordinatesJ2000(JD: float, correction: Correction):
		_func = _aaplus.CAAELPMPP02_EclipticRectangularCoordinatesJ2000
		_func.argtypes = [c_double, c_int, POINTER(AA3DCoordinate)]
		_func.restype = AA3DCoordinate
		_pDerivative = AA3DCoordinate()
		return _func(JD, correction.value, byref(_pDerivative))

	@staticmethod
	def EclipticRectangularCoordinatesJ2000_2(pT: list, nTSize: int, correction: Correction):
		_func = _aaplus.CAAELPMPP02_EclipticRectangularCoordinatesJ2000_2
		_func.argtypes = [c_double * nTSize, c_int, c_int, POINTER(AA3DCoordinate)]
		_func.restype = AA3DCoordinate
		_pDerivative = AA3DCoordinate()
		return _func(pT, nTSize, correction.value, byref(_pDerivative))


class AAEquationOfTime:
	@staticmethod
	def Calculate(JD: float, bHighPrecision: bool = True):
		_func = _aaplus.CAAEquationOfTime_Calculate
		_func.argtypes = [c_double, c_byte]
		_func.restype = c_double
		return _func(JD, bHighPrecision)


class AAEquinoxesAndSolstices:
	@staticmethod
	def NorthwardEquinox(Year: int, bHighPrecision: bool):
		_func = _aaplus.CAAEquinoxesAndSolstices_NorthwardEquinox
		_func.argtypes = [c_long, c_byte]
		_func.restype = c_double
		return _func(Year, bHighPrecision)

	@staticmethod
	def NorthernSolstice(Year: int, bHighPrecision: bool):
		_func = _aaplus.CAAEquinoxesAndSolstices_NorthernSolstice
		_func.argtypes = [c_long, c_byte]
		_func.restype = c_double
		return _func(Year, bHighPrecision)

	@staticmethod
	def SouthwardEquinox(Year: int, bHighPrecision: bool):
		_func = _aaplus.CAAEquinoxesAndSolstices_SouthwardEquinox
		_func.argtypes = [c_long, c_byte]
		_func.restype = c_double
		return _func(Year, bHighPrecision)

	@staticmethod
	def SouthernSolstice(Year: int, bHighPrecision: bool):
		_func = _aaplus.CAAEquinoxesAndSolstices_SouthernSolstice
		_func.argtypes = [c_long, c_byte]
		_func.restype = c_double
		return _func(Year, bHighPrecision)

	@staticmethod
	def LengthOfSpring(Year: int, bNorthernHemisphere: bool, bHighPrecision: bool):
		_func = _aaplus.CAAEquinoxesAndSolstices_LengthOfSpring
		_func.argtypes = [c_long, c_byte, c_byte]
		_func.restype = c_double
		return _func(Year, bNorthernHemisphere, bHighPrecision)

	@staticmethod
	def LengthOfSummer(Year: int, bNorthernHemisphere: bool, bHighPrecision: bool):
		_func = _aaplus.CAAEquinoxesAndSolstices_LengthOfSummer
		_func.argtypes = [c_long, c_byte, c_byte]
		_func.restype = c_double
		return _func(Year, bNorthernHemisphere, bHighPrecision)

	@staticmethod
	def LengthOfAutumn(Year: int, bNorthernHemisphere: bool, bHighPrecision: bool):
		_func = _aaplus.CAAEquinoxesAndSolstices_LengthOfAutumn
		_func.argtypes = [c_long, c_byte, c_byte]
		_func.restype = c_double
		return _func(Year, bNorthernHemisphere, bHighPrecision)

	@staticmethod
	def LengthOfWinter(Year: int, bNorthernHemisphere: bool, bHighPrecision: bool):
		_func = _aaplus.CAAEquinoxesAndSolstices_LengthOfWinter
		_func.argtypes = [c_long, c_byte, c_byte]
		_func.restype = c_double
		return _func(Year, bNorthernHemisphere, bHighPrecision)


class AAEquinoxesAndSolstices2:
	class Type(IntEnum):
		NotDefined = 0
		NorthwardEquinox = 1
		NorthernSolstice = 2
		SouthwardEquinox = 3
		SouthernSolstice = 4

	class AAEquinoxSolsticeDetails2(Structure):
		_fields_ = [
			('type', c_int),
			('JD', c_double),
		]

	@staticmethod
	def Calculate(StartJD: float, EndJD: float, StepInterval: float = 0.007, bHighPrecision: bool = True):
		_func = _aaplus.CAAEquinoxesAndSolstices2_Calculate
		_func.argtypes = [c_double, c_double, c_double, c_byte, POINTER(c_int)]
		_func.restype = POINTER(AAEquinoxesAndSolstices2.AAEquinoxSolsticeDetails2)
		_num = c_int()
		_ptr = _func(StartJD, EndJD, StepInterval, bHighPrecision, byref(_num))
		_res = []
		for x in range(0, _num.value):
			_res.append(_ptr[x])
		return _res


class AAFK5:
	@staticmethod
	def CorrectionInLongitude(Longitude: float, Latitude: float, JD: float):
		_func = _aaplus.CAAFK5_CorrectionInLongitude
		_func.argtypes = [c_double, c_double, c_double]
		_func.restype = c_double
		return _func(Longitude, Latitude, JD)

	@staticmethod
	def CorrectionInLatitude(Longitude: float, JD: float):
		_func = _aaplus.CAAFK5_CorrectionInLatitude
		_func.argtypes = [c_double, c_double]
		_func.restype = c_double
		return _func(Longitude, JD)

	@staticmethod
	def ConvertVSOPToFK5J2000(value: AA3DCoordinate):
		_func = _aaplus.CAAFK5_ConvertVSOPToFK5J2000
		_func.argtypes = [POINTER(AA3DCoordinate)]
		_func.restype = AA3DCoordinate
		return _func(byref(value))

	@staticmethod
	def ConvertVSOPToFK5B1950(value: AA3DCoordinate):
		_func = _aaplus.CAAFK5_ConvertVSOPToFK5B1950
		_func.argtypes = [POINTER(AA3DCoordinate)]
		_func.restype = AA3DCoordinate
		return _func(byref(value))

	@staticmethod
	def ConvertVSOPToFK5AnyEquinox(value: AA3DCoordinate, JDEquinox: float):
		_func = _aaplus.CAAFK5_ConvertVSOPToFK5AnyEquinox
		_func.argtypes = [POINTER(AA3DCoordinate), c_double]
		_func.restype = AA3DCoordinate
		return _func(byref(value), JDEquinox)


class AAGalileanMoonDetail(Structure):
	_fields_ = [
		('MeanLongitude', c_double),
		('TrueLongitude', c_double),
		('TropicalLongitude', c_double),
		('EquatorialLatitude', c_double),
		('r', c_double),
		('TrueRectangularCoordinates', AA3DCoordinate),
		('ApparentRectangularCoordinates', AA3DCoordinate),
		('bInTransit', c_byte),
		('bInOccultation', c_byte),
		('bInEclipse', c_byte),
		('bInShadowTransit', c_byte),
	]

class AAGalileanMoons:
	class AAGalileanMoonsDetails(Structure):
		_fields_ = [
			('Satellite1', AAGalileanMoonDetail),
			('Satellite2', AAGalileanMoonDetail),
			('Satellite3', AAGalileanMoonDetail),
			('Satellite4', AAGalileanMoonDetail),
		]

	@staticmethod
	def Calculate(JD: float, bHighPrecision: bool = True):
		_func = _aaplus.CAAGalileanMoons_Calculate
		_func.argtypes = [c_double, c_byte]
		_func.restype = AAGalileanMoons.AAGalileanMoonsDetails
		return _func(JD, bHighPrecision)


class AAGlobe:
	@staticmethod
	def RhoSinThetaPrime(GeographicalLatitude: float, Height: float):
		_func = _aaplus.CAAGlobe_RhoSinThetaPrime
		_func.argtypes = [c_double, c_double]
		_func.restype = c_double
		return _func(GeographicalLatitude, Height)

	@staticmethod
	def RhoCosThetaPrime(GeographicalLatitude: float, Height: float):
		_func = _aaplus.CAAGlobe_RhoCosThetaPrime
		_func.argtypes = [c_double, c_double]
		_func.restype = c_double
		return _func(GeographicalLatitude, Height)

	@staticmethod
	def RadiusOfParallelOfLatitude(GeographicalLatitude: float):
		_func = _aaplus.CAAGlobe_RadiusOfParallelOfLatitude
		_func.argtypes = [c_double]
		_func.restype = c_double
		return _func(GeographicalLatitude)

	@staticmethod
	def RadiusOfCurvature(GeographicalLatitude: float):
		_func = _aaplus.CAAGlobe_RadiusOfCurvature
		_func.argtypes = [c_double]
		_func.restype = c_double
		return _func(GeographicalLatitude)

	@staticmethod
	def DistanceBetweenPoints(GeographicalLatitude1: float, GeographicalLongitude1: float, GeographicalLatitude2: float, GeographicalLongitude2: float):
		_func = _aaplus.CAAGlobe_DistanceBetweenPoints
		_func.argtypes = [c_double, c_double, c_double, c_double]
		_func.restype = c_double
		return _func(GeographicalLatitude1, GeographicalLongitude1, GeographicalLatitude2, GeographicalLongitude2)


class AAIlluminatedFraction:
	@staticmethod
	def PhaseAngle(r: float, R: float, Delta: float):
		_func = _aaplus.CAAIlluminatedFraction_PhaseAngle
		_func.argtypes = [c_double, c_double, c_double]
		_func.restype = c_double
		return _func(r, R, Delta)

	@staticmethod
	def PhaseAngle_2(R: float, R0: float, B: float, L: float, L0: float, Delta: float):
		_func = _aaplus.CAAIlluminatedFraction_PhaseAngle_2
		_func.argtypes = [c_double, c_double, c_double, c_double, c_double, c_double]
		_func.restype = c_double
		return _func(R, R0, B, L, L0, Delta)

	@staticmethod
	def PhaseAngleRectangular(x: float, y: float, z: float, B: float, L: float, Delta: float):
		_func = _aaplus.CAAIlluminatedFraction_PhaseAngleRectangular
		_func.argtypes = [c_double, c_double, c_double, c_double, c_double, c_double]
		_func.restype = c_double
		return _func(x, y, z, B, L, Delta)

	@staticmethod
	def IlluminatedFraction(PhaseAngle: float):
		_func = _aaplus.CAAIlluminatedFraction_IlluminatedFraction
		_func.argtypes = [c_double]
		_func.restype = c_double
		return _func(PhaseAngle)

	@staticmethod
	def IlluminatedFraction_2(r: float, R: float, Delta: float):
		_func = _aaplus.CAAIlluminatedFraction_IlluminatedFraction_2
		_func.argtypes = [c_double, c_double, c_double]
		_func.restype = c_double
		return _func(r, R, Delta)

	@staticmethod
	def MercuryMagnitudeMuller(r: float, Delta: float, i: float):
		_func = _aaplus.CAAIlluminatedFraction_MercuryMagnitudeMuller
		_func.argtypes = [c_double, c_double, c_double]
		_func.restype = c_double
		return _func(r, Delta, i)

	@staticmethod
	def VenusMagnitudeMuller(r: float, Delta: float, i: float):
		_func = _aaplus.CAAIlluminatedFraction_VenusMagnitudeMuller
		_func.argtypes = [c_double, c_double, c_double]
		_func.restype = c_double
		return _func(r, Delta, i)

	@staticmethod
	def MarsMagnitudeMuller(r: float, Delta: float, i: float):
		_func = _aaplus.CAAIlluminatedFraction_MarsMagnitudeMuller
		_func.argtypes = [c_double, c_double, c_double]
		_func.restype = c_double
		return _func(r, Delta, i)

	@staticmethod
	def JupiterMagnitudeMuller(r: float, Delta: float):
		_func = _aaplus.CAAIlluminatedFraction_JupiterMagnitudeMuller
		_func.argtypes = [c_double, c_double]
		_func.restype = c_double
		return _func(r, Delta)

	@staticmethod
	def SaturnMagnitudeMuller(r: float, Delta: float, DeltaU: float, B: float):
		_func = _aaplus.CAAIlluminatedFraction_SaturnMagnitudeMuller
		_func.argtypes = [c_double, c_double, c_double, c_double]
		_func.restype = c_double
		return _func(r, Delta, DeltaU, B)

	@staticmethod
	def UranusMagnitudeMuller(r: float, Delta: float):
		_func = _aaplus.CAAIlluminatedFraction_UranusMagnitudeMuller
		_func.argtypes = [c_double, c_double]
		_func.restype = c_double
		return _func(r, Delta)

	@staticmethod
	def NeptuneMagnitudeMuller(r: float, Delta: float):
		_func = _aaplus.CAAIlluminatedFraction_NeptuneMagnitudeMuller
		_func.argtypes = [c_double, c_double]
		_func.restype = c_double
		return _func(r, Delta)

	@staticmethod
	def MercuryMagnitudeAA(r: float, Delta: float, i: float):
		_func = _aaplus.CAAIlluminatedFraction_MercuryMagnitudeAA
		_func.argtypes = [c_double, c_double, c_double]
		_func.restype = c_double
		return _func(r, Delta, i)

	@staticmethod
	def VenusMagnitudeAA(r: float, Delta: float, i: float):
		_func = _aaplus.CAAIlluminatedFraction_VenusMagnitudeAA
		_func.argtypes = [c_double, c_double, c_double]
		_func.restype = c_double
		return _func(r, Delta, i)

	@staticmethod
	def MarsMagnitudeAA(r: float, Delta: float, i: float):
		_func = _aaplus.CAAIlluminatedFraction_MarsMagnitudeAA
		_func.argtypes = [c_double, c_double, c_double]
		_func.restype = c_double
		return _func(r, Delta, i)

	@staticmethod
	def JupiterMagnitudeAA(r: float, Delta: float, i: float):
		_func = _aaplus.CAAIlluminatedFraction_JupiterMagnitudeAA
		_func.argtypes = [c_double, c_double, c_double]
		_func.restype = c_double
		return _func(r, Delta, i)

	@staticmethod
	def SaturnMagnitudeAA(r: float, Delta: float, DeltaU: float, B: float):
		_func = _aaplus.CAAIlluminatedFraction_SaturnMagnitudeAA
		_func.argtypes = [c_double, c_double, c_double, c_double]
		_func.restype = c_double
		return _func(r, Delta, DeltaU, B)

	@staticmethod
	def UranusMagnitudeAA(r: float, Delta: float):
		_func = _aaplus.CAAIlluminatedFraction_UranusMagnitudeAA
		_func.argtypes = [c_double, c_double]
		_func.restype = c_double
		return _func(r, Delta)

	@staticmethod
	def NeptuneMagnitudeAA(r: float, Delta: float):
		_func = _aaplus.CAAIlluminatedFraction_NeptuneMagnitudeAA
		_func.argtypes = [c_double, c_double]
		_func.restype = c_double
		return _func(r, Delta)

	@staticmethod
	def PlutoMagnitudeAA(r: float, Delta: float):
		_func = _aaplus.CAAIlluminatedFraction_PlutoMagnitudeAA
		_func.argtypes = [c_double, c_double]
		_func.restype = c_double
		return _func(r, Delta)


class AAInterpolate:
	@staticmethod
	def Interpolate(n: float, Y1: float, Y2: float, Y3: float):
		_func = _aaplus.CAAInterpolate_Interpolate
		_func.argtypes = [c_double, c_double, c_double, c_double]
		_func.restype = c_double
		return _func(n, Y1, Y2, Y3)

	@staticmethod
	def Interpolate_2(n: float, Y1: float, Y2: float, Y3: float, Y4: float, Y5: float):
		_func = _aaplus.CAAInterpolate_Interpolate_2
		_func.argtypes = [c_double, c_double, c_double, c_double, c_double, c_double]
		_func.restype = c_double
		return _func(n, Y1, Y2, Y3, Y4, Y5)

	@staticmethod
	def InterpolateToHalves(Y1: float, Y2: float, Y3: float, Y4: float):
		_func = _aaplus.CAAInterpolate_InterpolateToHalves
		_func.argtypes = [c_double, c_double, c_double, c_double]
		_func.restype = c_double
		return _func(Y1, Y2, Y3, Y4)

	@staticmethod
	def LagrangeInterpolate(X: float, n: int, pX: list, pY: list):
		_func = _aaplus.CAAInterpolate_LagrangeInterpolate
		_func.argtypes = [c_double, c_int, c_double * n, c_double * n]
		_func.restype = c_double
		return _func(X, n, pX, pY)

	@staticmethod
	def Extremum(Y1: float, Y2: float, Y3: float):
		_func = _aaplus.CAAInterpolate_Extremum
		_func.argtypes = [c_double, c_double, c_double, POINTER(c_double)]
		_func.restype = c_double
		_nm = c_double()
		return _func(Y1, Y2, Y3, byref(_nm))

	@staticmethod
	def Extremum_2(Y1: float, Y2: float, Y3: float, Y4: float, Y5: float, epsilon: float):
		_func = _aaplus.CAAInterpolate_Extremum_2
		_func.argtypes = [c_double, c_double, c_double, c_double, c_double, POINTER(c_double), c_double]
		_func.restype = c_double
		_nm = c_double()
		return _func(Y1, Y2, Y3, Y4, Y5, byref(_nm), epsilon)

	@staticmethod
	def Zero(Y1: float, Y2: float, Y3: float, epsilon: float):
		_func = _aaplus.CAAInterpolate_Zero
		_func.argtypes = [c_double, c_double, c_double, c_double]
		_func.restype = c_double
		return _func(Y1, Y2, Y3, epsilon)

	@staticmethod
	def Zero_2(Y1: float, Y2: float, Y3: float, Y4: float, Y5: float, epsilon: float):
		_func = _aaplus.CAAInterpolate_Zero_2
		_func.argtypes = [c_double, c_double, c_double, c_double, c_double, c_double]
		_func.restype = c_double
		return _func(Y1, Y2, Y3, Y4, Y5, epsilon)

	@staticmethod
	def Zero2(Y1: float, Y2: float, Y3: float, epsilon: float):
		_func = _aaplus.CAAInterpolate_Zero2
		_func.argtypes = [c_double, c_double, c_double, c_double]
		_func.restype = c_double
		return _func(Y1, Y2, Y3, epsilon)

	@staticmethod
	def Zero2_2(Y1: float, Y2: float, Y3: float, Y4: float, Y5: float, epsilon: float):
		_func = _aaplus.CAAInterpolate_Zero2_2
		_func.argtypes = [c_double, c_double, c_double, c_double, c_double, c_double]
		_func.restype = c_double
		return _func(Y1, Y2, Y3, Y4, Y5, epsilon)


class AAJewishCalendar:
	@staticmethod
	def DateOfPesach(Year: int, bGregorianCalendar: bool):
		_func = _aaplus.CAAJewishCalendar_DateOfPesach
		_func.argtypes = [c_long, c_byte]
		_func.restype = AAJewishCalendar.AACalendarDate
		return _func(Year, bGregorianCalendar)

	@staticmethod
	def IsLeap(Year: int):
		_func = _aaplus.CAAJewishCalendar_IsLeap
		_func.argtypes = [c_long]
		_func.restype = c_byte
		return _func(Year)

	@staticmethod
	def DaysInYear(Year: int):
		_func = _aaplus.CAAJewishCalendar_DaysInYear
		_func.argtypes = [c_long]
		_func.restype = c_long
		return _func(Year)


class AAJupiter:
	@staticmethod
	def EclipticLongitude(JD: float, bHighPrecision: bool):
		_func = _aaplus.CAAJupiter_EclipticLongitude
		_func.argtypes = [c_double, c_byte]
		_func.restype = c_double
		return _func(JD, bHighPrecision)

	@staticmethod
	def EclipticLatitude(JD: float, bHighPrecision: bool):
		_func = _aaplus.CAAJupiter_EclipticLatitude
		_func.argtypes = [c_double, c_byte]
		_func.restype = c_double
		return _func(JD, bHighPrecision)

	@staticmethod
	def RadiusVector(JD: float, bHighPrecision: bool):
		_func = _aaplus.CAAJupiter_RadiusVector
		_func.argtypes = [c_double, c_byte]
		_func.restype = c_double
		return _func(JD, bHighPrecision)


class AAKepler:
	@staticmethod
	def Calculate(M: float, e: float, nIterations: int):
		_func = _aaplus.CAAKepler_Calculate
		_func.argtypes = [c_double, c_double, c_int]
		_func.restype = c_double
		return _func(M, e, nIterations)


class AAMars:
	@staticmethod
	def EclipticLongitude(JD: float, bHighPrecision: bool):
		_func = _aaplus.CAAMars_EclipticLongitude
		_func.argtypes = [c_double, c_byte]
		_func.restype = c_double
		return _func(JD, bHighPrecision)

	@staticmethod
	def EclipticLatitude(JD: float, bHighPrecision: bool):
		_func = _aaplus.CAAMars_EclipticLatitude
		_func.argtypes = [c_double, c_byte]
		_func.restype = c_double
		return _func(JD, bHighPrecision)

	@staticmethod
	def RadiusVector(JD: float, bHighPrecision: bool):
		_func = _aaplus.CAAMars_RadiusVector
		_func.argtypes = [c_double, c_byte]
		_func.restype = c_double
		return _func(JD, bHighPrecision)


class AAMercury:
	@staticmethod
	def EclipticLongitude(JD: float, bHighPrecision: bool):
		_func = _aaplus.CAAMercury_EclipticLongitude
		_func.argtypes = [c_double, c_byte]
		_func.restype = c_double
		return _func(JD, bHighPrecision)

	@staticmethod
	def EclipticLatitude(JD: float, bHighPrecision: bool):
		_func = _aaplus.CAAMercury_EclipticLatitude
		_func.argtypes = [c_double, c_byte]
		_func.restype = c_double
		return _func(JD, bHighPrecision)

	@staticmethod
	def RadiusVector(JD: float, bHighPrecision: bool):
		_func = _aaplus.CAAMercury_RadiusVector
		_func.argtypes = [c_double, c_byte]
		_func.restype = c_double
		return _func(JD, bHighPrecision)


class AAMoon:
	@staticmethod
	def MeanLongitude(JD: float):
		_func = _aaplus.CAAMoon_MeanLongitude
		_func.argtypes = [c_double]
		_func.restype = c_double
		return _func(JD)

	@staticmethod
	def MeanElongation(JD: float):
		_func = _aaplus.CAAMoon_MeanElongation
		_func.argtypes = [c_double]
		_func.restype = c_double
		return _func(JD)

	@staticmethod
	def MeanAnomaly(JD: float):
		_func = _aaplus.CAAMoon_MeanAnomaly
		_func.argtypes = [c_double]
		_func.restype = c_double
		return _func(JD)

	@staticmethod
	def ArgumentOfLatitude(JD: float):
		_func = _aaplus.CAAMoon_ArgumentOfLatitude
		_func.argtypes = [c_double]
		_func.restype = c_double
		return _func(JD)

	@staticmethod
	def MeanLongitudeAscendingNode(JD: float):
		_func = _aaplus.CAAMoon_MeanLongitudeAscendingNode
		_func.argtypes = [c_double]
		_func.restype = c_double
		return _func(JD)

	@staticmethod
	def MeanLongitudePerigee(JD: float):
		_func = _aaplus.CAAMoon_MeanLongitudePerigee
		_func.argtypes = [c_double]
		_func.restype = c_double
		return _func(JD)

	@staticmethod
	def TrueLongitudeAscendingNode(JD: float):
		_func = _aaplus.CAAMoon_TrueLongitudeAscendingNode
		_func.argtypes = [c_double]
		_func.restype = c_double
		return _func(JD)

	@staticmethod
	def EclipticLongitude(JD: float):
		_func = _aaplus.CAAMoon_EclipticLongitude
		_func.argtypes = [c_double]
		_func.restype = c_double
		return _func(JD)

	@staticmethod
	def EclipticLatitude(JD: float):
		_func = _aaplus.CAAMoon_EclipticLatitude
		_func.argtypes = [c_double]
		_func.restype = c_double
		return _func(JD)

	@staticmethod
	def RadiusVector(JD: float):
		_func = _aaplus.CAAMoon_RadiusVector
		_func.argtypes = [c_double]
		_func.restype = c_double
		return _func(JD)

	@staticmethod
	def RadiusVectorToHorizontalParallax(RadiusVector: float):
		_func = _aaplus.CAAMoon_RadiusVectorToHorizontalParallax
		_func.argtypes = [c_double]
		_func.restype = c_double
		return _func(RadiusVector)

	@staticmethod
	def HorizontalParallaxToRadiusVector(Parallax: float):
		_func = _aaplus.CAAMoon_HorizontalParallaxToRadiusVector
		_func.argtypes = [c_double]
		_func.restype = c_double
		return _func(Parallax)
	
	@staticmethod
	def GetLunarPhaseAngle(dt: datetime, IsGregorian: bool = True):
		'''
		Calculates the Lunar phase angle (between 0 and 360 degress) for the given Python datetime in UTC.
		The returned angle can be used to determine the Moon phase:
		0 or 360 degrees - New Moon,
		more than 0 but less than 90 - Waxing Crescent,
		90 degrees - First Quarter,
		more than 90 but less the 180 - Waxing Gibbous,
		180 degrees - Full Moon,
		more than 180 but less than 270 - Waning Gibbous,
		270 degrees - Last Quarter,
		more than 270 but less then 360 - Waning Crescent.
		'''
		tt = AADate.DateTimeUTC2TT(dt, IsGregorian)
		return AACoordinateTransformation.MapTo0To360Range(AAMoon.EclipticLongitude(tt) - AASun.ApparentEclipticLongitude(tt, True))


class AAMoonIlluminatedFraction:
	@staticmethod
	def GeocentricElongation(ObjectAlpha: float, ObjectDelta: float, SunAlpha: float, SunDelta: float):
		_func = _aaplus.CAAMoonIlluminatedFraction_GeocentricElongation
		_func.argtypes = [c_double, c_double, c_double, c_double]
		_func.restype = c_double
		return _func(ObjectAlpha, ObjectDelta, SunAlpha, SunDelta)

	@staticmethod
	def PhaseAngle(GeocentricElongation: float, EarthObjectDistance: float, EarthSunDistance: float):
		_func = _aaplus.CAAMoonIlluminatedFraction_PhaseAngle
		_func.argtypes = [c_double, c_double, c_double]
		_func.restype = c_double
		return _func(GeocentricElongation, EarthObjectDistance, EarthSunDistance)

	@staticmethod
	def IlluminatedFraction(PhaseAngle: float):
		_func = _aaplus.CAAMoonIlluminatedFraction_IlluminatedFraction
		_func.argtypes = [c_double]
		_func.restype = c_double
		return _func(PhaseAngle)

	@staticmethod
	def PositionAngle(Alpha0: float, Delta0: float, Alpha: float, Delta: float):
		_func = _aaplus.CAAMoonIlluminatedFraction_PositionAngle
		_func.argtypes = [c_double, c_double, c_double, c_double]
		_func.restype = c_double
		return _func(Alpha0, Delta0, Alpha, Delta)


class AAMoonMaxDeclinations:
	@staticmethod
	def K(Year: float):
		_func = _aaplus.CAAMoonMaxDeclinations_K
		_func.argtypes = [c_double]
		_func.restype = c_double
		return _func(Year)

	@staticmethod
	def MeanGreatestDeclination(k: float, bNortherly: bool):
		_func = _aaplus.CAAMoonMaxDeclinations_MeanGreatestDeclination
		_func.argtypes = [c_double, c_byte]
		_func.restype = c_double
		return _func(k, bNortherly)

	@staticmethod
	def MeanGreatestDeclinationValue(k: float):
		_func = _aaplus.CAAMoonMaxDeclinations_MeanGreatestDeclinationValue
		_func.argtypes = [c_double]
		_func.restype = c_double
		return _func(k)

	@staticmethod
	def TrueGreatestDeclination(k: float, bNortherly: bool):
		_func = _aaplus.CAAMoonMaxDeclinations_TrueGreatestDeclination
		_func.argtypes = [c_double, c_byte]
		_func.restype = c_double
		return _func(k, bNortherly)

	@staticmethod
	def TrueGreatestDeclinationValue(k: float, bNortherly: bool):
		_func = _aaplus.CAAMoonMaxDeclinations_TrueGreatestDeclinationValue
		_func.argtypes = [c_double, c_byte]
		_func.restype = c_double
		return _func(k, bNortherly)


class AAMoonMaxDeclinations2:
	class Type(IntEnum):
		NotDefined = 0
		MaxNorthernDeclination = 1
		MaxSouthernDeclination = 2

	class Algorithm(IntEnum):
		MeeusTruncated = 0
		ELP2000 = 1

	class AAMoonMaxDeclinationsDetails2(Structure):
		_fields_ = [
			('type', c_int),
			('JD', c_double),
			('Declination', c_double),
			('RA', c_double),
		]

	@staticmethod
	def Calculate(StartJD: float, EndJD: float, StepInterval: float = 0.007, algorithm: Algorithm = Algorithm.MeeusTruncated):
		_func = _aaplus.CAAMoonMaxDeclinations2_Calculate
		_func.argtypes = [c_double, c_double, c_double, c_int, POINTER(c_int)]
		_func.restype = POINTER(AAMoonMaxDeclinations2.AAMoonMaxDeclinationsDetails2)
		_num = c_int()
		_ptr = _func(StartJD, EndJD, StepInterval, algorithm.value, byref(_num))
		_res = []
		for x in range(0, _num.value):
			_res.append(_ptr[x])
		return _res


class AAMoonNodes:
	@staticmethod
	def K(Year: float):
		_func = _aaplus.CAAMoonNodes_K
		_func.argtypes = [c_double]
		_func.restype = c_double
		return _func(Year)

	@staticmethod
	def PassageThroNode(k: float):
		_func = _aaplus.CAAMoonNodes_PassageThroNode
		_func.argtypes = [c_double]
		_func.restype = c_double
		return _func(k)


class AAMoonNodes2:
	class Type(IntEnum):
		NotDefined = 0
		Ascending = 1
		Descending = 2

	class Algorithm(IntEnum):
		MeeusTruncated = 0
		ELP2000 = 1

	class AAMoonNodesDetails2(Structure):
		_fields_ = [
			('type', c_int),
			('JD', c_double),
		]

	@staticmethod
	def Calculate(StartJD: float, EndJD: float, StepInterval: float = 0.007, algorithm: Algorithm = Algorithm.MeeusTruncated):
		_func = _aaplus.CAAMoonNodes2_Calculate
		_func.argtypes = [c_double, c_double, c_double, c_int, POINTER(c_int)]
		_func.restype = POINTER(AAMoonNodes2.AAMoonNodesDetails2)
		_num = c_int()
		_ptr = _func(StartJD, EndJD, StepInterval, algorithm.value, byref(_num))
		_res = []
		for x in range(0, _num.value):
			_res.append(_ptr[x])
		return _res


class AAMoonPerigeeApogee:
	@staticmethod
	def K(Year: float):
		_func = _aaplus.CAAMoonPerigeeApogee_K
		_func.argtypes = [c_double]
		_func.restype = c_double
		return _func(Year)

	@staticmethod
	def MeanPerigee(k: float):
		_func = _aaplus.CAAMoonPerigeeApogee_MeanPerigee
		_func.argtypes = [c_double]
		_func.restype = c_double
		return _func(k)

	@staticmethod
	def MeanApogee(k: float):
		_func = _aaplus.CAAMoonPerigeeApogee_MeanApogee
		_func.argtypes = [c_double]
		_func.restype = c_double
		return _func(k)

	@staticmethod
	def TruePerigee(k: float):
		_func = _aaplus.CAAMoonPerigeeApogee_TruePerigee
		_func.argtypes = [c_double]
		_func.restype = c_double
		return _func(k)

	@staticmethod
	def TrueApogee(k: float):
		_func = _aaplus.CAAMoonPerigeeApogee_TrueApogee
		_func.argtypes = [c_double]
		_func.restype = c_double
		return _func(k)

	@staticmethod
	def PerigeeParallax(k: float):
		_func = _aaplus.CAAMoonPerigeeApogee_PerigeeParallax
		_func.argtypes = [c_double]
		_func.restype = c_double
		return _func(k)

	@staticmethod
	def ApogeeParallax(k: float):
		_func = _aaplus.CAAMoonPerigeeApogee_ApogeeParallax
		_func.argtypes = [c_double]
		_func.restype = c_double
		return _func(k)


class AAMoonPerigeeApogee2:
	class Type(IntEnum):
		NotDefined = 0
		Perigee = 1
		Apogee = 2

	class Algorithm(IntEnum):
		MeeusTruncated = 0
		ELP2000 = 1

	class AAMoonPerigeeApogeeDetails2(Structure):
		_fields_ = [
			('type', c_int),
			('JD', c_double),
			('Value', c_double),
		]

	@staticmethod
	def Calculate(StartJD: float, EndJD: float, StepInterval: float = 0.007, algorithm: Algorithm = Algorithm.MeeusTruncated):
		_func = _aaplus.CAAMoonPerigeeApogee2_Calculate
		_func.argtypes = [c_double, c_double, c_double, c_int, POINTER(c_int)]
		_func.restype = POINTER(AAMoonPerigeeApogee2.AAMoonPerigeeApogeeDetails2)
		_num = c_int()
		_ptr = _func(StartJD, EndJD, StepInterval, algorithm.value, byref(_num))
		_res = []
		for x in range(0, _num.value):
			_res.append(_ptr[x])
		return _res


class AAMoonPhases:
	@staticmethod
	def K(Year: float):
		_func = _aaplus.CAAMoonPhases_K
		_func.argtypes = [c_double]
		_func.restype = c_double
		return _func(Year)

	@staticmethod
	def MeanPhase(k: float):
		_func = _aaplus.CAAMoonPhases_MeanPhase
		_func.argtypes = [c_double]
		_func.restype = c_double
		return _func(k)

	@staticmethod
	def TruePhase(k: float):
		_func = _aaplus.CAAMoonPhases_TruePhase
		_func.argtypes = [c_double]
		_func.restype = c_double
		return _func(k)


class AAMoonPhases2:
	class Type(IntEnum):
		NotDefined = 0
		NewMoon = 1
		FirstQuarter = 2
		FullMoon = 3
		LastQuarter = 4

	class Algorithm(IntEnum):
		MeeusTruncated = 0
		ELP2000 = 1

	class AAMoonPhasesDetails2(Structure):
		_fields_ = [
			('type', c_int),
			('JD', c_double),
		]

	@staticmethod
	def Calculate(StartJD: float, EndJD: float, StepInterval: float = 0.007, algorithm: Algorithm = Algorithm.MeeusTruncated):
		_func = _aaplus.CAAMoonPhases2_Calculate
		_func.argtypes = [c_double, c_double, c_double, c_int, POINTER(c_int)]
		_func.restype = POINTER(AAMoonPhases2.AAMoonPhasesDetails2)
		_num = c_int()
		_ptr = _func(StartJD, EndJD, StepInterval, algorithm.value, byref(_num))
		_res = []
		for x in range(0, _num.value):
			_res.append(_ptr[x])
		return _res


class AAMoslemCalendar:
	@staticmethod
	def MoslemToJulian(Year: int, Month: int, Day: int):
		_func = _aaplus.CAAMoslemCalendar_MoslemToJulian
		_func.argtypes = [c_long, c_long, c_long]
		_func.restype = AAMoslemCalendar.AACalendarDate
		return _func(Year, Month, Day)

	@staticmethod
	def JulianToMoslem(Year: int, Month: int, Day: int):
		_func = _aaplus.CAAMoslemCalendar_JulianToMoslem
		_func.argtypes = [c_long, c_long, c_long]
		_func.restype = AAMoslemCalendar.AACalendarDate
		return _func(Year, Month, Day)

	@staticmethod
	def IsLeap(Year: int):
		_func = _aaplus.CAAMoslemCalendar_IsLeap
		_func.argtypes = [c_long]
		_func.restype = c_byte
		return _func(Year)


class AANearParabolic:
	class AANearParabolicObjectElements(Structure):
		_fields_ = [
			('q', c_double),
			('i', c_double),
			('w', c_double),
			('omega', c_double),
			('JDEquinox', c_double),
			('T', c_double),
			('e', c_double),
		]

	class AANearParabolicObjectDetails(Structure):
		_fields_ = [
			('HeliocentricRectangularEquatorial', AA3DCoordinate),
			('HeliocentricRectangularEcliptical', AA3DCoordinate),
			('HeliocentricEclipticLongitude', c_double),
			('HeliocentricEclipticLatitude', c_double),
			('TrueGeocentricRA', c_double),
			('TrueGeocentricDeclination', c_double),
			('TrueGeocentricDistance', c_double),
			('TrueGeocentricLightTime', c_double),
			('AstrometricGeocentricRA', c_double),
			('AstrometricGeocentricDeclination', c_double),
			('AstrometricGeocentricDistance', c_double),
			('AstrometricGeocentricLightTime', c_double),
			('Elongation', c_double),
			('PhaseAngle', c_double),
		]

	@staticmethod
	def Calculate(JD: float, elements: AANearParabolicObjectElements, bHighPrecision: bool = True):
		_func = _aaplus.CAANearParabolic_Calculate
		_func.argtypes = [c_double, POINTER(AANearParabolic.AANearParabolicObjectElements), c_byte]
		_func.restype = AANearParabolic.AANearParabolicObjectDetails
		return _func(JD, byref(elements), bHighPrecision)

	@staticmethod
	def cbrt(x: float):
		_func = _aaplus.CAANearParabolic_cbrt
		_func.argtypes = [c_double]
		_func.restype = c_double
		return _func(x)

	@staticmethod
	def CalculateTrueAnomalyAndRadius(JD: float, elements: AANearParabolicObjectElements):
		_func = _aaplus.CAANearParabolic_CalculateTrueAnomalyAndRadius
		_func.argtypes = [c_double, POINTER(AANearParabolic.AANearParabolicObjectElements), POINTER(c_double), POINTER(c_double)]
		_func.restype = None
		_v = c_double()
		_r = c_double()
		_func(JD, byref(elements), byref(_v), byref(_r))
		return {'v': _v.value, 'r': _r.value}


class AANeptune:
	@staticmethod
	def EclipticLongitude(JD: float, bHighPrecision: bool):
		_func = _aaplus.CAANeptune_EclipticLongitude
		_func.argtypes = [c_double, c_byte]
		_func.restype = c_double
		return _func(JD, bHighPrecision)

	@staticmethod
	def EclipticLatitude(JD: float, bHighPrecision: bool):
		_func = _aaplus.CAANeptune_EclipticLatitude
		_func.argtypes = [c_double, c_byte]
		_func.restype = c_double
		return _func(JD, bHighPrecision)

	@staticmethod
	def RadiusVector(JD: float, bHighPrecision: bool):
		_func = _aaplus.CAANeptune_RadiusVector
		_func.argtypes = [c_double, c_byte]
		_func.restype = c_double
		return _func(JD, bHighPrecision)


class AANutation:
	@staticmethod
	def NutationInLongitude(JD: float):
		_func = _aaplus.CAANutation_NutationInLongitude
		_func.argtypes = [c_double]
		_func.restype = c_double
		return _func(JD)

	@staticmethod
	def NutationInObliquity(JD: float):
		_func = _aaplus.CAANutation_NutationInObliquity
		_func.argtypes = [c_double]
		_func.restype = c_double
		return _func(JD)

	@staticmethod
	def NutationInRightAscension(Alpha: float, Delta: float, Obliquity: float, NutationInLongitude: float, NutationInObliquity: float):
		_func = _aaplus.CAANutation_NutationInRightAscension
		_func.argtypes = [c_double, c_double, c_double, c_double, c_double]
		_func.restype = c_double
		return _func(Alpha, Delta, Obliquity, NutationInLongitude, NutationInObliquity)

	@staticmethod
	def NutationInDeclination(Alpha: float, Obliquity: float, NutationInLongitude: float, NutationInObliquity: float):
		_func = _aaplus.CAANutation_NutationInDeclination
		_func.argtypes = [c_double, c_double, c_double, c_double]
		_func.restype = c_double
		return _func(Alpha, Obliquity, NutationInLongitude, NutationInObliquity)

	@staticmethod
	def MeanObliquityOfEcliptic(JD: float):
		_func = _aaplus.CAANutation_MeanObliquityOfEcliptic
		_func.argtypes = [c_double]
		_func.restype = c_double
		return _func(JD)

	@staticmethod
	def TrueObliquityOfEcliptic(JD: float):
		_func = _aaplus.CAANutation_TrueObliquityOfEcliptic
		_func.argtypes = [c_double]
		_func.restype = c_double
		return _func(JD)


class AAParabolic:
	class AAParabolicObjectElements(Structure):
		_fields_ = [
			('q', c_double),
			('i', c_double),
			('w', c_double),
			('omega', c_double),
			('JDEquinox', c_double),
			('T', c_double),
		]

	class AAParabolicObjectDetails(Structure):
		_fields_ = [
			('HeliocentricRectangularEquatorial', AA3DCoordinate),
			('HeliocentricRectangularEcliptical', AA3DCoordinate),
			('HeliocentricEclipticLongitude', c_double),
			('HeliocentricEclipticLatitude', c_double),
			('TrueGeocentricRA', c_double),
			('TrueGeocentricDeclination', c_double),
			('TrueGeocentricDistance', c_double),
			('TrueGeocentricLightTime', c_double),
			('AstrometricGeocentricRA', c_double),
			('AstrometricGeocentricDeclination', c_double),
			('AstrometricGeocentricDistance', c_double),
			('AstrometricGeocentricLightTime', c_double),
			('Elongation', c_double),
			('PhaseAngle', c_double),
		]

	@staticmethod
	def CalculateBarkers(W: float, epsilon: float = 0.000001):
		_func = _aaplus.CAAParabolic_CalculateBarkers
		_func.argtypes = [c_double, c_double]
		_func.restype = c_double
		return _func(W, epsilon)

	@staticmethod
	def Calculate(JD: float, elements: AAParabolicObjectElements, bHighPrecision: bool = True, epsilon: float = 0.000001):
		_func = _aaplus.CAAParabolic_Calculate
		_func.argtypes = [c_double, POINTER(AAParabolic.AAParabolicObjectElements), c_byte, c_double]
		_func.restype = AAParabolic.AAParabolicObjectDetails
		return _func(JD, byref(elements), bHighPrecision, epsilon)


class AANodes:
	class AANodeObjectDetails(Structure):
		_fields_ = [
			('t', c_double),
			('radius', c_double),
		]

	@staticmethod
	def PassageThroAscendingNode(elements: AAElliptical.AAEllipticalObjectElements):
		_func = _aaplus.CAANodes_PassageThroAscendingNode
		_func.argtypes = [POINTER(AAElliptical.AAEllipticalObjectElements)]
		_func.restype = AANodes.AANodeObjectDetails
		return _func(byref(elements))

	@staticmethod
	def PassageThroDescendingNode(elements: AAElliptical.AAEllipticalObjectElements):
		_func = _aaplus.CAANodes_PassageThroDescendingNode
		_func.argtypes = [POINTER(AAElliptical.AAEllipticalObjectElements)]
		_func.restype = AANodes.AANodeObjectDetails
		return _func(byref(elements))

	@staticmethod
	def PassageThroAscendingNode_2(elements: AAParabolic.AAParabolicObjectElements):
		_func = _aaplus.CAANodes_PassageThroAscendingNode_2
		_func.argtypes = [POINTER(AAParabolic.AAParabolicObjectElements)]
		_func.restype = AANodes.AANodeObjectDetails
		return _func(byref(elements))

	@staticmethod
	def PassageThroDescendingNode_2(elements: AAParabolic.AAParabolicObjectElements):
		_func = _aaplus.CAANodes_PassageThroDescendingNode_2
		_func.argtypes = [POINTER(AAParabolic.AAParabolicObjectElements)]
		_func.restype = AANodes.AANodeObjectDetails
		return _func(byref(elements))


class AAParallactic:
	@staticmethod
	def ParallacticAngle(HourAngle: float, Latitude: float, delta: float):
		_func = _aaplus.CAAParallactic_ParallacticAngle
		_func.argtypes = [c_double, c_double, c_double]
		_func.restype = c_double
		return _func(HourAngle, Latitude, delta)

	@staticmethod
	def EclipticLongitudeOnHorizon(LocalSiderealTime: float, ObliquityOfEcliptic: float, Latitude: float):
		_func = _aaplus.CAAParallactic_EclipticLongitudeOnHorizon
		_func.argtypes = [c_double, c_double, c_double]
		_func.restype = c_double
		return _func(LocalSiderealTime, ObliquityOfEcliptic, Latitude)

	@staticmethod
	def AngleBetweenEclipticAndHorizon(LocalSiderealTime: float, ObliquityOfEcliptic: float, Latitude: float):
		_func = _aaplus.CAAParallactic_AngleBetweenEclipticAndHorizon
		_func.argtypes = [c_double, c_double, c_double]
		_func.restype = c_double
		return _func(LocalSiderealTime, ObliquityOfEcliptic, Latitude)

	@staticmethod
	def AngleBetweenNorthCelestialPoleAndNorthPoleOfEcliptic(Lambda: float, Beta: float, ObliquityOfEcliptic: float):
		_func = _aaplus.CAAParallactic_AngleBetweenNorthCelestialPoleAndNorthPoleOfEcliptic
		_func.argtypes = [c_double, c_double, c_double]
		_func.restype = c_double
		return _func(Lambda, Beta, ObliquityOfEcliptic)


class AAParallax:
	class AATopocentricEclipticDetails(Structure):
		_fields_ = [
			('Lambda', c_double),
			('Beta', c_double),
			('Semidiameter', c_double),
		]

	@staticmethod
	def Equatorial2TopocentricDelta(Alpha: float, Delta: float, Distance: float, Longitude: float, Latitude: float, Height: float, JD: float):
		_func = _aaplus.CAAParallax_Equatorial2TopocentricDelta
		_func.argtypes = [c_double, c_double, c_double, c_double, c_double, c_double, c_double]
		_func.restype = AA2DCoordinate
		return _func(Alpha, Delta, Distance, Longitude, Latitude, Height, JD)

	@staticmethod
	def Equatorial2Topocentric(Alpha: float, Delta: float, Distance: float, Longitude: float, Latitude: float, Height: float, JD: float):
		_func = _aaplus.CAAParallax_Equatorial2Topocentric
		_func.argtypes = [c_double, c_double, c_double, c_double, c_double, c_double, c_double]
		_func.restype = AA2DCoordinate
		return _func(Alpha, Delta, Distance, Longitude, Latitude, Height, JD)

	@staticmethod
	def Ecliptic2Topocentric(Lambda: float, Beta: float, Semidiameter: float, Distance: float, Epsilon: float, Latitude: float, Height: float, JD: float):
		_func = _aaplus.CAAParallax_Ecliptic2Topocentric
		_func.argtypes = [c_double, c_double, c_double, c_double, c_double, c_double, c_double, c_double]
		_func.restype = AAParallax.AATopocentricEclipticDetails
		return _func(Lambda, Beta, Semidiameter, Distance, Epsilon, Latitude, Height, JD)

	@staticmethod
	def ParallaxToDistance(Parallax: float):
		_func = _aaplus.CAAParallax_ParallaxToDistance
		_func.argtypes = [c_double]
		_func.restype = c_double
		return _func(Parallax)

	@staticmethod
	def DistanceToParallax(Distance: float):
		_func = _aaplus.CAAParallax_DistanceToParallax
		_func.argtypes = [c_double]
		_func.restype = c_double
		return _func(Distance)


class AAPhysicalJupiter:
	class AAPhysicalJupiterDetails(Structure):
		_fields_ = [
			('DE', c_double),
			('DS', c_double),
			('Geometricw1', c_double),
			('Geometricw2', c_double),
			('Apparentw1', c_double),
			('Apparentw2', c_double),
			('P', c_double),
		]

	@staticmethod
	def Calculate(JD: float, bHighPrecision: bool):
		_func = _aaplus.CAAPhysicalJupiter_Calculate
		_func.argtypes = [c_double, c_byte]
		_func.restype = AAPhysicalJupiter.AAPhysicalJupiterDetails
		return _func(JD, bHighPrecision)


class AAPhysicalMars:
	class AAPhysicalMarsDetails(Structure):
		_fields_ = [
			('DE', c_double),
			('DS', c_double),
			('w', c_double),
			('P', c_double),
			('X', c_double),
			('k', c_double),
			('q', c_double),
			('d', c_double),
		]

	@staticmethod
	def Calculate(JD: float, bHighPrecision: bool):
		_func = _aaplus.CAAPhysicalMars_Calculate
		_func.argtypes = [c_double, c_byte]
		_func.restype = AAPhysicalMars.AAPhysicalMarsDetails
		return _func(JD, bHighPrecision)


class AAPhysicalMoon:
	class AAPhysicalMoonDetails(Structure):
		_fields_ = [
			('ldash', c_double),
			('bdash', c_double),
			('ldash2', c_double),
			('bdash2', c_double),
			('l', c_double),
			('b', c_double),
			('P', c_double),
		]

	class AASelenographicMoonDetails(Structure):
		_fields_ = [
			('l0', c_double),
			('b0', c_double),
			('c0', c_double),
		]

	@staticmethod
	def CalculateGeocentric(JD: float):
		_func = _aaplus.CAAPhysicalMoon_CalculateGeocentric
		_func.argtypes = [c_double]
		_func.restype = AAPhysicalMoon.AAPhysicalMoonDetails
		return _func(JD)

	@staticmethod
	def CalculateTopocentric(JD: float, Longitude: float, Latitude: float):
		_func = _aaplus.CAAPhysicalMoon_CalculateTopocentric
		_func.argtypes = [c_double, c_double, c_double]
		_func.restype = AAPhysicalMoon.AAPhysicalMoonDetails
		return _func(JD, Longitude, Latitude)

	@staticmethod
	def CalculateSelenographicPositionOfSun(JD: float, bHighPrecision: bool):
		_func = _aaplus.CAAPhysicalMoon_CalculateSelenographicPositionOfSun
		_func.argtypes = [c_double, c_byte]
		_func.restype = AAPhysicalMoon.AASelenographicMoonDetails
		return _func(JD, bHighPrecision)

	@staticmethod
	def AltitudeOfSun(JD: float, Longitude: float, Latitude: float, bHighPrecision: bool):
		_func = _aaplus.CAAPhysicalMoon_AltitudeOfSun
		_func.argtypes = [c_double, c_double, c_double, c_byte]
		_func.restype = c_double
		return _func(JD, Longitude, Latitude, bHighPrecision)

	@staticmethod
	def TimeOfSunrise(JD: float, Longitude: float, Latitude: float, bHighPrecision: bool):
		_func = _aaplus.CAAPhysicalMoon_TimeOfSunrise
		_func.argtypes = [c_double, c_double, c_double, c_byte]
		_func.restype = c_double
		return _func(JD, Longitude, Latitude, bHighPrecision)

	@staticmethod
	def TimeOfSunset(JD: float, Longitude: float, Latitude: float, bHighPrecision: bool):
		_func = _aaplus.CAAPhysicalMoon_TimeOfSunset
		_func.argtypes = [c_double, c_double, c_double, c_byte]
		_func.restype = c_double
		return _func(JD, Longitude, Latitude, bHighPrecision)


class AAPhysicalSun:
	class AAPhysicalSunDetails(Structure):
		_fields_ = [
			('P', c_double),
			('B0', c_double),
			('L0', c_double),
		]

	@staticmethod
	def Calculate(JD: float, bHighPrecision: bool):
		_func = _aaplus.CAAPhysicalSun_Calculate
		_func.argtypes = [c_double, c_byte]
		_func.restype = AAPhysicalSun.AAPhysicalSunDetails
		return _func(JD, bHighPrecision)

	@staticmethod
	def TimeOfStartOfRotation(C: int):
		_func = _aaplus.CAAPhysicalSun_TimeOfStartOfRotation
		_func.argtypes = [c_long]
		_func.restype = c_double
		return _func(C)


class AAPlanetaryPhenomena:
	class Planet(IntEnum):
		MERCURY = 0
		VENUS = 1
		MARS = 2
		JUPITER = 3
		SATURN = 4
		URANUS = 5
		NEPTUNE = 6

	class Type(IntEnum):
		INFERIOR_CONJUNCTION = 0
		SUPERIOR_CONJUNCTION = 1
		OPPOSITION = 2
		CONJUNCTION = 3
		EASTERN_ELONGATION = 4
		WESTERN_ELONGATION = 5
		STATION1 = 6
		STATION2 = 7

	@staticmethod
	def K(Year: float, planet: Planet, type: Type):
		_func = _aaplus.CAAPlanetaryPhenomena_K
		_func.argtypes = [c_double, c_int, c_int]
		_func.restype = c_double
		return _func(Year, planet.value, type.value)

	@staticmethod
	def Mean(k: float, planet: Planet, type: Type):
		_func = _aaplus.CAAPlanetaryPhenomena_Mean
		_func.argtypes = [c_double, c_int, c_int]
		_func.restype = c_double
		return _func(k, planet.value, type.value)

	@staticmethod
	def _True(k: float, planet: Planet, type: Type):
		_func = _aaplus.CAAPlanetaryPhenomena_True
		_func.argtypes = [c_double, c_int, c_int]
		_func.restype = c_double
		return _func(k, planet.value, type.value)

	@staticmethod
	def ElongationValue(k: float, planet: Planet, bEastern: bool):
		_func = _aaplus.CAAPlanetaryPhenomena_ElongationValue
		_func.argtypes = [c_double, c_int, c_byte]
		_func.restype = c_double
		return _func(k, planet.value, bEastern)


class AAPlanetaryPhenomena2:
	class Type(IntEnum):
		NotDefined = 0
		InferiorConjunctionInEclipticLongitude = 1
		InferiorConjunctionInRA = 2
		InferiorConjunctionInAngularDistance = 3
		SuperiorConjunctionInEclipticLongitude = 4
		SuperiorConjunctionInRA = 5
		SuperiorConjunctionInAngularDistance = 6
		GreatestWesternElongationInEclipticLongitude = 7
		GreatestWesternElongationInRA = 8
		GreatestWesternElongationInAngularDistance = 9
		GreatestEasternElongationInEclipticLongitude = 10
		GreatestEasternElongationInRA = 11
		GreatestEasternElongationInAngularDistance = 12
		OppositionInEclipticLongitude = 13
		OppositionInRA = 14
		OppositionInAngularDistance = 15
		ConjunctionInEclipticLongitude = 16
		ConjunctionInRA = 17
		ConjunctionInAngularDistance = 18
		Station1InEclipticLongitude = 19
		Station1InRA = 20
		Station2InEclipticLongitude = 21
		Station2InRA = 22
		WesternQuadratureInEclipticLongitude = 23
		WesternQuadratureInRA = 24
		WesternQuadratureInAngularDistance = 25
		EasternQuadratureInEclipticLongitude = 26
		EasternQuadratureInRA = 27
		EasternQuadratureInAngularDistance = 28
		MaximumDistance = 29
		MinimumDistance = 30

	class Object(IntEnum):
		MERCURY = 0
		VENUS = 1
		MARS = 2
		JUPITER = 3
		SATURN = 4
		URANUS = 5
		NEPTUNE = 6

	class AAPlanetaryPhenomenaDetails2(Structure):
		_fields_ = [
			('type', c_int),
			('JD', c_double),
			('Value', c_double),
		]

	@staticmethod
	def Calculate(StartJD: float, EndJD: float, object: Object, StepInterval: float = 0.007, bHighPrecision: bool = True):
		_func = _aaplus.CAAPlanetaryPhenomena2_Calculate
		_func.argtypes = [c_double, c_double, c_int, c_double, c_byte, POINTER(c_int)]
		_func.restype = POINTER(AAPlanetaryPhenomena2.AAPlanetaryPhenomenaDetails2)
		_num = c_int()
		_ptr = _func(StartJD, EndJD, object.value, StepInterval, bHighPrecision, byref(_num))
		_res = []
		for x in range(0, _num.value):
			_res.append(_ptr[x])
		return _res


class AAPlanetPerihelionAphelion:
	@staticmethod
	def MercuryK(Year: float):
		_func = _aaplus.CAAPlanetPerihelionAphelion_MercuryK
		_func.argtypes = [c_double]
		_func.restype = c_double
		return _func(Year)

	@staticmethod
	def Mercury(k: float):
		_func = _aaplus.CAAPlanetPerihelionAphelion_Mercury
		_func.argtypes = [c_double]
		_func.restype = c_double
		return _func(k)

	@staticmethod
	def VenusK(Year: float):
		_func = _aaplus.CAAPlanetPerihelionAphelion_VenusK
		_func.argtypes = [c_double]
		_func.restype = c_double
		return _func(Year)

	@staticmethod
	def Venus(k: float):
		_func = _aaplus.CAAPlanetPerihelionAphelion_Venus
		_func.argtypes = [c_double]
		_func.restype = c_double
		return _func(k)

	@staticmethod
	def EarthK(Year: float):
		_func = _aaplus.CAAPlanetPerihelionAphelion_EarthK
		_func.argtypes = [c_double]
		_func.restype = c_double
		return _func(Year)

	@staticmethod
	def EarthPerihelion(k: float, bBarycentric: bool):
		_func = _aaplus.CAAPlanetPerihelionAphelion_EarthPerihelion
		_func.argtypes = [c_double, c_byte]
		_func.restype = c_double
		return _func(k, bBarycentric)

	@staticmethod
	def EarthAphelion(k: float, bBarycentric: bool):
		_func = _aaplus.CAAPlanetPerihelionAphelion_EarthAphelion
		_func.argtypes = [c_double, c_byte]
		_func.restype = c_double
		return _func(k, bBarycentric)

	@staticmethod
	def MarsK(Year: float):
		_func = _aaplus.CAAPlanetPerihelionAphelion_MarsK
		_func.argtypes = [c_double]
		_func.restype = c_double
		return _func(Year)

	@staticmethod
	def Mars(k: float):
		_func = _aaplus.CAAPlanetPerihelionAphelion_Mars
		_func.argtypes = [c_double]
		_func.restype = c_double
		return _func(k)

	@staticmethod
	def JupiterK(Year: float):
		_func = _aaplus.CAAPlanetPerihelionAphelion_JupiterK
		_func.argtypes = [c_double]
		_func.restype = c_double
		return _func(Year)

	@staticmethod
	def Jupiter(k: float):
		_func = _aaplus.CAAPlanetPerihelionAphelion_Jupiter
		_func.argtypes = [c_double]
		_func.restype = c_double
		return _func(k)

	@staticmethod
	def SaturnK(Year: float):
		_func = _aaplus.CAAPlanetPerihelionAphelion_SaturnK
		_func.argtypes = [c_double]
		_func.restype = c_double
		return _func(Year)

	@staticmethod
	def Saturn(k: float):
		_func = _aaplus.CAAPlanetPerihelionAphelion_Saturn
		_func.argtypes = [c_double]
		_func.restype = c_double
		return _func(k)

	@staticmethod
	def UranusK(Year: float):
		_func = _aaplus.CAAPlanetPerihelionAphelion_UranusK
		_func.argtypes = [c_double]
		_func.restype = c_double
		return _func(Year)

	@staticmethod
	def Uranus(k: float):
		_func = _aaplus.CAAPlanetPerihelionAphelion_Uranus
		_func.argtypes = [c_double]
		_func.restype = c_double
		return _func(k)

	@staticmethod
	def NeptuneK(Year: float):
		_func = _aaplus.CAAPlanetPerihelionAphelion_NeptuneK
		_func.argtypes = [c_double]
		_func.restype = c_double
		return _func(Year)

	@staticmethod
	def Neptune(k: float):
		_func = _aaplus.CAAPlanetPerihelionAphelion_Neptune
		_func.argtypes = [c_double]
		_func.restype = c_double
		return _func(k)


class AAPlanetPerihelionAphelion2:
	class Type(IntEnum):
		NotDefined = 0
		Perihelion = 1
		Aphelion = 2

	class Object(IntEnum):
		MERCURY = 0
		VENUS = 1
		EARTH = 2
		MARS = 3
		JUPITER = 4
		SATURN = 5
		URANUS = 6
		NEPTUNE = 7
		PLUTO = 8

	class AAPlanetPerihelionAphelionDetails2(Structure):
		_fields_ = [
			('type', c_int),
			('JD', c_double),
			('Value', c_double),
		]

	@staticmethod
	def Calculate(StartJD: float, EndJD: float, object: Object, StepInterval: float = 0.007, bHighPrecision: bool = True):
		_func = _aaplus.CAAPlanetPerihelionAphelion2_Calculate
		_func.argtypes = [c_double, c_double, c_int, c_double, c_byte, POINTER(c_int)]
		_func.restype = POINTER(AAPlanetPerihelionAphelion2.AAPlanetPerihelionAphelionDetails2)
		_num = c_int()
		_ptr = _func(StartJD, EndJD, object.value, StepInterval, bHighPrecision, byref(_num))
		_res = []
		for x in range(0, _num.value):
			_res.append(_ptr[x])
		return _res


class AAPluto:
	@staticmethod
	def EclipticLongitude(JD: float):
		_func = _aaplus.CAAPluto_EclipticLongitude
		_func.argtypes = [c_double]
		_func.restype = c_double
		return _func(JD)

	@staticmethod
	def EclipticLatitude(JD: float):
		_func = _aaplus.CAAPluto_EclipticLatitude
		_func.argtypes = [c_double]
		_func.restype = c_double
		return _func(JD)

	@staticmethod
	def RadiusVector(JD: float):
		_func = _aaplus.CAAPluto_RadiusVector
		_func.argtypes = [c_double]
		_func.restype = c_double
		return _func(JD)


class AAPrecession:
	@staticmethod
	def PrecessEquatorial(Alpha: float, Delta: float, JD0: float, JD: float):
		_func = _aaplus.CAAPrecession_PrecessEquatorial
		_func.argtypes = [c_double, c_double, c_double, c_double]
		_func.restype = AA2DCoordinate
		return _func(Alpha, Delta, JD0, JD)

	@staticmethod
	def PrecessEquatorialFK4(Alpha: float, Delta: float, JD0: float, JD: float):
		_func = _aaplus.CAAPrecession_PrecessEquatorialFK4
		_func.argtypes = [c_double, c_double, c_double, c_double]
		_func.restype = AA2DCoordinate
		return _func(Alpha, Delta, JD0, JD)

	@staticmethod
	def PrecessEcliptic(Lambda: float, Beta: float, JD0: float, JD: float):
		_func = _aaplus.CAAPrecession_PrecessEcliptic
		_func.argtypes = [c_double, c_double, c_double, c_double]
		_func.restype = AA2DCoordinate
		return _func(Lambda, Beta, JD0, JD)

	@staticmethod
	def EquatorialPMToEcliptic(Alpha: float, Delta: float, Beta: float, PMAlpha: float, PMDelta: float, Epsilon: float):
		_func = _aaplus.CAAPrecession_EquatorialPMToEcliptic
		_func.argtypes = [c_double, c_double, c_double, c_double, c_double, c_double]
		_func.restype = AA2DCoordinate
		return _func(Alpha, Delta, Beta, PMAlpha, PMDelta, Epsilon)

	@staticmethod
	def AdjustPositionUsingUniformProperMotion(t: float, Alpha: float, Delta: float, PMAlpha: float, PMDelta: float):
		_func = _aaplus.CAAPrecession_AdjustPositionUsingUniformProperMotion
		_func.argtypes = [c_double, c_double, c_double, c_double, c_double]
		_func.restype = AA2DCoordinate
		return _func(t, Alpha, Delta, PMAlpha, PMDelta)

	@staticmethod
	def AdjustPositionUsingMotionInSpace(r: float, deltar: float, t: float, Alpha: float, Delta: float, PMAlpha: float, PMDelta: float):
		_func = _aaplus.CAAPrecession_AdjustPositionUsingMotionInSpace
		_func.argtypes = [c_double, c_double, c_double, c_double, c_double, c_double, c_double]
		_func.restype = AA2DCoordinate
		return _func(r, deltar, t, Alpha, Delta, PMAlpha, PMDelta)


class AARefraction:
	@staticmethod
	def RefractionFromApparent(Altitude: float, Pressure: float, Temperature: float):
		_func = _aaplus.CAARefraction_RefractionFromApparent
		_func.argtypes = [c_double, c_double, c_double]
		_func.restype = c_double
		return _func(Altitude, Pressure, Temperature)

	@staticmethod
	def RefractionFromTrue(Altitude: float, Pressure: float, Temperature: float):
		_func = _aaplus.CAARefraction_RefractionFromTrue
		_func.argtypes = [c_double, c_double, c_double]
		_func.restype = c_double
		return _func(Altitude, Pressure, Temperature)


class AARiseTransitSet:
	class AARiseTransitSetDetails(Structure):
		_fields_ = [
			('bRiseValid', c_byte),
			('Rise', c_double),
			('bTransitValid', c_byte),
			('bTransitAboveHorizon', c_byte),
			('Transit', c_double),
			('bSetValid', c_byte),
			('Set', c_double),
		]

	@staticmethod
	def Calculate(JD: float, Alpha1: float, Delta1: float, Alpha2: float, Delta2: float, Alpha3: float, Delta3: float, Longitude: float, Latitude: float, h0: float):
		_func = _aaplus.CAARiseTransitSet_Calculate
		_func.argtypes = [c_double, c_double, c_double, c_double, c_double, c_double, c_double, c_double, c_double, c_double]
		_func.restype = AARiseTransitSet.AARiseTransitSetDetails
		return _func(JD, Alpha1, Delta1, Alpha2, Delta2, Alpha3, Delta3, Longitude, Latitude, h0)

	@staticmethod
	def CorrectRAValuesForInterpolation(Alpha1: float, Alpha2: float, Alpha3: float):
		_func = _aaplus.CAARiseTransitSet_CorrectRAValuesForInterpolation
		_func.argtypes = [POINTER(c_double), POINTER(c_double), POINTER(c_double)]
		_func.restype = None
		_Alpha1 = c_double(Alpha1)
		_Alpha2 = c_double(Alpha2)
		_Alpha3 = c_double(Alpha3)
		_func(byref(_Alpha1), byref(_Alpha2), byref(_Alpha3))
		return {'Alpha1': _Alpha1.value, 'Alpha2': _Alpha2.value, 'Alpha3': _Alpha3.value}


class AARiseTransitSet2:
	class Type(IntEnum):
		NotDefined = 0
		Rise = 1
		Set = 2
		SouthernTransit = 3
		NorthernTransit = 4
		CivilDusk = 5
		NauticalDusk = 6
		AstronomicalDusk = 7
		AstronomicalDawn = 8
		NauticalDawn = 9
		CivilDawn = 10

	class Object(IntEnum):
		SUN = 0
		MOON = 1
		MERCURY = 2
		VENUS = 3
		MARS = 4
		JUPITER = 5
		SATURN = 6
		URANUS = 7
		NEPTUNE = 8
		STAR = 9

	class MoonAlgorithm(IntEnum):
		MeeusTruncated = 0
		ELP2000 = 1

	class AARiseTransitSetDetails2(Structure):
		_fields_ = [
			('type', c_int),
			('JD', c_double),
			('Bearing', c_double),
			('GeometricAltitude', c_double),
			('bAboveHorizon', c_byte),
		]

	@staticmethod
	def Calculate(StartJD: float, EndJD: float, object: Object, Longitude: float, Latitude: float, h0: float, StepInterval: float = 0.007, bHighPrecision: bool = True):
		_func = _aaplus.CAARiseTransitSet2_Calculate
		_func.argtypes = [c_double, c_double, c_int, c_double, c_double, c_double, c_double, c_byte, POINTER(c_int)]
		_func.restype = POINTER(AARiseTransitSet2.AARiseTransitSetDetails2)
		_num = c_int()
		_ptr = _func(StartJD, EndJD, object.value, Longitude, Latitude, h0, StepInterval, bHighPrecision, byref(_num))
		_res = []
		for x in range(0, _num.value):
			_res.append(_ptr[x])
		return _res

	@staticmethod
	def CalculateMoon(StartJD: float, EndJD: float, Longitude: float, Latitude: float, RefractionAtHorizon: float = -0.5667, StepInterval: float = 0.007, algorithm: MoonAlgorithm = MoonAlgorithm.MeeusTruncated):
		_func = _aaplus.CAARiseTransitSet2_CalculateMoon
		_func.argtypes = [c_double, c_double, c_double, c_double, c_double, c_double, c_int, POINTER(c_int)]
		_func.restype = POINTER(AARiseTransitSet2.AARiseTransitSetDetails2)
		_num = c_int()
		_ptr = _func(StartJD, EndJD, Longitude, Latitude, RefractionAtHorizon, StepInterval, algorithm.value, byref(_num))
		_res = []
		for x in range(0, _num.value):
			_res.append(_ptr[x])
		return _res

	@staticmethod
	def CalculateStationary(StartJD: float, EndJD: float, Alpha: float, Delta: float, Longitude: float, Latitude: float, h0: float = -0.5667, StepInterval: float = 0.007):
		_func = _aaplus.CAARiseTransitSet2_CalculateStationary
		_func.argtypes = [c_double, c_double, c_double, c_double, c_double, c_double, c_double, c_double, POINTER(c_int)]
		_func.restype = POINTER(AARiseTransitSet2.AARiseTransitSetDetails2)
		_num = c_int()
		_ptr = _func(StartJD, EndJD, Alpha, Delta, Longitude, Latitude, h0, StepInterval, byref(_num))
		_res = []
		for x in range(0, _num.value):
			_res.append(_ptr[x])
		return _res


class AASaturn:
	@staticmethod
	def EclipticLongitude(JD: float, bHighPrecision: bool):
		_func = _aaplus.CAASaturn_EclipticLongitude
		_func.argtypes = [c_double, c_byte]
		_func.restype = c_double
		return _func(JD, bHighPrecision)

	@staticmethod
	def EclipticLatitude(JD: float, bHighPrecision: bool):
		_func = _aaplus.CAASaturn_EclipticLatitude
		_func.argtypes = [c_double, c_byte]
		_func.restype = c_double
		return _func(JD, bHighPrecision)

	@staticmethod
	def RadiusVector(JD: float, bHighPrecision: bool):
		_func = _aaplus.CAASaturn_RadiusVector
		_func.argtypes = [c_double, c_byte]
		_func.restype = c_double
		return _func(JD, bHighPrecision)


class AASaturnMoonDetail(Structure):
	_fields_ = [
		('TrueRectangularCoordinates', AA3DCoordinate),
		('ApparentRectangularCoordinates', AA3DCoordinate),
		('bInTransit', c_byte),
		('bInOccultation', c_byte),
		('bInEclipse', c_byte),
		('bInShadowTransit', c_byte),
	]

class AASaturnMoons:
	class AASaturnMoonsDetails(Structure):
		_fields_ = [
			('Satellite1', AASaturnMoonDetail),
			('Satellite2', AASaturnMoonDetail),
			('Satellite3', AASaturnMoonDetail),
			('Satellite4', AASaturnMoonDetail),
			('Satellite5', AASaturnMoonDetail),
			('Satellite6', AASaturnMoonDetail),
			('Satellite7', AASaturnMoonDetail),
			('Satellite8', AASaturnMoonDetail),
		]

	@staticmethod
	def Calculate(JD: float, bHighPrecision: bool):
		_func = _aaplus.CAASaturnMoons_Calculate
		_func.argtypes = [c_double, c_byte]
		_func.restype = AASaturnMoons.AASaturnMoonsDetails
		return _func(JD, bHighPrecision)


class AASaturnRings:
	class AASaturnRingDetails(Structure):
		_fields_ = [
			('B', c_double),
			('Bdash', c_double),
			('P', c_double),
			('a', c_double),
			('b', c_double),
			('DeltaU', c_double),
			('U1', c_double),
			('U2', c_double),
		]

	@staticmethod
	def Calculate(JD: float, bHighPrecision: bool):
		_func = _aaplus.CAASaturnRings_Calculate
		_func.argtypes = [c_double, c_byte]
		_func.restype = AASaturnRings.AASaturnRingDetails
		return _func(JD, bHighPrecision)


class AASidereal:
	@staticmethod
	def MeanGreenwichSiderealTime(JD: float):
		_func = _aaplus.CAASidereal_MeanGreenwichSiderealTime
		_func.argtypes = [c_double]
		_func.restype = c_double
		return _func(JD)

	@staticmethod
	def ApparentGreenwichSiderealTime(JD: float):
		_func = _aaplus.CAASidereal_ApparentGreenwichSiderealTime
		_func.argtypes = [c_double]
		_func.restype = c_double
		return _func(JD)


class AAStellarMagnitudes:
	@staticmethod
	def CombinedMagnitude(m1: float, m2: float):
		_func = _aaplus.CAAStellarMagnitudes_CombinedMagnitude
		_func.argtypes = [c_double, c_double]
		_func.restype = c_double
		return _func(m1, m2)

	@staticmethod
	def CombinedMagnitude_2(Magnitudes: int, pMagnitudes: list):
		_func = _aaplus.CAAStellarMagnitudes_CombinedMagnitude_2
		_func.argtypes = [c_int, c_double * Magnitudes]
		_func.restype = c_double
		return _func(Magnitudes, pMagnitudes)

	@staticmethod
	def BrightnessRatio(m1: float, m2: float):
		_func = _aaplus.CAAStellarMagnitudes_BrightnessRatio
		_func.argtypes = [c_double, c_double]
		_func.restype = c_double
		return _func(m1, m2)

	@staticmethod
	def MagnitudeDifference(brightnessRatio: float):
		_func = _aaplus.CAAStellarMagnitudes_MagnitudeDifference
		_func.argtypes = [c_double]
		_func.restype = c_double
		return _func(brightnessRatio)


class AASun:
	@staticmethod
	def GeometricEclipticLongitude(JD: float, bHighPrecision: bool):
		_func = _aaplus.CAASun_GeometricEclipticLongitude
		_func.argtypes = [c_double, c_byte]
		_func.restype = c_double
		return _func(JD, bHighPrecision)

	@staticmethod
	def GeometricEclipticLatitude(JD: float, bHighPrecision: bool):
		_func = _aaplus.CAASun_GeometricEclipticLatitude
		_func.argtypes = [c_double, c_byte]
		_func.restype = c_double
		return _func(JD, bHighPrecision)

	@staticmethod
	def GeometricEclipticLongitudeJ2000(JD: float, bHighPrecision: bool):
		_func = _aaplus.CAASun_GeometricEclipticLongitudeJ2000
		_func.argtypes = [c_double, c_byte]
		_func.restype = c_double
		return _func(JD, bHighPrecision)

	@staticmethod
	def GeometricEclipticLatitudeJ2000(JD: float, bHighPrecision: bool):
		_func = _aaplus.CAASun_GeometricEclipticLatitudeJ2000
		_func.argtypes = [c_double, c_byte]
		_func.restype = c_double
		return _func(JD, bHighPrecision)

	@staticmethod
	def GeometricFK5EclipticLongitude(JD: float, bHighPrecision: bool):
		_func = _aaplus.CAASun_GeometricFK5EclipticLongitude
		_func.argtypes = [c_double, c_byte]
		_func.restype = c_double
		return _func(JD, bHighPrecision)

	@staticmethod
	def GeometricFK5EclipticLatitude(JD: float, bHighPrecision: bool):
		_func = _aaplus.CAASun_GeometricFK5EclipticLatitude
		_func.argtypes = [c_double, c_byte]
		_func.restype = c_double
		return _func(JD, bHighPrecision)

	@staticmethod
	def ApparentEclipticLongitude(JD: float, bHighPrecision: bool):
		_func = _aaplus.CAASun_ApparentEclipticLongitude
		_func.argtypes = [c_double, c_byte]
		_func.restype = c_double
		return _func(JD, bHighPrecision)

	@staticmethod
	def ApparentEclipticLatitude(JD: float, bHighPrecision: bool):
		_func = _aaplus.CAASun_ApparentEclipticLatitude
		_func.argtypes = [c_double, c_byte]
		_func.restype = c_double
		return _func(JD, bHighPrecision)

	@staticmethod
	def VariationGeometricEclipticLongitude(JD: float):
		_func = _aaplus.CAASun_VariationGeometricEclipticLongitude
		_func.argtypes = [c_double]
		_func.restype = c_double
		return _func(JD)

	@staticmethod
	def EquatorialRectangularCoordinatesMeanEquinox(JD: float, bHighPrecision: bool):
		_func = _aaplus.CAASun_EquatorialRectangularCoordinatesMeanEquinox
		_func.argtypes = [c_double, c_byte]
		_func.restype = AA3DCoordinate
		return _func(JD, bHighPrecision)

	@staticmethod
	def EclipticRectangularCoordinatesJ2000(JD: float, bHighPrecision: bool):
		_func = _aaplus.CAASun_EclipticRectangularCoordinatesJ2000
		_func.argtypes = [c_double, c_byte]
		_func.restype = AA3DCoordinate
		return _func(JD, bHighPrecision)

	@staticmethod
	def EquatorialRectangularCoordinatesJ2000(JD: float, bHighPrecision: bool):
		_func = _aaplus.CAASun_EquatorialRectangularCoordinatesJ2000
		_func.argtypes = [c_double, c_byte]
		_func.restype = AA3DCoordinate
		return _func(JD, bHighPrecision)

	@staticmethod
	def EquatorialRectangularCoordinatesB1950(JD: float, bHighPrecision: bool):
		_func = _aaplus.CAASun_EquatorialRectangularCoordinatesB1950
		_func.argtypes = [c_double, c_byte]
		_func.restype = AA3DCoordinate
		return _func(JD, bHighPrecision)

	@staticmethod
	def EquatorialRectangularCoordinatesAnyEquinox(JD: float, JDEquinox: float, bHighPrecision: bool):
		_func = _aaplus.CAASun_EquatorialRectangularCoordinatesAnyEquinox
		_func.argtypes = [c_double, c_double, c_byte]
		_func.restype = AA3DCoordinate
		return _func(JD, JDEquinox, bHighPrecision)


class AAUranus:
	@staticmethod
	def EclipticLongitude(JD: float, bHighPrecision: bool):
		_func = _aaplus.CAAUranus_EclipticLongitude
		_func.argtypes = [c_double, c_byte]
		_func.restype = c_double
		return _func(JD, bHighPrecision)

	@staticmethod
	def EclipticLatitude(JD: float, bHighPrecision: bool):
		_func = _aaplus.CAAUranus_EclipticLatitude
		_func.argtypes = [c_double, c_byte]
		_func.restype = c_double
		return _func(JD, bHighPrecision)

	@staticmethod
	def RadiusVector(JD: float, bHighPrecision: bool):
		_func = _aaplus.CAAUranus_RadiusVector
		_func.argtypes = [c_double, c_byte]
		_func.restype = c_double
		return _func(JD, bHighPrecision)


class AAVenus:
	@staticmethod
	def EclipticLongitude(JD: float, bHighPrecision: bool):
		_func = _aaplus.CAAVenus_EclipticLongitude
		_func.argtypes = [c_double, c_byte]
		_func.restype = c_double
		return _func(JD, bHighPrecision)

	@staticmethod
	def EclipticLatitude(JD: float, bHighPrecision: bool):
		_func = _aaplus.CAAVenus_EclipticLatitude
		_func.argtypes = [c_double, c_byte]
		_func.restype = c_double
		return _func(JD, bHighPrecision)

	@staticmethod
	def RadiusVector(JD: float, bHighPrecision: bool):
		_func = _aaplus.CAAVenus_RadiusVector
		_func.argtypes = [c_double, c_byte]
		_func.restype = c_double
		return _func(JD, bHighPrecision)


class AAVSOP2013:
	def __init__(self):
		self.__ptr = self.__Create()

	def __del__(self):
		self.__Destroy()

	class Planet(IntEnum):
		MERCURY = 0
		VENUS = 1
		EARTH_MOON_BARYCENTER = 2
		MARS = 3
		JUPITER = 4
		SATURN = 5
		URANUS = 6
		NEPTUNE = 7
		PLUTO = 8

	class AAVSOP2013Orbit(Structure):
		_fields_ = [
			('a', c_double),
			('lambda', c_double),
			('k', c_double),
			('h', c_double),
			('q', c_double),
			('p', c_double)
		]

	class AAVSOP2013Position(Structure):
		_fields_ = [
			('X', c_double),
			('Y', c_double),
			('Z', c_double),
			('X_DASH', c_double),
			('Y_DASH', c_double),
			('Z_DASH', c_double)
		]

	@staticmethod
	def CalculateMeanMotion(planet: Planet, a: float):
		_func = _aaplus.CAAVSOP2013_CalculateMeanMotion
		_func.argtypes = [c_int, c_double]
		_func.restype = c_double
		return _func(planet, a)
	
	@staticmethod
	def OrbitToElements(JD: float, planet: Planet, orbit: AAVSOP2013Orbit):
		_func = _aaplus.CAAVSOP2013_OrbitToElements
		_func.argtypes = [c_double, c_int, POINTER(AAVSOP2013.AAVSOP2013Orbit)]
		_func.restype = AAElliptical.AAEllipticalObjectElements
		return _func(JD, planet, byref(orbit))
	
	@staticmethod
	def Ecliptic2Equatorial(value: AAVSOP2013Position):
		_func = _aaplus.CAAVSOP2013_Ecliptic2Equatorial
		_func.argtypes = [POINTER(AAVSOP2013.AAVSOP2013Position)]
		_func.restype = AAVSOP2013.AAVSOP2013Position 
		return _func(byref(value))
	
	def __Create(self):
		_func = _aaplus.CAAVSOP2013_Create
		_func.argtypes = []
		_func.restype = c_void_p
		return _func()
	
	def __GetBinaryFilesDirectory(self):
		_func = _aaplus.CAAVSOP2013_GetBinaryFilesDirectory
		_func.argtypes = [c_void_p]
		_func.restype = c_char_p
		return _func(self.__ptr)
	
	def __SetBinaryFilesDirectory(self, dir: bytes):
		_func = _aaplus.CAAVSOP2013_SetBinaryFilesDirectory
		_func.argtypes = [c_void_p, c_char_p]
		_func.restype = None
		_buf = create_string_buffer(dir)
		_func(self.__ptr, _buf)
	
	def __Destroy(self):
		_func = _aaplus.CAAVSOP2013_Destroy
		_func.argtypes = [c_void_p]
		_func.restype = None
		_func(self.__ptr)

	def GetBinaryFilesDirectory(self):
		return self.__GetBinaryFilesDirectory().decode(encoding='ascii')
	
	def SetBinaryFilesDirectory(self, dir: str):
		self.__SetBinaryFilesDirectory(dir.encode(encoding='ascii'))


class AAVSOP87:
	class VSOP87Coefficient(Structure):
		_fields_ = [
			('A', c_double),
			('B', c_double),
			('C', c_double),
		]

	class VSOP87Coefficient2(Structure):
		_fields_ = [
			('pCoefficients', c_void_p),
			('nCoefficientsSize', c_size_t),
		]

	@staticmethod
	def Calculate(JD: float, pTable: list, nTableSize: int, bAngle: bool):
		_func = _aaplus.CAAVSOP87_Calculate
		_func.argtypes = [c_double, AAVSOP87.VSOP87Coefficient2 * nTableSize, c_size_t, c_byte]
		_func.restype = c_double
		return _func(JD, pTable, nTableSize, bAngle)

	@staticmethod
	def Calculate_Dash(JD: float, pTable: list, nTableSize: int):
		_func = _aaplus.CAAVSOP87_Calculate_Dash
		_func.argtypes = [c_double, AAVSOP87.VSOP87Coefficient2 * nTableSize, c_size_t]
		_func.restype = c_double
		return _func(JD, pTable, nTableSize)


class AAVSOP87A_Earth:
	@staticmethod
	def Earth_X(JD: float):
		_func = _aaplus.CAAVSOP87A_Earth_X
		_func.argtypes = [c_double]
		_func.restype = c_double
		return _func(JD)

	@staticmethod
	def Earth_X_DASH(JD: float):
		_func = _aaplus.CAAVSOP87A_Earth_X_DASH
		_func.argtypes = [c_double]
		_func.restype = c_double
		return _func(JD)

	@staticmethod
	def Earth_Y(JD: float):
		_func = _aaplus.CAAVSOP87A_Earth_Y
		_func.argtypes = [c_double]
		_func.restype = c_double
		return _func(JD)

	@staticmethod
	def Earth_Y_DASH(JD: float):
		_func = _aaplus.CAAVSOP87A_Earth_Y_DASH
		_func.argtypes = [c_double]
		_func.restype = c_double
		return _func(JD)

	@staticmethod
	def Earth_Z(JD: float):
		_func = _aaplus.CAAVSOP87A_Earth_Z
		_func.argtypes = [c_double]
		_func.restype = c_double
		return _func(JD)

	@staticmethod
	def Earth_Z_DASH(JD: float):
		_func = _aaplus.CAAVSOP87A_Earth_Z_DASH
		_func.argtypes = [c_double]
		_func.restype = c_double
		return _func(JD)


class AAVSOP87A_EMB:
	@staticmethod
	def EMB_X(JD: float):
		_func = _aaplus.CAAVSOP87A_EMB_X
		_func.argtypes = [c_double]
		_func.restype = c_double
		return _func(JD)

	@staticmethod
	def EMB_X_DASH(JD: float):
		_func = _aaplus.CAAVSOP87A_EMB_X_DASH
		_func.argtypes = [c_double]
		_func.restype = c_double
		return _func(JD)

	@staticmethod
	def EMB_Y(JD: float):
		_func = _aaplus.CAAVSOP87A_EMB_Y
		_func.argtypes = [c_double]
		_func.restype = c_double
		return _func(JD)

	@staticmethod
	def EMB_Y_DASH(JD: float):
		_func = _aaplus.CAAVSOP87A_EMB_Y_DASH
		_func.argtypes = [c_double]
		_func.restype = c_double
		return _func(JD)

	@staticmethod
	def EMB_Z(JD: float):
		_func = _aaplus.CAAVSOP87A_EMB_Z
		_func.argtypes = [c_double]
		_func.restype = c_double
		return _func(JD)

	@staticmethod
	def EMB_Z_DASH(JD: float):
		_func = _aaplus.CAAVSOP87A_EMB_Z_DASH
		_func.argtypes = [c_double]
		_func.restype = c_double
		return _func(JD)


class AAVSOP87A_Jupiter:
	@staticmethod
	def Jupiter_X(JD: float):
		_func = _aaplus.CAAVSOP87A_Jupiter_X
		_func.argtypes = [c_double]
		_func.restype = c_double
		return _func(JD)

	@staticmethod
	def Jupiter_X_DASH(JD: float):
		_func = _aaplus.CAAVSOP87A_Jupiter_X_DASH
		_func.argtypes = [c_double]
		_func.restype = c_double
		return _func(JD)

	@staticmethod
	def Jupiter_Y(JD: float):
		_func = _aaplus.CAAVSOP87A_Jupiter_Y
		_func.argtypes = [c_double]
		_func.restype = c_double
		return _func(JD)

	@staticmethod
	def Jupiter_Y_DASH(JD: float):
		_func = _aaplus.CAAVSOP87A_Jupiter_Y_DASH
		_func.argtypes = [c_double]
		_func.restype = c_double
		return _func(JD)

	@staticmethod
	def Jupiter_Z(JD: float):
		_func = _aaplus.CAAVSOP87A_Jupiter_Z
		_func.argtypes = [c_double]
		_func.restype = c_double
		return _func(JD)

	@staticmethod
	def Jupiter_Z_DASH(JD: float):
		_func = _aaplus.CAAVSOP87A_Jupiter_Z_DASH
		_func.argtypes = [c_double]
		_func.restype = c_double
		return _func(JD)


class AAVSOP87A_Mars:
	@staticmethod
	def Mars_X(JD: float):
		_func = _aaplus.CAAVSOP87A_Mars_X
		_func.argtypes = [c_double]
		_func.restype = c_double
		return _func(JD)

	@staticmethod
	def Mars_X_DASH(JD: float):
		_func = _aaplus.CAAVSOP87A_Mars_X_DASH
		_func.argtypes = [c_double]
		_func.restype = c_double
		return _func(JD)

	@staticmethod
	def Mars_Y(JD: float):
		_func = _aaplus.CAAVSOP87A_Mars_Y
		_func.argtypes = [c_double]
		_func.restype = c_double
		return _func(JD)

	@staticmethod
	def Mars_Y_DASH(JD: float):
		_func = _aaplus.CAAVSOP87A_Mars_Y_DASH
		_func.argtypes = [c_double]
		_func.restype = c_double
		return _func(JD)

	@staticmethod
	def Mars_Z(JD: float):
		_func = _aaplus.CAAVSOP87A_Mars_Z
		_func.argtypes = [c_double]
		_func.restype = c_double
		return _func(JD)

	@staticmethod
	def Mars_Z_DASH(JD: float):
		_func = _aaplus.CAAVSOP87A_Mars_Z_DASH
		_func.argtypes = [c_double]
		_func.restype = c_double
		return _func(JD)


class AAVSOP87A_Mercury:
	@staticmethod
	def Mercury_X(JD: float):
		_func = _aaplus.CAAVSOP87A_Mercury_X
		_func.argtypes = [c_double]
		_func.restype = c_double
		return _func(JD)

	@staticmethod
	def Mercury_X_DASH(JD: float):
		_func = _aaplus.CAAVSOP87A_Mercury_X_DASH
		_func.argtypes = [c_double]
		_func.restype = c_double
		return _func(JD)

	@staticmethod
	def Mercury_Y(JD: float):
		_func = _aaplus.CAAVSOP87A_Mercury_Y
		_func.argtypes = [c_double]
		_func.restype = c_double
		return _func(JD)

	@staticmethod
	def Mercury_Y_DASH(JD: float):
		_func = _aaplus.CAAVSOP87A_Mercury_Y_DASH
		_func.argtypes = [c_double]
		_func.restype = c_double
		return _func(JD)

	@staticmethod
	def Mercury_Z(JD: float):
		_func = _aaplus.CAAVSOP87A_Mercury_Z
		_func.argtypes = [c_double]
		_func.restype = c_double
		return _func(JD)

	@staticmethod
	def Mercury_Z_DASH(JD: float):
		_func = _aaplus.CAAVSOP87A_Mercury_Z_DASH
		_func.argtypes = [c_double]
		_func.restype = c_double
		return _func(JD)


class AAVSOP87A_Neptune:
	@staticmethod
	def Neptune_X(JD: float):
		_func = _aaplus.CAAVSOP87A_Neptune_X
		_func.argtypes = [c_double]
		_func.restype = c_double
		return _func(JD)

	@staticmethod
	def Neptune_X_DASH(JD: float):
		_func = _aaplus.CAAVSOP87A_Neptune_X_DASH
		_func.argtypes = [c_double]
		_func.restype = c_double
		return _func(JD)

	@staticmethod
	def Neptune_Y(JD: float):
		_func = _aaplus.CAAVSOP87A_Neptune_Y
		_func.argtypes = [c_double]
		_func.restype = c_double
		return _func(JD)

	@staticmethod
	def Neptune_Y_DASH(JD: float):
		_func = _aaplus.CAAVSOP87A_Neptune_Y_DASH
		_func.argtypes = [c_double]
		_func.restype = c_double
		return _func(JD)

	@staticmethod
	def Neptune_Z(JD: float):
		_func = _aaplus.CAAVSOP87A_Neptune_Z
		_func.argtypes = [c_double]
		_func.restype = c_double
		return _func(JD)

	@staticmethod
	def Neptune_Z_DASH(JD: float):
		_func = _aaplus.CAAVSOP87A_Neptune_Z_DASH
		_func.argtypes = [c_double]
		_func.restype = c_double
		return _func(JD)


class AAVSOP87A_Saturn:
	@staticmethod
	def Saturn_X(JD: float):
		_func = _aaplus.CAAVSOP87A_Saturn_X
		_func.argtypes = [c_double]
		_func.restype = c_double
		return _func(JD)

	@staticmethod
	def Saturn_X_DASH(JD: float):
		_func = _aaplus.CAAVSOP87A_Saturn_X_DASH
		_func.argtypes = [c_double]
		_func.restype = c_double
		return _func(JD)

	@staticmethod
	def Saturn_Y(JD: float):
		_func = _aaplus.CAAVSOP87A_Saturn_Y
		_func.argtypes = [c_double]
		_func.restype = c_double
		return _func(JD)

	@staticmethod
	def Saturn_Y_DASH(JD: float):
		_func = _aaplus.CAAVSOP87A_Saturn_Y_DASH
		_func.argtypes = [c_double]
		_func.restype = c_double
		return _func(JD)

	@staticmethod
	def Saturn_Z(JD: float):
		_func = _aaplus.CAAVSOP87A_Saturn_Z
		_func.argtypes = [c_double]
		_func.restype = c_double
		return _func(JD)

	@staticmethod
	def Saturn_Z_DASH(JD: float):
		_func = _aaplus.CAAVSOP87A_Saturn_Z_DASH
		_func.argtypes = [c_double]
		_func.restype = c_double
		return _func(JD)


class AAVSOP87A_Uranus:
	@staticmethod
	def Uranus_X(JD: float):
		_func = _aaplus.CAAVSOP87A_Uranus_X
		_func.argtypes = [c_double]
		_func.restype = c_double
		return _func(JD)

	@staticmethod
	def Uranus_X_DASH(JD: float):
		_func = _aaplus.CAAVSOP87A_Uranus_X_DASH
		_func.argtypes = [c_double]
		_func.restype = c_double
		return _func(JD)

	@staticmethod
	def Uranus_Y(JD: float):
		_func = _aaplus.CAAVSOP87A_Uranus_Y
		_func.argtypes = [c_double]
		_func.restype = c_double
		return _func(JD)

	@staticmethod
	def Uranus_Y_DASH(JD: float):
		_func = _aaplus.CAAVSOP87A_Uranus_Y_DASH
		_func.argtypes = [c_double]
		_func.restype = c_double
		return _func(JD)

	@staticmethod
	def Uranus_Z(JD: float):
		_func = _aaplus.CAAVSOP87A_Uranus_Z
		_func.argtypes = [c_double]
		_func.restype = c_double
		return _func(JD)

	@staticmethod
	def Uranus_Z_DASH(JD: float):
		_func = _aaplus.CAAVSOP87A_Uranus_Z_DASH
		_func.argtypes = [c_double]
		_func.restype = c_double
		return _func(JD)


class AAVSOP87A_Venus:
	@staticmethod
	def Venus_X(JD: float):
		_func = _aaplus.CAAVSOP87A_Venus_X
		_func.argtypes = [c_double]
		_func.restype = c_double
		return _func(JD)

	@staticmethod
	def Venus_X_DASH(JD: float):
		_func = _aaplus.CAAVSOP87A_Venus_X_DASH
		_func.argtypes = [c_double]
		_func.restype = c_double
		return _func(JD)

	@staticmethod
	def Venus_Y(JD: float):
		_func = _aaplus.CAAVSOP87A_Venus_Y
		_func.argtypes = [c_double]
		_func.restype = c_double
		return _func(JD)

	@staticmethod
	def Venus_Y_DASH(JD: float):
		_func = _aaplus.CAAVSOP87A_Venus_Y_DASH
		_func.argtypes = [c_double]
		_func.restype = c_double
		return _func(JD)

	@staticmethod
	def Venus_Z(JD: float):
		_func = _aaplus.CAAVSOP87A_Venus_Z
		_func.argtypes = [c_double]
		_func.restype = c_double
		return _func(JD)

	@staticmethod
	def Venus_Z_DASH(JD: float):
		_func = _aaplus.CAAVSOP87A_Venus_Z_DASH
		_func.argtypes = [c_double]
		_func.restype = c_double
		return _func(JD)


class AAVSOP87B_Earth:
	@staticmethod
	def Earth_L(JD: float):
		_func = _aaplus.CAAVSOP87B_Earth_L
		_func.argtypes = [c_double]
		_func.restype = c_double
		return _func(JD)

	@staticmethod
	def Earth_L_DASH(JD: float):
		_func = _aaplus.CAAVSOP87B_Earth_L_DASH
		_func.argtypes = [c_double]
		_func.restype = c_double
		return _func(JD)

	@staticmethod
	def Earth_B(JD: float):
		_func = _aaplus.CAAVSOP87B_Earth_B
		_func.argtypes = [c_double]
		_func.restype = c_double
		return _func(JD)

	@staticmethod
	def Earth_B_DASH(JD: float):
		_func = _aaplus.CAAVSOP87B_Earth_B_DASH
		_func.argtypes = [c_double]
		_func.restype = c_double
		return _func(JD)

	@staticmethod
	def Earth_R(JD: float):
		_func = _aaplus.CAAVSOP87B_Earth_R
		_func.argtypes = [c_double]
		_func.restype = c_double
		return _func(JD)

	@staticmethod
	def Earth_R_DASH(JD: float):
		_func = _aaplus.CAAVSOP87B_Earth_R_DASH
		_func.argtypes = [c_double]
		_func.restype = c_double
		return _func(JD)


class AAVSOP87B_Jupiter:
	@staticmethod
	def Jupiter_L(JD: float):
		_func = _aaplus.CAAVSOP87B_Jupiter_L
		_func.argtypes = [c_double]
		_func.restype = c_double
		return _func(JD)

	@staticmethod
	def Jupiter_L_DASH(JD: float):
		_func = _aaplus.CAAVSOP87B_Jupiter_L_DASH
		_func.argtypes = [c_double]
		_func.restype = c_double
		return _func(JD)

	@staticmethod
	def Jupiter_B(JD: float):
		_func = _aaplus.CAAVSOP87B_Jupiter_B
		_func.argtypes = [c_double]
		_func.restype = c_double
		return _func(JD)

	@staticmethod
	def Jupiter_B_DASH(JD: float):
		_func = _aaplus.CAAVSOP87B_Jupiter_B_DASH
		_func.argtypes = [c_double]
		_func.restype = c_double
		return _func(JD)

	@staticmethod
	def Jupiter_R(JD: float):
		_func = _aaplus.CAAVSOP87B_Jupiter_R
		_func.argtypes = [c_double]
		_func.restype = c_double
		return _func(JD)

	@staticmethod
	def Jupiter_R_DASH(JD: float):
		_func = _aaplus.CAAVSOP87B_Jupiter_R_DASH
		_func.argtypes = [c_double]
		_func.restype = c_double
		return _func(JD)


class AAVSOP87B_Mars:
	@staticmethod
	def Mars_L(JD: float):
		_func = _aaplus.CAAVSOP87B_Mars_L
		_func.argtypes = [c_double]
		_func.restype = c_double
		return _func(JD)

	@staticmethod
	def Mars_L_DASH(JD: float):
		_func = _aaplus.CAAVSOP87B_Mars_L_DASH
		_func.argtypes = [c_double]
		_func.restype = c_double
		return _func(JD)

	@staticmethod
	def Mars_B(JD: float):
		_func = _aaplus.CAAVSOP87B_Mars_B
		_func.argtypes = [c_double]
		_func.restype = c_double
		return _func(JD)

	@staticmethod
	def Mars_B_DASH(JD: float):
		_func = _aaplus.CAAVSOP87B_Mars_B_DASH
		_func.argtypes = [c_double]
		_func.restype = c_double
		return _func(JD)

	@staticmethod
	def Mars_R(JD: float):
		_func = _aaplus.CAAVSOP87B_Mars_R
		_func.argtypes = [c_double]
		_func.restype = c_double
		return _func(JD)

	@staticmethod
	def Mars_R_DASH(JD: float):
		_func = _aaplus.CAAVSOP87B_Mars_R_DASH
		_func.argtypes = [c_double]
		_func.restype = c_double
		return _func(JD)


class AAVSOP87B_Mercury:
	@staticmethod
	def Mercury_L(JD: float):
		_func = _aaplus.CAAVSOP87B_Mercury_L
		_func.argtypes = [c_double]
		_func.restype = c_double
		return _func(JD)

	@staticmethod
	def Mercury_L_DASH(JD: float):
		_func = _aaplus.CAAVSOP87B_Mercury_L_DASH
		_func.argtypes = [c_double]
		_func.restype = c_double
		return _func(JD)

	@staticmethod
	def Mercury_B(JD: float):
		_func = _aaplus.CAAVSOP87B_Mercury_B
		_func.argtypes = [c_double]
		_func.restype = c_double
		return _func(JD)

	@staticmethod
	def Mercury_B_DASH(JD: float):
		_func = _aaplus.CAAVSOP87B_Mercury_B_DASH
		_func.argtypes = [c_double]
		_func.restype = c_double
		return _func(JD)

	@staticmethod
	def Mercury_R(JD: float):
		_func = _aaplus.CAAVSOP87B_Mercury_R
		_func.argtypes = [c_double]
		_func.restype = c_double
		return _func(JD)

	@staticmethod
	def Mercury_R_DASH(JD: float):
		_func = _aaplus.CAAVSOP87B_Mercury_R_DASH
		_func.argtypes = [c_double]
		_func.restype = c_double
		return _func(JD)


class AAVSOP87B_Neptune:
	@staticmethod
	def Neptune_L(JD: float):
		_func = _aaplus.CAAVSOP87B_Neptune_L
		_func.argtypes = [c_double]
		_func.restype = c_double
		return _func(JD)

	@staticmethod
	def Neptune_L_DASH(JD: float):
		_func = _aaplus.CAAVSOP87B_Neptune_L_DASH
		_func.argtypes = [c_double]
		_func.restype = c_double
		return _func(JD)

	@staticmethod
	def Neptune_B(JD: float):
		_func = _aaplus.CAAVSOP87B_Neptune_B
		_func.argtypes = [c_double]
		_func.restype = c_double
		return _func(JD)

	@staticmethod
	def Neptune_B_DASH(JD: float):
		_func = _aaplus.CAAVSOP87B_Neptune_B_DASH
		_func.argtypes = [c_double]
		_func.restype = c_double
		return _func(JD)

	@staticmethod
	def Neptune_R(JD: float):
		_func = _aaplus.CAAVSOP87B_Neptune_R
		_func.argtypes = [c_double]
		_func.restype = c_double
		return _func(JD)

	@staticmethod
	def Neptune_R_DASH(JD: float):
		_func = _aaplus.CAAVSOP87B_Neptune_R_DASH
		_func.argtypes = [c_double]
		_func.restype = c_double
		return _func(JD)


class AAVSOP87B_Saturn:
	@staticmethod
	def Saturn_L(JD: float):
		_func = _aaplus.CAAVSOP87B_Saturn_L
		_func.argtypes = [c_double]
		_func.restype = c_double
		return _func(JD)

	@staticmethod
	def Saturn_L_DASH(JD: float):
		_func = _aaplus.CAAVSOP87B_Saturn_L_DASH
		_func.argtypes = [c_double]
		_func.restype = c_double
		return _func(JD)

	@staticmethod
	def Saturn_B(JD: float):
		_func = _aaplus.CAAVSOP87B_Saturn_B
		_func.argtypes = [c_double]
		_func.restype = c_double
		return _func(JD)

	@staticmethod
	def Saturn_B_DASH(JD: float):
		_func = _aaplus.CAAVSOP87B_Saturn_B_DASH
		_func.argtypes = [c_double]
		_func.restype = c_double
		return _func(JD)

	@staticmethod
	def Saturn_R(JD: float):
		_func = _aaplus.CAAVSOP87B_Saturn_R
		_func.argtypes = [c_double]
		_func.restype = c_double
		return _func(JD)

	@staticmethod
	def Saturn_R_DASH(JD: float):
		_func = _aaplus.CAAVSOP87B_Saturn_R_DASH
		_func.argtypes = [c_double]
		_func.restype = c_double
		return _func(JD)


class AAVSOP87B_Uranus:
	@staticmethod
	def Uranus_L(JD: float):
		_func = _aaplus.CAAVSOP87B_Uranus_L
		_func.argtypes = [c_double]
		_func.restype = c_double
		return _func(JD)

	@staticmethod
	def Uranus_L_DASH(JD: float):
		_func = _aaplus.CAAVSOP87B_Uranus_L_DASH
		_func.argtypes = [c_double]
		_func.restype = c_double
		return _func(JD)

	@staticmethod
	def Uranus_B(JD: float):
		_func = _aaplus.CAAVSOP87B_Uranus_B
		_func.argtypes = [c_double]
		_func.restype = c_double
		return _func(JD)

	@staticmethod
	def Uranus_B_DASH(JD: float):
		_func = _aaplus.CAAVSOP87B_Uranus_B_DASH
		_func.argtypes = [c_double]
		_func.restype = c_double
		return _func(JD)

	@staticmethod
	def Uranus_R(JD: float):
		_func = _aaplus.CAAVSOP87B_Uranus_R
		_func.argtypes = [c_double]
		_func.restype = c_double
		return _func(JD)

	@staticmethod
	def Uranus_R_DASH(JD: float):
		_func = _aaplus.CAAVSOP87B_Uranus_R_DASH
		_func.argtypes = [c_double]
		_func.restype = c_double
		return _func(JD)


class AAVSOP87B_Venus:
	@staticmethod
	def Venus_L(JD: float):
		_func = _aaplus.CAAVSOP87B_Venus_L
		_func.argtypes = [c_double]
		_func.restype = c_double
		return _func(JD)

	@staticmethod
	def Venus_L_DASH(JD: float):
		_func = _aaplus.CAAVSOP87B_Venus_L_DASH
		_func.argtypes = [c_double]
		_func.restype = c_double
		return _func(JD)

	@staticmethod
	def Venus_B(JD: float):
		_func = _aaplus.CAAVSOP87B_Venus_B
		_func.argtypes = [c_double]
		_func.restype = c_double
		return _func(JD)

	@staticmethod
	def Venus_B_DASH(JD: float):
		_func = _aaplus.CAAVSOP87B_Venus_B_DASH
		_func.argtypes = [c_double]
		_func.restype = c_double
		return _func(JD)

	@staticmethod
	def Venus_R(JD: float):
		_func = _aaplus.CAAVSOP87B_Venus_R
		_func.argtypes = [c_double]
		_func.restype = c_double
		return _func(JD)

	@staticmethod
	def Venus_R_DASH(JD: float):
		_func = _aaplus.CAAVSOP87B_Venus_R_DASH
		_func.argtypes = [c_double]
		_func.restype = c_double
		return _func(JD)


class AAVSOP87C_Earth:
	@staticmethod
	def Earth_X(JD: float):
		_func = _aaplus.CAAVSOP87C_Earth_X
		_func.argtypes = [c_double]
		_func.restype = c_double
		return _func(JD)

	@staticmethod
	def Earth_X_DASH(JD: float):
		_func = _aaplus.CAAVSOP87C_Earth_X_DASH
		_func.argtypes = [c_double]
		_func.restype = c_double
		return _func(JD)

	@staticmethod
	def Earth_Y(JD: float):
		_func = _aaplus.CAAVSOP87C_Earth_Y
		_func.argtypes = [c_double]
		_func.restype = c_double
		return _func(JD)

	@staticmethod
	def Earth_Y_DASH(JD: float):
		_func = _aaplus.CAAVSOP87C_Earth_Y_DASH
		_func.argtypes = [c_double]
		_func.restype = c_double
		return _func(JD)

	@staticmethod
	def Earth_Z(JD: float):
		_func = _aaplus.CAAVSOP87C_Earth_Z
		_func.argtypes = [c_double]
		_func.restype = c_double
		return _func(JD)

	@staticmethod
	def Earth_Z_DASH(JD: float):
		_func = _aaplus.CAAVSOP87C_Earth_Z_DASH
		_func.argtypes = [c_double]
		_func.restype = c_double
		return _func(JD)


class AAVSOP87C_Jupiter:
	@staticmethod
	def Jupiter_X(JD: float):
		_func = _aaplus.CAAVSOP87C_Jupiter_X
		_func.argtypes = [c_double]
		_func.restype = c_double
		return _func(JD)

	@staticmethod
	def Jupiter_X_DASH(JD: float):
		_func = _aaplus.CAAVSOP87C_Jupiter_X_DASH
		_func.argtypes = [c_double]
		_func.restype = c_double
		return _func(JD)

	@staticmethod
	def Jupiter_Y(JD: float):
		_func = _aaplus.CAAVSOP87C_Jupiter_Y
		_func.argtypes = [c_double]
		_func.restype = c_double
		return _func(JD)

	@staticmethod
	def Jupiter_Y_DASH(JD: float):
		_func = _aaplus.CAAVSOP87C_Jupiter_Y_DASH
		_func.argtypes = [c_double]
		_func.restype = c_double
		return _func(JD)

	@staticmethod
	def Jupiter_Z(JD: float):
		_func = _aaplus.CAAVSOP87C_Jupiter_Z
		_func.argtypes = [c_double]
		_func.restype = c_double
		return _func(JD)

	@staticmethod
	def Jupiter_Z_DASH(JD: float):
		_func = _aaplus.CAAVSOP87C_Jupiter_Z_DASH
		_func.argtypes = [c_double]
		_func.restype = c_double
		return _func(JD)


class AAVSOP87C_Mars:
	@staticmethod
	def Mars_X(JD: float):
		_func = _aaplus.CAAVSOP87C_Mars_X
		_func.argtypes = [c_double]
		_func.restype = c_double
		return _func(JD)

	@staticmethod
	def Mars_X_DASH(JD: float):
		_func = _aaplus.CAAVSOP87C_Mars_X_DASH
		_func.argtypes = [c_double]
		_func.restype = c_double
		return _func(JD)

	@staticmethod
	def Mars_Y(JD: float):
		_func = _aaplus.CAAVSOP87C_Mars_Y
		_func.argtypes = [c_double]
		_func.restype = c_double
		return _func(JD)

	@staticmethod
	def Mars_Y_DASH(JD: float):
		_func = _aaplus.CAAVSOP87C_Mars_Y_DASH
		_func.argtypes = [c_double]
		_func.restype = c_double
		return _func(JD)

	@staticmethod
	def Mars_Z(JD: float):
		_func = _aaplus.CAAVSOP87C_Mars_Z
		_func.argtypes = [c_double]
		_func.restype = c_double
		return _func(JD)

	@staticmethod
	def Mars_Z_DASH(JD: float):
		_func = _aaplus.CAAVSOP87C_Mars_Z_DASH
		_func.argtypes = [c_double]
		_func.restype = c_double
		return _func(JD)


class AAVSOP87C_Mercury:
	@staticmethod
	def Mercury_X(JD: float):
		_func = _aaplus.CAAVSOP87C_Mercury_X
		_func.argtypes = [c_double]
		_func.restype = c_double
		return _func(JD)

	@staticmethod
	def Mercury_X_DASH(JD: float):
		_func = _aaplus.CAAVSOP87C_Mercury_X_DASH
		_func.argtypes = [c_double]
		_func.restype = c_double
		return _func(JD)

	@staticmethod
	def Mercury_Y(JD: float):
		_func = _aaplus.CAAVSOP87C_Mercury_Y
		_func.argtypes = [c_double]
		_func.restype = c_double
		return _func(JD)

	@staticmethod
	def Mercury_Y_DASH(JD: float):
		_func = _aaplus.CAAVSOP87C_Mercury_Y_DASH
		_func.argtypes = [c_double]
		_func.restype = c_double
		return _func(JD)

	@staticmethod
	def Mercury_Z(JD: float):
		_func = _aaplus.CAAVSOP87C_Mercury_Z
		_func.argtypes = [c_double]
		_func.restype = c_double
		return _func(JD)

	@staticmethod
	def Mercury_Z_DASH(JD: float):
		_func = _aaplus.CAAVSOP87C_Mercury_Z_DASH
		_func.argtypes = [c_double]
		_func.restype = c_double
		return _func(JD)


class AAVSOP87C_Neptune:
	@staticmethod
	def Neptune_X(JD: float):
		_func = _aaplus.CAAVSOP87C_Neptune_X
		_func.argtypes = [c_double]
		_func.restype = c_double
		return _func(JD)

	@staticmethod
	def Neptune_X_DASH(JD: float):
		_func = _aaplus.CAAVSOP87C_Neptune_X_DASH
		_func.argtypes = [c_double]
		_func.restype = c_double
		return _func(JD)

	@staticmethod
	def Neptune_Y(JD: float):
		_func = _aaplus.CAAVSOP87C_Neptune_Y
		_func.argtypes = [c_double]
		_func.restype = c_double
		return _func(JD)

	@staticmethod
	def Neptune_Y_DASH(JD: float):
		_func = _aaplus.CAAVSOP87C_Neptune_Y_DASH
		_func.argtypes = [c_double]
		_func.restype = c_double
		return _func(JD)

	@staticmethod
	def Neptune_Z(JD: float):
		_func = _aaplus.CAAVSOP87C_Neptune_Z
		_func.argtypes = [c_double]
		_func.restype = c_double
		return _func(JD)

	@staticmethod
	def Neptune_Z_DASH(JD: float):
		_func = _aaplus.CAAVSOP87C_Neptune_Z_DASH
		_func.argtypes = [c_double]
		_func.restype = c_double
		return _func(JD)


class AAVSOP87C_Saturn:
	@staticmethod
	def Saturn_X(JD: float):
		_func = _aaplus.CAAVSOP87C_Saturn_X
		_func.argtypes = [c_double]
		_func.restype = c_double
		return _func(JD)

	@staticmethod
	def Saturn_X_DASH(JD: float):
		_func = _aaplus.CAAVSOP87C_Saturn_X_DASH
		_func.argtypes = [c_double]
		_func.restype = c_double
		return _func(JD)

	@staticmethod
	def Saturn_Y(JD: float):
		_func = _aaplus.CAAVSOP87C_Saturn_Y
		_func.argtypes = [c_double]
		_func.restype = c_double
		return _func(JD)

	@staticmethod
	def Saturn_Y_DASH(JD: float):
		_func = _aaplus.CAAVSOP87C_Saturn_Y_DASH
		_func.argtypes = [c_double]
		_func.restype = c_double
		return _func(JD)

	@staticmethod
	def Saturn_Z(JD: float):
		_func = _aaplus.CAAVSOP87C_Saturn_Z
		_func.argtypes = [c_double]
		_func.restype = c_double
		return _func(JD)

	@staticmethod
	def Saturn_Z_DASH(JD: float):
		_func = _aaplus.CAAVSOP87C_Saturn_Z_DASH
		_func.argtypes = [c_double]
		_func.restype = c_double
		return _func(JD)


class AAVSOP87C_Uranus:
	@staticmethod
	def Uranus_X(JD: float):
		_func = _aaplus.CAAVSOP87C_Uranus_X
		_func.argtypes = [c_double]
		_func.restype = c_double
		return _func(JD)

	@staticmethod
	def Uranus_X_DASH(JD: float):
		_func = _aaplus.CAAVSOP87C_Uranus_X_DASH
		_func.argtypes = [c_double]
		_func.restype = c_double
		return _func(JD)

	@staticmethod
	def Uranus_Y(JD: float):
		_func = _aaplus.CAAVSOP87C_Uranus_Y
		_func.argtypes = [c_double]
		_func.restype = c_double
		return _func(JD)

	@staticmethod
	def Uranus_Y_DASH(JD: float):
		_func = _aaplus.CAAVSOP87C_Uranus_Y_DASH
		_func.argtypes = [c_double]
		_func.restype = c_double
		return _func(JD)

	@staticmethod
	def Uranus_Z(JD: float):
		_func = _aaplus.CAAVSOP87C_Uranus_Z
		_func.argtypes = [c_double]
		_func.restype = c_double
		return _func(JD)

	@staticmethod
	def Uranus_Z_DASH(JD: float):
		_func = _aaplus.CAAVSOP87C_Uranus_Z_DASH
		_func.argtypes = [c_double]
		_func.restype = c_double
		return _func(JD)


class AAVSOP87C_Venus:
	@staticmethod
	def Venus_X(JD: float):
		_func = _aaplus.CAAVSOP87C_Venus_X
		_func.argtypes = [c_double]
		_func.restype = c_double
		return _func(JD)

	@staticmethod
	def Venus_X_DASH(JD: float):
		_func = _aaplus.CAAVSOP87C_Venus_X_DASH
		_func.argtypes = [c_double]
		_func.restype = c_double
		return _func(JD)

	@staticmethod
	def Venus_Y(JD: float):
		_func = _aaplus.CAAVSOP87C_Venus_Y
		_func.argtypes = [c_double]
		_func.restype = c_double
		return _func(JD)

	@staticmethod
	def Venus_Y_DASH(JD: float):
		_func = _aaplus.CAAVSOP87C_Venus_Y_DASH
		_func.argtypes = [c_double]
		_func.restype = c_double
		return _func(JD)

	@staticmethod
	def Venus_Z(JD: float):
		_func = _aaplus.CAAVSOP87C_Venus_Z
		_func.argtypes = [c_double]
		_func.restype = c_double
		return _func(JD)

	@staticmethod
	def Venus_Z_DASH(JD: float):
		_func = _aaplus.CAAVSOP87C_Venus_Z_DASH
		_func.argtypes = [c_double]
		_func.restype = c_double
		return _func(JD)


class AAVSOP87D_Earth:
	@staticmethod
	def Earth_L(JD: float):
		_func = _aaplus.CAAVSOP87D_Earth_L
		_func.argtypes = [c_double]
		_func.restype = c_double
		return _func(JD)

	@staticmethod
	def Earth_L_DASH(JD: float):
		_func = _aaplus.CAAVSOP87D_Earth_L_DASH
		_func.argtypes = [c_double]
		_func.restype = c_double
		return _func(JD)

	@staticmethod
	def Earth_B(JD: float):
		_func = _aaplus.CAAVSOP87D_Earth_B
		_func.argtypes = [c_double]
		_func.restype = c_double
		return _func(JD)

	@staticmethod
	def Earth_B_DASH(JD: float):
		_func = _aaplus.CAAVSOP87D_Earth_B_DASH
		_func.argtypes = [c_double]
		_func.restype = c_double
		return _func(JD)

	@staticmethod
	def Earth_R(JD: float):
		_func = _aaplus.CAAVSOP87D_Earth_R
		_func.argtypes = [c_double]
		_func.restype = c_double
		return _func(JD)

	@staticmethod
	def Earth_R_DASH(JD: float):
		_func = _aaplus.CAAVSOP87D_Earth_R_DASH
		_func.argtypes = [c_double]
		_func.restype = c_double
		return _func(JD)


class AAVSOP87D_Jupiter:
	@staticmethod
	def Jupiter_L(JD: float):
		_func = _aaplus.CAAVSOP87D_Jupiter_L
		_func.argtypes = [c_double]
		_func.restype = c_double
		return _func(JD)

	@staticmethod
	def Jupiter_L_DASH(JD: float):
		_func = _aaplus.CAAVSOP87D_Jupiter_L_DASH
		_func.argtypes = [c_double]
		_func.restype = c_double
		return _func(JD)

	@staticmethod
	def Jupiter_B(JD: float):
		_func = _aaplus.CAAVSOP87D_Jupiter_B
		_func.argtypes = [c_double]
		_func.restype = c_double
		return _func(JD)

	@staticmethod
	def Jupiter_B_DASH(JD: float):
		_func = _aaplus.CAAVSOP87D_Jupiter_B_DASH
		_func.argtypes = [c_double]
		_func.restype = c_double
		return _func(JD)

	@staticmethod
	def Jupiter_R(JD: float):
		_func = _aaplus.CAAVSOP87D_Jupiter_R
		_func.argtypes = [c_double]
		_func.restype = c_double
		return _func(JD)

	@staticmethod
	def Jupiter_R_DASH(JD: float):
		_func = _aaplus.CAAVSOP87D_Jupiter_R_DASH
		_func.argtypes = [c_double]
		_func.restype = c_double
		return _func(JD)


class AAVSOP87D_Mars:
	@staticmethod
	def Mars_L(JD: float):
		_func = _aaplus.CAAVSOP87D_Mars_L
		_func.argtypes = [c_double]
		_func.restype = c_double
		return _func(JD)

	@staticmethod
	def Mars_L_DASH(JD: float):
		_func = _aaplus.CAAVSOP87D_Mars_L_DASH
		_func.argtypes = [c_double]
		_func.restype = c_double
		return _func(JD)

	@staticmethod
	def Mars_B(JD: float):
		_func = _aaplus.CAAVSOP87D_Mars_B
		_func.argtypes = [c_double]
		_func.restype = c_double
		return _func(JD)

	@staticmethod
	def Mars_B_DASH(JD: float):
		_func = _aaplus.CAAVSOP87D_Mars_B_DASH
		_func.argtypes = [c_double]
		_func.restype = c_double
		return _func(JD)

	@staticmethod
	def Mars_R(JD: float):
		_func = _aaplus.CAAVSOP87D_Mars_R
		_func.argtypes = [c_double]
		_func.restype = c_double
		return _func(JD)

	@staticmethod
	def Mars_R_DASH(JD: float):
		_func = _aaplus.CAAVSOP87D_Mars_R_DASH
		_func.argtypes = [c_double]
		_func.restype = c_double
		return _func(JD)


class AAVSOP87D_Mercury:
	@staticmethod
	def Mercury_L(JD: float):
		_func = _aaplus.CAAVSOP87D_Mercury_L
		_func.argtypes = [c_double]
		_func.restype = c_double
		return _func(JD)

	@staticmethod
	def Mercury_L_DASH(JD: float):
		_func = _aaplus.CAAVSOP87D_Mercury_L_DASH
		_func.argtypes = [c_double]
		_func.restype = c_double
		return _func(JD)

	@staticmethod
	def Mercury_B(JD: float):
		_func = _aaplus.CAAVSOP87D_Mercury_B
		_func.argtypes = [c_double]
		_func.restype = c_double
		return _func(JD)

	@staticmethod
	def Mercury_B_DASH(JD: float):
		_func = _aaplus.CAAVSOP87D_Mercury_B_DASH
		_func.argtypes = [c_double]
		_func.restype = c_double
		return _func(JD)

	@staticmethod
	def Mercury_R(JD: float):
		_func = _aaplus.CAAVSOP87D_Mercury_R
		_func.argtypes = [c_double]
		_func.restype = c_double
		return _func(JD)

	@staticmethod
	def Mercury_R_DASH(JD: float):
		_func = _aaplus.CAAVSOP87D_Mercury_R_DASH
		_func.argtypes = [c_double]
		_func.restype = c_double
		return _func(JD)


class AAVSOP87D_Neptune:
	@staticmethod
	def Neptune_L(JD: float):
		_func = _aaplus.CAAVSOP87D_Neptune_L
		_func.argtypes = [c_double]
		_func.restype = c_double
		return _func(JD)

	@staticmethod
	def Neptune_L_DASH(JD: float):
		_func = _aaplus.CAAVSOP87D_Neptune_L_DASH
		_func.argtypes = [c_double]
		_func.restype = c_double
		return _func(JD)

	@staticmethod
	def Neptune_B(JD: float):
		_func = _aaplus.CAAVSOP87D_Neptune_B
		_func.argtypes = [c_double]
		_func.restype = c_double
		return _func(JD)

	@staticmethod
	def Neptune_B_DASH(JD: float):
		_func = _aaplus.CAAVSOP87D_Neptune_B_DASH
		_func.argtypes = [c_double]
		_func.restype = c_double
		return _func(JD)

	@staticmethod
	def Neptune_R(JD: float):
		_func = _aaplus.CAAVSOP87D_Neptune_R
		_func.argtypes = [c_double]
		_func.restype = c_double
		return _func(JD)

	@staticmethod
	def Neptune_R_DASH(JD: float):
		_func = _aaplus.CAAVSOP87D_Neptune_R_DASH
		_func.argtypes = [c_double]
		_func.restype = c_double
		return _func(JD)


class AAVSOP87D_Saturn:
	@staticmethod
	def Saturn_L(JD: float):
		_func = _aaplus.CAAVSOP87D_Saturn_L
		_func.argtypes = [c_double]
		_func.restype = c_double
		return _func(JD)

	@staticmethod
	def Saturn_L_DASH(JD: float):
		_func = _aaplus.CAAVSOP87D_Saturn_L_DASH
		_func.argtypes = [c_double]
		_func.restype = c_double
		return _func(JD)

	@staticmethod
	def Saturn_B(JD: float):
		_func = _aaplus.CAAVSOP87D_Saturn_B
		_func.argtypes = [c_double]
		_func.restype = c_double
		return _func(JD)

	@staticmethod
	def Saturn_B_DASH(JD: float):
		_func = _aaplus.CAAVSOP87D_Saturn_B_DASH
		_func.argtypes = [c_double]
		_func.restype = c_double
		return _func(JD)

	@staticmethod
	def Saturn_R(JD: float):
		_func = _aaplus.CAAVSOP87D_Saturn_R
		_func.argtypes = [c_double]
		_func.restype = c_double
		return _func(JD)

	@staticmethod
	def Saturn_R_DASH(JD: float):
		_func = _aaplus.CAAVSOP87D_Saturn_R_DASH
		_func.argtypes = [c_double]
		_func.restype = c_double
		return _func(JD)


class AAVSOP87D_Uranus:
	@staticmethod
	def Uranus_L(JD: float):
		_func = _aaplus.CAAVSOP87D_Uranus_L
		_func.argtypes = [c_double]
		_func.restype = c_double
		return _func(JD)

	@staticmethod
	def Uranus_L_DASH(JD: float):
		_func = _aaplus.CAAVSOP87D_Uranus_L_DASH
		_func.argtypes = [c_double]
		_func.restype = c_double
		return _func(JD)

	@staticmethod
	def Uranus_B(JD: float):
		_func = _aaplus.CAAVSOP87D_Uranus_B
		_func.argtypes = [c_double]
		_func.restype = c_double
		return _func(JD)

	@staticmethod
	def Uranus_B_DASH(JD: float):
		_func = _aaplus.CAAVSOP87D_Uranus_B_DASH
		_func.argtypes = [c_double]
		_func.restype = c_double
		return _func(JD)

	@staticmethod
	def Uranus_R(JD: float):
		_func = _aaplus.CAAVSOP87D_Uranus_R
		_func.argtypes = [c_double]
		_func.restype = c_double
		return _func(JD)

	@staticmethod
	def Uranus_R_DASH(JD: float):
		_func = _aaplus.CAAVSOP87D_Uranus_R_DASH
		_func.argtypes = [c_double]
		_func.restype = c_double
		return _func(JD)


class AAVSOP87D_Venus:
	@staticmethod
	def Venus_L(JD: float):
		_func = _aaplus.CAAVSOP87D_Venus_L
		_func.argtypes = [c_double]
		_func.restype = c_double
		return _func(JD)

	@staticmethod
	def Venus_L_DASH(JD: float):
		_func = _aaplus.CAAVSOP87D_Venus_L_DASH
		_func.argtypes = [c_double]
		_func.restype = c_double
		return _func(JD)

	@staticmethod
	def Venus_B(JD: float):
		_func = _aaplus.CAAVSOP87D_Venus_B
		_func.argtypes = [c_double]
		_func.restype = c_double
		return _func(JD)

	@staticmethod
	def Venus_B_DASH(JD: float):
		_func = _aaplus.CAAVSOP87D_Venus_B_DASH
		_func.argtypes = [c_double]
		_func.restype = c_double
		return _func(JD)

	@staticmethod
	def Venus_R(JD: float):
		_func = _aaplus.CAAVSOP87D_Venus_R
		_func.argtypes = [c_double]
		_func.restype = c_double
		return _func(JD)

	@staticmethod
	def Venus_R_DASH(JD: float):
		_func = _aaplus.CAAVSOP87D_Venus_R_DASH
		_func.argtypes = [c_double]
		_func.restype = c_double
		return _func(JD)


class AAVSOP87E_Earth:
	@staticmethod
	def Earth_X(JD: float):
		_func = _aaplus.CAAVSOP87E_Earth_X
		_func.argtypes = [c_double]
		_func.restype = c_double
		return _func(JD)

	@staticmethod
	def Earth_X_DASH(JD: float):
		_func = _aaplus.CAAVSOP87E_Earth_X_DASH
		_func.argtypes = [c_double]
		_func.restype = c_double
		return _func(JD)

	@staticmethod
	def Earth_Y(JD: float):
		_func = _aaplus.CAAVSOP87E_Earth_Y
		_func.argtypes = [c_double]
		_func.restype = c_double
		return _func(JD)

	@staticmethod
	def Earth_Y_DASH(JD: float):
		_func = _aaplus.CAAVSOP87E_Earth_Y_DASH
		_func.argtypes = [c_double]
		_func.restype = c_double
		return _func(JD)

	@staticmethod
	def Earth_Z(JD: float):
		_func = _aaplus.CAAVSOP87E_Earth_Z
		_func.argtypes = [c_double]
		_func.restype = c_double
		return _func(JD)

	@staticmethod
	def Earth_Z_DASH(JD: float):
		_func = _aaplus.CAAVSOP87E_Earth_Z_DASH
		_func.argtypes = [c_double]
		_func.restype = c_double
		return _func(JD)


class AAVSOP87E_Jupiter:
	@staticmethod
	def Jupiter_X(JD: float):
		_func = _aaplus.CAAVSOP87E_Jupiter_X
		_func.argtypes = [c_double]
		_func.restype = c_double
		return _func(JD)

	@staticmethod
	def Jupiter_X_DASH(JD: float):
		_func = _aaplus.CAAVSOP87E_Jupiter_X_DASH
		_func.argtypes = [c_double]
		_func.restype = c_double
		return _func(JD)

	@staticmethod
	def Jupiter_Y(JD: float):
		_func = _aaplus.CAAVSOP87E_Jupiter_Y
		_func.argtypes = [c_double]
		_func.restype = c_double
		return _func(JD)

	@staticmethod
	def Jupiter_Y_DASH(JD: float):
		_func = _aaplus.CAAVSOP87E_Jupiter_Y_DASH
		_func.argtypes = [c_double]
		_func.restype = c_double
		return _func(JD)

	@staticmethod
	def Jupiter_Z(JD: float):
		_func = _aaplus.CAAVSOP87E_Jupiter_Z
		_func.argtypes = [c_double]
		_func.restype = c_double
		return _func(JD)

	@staticmethod
	def Jupiter_Z_DASH(JD: float):
		_func = _aaplus.CAAVSOP87E_Jupiter_Z_DASH
		_func.argtypes = [c_double]
		_func.restype = c_double
		return _func(JD)


class AAVSOP87E_Mars:
	@staticmethod
	def Mars_X(JD: float):
		_func = _aaplus.CAAVSOP87E_Mars_X
		_func.argtypes = [c_double]
		_func.restype = c_double
		return _func(JD)

	@staticmethod
	def Mars_X_DASH(JD: float):
		_func = _aaplus.CAAVSOP87E_Mars_X_DASH
		_func.argtypes = [c_double]
		_func.restype = c_double
		return _func(JD)

	@staticmethod
	def Mars_Y(JD: float):
		_func = _aaplus.CAAVSOP87E_Mars_Y
		_func.argtypes = [c_double]
		_func.restype = c_double
		return _func(JD)

	@staticmethod
	def Mars_Y_DASH(JD: float):
		_func = _aaplus.CAAVSOP87E_Mars_Y_DASH
		_func.argtypes = [c_double]
		_func.restype = c_double
		return _func(JD)

	@staticmethod
	def Mars_Z(JD: float):
		_func = _aaplus.CAAVSOP87E_Mars_Z
		_func.argtypes = [c_double]
		_func.restype = c_double
		return _func(JD)

	@staticmethod
	def Mars_Z_DASH(JD: float):
		_func = _aaplus.CAAVSOP87E_Mars_Z_DASH
		_func.argtypes = [c_double]
		_func.restype = c_double
		return _func(JD)


class AAVSOP87E_Mercury:
	@staticmethod
	def Mercury_X(JD: float):
		_func = _aaplus.CAAVSOP87E_Mercury_X
		_func.argtypes = [c_double]
		_func.restype = c_double
		return _func(JD)

	@staticmethod
	def Mercury_X_DASH(JD: float):
		_func = _aaplus.CAAVSOP87E_Mercury_X_DASH
		_func.argtypes = [c_double]
		_func.restype = c_double
		return _func(JD)

	@staticmethod
	def Mercury_Y(JD: float):
		_func = _aaplus.CAAVSOP87E_Mercury_Y
		_func.argtypes = [c_double]
		_func.restype = c_double
		return _func(JD)

	@staticmethod
	def Mercury_Y_DASH(JD: float):
		_func = _aaplus.CAAVSOP87E_Mercury_Y_DASH
		_func.argtypes = [c_double]
		_func.restype = c_double
		return _func(JD)

	@staticmethod
	def Mercury_Z(JD: float):
		_func = _aaplus.CAAVSOP87E_Mercury_Z
		_func.argtypes = [c_double]
		_func.restype = c_double
		return _func(JD)

	@staticmethod
	def Mercury_Z_DASH(JD: float):
		_func = _aaplus.CAAVSOP87E_Mercury_Z_DASH
		_func.argtypes = [c_double]
		_func.restype = c_double
		return _func(JD)


class AAVSOP87E_Neptune:
	@staticmethod
	def Neptune_X(JD: float):
		_func = _aaplus.CAAVSOP87E_Neptune_X
		_func.argtypes = [c_double]
		_func.restype = c_double
		return _func(JD)

	@staticmethod
	def Neptune_X_DASH(JD: float):
		_func = _aaplus.CAAVSOP87E_Neptune_X_DASH
		_func.argtypes = [c_double]
		_func.restype = c_double
		return _func(JD)

	@staticmethod
	def Neptune_Y(JD: float):
		_func = _aaplus.CAAVSOP87E_Neptune_Y
		_func.argtypes = [c_double]
		_func.restype = c_double
		return _func(JD)

	@staticmethod
	def Neptune_Y_DASH(JD: float):
		_func = _aaplus.CAAVSOP87E_Neptune_Y_DASH
		_func.argtypes = [c_double]
		_func.restype = c_double
		return _func(JD)

	@staticmethod
	def Neptune_Z(JD: float):
		_func = _aaplus.CAAVSOP87E_Neptune_Z
		_func.argtypes = [c_double]
		_func.restype = c_double
		return _func(JD)

	@staticmethod
	def Neptune_Z_DASH(JD: float):
		_func = _aaplus.CAAVSOP87E_Neptune_Z_DASH
		_func.argtypes = [c_double]
		_func.restype = c_double
		return _func(JD)


class AAVSOP87E_Saturn:
	@staticmethod
	def Saturn_X(JD: float):
		_func = _aaplus.CAAVSOP87E_Saturn_X
		_func.argtypes = [c_double]
		_func.restype = c_double
		return _func(JD)

	@staticmethod
	def Saturn_X_DASH(JD: float):
		_func = _aaplus.CAAVSOP87E_Saturn_X_DASH
		_func.argtypes = [c_double]
		_func.restype = c_double
		return _func(JD)

	@staticmethod
	def Saturn_Y(JD: float):
		_func = _aaplus.CAAVSOP87E_Saturn_Y
		_func.argtypes = [c_double]
		_func.restype = c_double
		return _func(JD)

	@staticmethod
	def Saturn_Y_DASH(JD: float):
		_func = _aaplus.CAAVSOP87E_Saturn_Y_DASH
		_func.argtypes = [c_double]
		_func.restype = c_double
		return _func(JD)

	@staticmethod
	def Saturn_Z(JD: float):
		_func = _aaplus.CAAVSOP87E_Saturn_Z
		_func.argtypes = [c_double]
		_func.restype = c_double
		return _func(JD)

	@staticmethod
	def Saturn_Z_DASH(JD: float):
		_func = _aaplus.CAAVSOP87E_Saturn_Z_DASH
		_func.argtypes = [c_double]
		_func.restype = c_double
		return _func(JD)


class AAVSOP87E_Sun:
	@staticmethod
	def Sun_X(JD: float):
		_func = _aaplus.CAAVSOP87E_Sun_X
		_func.argtypes = [c_double]
		_func.restype = c_double
		return _func(JD)

	@staticmethod
	def Sun_X_DASH(JD: float):
		_func = _aaplus.CAAVSOP87E_Sun_X_DASH
		_func.argtypes = [c_double]
		_func.restype = c_double
		return _func(JD)

	@staticmethod
	def Sun_Y(JD: float):
		_func = _aaplus.CAAVSOP87E_Sun_Y
		_func.argtypes = [c_double]
		_func.restype = c_double
		return _func(JD)

	@staticmethod
	def Sun_Y_DASH(JD: float):
		_func = _aaplus.CAAVSOP87E_Sun_Y_DASH
		_func.argtypes = [c_double]
		_func.restype = c_double
		return _func(JD)

	@staticmethod
	def Sun_Z(JD: float):
		_func = _aaplus.CAAVSOP87E_Sun_Z
		_func.argtypes = [c_double]
		_func.restype = c_double
		return _func(JD)

	@staticmethod
	def Sun_Z_DASH(JD: float):
		_func = _aaplus.CAAVSOP87E_Sun_Z_DASH
		_func.argtypes = [c_double]
		_func.restype = c_double
		return _func(JD)


class AAVSOP87E_Uranus:
	@staticmethod
	def Uranus_X(JD: float):
		_func = _aaplus.CAAVSOP87E_Uranus_X
		_func.argtypes = [c_double]
		_func.restype = c_double
		return _func(JD)

	@staticmethod
	def Uranus_X_DASH(JD: float):
		_func = _aaplus.CAAVSOP87E_Uranus_X_DASH
		_func.argtypes = [c_double]
		_func.restype = c_double
		return _func(JD)

	@staticmethod
	def Uranus_Y(JD: float):
		_func = _aaplus.CAAVSOP87E_Uranus_Y
		_func.argtypes = [c_double]
		_func.restype = c_double
		return _func(JD)

	@staticmethod
	def Uranus_Y_DASH(JD: float):
		_func = _aaplus.CAAVSOP87E_Uranus_Y_DASH
		_func.argtypes = [c_double]
		_func.restype = c_double
		return _func(JD)

	@staticmethod
	def Uranus_Z(JD: float):
		_func = _aaplus.CAAVSOP87E_Uranus_Z
		_func.argtypes = [c_double]
		_func.restype = c_double
		return _func(JD)

	@staticmethod
	def Uranus_Z_DASH(JD: float):
		_func = _aaplus.CAAVSOP87E_Uranus_Z_DASH
		_func.argtypes = [c_double]
		_func.restype = c_double
		return _func(JD)


class AAVSOP87E_Venus:
	@staticmethod
	def Venus_X(JD: float):
		_func = _aaplus.CAAVSOP87E_Venus_X
		_func.argtypes = [c_double]
		_func.restype = c_double
		return _func(JD)

	@staticmethod
	def Venus_X_DASH(JD: float):
		_func = _aaplus.CAAVSOP87E_Venus_X_DASH
		_func.argtypes = [c_double]
		_func.restype = c_double
		return _func(JD)

	@staticmethod
	def Venus_Y(JD: float):
		_func = _aaplus.CAAVSOP87E_Venus_Y
		_func.argtypes = [c_double]
		_func.restype = c_double
		return _func(JD)

	@staticmethod
	def Venus_Y_DASH(JD: float):
		_func = _aaplus.CAAVSOP87E_Venus_Y_DASH
		_func.argtypes = [c_double]
		_func.restype = c_double
		return _func(JD)

	@staticmethod
	def Venus_Z(JD: float):
		_func = _aaplus.CAAVSOP87E_Venus_Z
		_func.argtypes = [c_double]
		_func.restype = c_double
		return _func(JD)

	@staticmethod
	def Venus_Z_DASH(JD: float):
		_func = _aaplus.CAAVSOP87E_Venus_Z_DASH
		_func.argtypes = [c_double]
		_func.restype = c_double
		return _func(JD)


class AAVSOP87_EMB:
	@staticmethod
	def EMB_A(JD: float):
		_func = _aaplus.CAAVSOP87_EMB_A
		_func.argtypes = [c_double]
		_func.restype = c_double
		return _func(JD)

	@staticmethod
	def EMB_L(JD: float):
		_func = _aaplus.CAAVSOP87_EMB_L
		_func.argtypes = [c_double]
		_func.restype = c_double
		return _func(JD)

	@staticmethod
	def EMB_K(JD: float):
		_func = _aaplus.CAAVSOP87_EMB_K
		_func.argtypes = [c_double]
		_func.restype = c_double
		return _func(JD)

	@staticmethod
	def EMB_H(JD: float):
		_func = _aaplus.CAAVSOP87_EMB_H
		_func.argtypes = [c_double]
		_func.restype = c_double
		return _func(JD)

	@staticmethod
	def EMB_Q(JD: float):
		_func = _aaplus.CAAVSOP87_EMB_Q
		_func.argtypes = [c_double]
		_func.restype = c_double
		return _func(JD)

	@staticmethod
	def EMB_P(JD: float):
		_func = _aaplus.CAAVSOP87_EMB_P
		_func.argtypes = [c_double]
		_func.restype = c_double
		return _func(JD)


class AAVSOP87_Jupiter:
	@staticmethod
	def Jupiter_A(JD: float):
		_func = _aaplus.CAAVSOP87_Jupiter_A
		_func.argtypes = [c_double]
		_func.restype = c_double
		return _func(JD)

	@staticmethod
	def Jupiter_L(JD: float):
		_func = _aaplus.CAAVSOP87_Jupiter_L
		_func.argtypes = [c_double]
		_func.restype = c_double
		return _func(JD)

	@staticmethod
	def Jupiter_K(JD: float):
		_func = _aaplus.CAAVSOP87_Jupiter_K
		_func.argtypes = [c_double]
		_func.restype = c_double
		return _func(JD)

	@staticmethod
	def Jupiter_H(JD: float):
		_func = _aaplus.CAAVSOP87_Jupiter_H
		_func.argtypes = [c_double]
		_func.restype = c_double
		return _func(JD)

	@staticmethod
	def Jupiter_Q(JD: float):
		_func = _aaplus.CAAVSOP87_Jupiter_Q
		_func.argtypes = [c_double]
		_func.restype = c_double
		return _func(JD)

	@staticmethod
	def Jupiter_P(JD: float):
		_func = _aaplus.CAAVSOP87_Jupiter_P
		_func.argtypes = [c_double]
		_func.restype = c_double
		return _func(JD)


class AAVSOP87_Mars:
	@staticmethod
	def Mars_A(JD: float):
		_func = _aaplus.CAAVSOP87_Mars_A
		_func.argtypes = [c_double]
		_func.restype = c_double
		return _func(JD)

	@staticmethod
	def Mars_L(JD: float):
		_func = _aaplus.CAAVSOP87_Mars_L
		_func.argtypes = [c_double]
		_func.restype = c_double
		return _func(JD)

	@staticmethod
	def Mars_K(JD: float):
		_func = _aaplus.CAAVSOP87_Mars_K
		_func.argtypes = [c_double]
		_func.restype = c_double
		return _func(JD)

	@staticmethod
	def Mars_H(JD: float):
		_func = _aaplus.CAAVSOP87_Mars_H
		_func.argtypes = [c_double]
		_func.restype = c_double
		return _func(JD)

	@staticmethod
	def Mars_Q(JD: float):
		_func = _aaplus.CAAVSOP87_Mars_Q
		_func.argtypes = [c_double]
		_func.restype = c_double
		return _func(JD)

	@staticmethod
	def Mars_P(JD: float):
		_func = _aaplus.CAAVSOP87_Mars_P
		_func.argtypes = [c_double]
		_func.restype = c_double
		return _func(JD)


class AAVSOP87_Mercury:
	@staticmethod
	def Mercury_A(JD: float):
		_func = _aaplus.CAAVSOP87_Mercury_A
		_func.argtypes = [c_double]
		_func.restype = c_double
		return _func(JD)

	@staticmethod
	def Mercury_L(JD: float):
		_func = _aaplus.CAAVSOP87_Mercury_L
		_func.argtypes = [c_double]
		_func.restype = c_double
		return _func(JD)

	@staticmethod
	def Mercury_K(JD: float):
		_func = _aaplus.CAAVSOP87_Mercury_K
		_func.argtypes = [c_double]
		_func.restype = c_double
		return _func(JD)

	@staticmethod
	def Mercury_H(JD: float):
		_func = _aaplus.CAAVSOP87_Mercury_H
		_func.argtypes = [c_double]
		_func.restype = c_double
		return _func(JD)

	@staticmethod
	def Mercury_Q(JD: float):
		_func = _aaplus.CAAVSOP87_Mercury_Q
		_func.argtypes = [c_double]
		_func.restype = c_double
		return _func(JD)

	@staticmethod
	def Mercury_P(JD: float):
		_func = _aaplus.CAAVSOP87_Mercury_P
		_func.argtypes = [c_double]
		_func.restype = c_double
		return _func(JD)


class AAVSOP87_Neptune:
	@staticmethod
	def Neptune_A(JD: float):
		_func = _aaplus.CAAVSOP87_Neptune_A
		_func.argtypes = [c_double]
		_func.restype = c_double
		return _func(JD)

	@staticmethod
	def Neptune_L(JD: float):
		_func = _aaplus.CAAVSOP87_Neptune_L
		_func.argtypes = [c_double]
		_func.restype = c_double
		return _func(JD)

	@staticmethod
	def Neptune_K(JD: float):
		_func = _aaplus.CAAVSOP87_Neptune_K
		_func.argtypes = [c_double]
		_func.restype = c_double
		return _func(JD)

	@staticmethod
	def Neptune_H(JD: float):
		_func = _aaplus.CAAVSOP87_Neptune_H
		_func.argtypes = [c_double]
		_func.restype = c_double
		return _func(JD)

	@staticmethod
	def Neptune_Q(JD: float):
		_func = _aaplus.CAAVSOP87_Neptune_Q
		_func.argtypes = [c_double]
		_func.restype = c_double
		return _func(JD)

	@staticmethod
	def Neptune_P(JD: float):
		_func = _aaplus.CAAVSOP87_Neptune_P
		_func.argtypes = [c_double]
		_func.restype = c_double
		return _func(JD)


class AAVSOP87_Saturn:
	@staticmethod
	def Saturn_A(JD: float):
		_func = _aaplus.CAAVSOP87_Saturn_A
		_func.argtypes = [c_double]
		_func.restype = c_double
		return _func(JD)

	@staticmethod
	def Saturn_L(JD: float):
		_func = _aaplus.CAAVSOP87_Saturn_L
		_func.argtypes = [c_double]
		_func.restype = c_double
		return _func(JD)

	@staticmethod
	def Saturn_K(JD: float):
		_func = _aaplus.CAAVSOP87_Saturn_K
		_func.argtypes = [c_double]
		_func.restype = c_double
		return _func(JD)

	@staticmethod
	def Saturn_H(JD: float):
		_func = _aaplus.CAAVSOP87_Saturn_H
		_func.argtypes = [c_double]
		_func.restype = c_double
		return _func(JD)

	@staticmethod
	def Saturn_Q(JD: float):
		_func = _aaplus.CAAVSOP87_Saturn_Q
		_func.argtypes = [c_double]
		_func.restype = c_double
		return _func(JD)

	@staticmethod
	def Saturn_P(JD: float):
		_func = _aaplus.CAAVSOP87_Saturn_P
		_func.argtypes = [c_double]
		_func.restype = c_double
		return _func(JD)


class AAVSOP87_Uranus:
	@staticmethod
	def Uranus_A(JD: float):
		_func = _aaplus.CAAVSOP87_Uranus_A
		_func.argtypes = [c_double]
		_func.restype = c_double
		return _func(JD)

	@staticmethod
	def Uranus_L(JD: float):
		_func = _aaplus.CAAVSOP87_Uranus_L
		_func.argtypes = [c_double]
		_func.restype = c_double
		return _func(JD)

	@staticmethod
	def Uranus_K(JD: float):
		_func = _aaplus.CAAVSOP87_Uranus_K
		_func.argtypes = [c_double]
		_func.restype = c_double
		return _func(JD)

	@staticmethod
	def Uranus_H(JD: float):
		_func = _aaplus.CAAVSOP87_Uranus_H
		_func.argtypes = [c_double]
		_func.restype = c_double
		return _func(JD)

	@staticmethod
	def Uranus_Q(JD: float):
		_func = _aaplus.CAAVSOP87_Uranus_Q
		_func.argtypes = [c_double]
		_func.restype = c_double
		return _func(JD)

	@staticmethod
	def Uranus_P(JD: float):
		_func = _aaplus.CAAVSOP87_Uranus_P
		_func.argtypes = [c_double]
		_func.restype = c_double
		return _func(JD)


class AAVSOP87_Venus:
	@staticmethod
	def Venus_A(JD: float):
		_func = _aaplus.CAAVSOP87_Venus_A
		_func.argtypes = [c_double]
		_func.restype = c_double
		return _func(JD)

	@staticmethod
	def Venus_L(JD: float):
		_func = _aaplus.CAAVSOP87_Venus_L
		_func.argtypes = [c_double]
		_func.restype = c_double
		return _func(JD)

	@staticmethod
	def Venus_K(JD: float):
		_func = _aaplus.CAAVSOP87_Venus_K
		_func.argtypes = [c_double]
		_func.restype = c_double
		return _func(JD)

	@staticmethod
	def Venus_H(JD: float):
		_func = _aaplus.CAAVSOP87_Venus_H
		_func.argtypes = [c_double]
		_func.restype = c_double
		return _func(JD)

	@staticmethod
	def Venus_Q(JD: float):
		_func = _aaplus.CAAVSOP87_Venus_Q
		_func.argtypes = [c_double]
		_func.restype = c_double
		return _func(JD)

	@staticmethod
	def Venus_P(JD: float):
		_func = _aaplus.CAAVSOP87_Venus_P
		_func.argtypes = [c_double]
		_func.restype = c_double
		return _func(JD)


