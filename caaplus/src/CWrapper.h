#pragma once

#ifndef __CWRAPPER_H__
#define __CWRAPPER_H__

#include "AA+.h"
#include "AAELPMPP02.h"

#ifdef _WIN32
#define AAPLUS_EXPORT_LIB __declspec(dllexport)
#else
#define AAPLUS_EXPORT_LIB
#endif

extern "C" {
	/* CAAPlus export functions */
	AAPLUS_EXPORT_LIB const char* CAAPlus_Version() { return CAAPlus::Version(); }
	AAPLUS_EXPORT_LIB int CAAPlus_VersionNumber() { return CAAPlus::VersionNumber(); }

	/* CAAAberration export functions */
	AAPLUS_EXPORT_LIB CAA3DCoordinate CAAAberration_EarthVelocity(double JD, bool bHighPrecision) { return CAAAberration::EarthVelocity(JD, bHighPrecision); }
	AAPLUS_EXPORT_LIB CAA2DCoordinate CAAAberration_EclipticAberration(double Alpha, double Delta, double JD, bool bHighPrecision) { return CAAAberration::EclipticAberration(Alpha, Delta, JD, bHighPrecision); }
	AAPLUS_EXPORT_LIB CAA2DCoordinate CAAAberration_EquatorialAberration(double Lambda, double Beta, double JD, bool bHighPrecision) { return CAAAberration::EquatorialAberration(Lambda, Beta, JD, bHighPrecision); }

	/* CAAAngularSeparation export functions */
	AAPLUS_EXPORT_LIB double CAAAngularSeparation_Separation(double Alpha1, double Delta1, double Alpha2, double Delta2) { return CAAAngularSeparation::Separation(Alpha1, Delta1, Alpha2, Delta2); }
	AAPLUS_EXPORT_LIB double CAAAngularSeparation_PositionAngle(double Alpha1, double Delta1, double Alpha2, double Delta2) { return CAAAngularSeparation::PositionAngle(Alpha1, Delta1, Alpha2, Delta2); }
	AAPLUS_EXPORT_LIB double CAAAngularSeparation_DistanceFromGreatArc(double Alpha1, double Delta1, double Alpha2, double Delta2, double Alpha3, double Delta3) { return CAAAngularSeparation::DistanceFromGreatArc(Alpha1, Delta1, Alpha2, Delta2, Alpha3, Delta3); }
	AAPLUS_EXPORT_LIB double CAAAngularSeparation_SmallestCircle(double Alpha1, double Delta1, double Alpha2, double Delta2, double Alpha3, double Delta3, bool& bType1) { return CAAAngularSeparation::SmallestCircle(Alpha1, Delta1, Alpha2, Delta2, Alpha3, Delta3, bType1); }

	/* CAABinaryStar export functions */
	AAPLUS_EXPORT_LIB CAABinaryStarDetails CAABinaryStar_Calculate(double t, double P, double T, double e, double a, double i, double omega, double w) { return CAABinaryStar::Calculate(t, P, T, e, a, i, omega, w); }
	AAPLUS_EXPORT_LIB double CAABinaryStar_ApparentEccentricity(double e, double i, double w) { return CAABinaryStar::ApparentEccentricity(e, i, w); }

	/* CAACoordinateTransformation export functions */
	AAPLUS_EXPORT_LIB CAA2DCoordinate CAACoordinateTransformation_Equatorial2Ecliptic(double Alpha, double Delta, double Epsilon) { return CAACoordinateTransformation::Equatorial2Ecliptic(Alpha, Delta, Epsilon); }
	AAPLUS_EXPORT_LIB CAA2DCoordinate CAACoordinateTransformation_Ecliptic2Equatorial(double Lambda, double Beta, double Epsilon) { return CAACoordinateTransformation::Ecliptic2Equatorial(Lambda, Beta, Epsilon); }
	AAPLUS_EXPORT_LIB CAA2DCoordinate CAACoordinateTransformation_Equatorial2Horizontal(double LocalHourAngle, double Delta, double Latitude) { return CAACoordinateTransformation::Equatorial2Horizontal(LocalHourAngle, Delta, Latitude); }
	AAPLUS_EXPORT_LIB CAA2DCoordinate CAACoordinateTransformation_Horizontal2Equatorial(double A, double h, double Latitude) { return CAACoordinateTransformation::Horizontal2Equatorial(A, h, Latitude); }
	AAPLUS_EXPORT_LIB CAA2DCoordinate CAACoordinateTransformation_Equatorial2Galactic(double Alpha, double Delta) { return CAACoordinateTransformation::Equatorial2Galactic(Alpha, Delta); }
	AAPLUS_EXPORT_LIB CAA2DCoordinate CAACoordinateTransformation_Galactic2Equatorial(double l, double b) { return CAACoordinateTransformation::Galactic2Equatorial(l, b); }
	AAPLUS_EXPORT_LIB double CAACoordinateTransformation_DegreesToRadians(double Degrees) { return CAACoordinateTransformation::DegreesToRadians(Degrees); }
	AAPLUS_EXPORT_LIB double CAACoordinateTransformation_RadiansToDegrees(double Radians) { return CAACoordinateTransformation::RadiansToDegrees(Radians); }
	AAPLUS_EXPORT_LIB double CAACoordinateTransformation_RadiansToHours(double Radians) { return CAACoordinateTransformation::RadiansToHours(Radians); }
	AAPLUS_EXPORT_LIB double CAACoordinateTransformation_HoursToRadians(double Hours) { return CAACoordinateTransformation::HoursToRadians(Hours); }
	AAPLUS_EXPORT_LIB double CAACoordinateTransformation_HoursToDegrees(double Hours) { return CAACoordinateTransformation::HoursToDegrees(Hours); }
	AAPLUS_EXPORT_LIB double CAACoordinateTransformation_DegreesToHours(double Degrees) { return CAACoordinateTransformation::DegreesToHours(Degrees); }
	AAPLUS_EXPORT_LIB double CAACoordinateTransformation_PI() { return CAACoordinateTransformation::PI(); }
	AAPLUS_EXPORT_LIB double CAACoordinateTransformation_MapTo0To360Range(double Degrees) { return CAACoordinateTransformation::MapTo0To360Range(Degrees); }
	AAPLUS_EXPORT_LIB double CAACoordinateTransformation_MapToMinus90To90Range(double Degrees) { return CAACoordinateTransformation::MapToMinus90To90Range(Degrees); }
	AAPLUS_EXPORT_LIB double CAACoordinateTransformation_MapTo0To24Range(double HourAngle) { return CAACoordinateTransformation::MapTo0To24Range(HourAngle); }
	AAPLUS_EXPORT_LIB double CAACoordinateTransformation_MapTo0To2PIRange(double Angle) { return CAACoordinateTransformation::MapTo0To2PIRange(Angle); }
	AAPLUS_EXPORT_LIB double CAACoordinateTransformation_DMSToDegrees(double Degrees, double Minutes, double Seconds, bool bPositive) { return CAACoordinateTransformation::DMSToDegrees(Degrees, Minutes, Seconds, bPositive); }

	/* CAADate export functions */
	AAPLUS_EXPORT_LIB double CAADate_DateToJD(long Year, long Month, double Day, bool bGregorianCalendar) { return CAADate::DateToJD(Year, Month, Day, bGregorianCalendar); }
	AAPLUS_EXPORT_LIB bool CAADate_IsLeap(long Year, bool bGregorianCalendar) { return CAADate::IsLeap(Year, bGregorianCalendar); }
	AAPLUS_EXPORT_LIB void CAADate_DayOfYearToDayAndMonth(long DayOfYear, bool bLeap, long& DayOfMonth, long& Month) { return CAADate::DayOfYearToDayAndMonth(DayOfYear, bLeap, DayOfMonth, Month); }
	AAPLUS_EXPORT_LIB CAACalendarDate CAADate_JulianToGregorian(long Year, long Month, long Day) { return CAADate::JulianToGregorian(Year, Month, Day); }
	AAPLUS_EXPORT_LIB CAACalendarDate CAADate_GregorianToJulian(long Year, long Month, long Day) { return CAADate::GregorianToJulian(Year, Month, Day); }
	AAPLUS_EXPORT_LIB long CAADate_INT(double value) { return CAADate::INT(value); }
	AAPLUS_EXPORT_LIB bool CAADate_AfterPapalReform(long Year, long Month, double Day) { return CAADate::AfterPapalReform(Year, Month, Day); }
	AAPLUS_EXPORT_LIB bool CAADate_AfterPapalReform_2(double JD) { return CAADate::AfterPapalReform(JD); }
	AAPLUS_EXPORT_LIB double CAADate_DayOfYear(double JD, long Year, bool bGregorianCalendar) { return CAADate::DayOfYear(JD, Year, bGregorianCalendar); }
	AAPLUS_EXPORT_LIB long CAADate_DaysInMonth(long Month, bool bLeap) { return CAADate::DaysInMonth(Month, bLeap); }
	
	/* CAADate extra */
	AAPLUS_EXPORT_LIB void* CAADate_Create(long year, long month, double day, double hour, double minute, double second, bool IsGregorian) { return new CAADate(year, month, day, hour, minute, second, IsGregorian); }
	AAPLUS_EXPORT_LIB void CAADate_Get(void* self, long& year, long& month, long& day, long& hour, long& minute, double& second) { return static_cast<CAADate*>(self)->Get(year, month, day, hour, minute, second); }
	AAPLUS_EXPORT_LIB void CAADate_Set(void* self, long year, long month, double day, double hour, double minute, double second, bool IsGregorian) { static_cast<CAADate*>(self)->Set(year, month, day, hour, minute, second, IsGregorian); }
	AAPLUS_EXPORT_LIB CAADate::DOW CAADate_DayOfWeek(void* self) { return static_cast<CAADate*>(self)->DayOfWeek(); }
	AAPLUS_EXPORT_LIB long CAADate_DaysInYear(void* self) { return static_cast<CAADate*>(self)->DaysInYear(); }
	AAPLUS_EXPORT_LIB double CAADate_FractionalYear(void* self) { return static_cast<CAADate*>(self)->FractionalYear(); }
	AAPLUS_EXPORT_LIB bool CAADate_InGregorianCalendar(void* self) { return static_cast<CAADate*>(self)->InGregorianCalendar(); }
	AAPLUS_EXPORT_LIB bool CAADate_Leap(void* self) { return static_cast<CAADate*>(self)->Leap(); }
	AAPLUS_EXPORT_LIB void CAADate_SetInGregorianCalendar(void* self, bool IsGregorian) { static_cast<CAADate*>(self)->SetInGregorianCalendar(IsGregorian); }
	AAPLUS_EXPORT_LIB double CAADate_Julian(void* self) { return static_cast<CAADate*>(self)->Julian(); }
	AAPLUS_EXPORT_LIB void CAADate_Destroy(void* self) { delete self; }

	AAPLUS_EXPORT_LIB void CAADate_JDToDateParts(double JD, bool IsGregorian, long& year, long& month, long& day, long& hour, long& minute, double& second) {
		auto pDate = new CAADate(JD, IsGregorian);
		pDate->Get(year, month, day, hour, minute, second);
		delete pDate;
	}

	/* CAADiameters export functions */
	AAPLUS_EXPORT_LIB double CAADiameters_SunSemidiameterA(double Delta) { return CAADiameters::SunSemidiameterA(Delta); }
	AAPLUS_EXPORT_LIB double CAADiameters_MercurySemidiameterA(double Delta) { return CAADiameters::MercurySemidiameterA(Delta); }
	AAPLUS_EXPORT_LIB double CAADiameters_VenusSemidiameterA(double Delta) { return CAADiameters::VenusSemidiameterA(Delta); }
	AAPLUS_EXPORT_LIB double CAADiameters_MarsSemidiameterA(double Delta) { return CAADiameters::MarsSemidiameterA(Delta); }
	AAPLUS_EXPORT_LIB double CAADiameters_JupiterEquatorialSemidiameterA(double Delta) { return CAADiameters::JupiterEquatorialSemidiameterA(Delta); }
	AAPLUS_EXPORT_LIB double CAADiameters_JupiterPolarSemidiameterA(double Delta) { return CAADiameters::JupiterPolarSemidiameterA(Delta); }
	AAPLUS_EXPORT_LIB double CAADiameters_SaturnEquatorialSemidiameterA(double Delta) { return CAADiameters::SaturnEquatorialSemidiameterA(Delta); }
	AAPLUS_EXPORT_LIB double CAADiameters_SaturnPolarSemidiameterA(double Delta) { return CAADiameters::SaturnPolarSemidiameterA(Delta); }
	AAPLUS_EXPORT_LIB double CAADiameters_UranusSemidiameterA(double Delta) { return CAADiameters::UranusSemidiameterA(Delta); }
	AAPLUS_EXPORT_LIB double CAADiameters_NeptuneSemidiameterA(double Delta) { return CAADiameters::NeptuneSemidiameterA(Delta); }
	AAPLUS_EXPORT_LIB double CAADiameters_MercurySemidiameterB(double Delta) { return CAADiameters::MercurySemidiameterB(Delta); }
	AAPLUS_EXPORT_LIB double CAADiameters_VenusSemidiameterB(double Delta) { return CAADiameters::VenusSemidiameterB(Delta); }
	AAPLUS_EXPORT_LIB double CAADiameters_MarsSemidiameterB(double Delta) { return CAADiameters::MarsSemidiameterB(Delta); }
	AAPLUS_EXPORT_LIB double CAADiameters_JupiterEquatorialSemidiameterB(double Delta) { return CAADiameters::JupiterEquatorialSemidiameterB(Delta); }
	AAPLUS_EXPORT_LIB double CAADiameters_JupiterPolarSemidiameterB(double Delta) { return CAADiameters::JupiterPolarSemidiameterB(Delta); }
	AAPLUS_EXPORT_LIB double CAADiameters_SaturnEquatorialSemidiameterB(double Delta) { return CAADiameters::SaturnEquatorialSemidiameterB(Delta); }
	AAPLUS_EXPORT_LIB double CAADiameters_SaturnPolarSemidiameterB(double Delta) { return CAADiameters::SaturnPolarSemidiameterB(Delta); }
	AAPLUS_EXPORT_LIB double CAADiameters_UranusSemidiameterB(double Delta) { return CAADiameters::UranusSemidiameterB(Delta); }
	AAPLUS_EXPORT_LIB double CAADiameters_NeptuneSemidiameterB(double Delta) { return CAADiameters::NeptuneSemidiameterB(Delta); }
	AAPLUS_EXPORT_LIB double CAADiameters_PlutoSemidiameterB(double Delta) { return CAADiameters::PlutoSemidiameterB(Delta); }
	AAPLUS_EXPORT_LIB double CAADiameters_ApparentAsteroidDiameter(double Delta, double d) { return CAADiameters::ApparentAsteroidDiameter(Delta, d); }
	AAPLUS_EXPORT_LIB double CAADiameters_GeocentricMoonSemidiameter(double Delta) { return CAADiameters::GeocentricMoonSemidiameter(Delta); }
	AAPLUS_EXPORT_LIB double CAADiameters_ApparentSaturnPolarSemidiameterA(double Delta, double B) { return CAADiameters::ApparentSaturnPolarSemidiameterA(Delta, B); }
	AAPLUS_EXPORT_LIB double CAADiameters_ApparentSaturnPolarSemidiameterB(double Delta, double B) { return CAADiameters::ApparentSaturnPolarSemidiameterB(Delta, B); }
	AAPLUS_EXPORT_LIB double CAADiameters_TopocentricMoonSemidiameter(double DistanceDelta, double Delta, double H, double Latitude, double Height) { return CAADiameters::TopocentricMoonSemidiameter(DistanceDelta, Delta, H, Latitude, Height); }
	AAPLUS_EXPORT_LIB double CAADiameters_AsteroidDiameter(double H, double A) { return CAADiameters::AsteroidDiameter(H, A); }

	/* CAADynamicalTime export functions */
	AAPLUS_EXPORT_LIB CAADynamicalTime::DELTAT_PROC CAADynamicalTime_SetUserDefinedDeltaT(CAADynamicalTime::DELTAT_PROC pProc) { return CAADynamicalTime::SetUserDefinedDeltaT(pProc); }
	AAPLUS_EXPORT_LIB double CAADynamicalTime_DeltaT(double JD) { return CAADynamicalTime::DeltaT(JD); }
	AAPLUS_EXPORT_LIB double CAADynamicalTime_CumulativeLeapSeconds(double JD) { return CAADynamicalTime::CumulativeLeapSeconds(JD); }
	AAPLUS_EXPORT_LIB double CAADynamicalTime_TT2UTC(double JD) { return CAADynamicalTime::TT2UTC(JD); }
	AAPLUS_EXPORT_LIB double CAADynamicalTime_UTC2TT(double JD) { return CAADynamicalTime::UTC2TT(JD); }
	AAPLUS_EXPORT_LIB double CAADynamicalTime_TT2TAI(double JD) { return CAADynamicalTime::TT2TAI(JD); }
	AAPLUS_EXPORT_LIB double CAADynamicalTime_TAI2TT(double JD) { return CAADynamicalTime::TAI2TT(JD); }
	AAPLUS_EXPORT_LIB double CAADynamicalTime_TT2UT1(double JD) { return CAADynamicalTime::TT2UT1(JD); }
	AAPLUS_EXPORT_LIB double CAADynamicalTime_UT12TT(double JD) { return CAADynamicalTime::UT12TT(JD); }
	AAPLUS_EXPORT_LIB double CAADynamicalTime_UT1MinusUTC(double JD) { return CAADynamicalTime::UT1MinusUTC(JD); }

	/* CAAEarth export functions */
	AAPLUS_EXPORT_LIB double CAAEarth_EclipticLongitude(double JD, bool bHighPrecision) { return CAAEarth::EclipticLongitude(JD, bHighPrecision); }
	AAPLUS_EXPORT_LIB double CAAEarth_EclipticLatitude(double JD, bool bHighPrecision) { return CAAEarth::EclipticLatitude(JD, bHighPrecision); }
	AAPLUS_EXPORT_LIB double CAAEarth_RadiusVector(double JD, bool bHighPrecision) { return CAAEarth::RadiusVector(JD, bHighPrecision); }
	AAPLUS_EXPORT_LIB double CAAEarth_SunMeanAnomaly(double JD) { return CAAEarth::SunMeanAnomaly(JD); }
	AAPLUS_EXPORT_LIB double CAAEarth_Eccentricity(double JD) { return CAAEarth::Eccentricity(JD); }
	AAPLUS_EXPORT_LIB double CAAEarth_EclipticLongitudeJ2000(double JD, bool bHighPrecision) { return CAAEarth::EclipticLongitudeJ2000(JD, bHighPrecision); }
	AAPLUS_EXPORT_LIB double CAAEarth_EclipticLatitudeJ2000(double JD, bool bHighPrecision) { return CAAEarth::EclipticLatitudeJ2000(JD, bHighPrecision); }

	/* CAAEaster export functions */
	AAPLUS_EXPORT_LIB CAAEasterDetails CAAEaster_Calculate(int nYear, bool GregorianCalendar) { return CAAEaster::Calculate(nYear, GregorianCalendar); }

	/* CAAEclipses export functions */
	AAPLUS_EXPORT_LIB CAASolarEclipseDetails CAAEclipses_CalculateSolar(double k) { return CAAEclipses::CalculateSolar(k); }
	AAPLUS_EXPORT_LIB CAALunarEclipseDetails CAAEclipses_CalculateLunar(double k) { return CAAEclipses::CalculateLunar(k); }

	/* CAAEclipticalElements export functions */
	AAPLUS_EXPORT_LIB CAAEclipticalElementDetails CAAEclipticalElements_Calculate(double i0, double w0, double omega0, double JD0, double JD) { return CAAEclipticalElements::Calculate(i0, w0, omega0, JD0, JD); }
	AAPLUS_EXPORT_LIB CAAEclipticalElementDetails CAAEclipticalElements_FK4B1950ToFK5J2000(double i0, double w0, double omega0) { return CAAEclipticalElements::FK4B1950ToFK5J2000(i0, w0, omega0); }

	/* CAAElementsPlanetaryOrbit export functions */
	AAPLUS_EXPORT_LIB double CAAElementsPlanetaryOrbit_MercuryMeanLongitude(double JD) { return CAAElementsPlanetaryOrbit::MercuryMeanLongitude(JD); }
	AAPLUS_EXPORT_LIB double CAAElementsPlanetaryOrbit_MercurySemimajorAxis(double JD) { return CAAElementsPlanetaryOrbit::MercurySemimajorAxis(JD); }
	AAPLUS_EXPORT_LIB double CAAElementsPlanetaryOrbit_MercuryEccentricity(double JD) { return CAAElementsPlanetaryOrbit::MercuryEccentricity(JD); }
	AAPLUS_EXPORT_LIB double CAAElementsPlanetaryOrbit_MercuryInclination(double JD) { return CAAElementsPlanetaryOrbit::MercuryInclination(JD); }
	AAPLUS_EXPORT_LIB double CAAElementsPlanetaryOrbit_MercuryLongitudeAscendingNode(double JD) { return CAAElementsPlanetaryOrbit::MercuryLongitudeAscendingNode(JD); }
	AAPLUS_EXPORT_LIB double CAAElementsPlanetaryOrbit_MercuryLongitudePerihelion(double JD) { return CAAElementsPlanetaryOrbit::MercuryLongitudePerihelion(JD); }
	AAPLUS_EXPORT_LIB double CAAElementsPlanetaryOrbit_VenusMeanLongitude(double JD) { return CAAElementsPlanetaryOrbit::VenusMeanLongitude(JD); }
	AAPLUS_EXPORT_LIB double CAAElementsPlanetaryOrbit_VenusSemimajorAxis(double JD) { return CAAElementsPlanetaryOrbit::VenusSemimajorAxis(JD); }
	AAPLUS_EXPORT_LIB double CAAElementsPlanetaryOrbit_VenusEccentricity(double JD) { return CAAElementsPlanetaryOrbit::VenusEccentricity(JD); }
	AAPLUS_EXPORT_LIB double CAAElementsPlanetaryOrbit_VenusInclination(double JD) { return CAAElementsPlanetaryOrbit::VenusInclination(JD); }
	AAPLUS_EXPORT_LIB double CAAElementsPlanetaryOrbit_VenusLongitudeAscendingNode(double JD) { return CAAElementsPlanetaryOrbit::VenusLongitudeAscendingNode(JD); }
	AAPLUS_EXPORT_LIB double CAAElementsPlanetaryOrbit_VenusLongitudePerihelion(double JD) { return CAAElementsPlanetaryOrbit::VenusLongitudePerihelion(JD); }
	AAPLUS_EXPORT_LIB double CAAElementsPlanetaryOrbit_EarthMeanLongitude(double JD) { return CAAElementsPlanetaryOrbit::EarthMeanLongitude(JD); }
	AAPLUS_EXPORT_LIB double CAAElementsPlanetaryOrbit_EarthSemimajorAxis(double JD) { return CAAElementsPlanetaryOrbit::EarthSemimajorAxis(JD); }
	AAPLUS_EXPORT_LIB double CAAElementsPlanetaryOrbit_EarthEccentricity(double JD) { return CAAElementsPlanetaryOrbit::EarthEccentricity(JD); }
	AAPLUS_EXPORT_LIB double CAAElementsPlanetaryOrbit_EarthInclination(double JD) { return CAAElementsPlanetaryOrbit::EarthInclination(JD); }
	AAPLUS_EXPORT_LIB double CAAElementsPlanetaryOrbit_EarthLongitudePerihelion(double JD) { return CAAElementsPlanetaryOrbit::EarthLongitudePerihelion(JD); }
	AAPLUS_EXPORT_LIB double CAAElementsPlanetaryOrbit_MarsMeanLongitude(double JD) { return CAAElementsPlanetaryOrbit::MarsMeanLongitude(JD); }
	AAPLUS_EXPORT_LIB double CAAElementsPlanetaryOrbit_MarsSemimajorAxis(double JD) { return CAAElementsPlanetaryOrbit::MarsSemimajorAxis(JD); }
	AAPLUS_EXPORT_LIB double CAAElementsPlanetaryOrbit_MarsEccentricity(double JD) { return CAAElementsPlanetaryOrbit::MarsEccentricity(JD); }
	AAPLUS_EXPORT_LIB double CAAElementsPlanetaryOrbit_MarsInclination(double JD) { return CAAElementsPlanetaryOrbit::MarsInclination(JD); }
	AAPLUS_EXPORT_LIB double CAAElementsPlanetaryOrbit_MarsLongitudeAscendingNode(double JD) { return CAAElementsPlanetaryOrbit::MarsLongitudeAscendingNode(JD); }
	AAPLUS_EXPORT_LIB double CAAElementsPlanetaryOrbit_MarsLongitudePerihelion(double JD) { return CAAElementsPlanetaryOrbit::MarsLongitudePerihelion(JD); }
	AAPLUS_EXPORT_LIB double CAAElementsPlanetaryOrbit_JupiterMeanLongitude(double JD) { return CAAElementsPlanetaryOrbit::JupiterMeanLongitude(JD); }
	AAPLUS_EXPORT_LIB double CAAElementsPlanetaryOrbit_JupiterSemimajorAxis(double JD) { return CAAElementsPlanetaryOrbit::JupiterSemimajorAxis(JD); }
	AAPLUS_EXPORT_LIB double CAAElementsPlanetaryOrbit_JupiterEccentricity(double JD) { return CAAElementsPlanetaryOrbit::JupiterEccentricity(JD); }
	AAPLUS_EXPORT_LIB double CAAElementsPlanetaryOrbit_JupiterInclination(double JD) { return CAAElementsPlanetaryOrbit::JupiterInclination(JD); }
	AAPLUS_EXPORT_LIB double CAAElementsPlanetaryOrbit_JupiterLongitudeAscendingNode(double JD) { return CAAElementsPlanetaryOrbit::JupiterLongitudeAscendingNode(JD); }
	AAPLUS_EXPORT_LIB double CAAElementsPlanetaryOrbit_JupiterLongitudePerihelion(double JD) { return CAAElementsPlanetaryOrbit::JupiterLongitudePerihelion(JD); }
	AAPLUS_EXPORT_LIB double CAAElementsPlanetaryOrbit_SaturnMeanLongitude(double JD) { return CAAElementsPlanetaryOrbit::SaturnMeanLongitude(JD); }
	AAPLUS_EXPORT_LIB double CAAElementsPlanetaryOrbit_SaturnSemimajorAxis(double JD) { return CAAElementsPlanetaryOrbit::SaturnSemimajorAxis(JD); }
	AAPLUS_EXPORT_LIB double CAAElementsPlanetaryOrbit_SaturnEccentricity(double JD) { return CAAElementsPlanetaryOrbit::SaturnEccentricity(JD); }
	AAPLUS_EXPORT_LIB double CAAElementsPlanetaryOrbit_SaturnInclination(double JD) { return CAAElementsPlanetaryOrbit::SaturnInclination(JD); }
	AAPLUS_EXPORT_LIB double CAAElementsPlanetaryOrbit_SaturnLongitudeAscendingNode(double JD) { return CAAElementsPlanetaryOrbit::SaturnLongitudeAscendingNode(JD); }
	AAPLUS_EXPORT_LIB double CAAElementsPlanetaryOrbit_SaturnLongitudePerihelion(double JD) { return CAAElementsPlanetaryOrbit::SaturnLongitudePerihelion(JD); }
	AAPLUS_EXPORT_LIB double CAAElementsPlanetaryOrbit_UranusMeanLongitude(double JD) { return CAAElementsPlanetaryOrbit::UranusMeanLongitude(JD); }
	AAPLUS_EXPORT_LIB double CAAElementsPlanetaryOrbit_UranusSemimajorAxis(double JD) { return CAAElementsPlanetaryOrbit::UranusSemimajorAxis(JD); }
	AAPLUS_EXPORT_LIB double CAAElementsPlanetaryOrbit_UranusEccentricity(double JD) { return CAAElementsPlanetaryOrbit::UranusEccentricity(JD); }
	AAPLUS_EXPORT_LIB double CAAElementsPlanetaryOrbit_UranusInclination(double JD) { return CAAElementsPlanetaryOrbit::UranusInclination(JD); }
	AAPLUS_EXPORT_LIB double CAAElementsPlanetaryOrbit_UranusLongitudeAscendingNode(double JD) { return CAAElementsPlanetaryOrbit::UranusLongitudeAscendingNode(JD); }
	AAPLUS_EXPORT_LIB double CAAElementsPlanetaryOrbit_UranusLongitudePerihelion(double JD) { return CAAElementsPlanetaryOrbit::UranusLongitudePerihelion(JD); }
	AAPLUS_EXPORT_LIB double CAAElementsPlanetaryOrbit_NeptuneMeanLongitude(double JD) { return CAAElementsPlanetaryOrbit::NeptuneMeanLongitude(JD); }
	AAPLUS_EXPORT_LIB double CAAElementsPlanetaryOrbit_NeptuneSemimajorAxis(double JD) { return CAAElementsPlanetaryOrbit::NeptuneSemimajorAxis(JD); }
	AAPLUS_EXPORT_LIB double CAAElementsPlanetaryOrbit_NeptuneEccentricity(double JD) { return CAAElementsPlanetaryOrbit::NeptuneEccentricity(JD); }
	AAPLUS_EXPORT_LIB double CAAElementsPlanetaryOrbit_NeptuneInclination(double JD) { return CAAElementsPlanetaryOrbit::NeptuneInclination(JD); }
	AAPLUS_EXPORT_LIB double CAAElementsPlanetaryOrbit_NeptuneLongitudeAscendingNode(double JD) { return CAAElementsPlanetaryOrbit::NeptuneLongitudeAscendingNode(JD); }
	AAPLUS_EXPORT_LIB double CAAElementsPlanetaryOrbit_NeptuneLongitudePerihelion(double JD) { return CAAElementsPlanetaryOrbit::NeptuneLongitudePerihelion(JD); }
	AAPLUS_EXPORT_LIB double CAAElementsPlanetaryOrbit_MercuryMeanLongitudeJ2000(double JD) { return CAAElementsPlanetaryOrbit::MercuryMeanLongitudeJ2000(JD); }
	AAPLUS_EXPORT_LIB double CAAElementsPlanetaryOrbit_MercuryInclinationJ2000(double JD) { return CAAElementsPlanetaryOrbit::MercuryInclinationJ2000(JD); }
	AAPLUS_EXPORT_LIB double CAAElementsPlanetaryOrbit_MercuryLongitudeAscendingNodeJ2000(double JD) { return CAAElementsPlanetaryOrbit::MercuryLongitudeAscendingNodeJ2000(JD); }
	AAPLUS_EXPORT_LIB double CAAElementsPlanetaryOrbit_MercuryLongitudePerihelionJ2000(double JD) { return CAAElementsPlanetaryOrbit::MercuryLongitudePerihelionJ2000(JD); }
	AAPLUS_EXPORT_LIB double CAAElementsPlanetaryOrbit_VenusMeanLongitudeJ2000(double JD) { return CAAElementsPlanetaryOrbit::VenusMeanLongitudeJ2000(JD); }
	AAPLUS_EXPORT_LIB double CAAElementsPlanetaryOrbit_VenusInclinationJ2000(double JD) { return CAAElementsPlanetaryOrbit::VenusInclinationJ2000(JD); }
	AAPLUS_EXPORT_LIB double CAAElementsPlanetaryOrbit_VenusLongitudeAscendingNodeJ2000(double JD) { return CAAElementsPlanetaryOrbit::VenusLongitudeAscendingNodeJ2000(JD); }
	AAPLUS_EXPORT_LIB double CAAElementsPlanetaryOrbit_VenusLongitudePerihelionJ2000(double JD) { return CAAElementsPlanetaryOrbit::VenusLongitudePerihelionJ2000(JD); }
	AAPLUS_EXPORT_LIB double CAAElementsPlanetaryOrbit_EarthMeanLongitudeJ2000(double JD) { return CAAElementsPlanetaryOrbit::EarthMeanLongitudeJ2000(JD); }
	AAPLUS_EXPORT_LIB double CAAElementsPlanetaryOrbit_EarthInclinationJ2000(double JD) { return CAAElementsPlanetaryOrbit::EarthInclinationJ2000(JD); }
	AAPLUS_EXPORT_LIB double CAAElementsPlanetaryOrbit_EarthLongitudeAscendingNodeJ2000(double JD) { return CAAElementsPlanetaryOrbit::EarthLongitudeAscendingNodeJ2000(JD); }
	AAPLUS_EXPORT_LIB double CAAElementsPlanetaryOrbit_EarthLongitudePerihelionJ2000(double JD) { return CAAElementsPlanetaryOrbit::EarthLongitudePerihelionJ2000(JD); }
	AAPLUS_EXPORT_LIB double CAAElementsPlanetaryOrbit_MarsMeanLongitudeJ2000(double JD) { return CAAElementsPlanetaryOrbit::MarsMeanLongitudeJ2000(JD); }
	AAPLUS_EXPORT_LIB double CAAElementsPlanetaryOrbit_MarsInclinationJ2000(double JD) { return CAAElementsPlanetaryOrbit::MarsInclinationJ2000(JD); }
	AAPLUS_EXPORT_LIB double CAAElementsPlanetaryOrbit_MarsLongitudeAscendingNodeJ2000(double JD) { return CAAElementsPlanetaryOrbit::MarsLongitudeAscendingNodeJ2000(JD); }
	AAPLUS_EXPORT_LIB double CAAElementsPlanetaryOrbit_MarsLongitudePerihelionJ2000(double JD) { return CAAElementsPlanetaryOrbit::MarsLongitudePerihelionJ2000(JD); }
	AAPLUS_EXPORT_LIB double CAAElementsPlanetaryOrbit_JupiterMeanLongitudeJ2000(double JD) { return CAAElementsPlanetaryOrbit::JupiterMeanLongitudeJ2000(JD); }
	AAPLUS_EXPORT_LIB double CAAElementsPlanetaryOrbit_JupiterInclinationJ2000(double JD) { return CAAElementsPlanetaryOrbit::JupiterInclinationJ2000(JD); }
	AAPLUS_EXPORT_LIB double CAAElementsPlanetaryOrbit_JupiterLongitudeAscendingNodeJ2000(double JD) { return CAAElementsPlanetaryOrbit::JupiterLongitudeAscendingNodeJ2000(JD); }
	AAPLUS_EXPORT_LIB double CAAElementsPlanetaryOrbit_JupiterLongitudePerihelionJ2000(double JD) { return CAAElementsPlanetaryOrbit::JupiterLongitudePerihelionJ2000(JD); }
	AAPLUS_EXPORT_LIB double CAAElementsPlanetaryOrbit_SaturnMeanLongitudeJ2000(double JD) { return CAAElementsPlanetaryOrbit::SaturnMeanLongitudeJ2000(JD); }
	AAPLUS_EXPORT_LIB double CAAElementsPlanetaryOrbit_SaturnInclinationJ2000(double JD) { return CAAElementsPlanetaryOrbit::SaturnInclinationJ2000(JD); }
	AAPLUS_EXPORT_LIB double CAAElementsPlanetaryOrbit_SaturnLongitudeAscendingNodeJ2000(double JD) { return CAAElementsPlanetaryOrbit::SaturnLongitudeAscendingNodeJ2000(JD); }
	AAPLUS_EXPORT_LIB double CAAElementsPlanetaryOrbit_SaturnLongitudePerihelionJ2000(double JD) { return CAAElementsPlanetaryOrbit::SaturnLongitudePerihelionJ2000(JD); }
	AAPLUS_EXPORT_LIB double CAAElementsPlanetaryOrbit_UranusMeanLongitudeJ2000(double JD) { return CAAElementsPlanetaryOrbit::UranusMeanLongitudeJ2000(JD); }
	AAPLUS_EXPORT_LIB double CAAElementsPlanetaryOrbit_UranusInclinationJ2000(double JD) { return CAAElementsPlanetaryOrbit::UranusInclinationJ2000(JD); }
	AAPLUS_EXPORT_LIB double CAAElementsPlanetaryOrbit_UranusLongitudeAscendingNodeJ2000(double JD) { return CAAElementsPlanetaryOrbit::UranusLongitudeAscendingNodeJ2000(JD); }
	AAPLUS_EXPORT_LIB double CAAElementsPlanetaryOrbit_UranusLongitudePerihelionJ2000(double JD) { return CAAElementsPlanetaryOrbit::UranusLongitudePerihelionJ2000(JD); }
	AAPLUS_EXPORT_LIB double CAAElementsPlanetaryOrbit_NeptuneMeanLongitudeJ2000(double JD) { return CAAElementsPlanetaryOrbit::NeptuneMeanLongitudeJ2000(JD); }
	AAPLUS_EXPORT_LIB double CAAElementsPlanetaryOrbit_NeptuneInclinationJ2000(double JD) { return CAAElementsPlanetaryOrbit::NeptuneInclinationJ2000(JD); }
	AAPLUS_EXPORT_LIB double CAAElementsPlanetaryOrbit_NeptuneLongitudeAscendingNodeJ2000(double JD) { return CAAElementsPlanetaryOrbit::NeptuneLongitudeAscendingNodeJ2000(JD); }
	AAPLUS_EXPORT_LIB double CAAElementsPlanetaryOrbit_NeptuneLongitudePerihelionJ2000(double JD) { return CAAElementsPlanetaryOrbit::NeptuneLongitudePerihelionJ2000(JD); }

	/* CAAElliptical export functions */
	AAPLUS_EXPORT_LIB double CAAElliptical_DistanceToLightTime(double Distance) { return CAAElliptical::DistanceToLightTime(Distance); }
	AAPLUS_EXPORT_LIB CAAEllipticalPlanetaryDetails CAAElliptical_Calculate(double JD, CAAElliptical::Object object, bool bHighPrecision) { return CAAElliptical::Calculate(JD, object, bHighPrecision); }
	AAPLUS_EXPORT_LIB double CAAElliptical_SemiMajorAxisFromPerihelionDistance(double q, double e) { return CAAElliptical::SemiMajorAxisFromPerihelionDistance(q, e); }
	AAPLUS_EXPORT_LIB double CAAElliptical_MeanMotionFromSemiMajorAxis(double a) { return CAAElliptical::MeanMotionFromSemiMajorAxis(a); }
	AAPLUS_EXPORT_LIB CAAEllipticalObjectDetails CAAElliptical_Calculate_2(double JD, const CAAEllipticalObjectElements& elements, bool bHighPrecision) { return CAAElliptical::Calculate(JD, elements, bHighPrecision); }
	AAPLUS_EXPORT_LIB double CAAElliptical_InstantaneousVelocity(double r, double a) { return CAAElliptical::InstantaneousVelocity(r, a); }
	AAPLUS_EXPORT_LIB double CAAElliptical_VelocityAtPerihelion(double e, double a) { return CAAElliptical::VelocityAtPerihelion(e, a); }
	AAPLUS_EXPORT_LIB double CAAElliptical_VelocityAtAphelion(double e, double a) { return CAAElliptical::VelocityAtAphelion(e, a); }
	AAPLUS_EXPORT_LIB double CAAElliptical_LengthOfEllipse(double e, double a) { return CAAElliptical::LengthOfEllipse(e, a); }
	AAPLUS_EXPORT_LIB double CAAElliptical_CometMagnitude(double g, double delta, double k, double r) { return CAAElliptical::CometMagnitude(g, delta, k, r); }
	AAPLUS_EXPORT_LIB double CAAElliptical_MinorPlanetMagnitude(double H, double delta, double G, double r, double PhaseAngle) { return CAAElliptical::MinorPlanetMagnitude(H, delta, G, r, PhaseAngle); }

	/* CAAELP2000 export functions */
	AAPLUS_EXPORT_LIB double CAAELP2000_EclipticLongitude(double JD) { return CAAELP2000::EclipticLongitude(JD); }
	AAPLUS_EXPORT_LIB double CAAELP2000_EclipticLongitude_2(const double* pT, int nTSize) { return CAAELP2000::EclipticLongitude(pT, nTSize); }
	AAPLUS_EXPORT_LIB double CAAELP2000_EclipticLatitude(double JD) { return CAAELP2000::EclipticLatitude(JD); }
	AAPLUS_EXPORT_LIB double CAAELP2000_EclipticLatitude_2(const double* pT, int nTSize) { return CAAELP2000::EclipticLatitude(pT, nTSize); }
	AAPLUS_EXPORT_LIB double CAAELP2000_RadiusVector(double JD) { return CAAELP2000::RadiusVector(JD); }
	AAPLUS_EXPORT_LIB double CAAELP2000_RadiusVector_2(const double* pT, int nTSize) { return CAAELP2000::RadiusVector(pT, nTSize); }
	AAPLUS_EXPORT_LIB CAA3DCoordinate CAAELP2000_EclipticRectangularCoordinates(double JD) { return CAAELP2000::EclipticRectangularCoordinates(JD); }
	AAPLUS_EXPORT_LIB CAA3DCoordinate CAAELP2000_EclipticRectangularCoordinatesJ2000(double JD) { return CAAELP2000::EclipticRectangularCoordinatesJ2000(JD); }
	AAPLUS_EXPORT_LIB CAA3DCoordinate CAAELP2000_EquatorialRectangularCoordinatesFK5(double JD) { return CAAELP2000::EquatorialRectangularCoordinatesFK5(JD); }
	AAPLUS_EXPORT_LIB double CAAELP2000_MoonMeanMeanLongitude(const double* pT, int nTSize) { return CAAELP2000::MoonMeanMeanLongitude(pT, nTSize); }
	AAPLUS_EXPORT_LIB double CAAELP2000_MoonMeanMeanLongitude_2(double JD) { return CAAELP2000::MoonMeanMeanLongitude(JD); }
	AAPLUS_EXPORT_LIB double CAAELP2000_MeanLongitudeLunarPerigee(const double* pT, int nTSize) { return CAAELP2000::MeanLongitudeLunarPerigee(pT, nTSize); }
	AAPLUS_EXPORT_LIB double CAAELP2000_MeanLongitudeLunarPerigee_2(double JD) { return CAAELP2000::MeanLongitudeLunarPerigee(JD); }
	AAPLUS_EXPORT_LIB double CAAELP2000_MeanLongitudeLunarAscendingNode(const double* pT, int nTSize) { return CAAELP2000::MeanLongitudeLunarAscendingNode(pT, nTSize); }
	AAPLUS_EXPORT_LIB double CAAELP2000_MeanLongitudeLunarAscendingNode_2(double JD) { return CAAELP2000::MeanLongitudeLunarAscendingNode(JD); }
	AAPLUS_EXPORT_LIB double CAAELP2000_MeanHeliocentricMeanLongitudeEarthMoonBarycentre(const double* pT, int nTSize) { return CAAELP2000::MeanHeliocentricMeanLongitudeEarthMoonBarycentre(pT, nTSize); }
	AAPLUS_EXPORT_LIB double CAAELP2000_MeanHeliocentricMeanLongitudeEarthMoonBarycentre_2(double JD) { return CAAELP2000::MeanHeliocentricMeanLongitudeEarthMoonBarycentre(JD); }
	AAPLUS_EXPORT_LIB double CAAELP2000_MeanLongitudeOfPerihelionOfEarthMoonBarycentre(const double* pT, int nTSize) { return CAAELP2000::MeanLongitudeOfPerihelionOfEarthMoonBarycentre(pT, nTSize); }
	AAPLUS_EXPORT_LIB double CAAELP2000_MeanLongitudeOfPerihelionOfEarthMoonBarycentre_2(double JD) { return CAAELP2000::MeanLongitudeOfPerihelionOfEarthMoonBarycentre(JD); }
	AAPLUS_EXPORT_LIB double CAAELP2000_MoonMeanSolarElongation(const double* pT, int nTSize) { return CAAELP2000::MoonMeanSolarElongation(pT, nTSize); }
	AAPLUS_EXPORT_LIB double CAAELP2000_MoonMeanSolarElongation_2(double JD) { return CAAELP2000::MoonMeanSolarElongation(JD); }
	AAPLUS_EXPORT_LIB double CAAELP2000_SunMeanAnomaly(const double* pT, int nTSize) { return CAAELP2000::SunMeanAnomaly(pT, nTSize); }
	AAPLUS_EXPORT_LIB double CAAELP2000_SunMeanAnomaly_2(double JD) { return CAAELP2000::SunMeanAnomaly(JD); }
	AAPLUS_EXPORT_LIB double CAAELP2000_MoonMeanAnomaly(const double* pT, int nTSize) { return CAAELP2000::MoonMeanAnomaly(pT, nTSize); }
	AAPLUS_EXPORT_LIB double CAAELP2000_MoonMeanAnomaly_2(double JD) { return CAAELP2000::MoonMeanAnomaly(JD); }
	AAPLUS_EXPORT_LIB double CAAELP2000_MoonMeanArgumentOfLatitude(const double* pT, int nTSize) { return CAAELP2000::MoonMeanArgumentOfLatitude(pT, nTSize); }
	AAPLUS_EXPORT_LIB double CAAELP2000_MoonMeanArgumentOfLatitude_2(double JD) { return CAAELP2000::MoonMeanArgumentOfLatitude(JD); }
	AAPLUS_EXPORT_LIB double CAAELP2000_MercuryMeanLongitude(double T) { return CAAELP2000::MercuryMeanLongitude(T); }
	AAPLUS_EXPORT_LIB double CAAELP2000_VenusMeanLongitude(double T) { return CAAELP2000::VenusMeanLongitude(T); }
	AAPLUS_EXPORT_LIB double CAAELP2000_MarsMeanLongitude(double T) { return CAAELP2000::MarsMeanLongitude(T); }
	AAPLUS_EXPORT_LIB double CAAELP2000_JupiterMeanLongitude(double T) { return CAAELP2000::JupiterMeanLongitude(T); }
	AAPLUS_EXPORT_LIB double CAAELP2000_SaturnMeanLongitude(double T) { return CAAELP2000::SaturnMeanLongitude(T); }
	AAPLUS_EXPORT_LIB double CAAELP2000_UranusMeanLongitude(double T) { return CAAELP2000::UranusMeanLongitude(T); }
	AAPLUS_EXPORT_LIB double CAAELP2000_NeptuneMeanLongitude(double T) { return CAAELP2000::NeptuneMeanLongitude(T); }

	/* CAAELPMPP02 export functions */
	AAPLUS_EXPORT_LIB double CAAELPMPP02_EclipticLongitude(double JD, CAAELPMPP02::Correction correction, double* pDerivative) { return CAAELPMPP02::EclipticLongitude(JD, correction, pDerivative); }
	AAPLUS_EXPORT_LIB double CAAELPMPP02_EclipticLongitude_2(const double* pT, int nTSize, CAAELPMPP02::Correction correction, double* pDerivative) { return CAAELPMPP02::EclipticLongitude(pT, nTSize, correction, pDerivative); }
	AAPLUS_EXPORT_LIB double CAAELPMPP02_EclipticLatitude(double JD, CAAELPMPP02::Correction correction, double* pDerivative) { return CAAELPMPP02::EclipticLatitude(JD, correction, pDerivative); }
	AAPLUS_EXPORT_LIB double CAAELPMPP02_EclipticLatitude_2(const double* pT, int nTSize, CAAELPMPP02::Correction correction, double* pDerivative) { return CAAELPMPP02::EclipticLatitude(pT, nTSize, correction, pDerivative); }
	AAPLUS_EXPORT_LIB double CAAELPMPP02_RadiusVector(double JD, CAAELPMPP02::Correction correction, double* pDerivative) { return CAAELPMPP02::RadiusVector(JD, correction, pDerivative); }
	AAPLUS_EXPORT_LIB double CAAELPMPP02_RadiusVector_2(const double* pT, int nTSize, CAAELPMPP02::Correction correction, double* pDerivative) { return CAAELPMPP02::RadiusVector(pT, nTSize, correction, pDerivative); }
	AAPLUS_EXPORT_LIB CAA3DCoordinate CAAELPMPP02_EclipticRectangularCoordinates(double JD, CAAELPMPP02::Correction correction, CAA3DCoordinate* pDerivative) { return CAAELPMPP02::EclipticRectangularCoordinates(JD, correction, pDerivative); }
	AAPLUS_EXPORT_LIB CAA3DCoordinate CAAELPMPP02_EclipticRectangularCoordinates_2(const double* pT, int nTSize, CAAELPMPP02::Correction correction, CAA3DCoordinate* pDerivative) { return CAAELPMPP02::EclipticRectangularCoordinates(pT, nTSize, correction, pDerivative); }
	AAPLUS_EXPORT_LIB CAA3DCoordinate CAAELPMPP02_EclipticRectangularCoordinatesJ2000(double JD, CAAELPMPP02::Correction correction, CAA3DCoordinate* pDerivative) { return CAAELPMPP02::EclipticRectangularCoordinatesJ2000(JD, correction, pDerivative); }
	AAPLUS_EXPORT_LIB CAA3DCoordinate CAAELPMPP02_EclipticRectangularCoordinatesJ2000_2(const double* pT, int nTSize, CAAELPMPP02::Correction correction, CAA3DCoordinate* pDerivative) { return CAAELPMPP02::EclipticRectangularCoordinatesJ2000(pT, nTSize, correction, pDerivative); }

	/* CAAEquationOfTime export functions */
	AAPLUS_EXPORT_LIB double CAAEquationOfTime_Calculate(double JD, bool bHighPrecision) { return CAAEquationOfTime::Calculate(JD, bHighPrecision); }

	/* CAAEquinoxesAndSolstices export functions */
	AAPLUS_EXPORT_LIB double CAAEquinoxesAndSolstices_NorthwardEquinox(long Year, bool bHighPrecision) { return CAAEquinoxesAndSolstices::NorthwardEquinox(Year, bHighPrecision); }
	AAPLUS_EXPORT_LIB double CAAEquinoxesAndSolstices_NorthernSolstice(long Year, bool bHighPrecision) { return CAAEquinoxesAndSolstices::NorthernSolstice(Year, bHighPrecision); }
	AAPLUS_EXPORT_LIB double CAAEquinoxesAndSolstices_SouthwardEquinox(long Year, bool bHighPrecision) { return CAAEquinoxesAndSolstices::SouthwardEquinox(Year, bHighPrecision); }
	AAPLUS_EXPORT_LIB double CAAEquinoxesAndSolstices_SouthernSolstice(long Year, bool bHighPrecision) { return CAAEquinoxesAndSolstices::SouthernSolstice(Year, bHighPrecision); }
	AAPLUS_EXPORT_LIB double CAAEquinoxesAndSolstices_LengthOfSpring(long Year, bool bNorthernHemisphere, bool bHighPrecision) { return CAAEquinoxesAndSolstices::LengthOfSpring(Year, bNorthernHemisphere, bHighPrecision); }
	AAPLUS_EXPORT_LIB double CAAEquinoxesAndSolstices_LengthOfSummer(long Year, bool bNorthernHemisphere, bool bHighPrecision) { return CAAEquinoxesAndSolstices::LengthOfSummer(Year, bNorthernHemisphere, bHighPrecision); }
	AAPLUS_EXPORT_LIB double CAAEquinoxesAndSolstices_LengthOfAutumn(long Year, bool bNorthernHemisphere, bool bHighPrecision) { return CAAEquinoxesAndSolstices::LengthOfAutumn(Year, bNorthernHemisphere, bHighPrecision); }
	AAPLUS_EXPORT_LIB double CAAEquinoxesAndSolstices_LengthOfWinter(long Year, bool bNorthernHemisphere, bool bHighPrecision) { return CAAEquinoxesAndSolstices::LengthOfWinter(Year, bNorthernHemisphere, bHighPrecision); }

	/* CAAEquinoxesAndSolstices2 export functions */
	AAPLUS_EXPORT_LIB CAAEquinoxSolsticeDetails2* CAAEquinoxesAndSolstices2_Calculate(double StartJD, double EndJD, double StepInterval, bool bHighPrecision, int* count) {
		auto res = CAAEquinoxesAndSolstices2::Calculate(StartJD, EndJD, StepInterval, bHighPrecision);
		*count = static_cast<int>(res.size());
		auto data = new CAAEquinoxSolsticeDetails2[*count];
		for (auto i = 0; i < *count; i++) data[i] = res[i];
		return data;
	}
	AAPLUS_EXPORT_LIB void CAAEquinoxesAndSolstices2_DestroyData(CAAEquinoxSolsticeDetails2* data) {
		delete[] data;
	}

	/* CAAFK5 export functions */
	AAPLUS_EXPORT_LIB double CAAFK5_CorrectionInLongitude(double Longitude, double Latitude, double JD) { return CAAFK5::CorrectionInLongitude(Longitude, Latitude, JD); }
	AAPLUS_EXPORT_LIB double CAAFK5_CorrectionInLatitude(double Longitude, double JD) { return CAAFK5::CorrectionInLatitude(Longitude, JD); }
	AAPLUS_EXPORT_LIB CAA3DCoordinate CAAFK5_ConvertVSOPToFK5J2000(const CAA3DCoordinate& value) { return CAAFK5::ConvertVSOPToFK5J2000(value); }
	AAPLUS_EXPORT_LIB CAA3DCoordinate CAAFK5_ConvertVSOPToFK5B1950(const CAA3DCoordinate& value) { return CAAFK5::ConvertVSOPToFK5B1950(value); }
	AAPLUS_EXPORT_LIB CAA3DCoordinate CAAFK5_ConvertVSOPToFK5AnyEquinox(const CAA3DCoordinate& value, double JDEquinox) { return CAAFK5::ConvertVSOPToFK5AnyEquinox(value, JDEquinox); }

	/* CAAGalileanMoons export functions */
	AAPLUS_EXPORT_LIB CAAGalileanMoonsDetails CAAGalileanMoons_Calculate(double JD, bool bHighPrecision) { return CAAGalileanMoons::Calculate(JD, bHighPrecision); }

	/* CAAGlobe export functions */
	AAPLUS_EXPORT_LIB double CAAGlobe_RhoSinThetaPrime(double GeographicalLatitude, double Height) { return CAAGlobe::RhoSinThetaPrime(GeographicalLatitude, Height); }
	AAPLUS_EXPORT_LIB double CAAGlobe_RhoCosThetaPrime(double GeographicalLatitude, double Height) { return CAAGlobe::RhoCosThetaPrime(GeographicalLatitude, Height); }
	AAPLUS_EXPORT_LIB double CAAGlobe_RadiusOfParallelOfLatitude(double GeographicalLatitude) { return CAAGlobe::RadiusOfParallelOfLatitude(GeographicalLatitude); }
	AAPLUS_EXPORT_LIB double CAAGlobe_RadiusOfCurvature(double GeographicalLatitude) { return CAAGlobe::RadiusOfCurvature(GeographicalLatitude); }
	AAPLUS_EXPORT_LIB double CAAGlobe_DistanceBetweenPoints(double GeographicalLatitude1, double GeographicalLongitude1, double GeographicalLatitude2, double GeographicalLongitude2) { return CAAGlobe::DistanceBetweenPoints(GeographicalLatitude1, GeographicalLongitude1, GeographicalLatitude2, GeographicalLongitude2); }

	/* CAAIlluminatedFraction export functions */
	AAPLUS_EXPORT_LIB double CAAIlluminatedFraction_PhaseAngle(double r, double R, double Delta) { return CAAIlluminatedFraction::PhaseAngle(r, R, Delta); }
	AAPLUS_EXPORT_LIB double CAAIlluminatedFraction_PhaseAngle_2(double R, double R0, double B, double L, double L0, double Delta) { return CAAIlluminatedFraction::PhaseAngle(R, R0, B, L, L0, Delta); }
	AAPLUS_EXPORT_LIB double CAAIlluminatedFraction_PhaseAngleRectangular(double x, double y, double z, double B, double L, double Delta) { return CAAIlluminatedFraction::PhaseAngleRectangular(x, y, z, B, L, Delta); }
	AAPLUS_EXPORT_LIB double CAAIlluminatedFraction_IlluminatedFraction(double PhaseAngle) { return CAAIlluminatedFraction::IlluminatedFraction(PhaseAngle); }
	AAPLUS_EXPORT_LIB double CAAIlluminatedFraction_IlluminatedFraction_2(double r, double R, double Delta) { return CAAIlluminatedFraction::IlluminatedFraction(r, R, Delta); }
	AAPLUS_EXPORT_LIB double CAAIlluminatedFraction_MercuryMagnitudeMuller(double r, double Delta, double i) { return CAAIlluminatedFraction::MercuryMagnitudeMuller(r, Delta, i); }
	AAPLUS_EXPORT_LIB double CAAIlluminatedFraction_VenusMagnitudeMuller(double r, double Delta, double i) { return CAAIlluminatedFraction::VenusMagnitudeMuller(r, Delta, i); }
	AAPLUS_EXPORT_LIB double CAAIlluminatedFraction_MarsMagnitudeMuller(double r, double Delta, double i) { return CAAIlluminatedFraction::MarsMagnitudeMuller(r, Delta, i); }
	AAPLUS_EXPORT_LIB double CAAIlluminatedFraction_JupiterMagnitudeMuller(double r, double Delta) { return CAAIlluminatedFraction::JupiterMagnitudeMuller(r, Delta); }
	AAPLUS_EXPORT_LIB double CAAIlluminatedFraction_SaturnMagnitudeMuller(double r, double Delta, double DeltaU, double B) { return CAAIlluminatedFraction::SaturnMagnitudeMuller(r, Delta, DeltaU, B); }
	AAPLUS_EXPORT_LIB double CAAIlluminatedFraction_UranusMagnitudeMuller(double r, double Delta) { return CAAIlluminatedFraction::UranusMagnitudeMuller(r, Delta); }
	AAPLUS_EXPORT_LIB double CAAIlluminatedFraction_NeptuneMagnitudeMuller(double r, double Delta) { return CAAIlluminatedFraction::NeptuneMagnitudeMuller(r, Delta); }
	AAPLUS_EXPORT_LIB double CAAIlluminatedFraction_MercuryMagnitudeAA(double r, double Delta, double i) { return CAAIlluminatedFraction::MercuryMagnitudeAA(r, Delta, i); }
	AAPLUS_EXPORT_LIB double CAAIlluminatedFraction_VenusMagnitudeAA(double r, double Delta, double i) { return CAAIlluminatedFraction::VenusMagnitudeAA(r, Delta, i); }
	AAPLUS_EXPORT_LIB double CAAIlluminatedFraction_MarsMagnitudeAA(double r, double Delta, double i) { return CAAIlluminatedFraction::MarsMagnitudeAA(r, Delta, i); }
	AAPLUS_EXPORT_LIB double CAAIlluminatedFraction_JupiterMagnitudeAA(double r, double Delta, double i) { return CAAIlluminatedFraction::JupiterMagnitudeAA(r, Delta, i); }
	AAPLUS_EXPORT_LIB double CAAIlluminatedFraction_SaturnMagnitudeAA(double r, double Delta, double DeltaU, double B) { return CAAIlluminatedFraction::SaturnMagnitudeAA(r, Delta, DeltaU, B); }
	AAPLUS_EXPORT_LIB double CAAIlluminatedFraction_UranusMagnitudeAA(double r, double Delta) { return CAAIlluminatedFraction::UranusMagnitudeAA(r, Delta); }
	AAPLUS_EXPORT_LIB double CAAIlluminatedFraction_NeptuneMagnitudeAA(double r, double Delta) { return CAAIlluminatedFraction::NeptuneMagnitudeAA(r, Delta); }
	AAPLUS_EXPORT_LIB double CAAIlluminatedFraction_PlutoMagnitudeAA(double r, double Delta) { return CAAIlluminatedFraction::PlutoMagnitudeAA(r, Delta); }

	/* CAAInterpolate export functions */
	AAPLUS_EXPORT_LIB double CAAInterpolate_Interpolate(double n, double Y1, double Y2, double Y3) { return CAAInterpolate::Interpolate(n, Y1, Y2, Y3); }
	AAPLUS_EXPORT_LIB double CAAInterpolate_Interpolate_2(double n, double Y1, double Y2, double Y3, double Y4, double Y5) { return CAAInterpolate::Interpolate(n, Y1, Y2, Y3, Y4, Y5); }
	AAPLUS_EXPORT_LIB double CAAInterpolate_InterpolateToHalves(double Y1, double Y2, double Y3, double Y4) { return CAAInterpolate::InterpolateToHalves(Y1, Y2, Y3, Y4); }
	AAPLUS_EXPORT_LIB double CAAInterpolate_LagrangeInterpolate(double X, int n, const double* pX, const double* pY) { return CAAInterpolate::LagrangeInterpolate(X, n, pX, pY); }
	AAPLUS_EXPORT_LIB double CAAInterpolate_Extremum(double Y1, double Y2, double Y3, double& nm) { return CAAInterpolate::Extremum(Y1, Y2, Y3, nm); }
	AAPLUS_EXPORT_LIB double CAAInterpolate_Extremum_2(double Y1, double Y2, double Y3, double Y4, double Y5, double& nm, double epsilon) { return CAAInterpolate::Extremum(Y1, Y2, Y3, Y4, Y5, nm, epsilon); }
	AAPLUS_EXPORT_LIB double CAAInterpolate_Zero(double Y1, double Y2, double Y3, double epsilon) { return CAAInterpolate::Zero(Y1, Y2, Y3, epsilon); }
	AAPLUS_EXPORT_LIB double CAAInterpolate_Zero_2(double Y1, double Y2, double Y3, double Y4, double Y5, double epsilon) { return CAAInterpolate::Zero(Y1, Y2, Y3, Y4, Y5, epsilon); }
	AAPLUS_EXPORT_LIB double CAAInterpolate_Zero2(double Y1, double Y2, double Y3, double epsilon) { return CAAInterpolate::Zero2(Y1, Y2, Y3, epsilon); }
	AAPLUS_EXPORT_LIB double CAAInterpolate_Zero2_2(double Y1, double Y2, double Y3, double Y4, double Y5, double epsilon) { return CAAInterpolate::Zero2(Y1, Y2, Y3, Y4, Y5, epsilon); }

	/* CAAJewishCalendar export functions */
	AAPLUS_EXPORT_LIB CAACalendarDate CAAJewishCalendar_DateOfPesach(long Year, bool bGregorianCalendar) { return CAAJewishCalendar::DateOfPesach(Year, bGregorianCalendar); }
	AAPLUS_EXPORT_LIB bool CAAJewishCalendar_IsLeap(long Year) { return CAAJewishCalendar::IsLeap(Year); }
	AAPLUS_EXPORT_LIB long CAAJewishCalendar_DaysInYear(long Year) { return CAAJewishCalendar::DaysInYear(Year); }

	/* CAAJupiter export functions */
	AAPLUS_EXPORT_LIB double CAAJupiter_EclipticLongitude(double JD, bool bHighPrecision) { return CAAJupiter::EclipticLongitude(JD, bHighPrecision); }
	AAPLUS_EXPORT_LIB double CAAJupiter_EclipticLatitude(double JD, bool bHighPrecision) { return CAAJupiter::EclipticLatitude(JD, bHighPrecision); }
	AAPLUS_EXPORT_LIB double CAAJupiter_RadiusVector(double JD, bool bHighPrecision) { return CAAJupiter::RadiusVector(JD, bHighPrecision); }

	/* CAAKepler export functions */
	AAPLUS_EXPORT_LIB double CAAKepler_Calculate(double M, double e, int nIterations) { return CAAKepler::Calculate(M, e, nIterations); }

	/* CAAMars export functions */
	AAPLUS_EXPORT_LIB double CAAMars_EclipticLongitude(double JD, bool bHighPrecision) { return CAAMars::EclipticLongitude(JD, bHighPrecision); }
	AAPLUS_EXPORT_LIB double CAAMars_EclipticLatitude(double JD, bool bHighPrecision) { return CAAMars::EclipticLatitude(JD, bHighPrecision); }
	AAPLUS_EXPORT_LIB double CAAMars_RadiusVector(double JD, bool bHighPrecision) { return CAAMars::RadiusVector(JD, bHighPrecision); }

	/* CAAMercury export functions */
	AAPLUS_EXPORT_LIB double CAAMercury_EclipticLongitude(double JD, bool bHighPrecision) { return CAAMercury::EclipticLongitude(JD, bHighPrecision); }
	AAPLUS_EXPORT_LIB double CAAMercury_EclipticLatitude(double JD, bool bHighPrecision) { return CAAMercury::EclipticLatitude(JD, bHighPrecision); }
	AAPLUS_EXPORT_LIB double CAAMercury_RadiusVector(double JD, bool bHighPrecision) { return CAAMercury::RadiusVector(JD, bHighPrecision); }

	/* CAAMoon export functions */
	AAPLUS_EXPORT_LIB double CAAMoon_MeanLongitude(double JD) { return CAAMoon::MeanLongitude(JD); }
	AAPLUS_EXPORT_LIB double CAAMoon_MeanElongation(double JD) { return CAAMoon::MeanElongation(JD); }
	AAPLUS_EXPORT_LIB double CAAMoon_MeanAnomaly(double JD) { return CAAMoon::MeanAnomaly(JD); }
	AAPLUS_EXPORT_LIB double CAAMoon_ArgumentOfLatitude(double JD) { return CAAMoon::ArgumentOfLatitude(JD); }
	AAPLUS_EXPORT_LIB double CAAMoon_MeanLongitudeAscendingNode(double JD) { return CAAMoon::MeanLongitudeAscendingNode(JD); }
	AAPLUS_EXPORT_LIB double CAAMoon_MeanLongitudePerigee(double JD) { return CAAMoon::MeanLongitudePerigee(JD); }
	AAPLUS_EXPORT_LIB double CAAMoon_TrueLongitudeAscendingNode(double JD) { return CAAMoon::TrueLongitudeAscendingNode(JD); }
	AAPLUS_EXPORT_LIB double CAAMoon_EclipticLongitude(double JD) { return CAAMoon::EclipticLongitude(JD); }
	AAPLUS_EXPORT_LIB double CAAMoon_EclipticLatitude(double JD) { return CAAMoon::EclipticLatitude(JD); }
	AAPLUS_EXPORT_LIB double CAAMoon_RadiusVector(double JD) { return CAAMoon::RadiusVector(JD); }
	AAPLUS_EXPORT_LIB double CAAMoon_RadiusVectorToHorizontalParallax(double RadiusVector) { return CAAMoon::RadiusVectorToHorizontalParallax(RadiusVector); }
	AAPLUS_EXPORT_LIB double CAAMoon_HorizontalParallaxToRadiusVector(double Parallax) { return CAAMoon::HorizontalParallaxToRadiusVector(Parallax); }

	/* CAAMoonIlluminatedFraction export functions */
	AAPLUS_EXPORT_LIB double CAAMoonIlluminatedFraction_GeocentricElongation(double ObjectAlpha, double ObjectDelta, double SunAlpha, double SunDelta) { return CAAMoonIlluminatedFraction::GeocentricElongation(ObjectAlpha, ObjectDelta, SunAlpha, SunDelta); }
	AAPLUS_EXPORT_LIB double CAAMoonIlluminatedFraction_PhaseAngle(double GeocentricElongation, double EarthObjectDistance, double EarthSunDistance) { return CAAMoonIlluminatedFraction::PhaseAngle(GeocentricElongation, EarthObjectDistance, EarthSunDistance); }
	AAPLUS_EXPORT_LIB double CAAMoonIlluminatedFraction_IlluminatedFraction(double PhaseAngle) { return CAAMoonIlluminatedFraction::IlluminatedFraction(PhaseAngle); }
	AAPLUS_EXPORT_LIB double CAAMoonIlluminatedFraction_PositionAngle(double Alpha0, double Delta0, double Alpha, double Delta) { return CAAMoonIlluminatedFraction::PositionAngle(Alpha0, Delta0, Alpha, Delta); }

	/* CAAMoonMaxDeclinations export functions */
	AAPLUS_EXPORT_LIB double CAAMoonMaxDeclinations_K(double Year) { return CAAMoonMaxDeclinations::K(Year); }
	AAPLUS_EXPORT_LIB double CAAMoonMaxDeclinations_MeanGreatestDeclination(double k, bool bNortherly) { return CAAMoonMaxDeclinations::MeanGreatestDeclination(k, bNortherly); }
	AAPLUS_EXPORT_LIB double CAAMoonMaxDeclinations_MeanGreatestDeclinationValue(double k) { return CAAMoonMaxDeclinations::MeanGreatestDeclinationValue(k); }
	AAPLUS_EXPORT_LIB double CAAMoonMaxDeclinations_TrueGreatestDeclination(double k, bool bNortherly) { return CAAMoonMaxDeclinations::TrueGreatestDeclination(k, bNortherly); }
	AAPLUS_EXPORT_LIB double CAAMoonMaxDeclinations_TrueGreatestDeclinationValue(double k, bool bNortherly) { return CAAMoonMaxDeclinations::TrueGreatestDeclinationValue(k, bNortherly); }

	/* CAAMoonMaxDeclinations2 export functions */
	AAPLUS_EXPORT_LIB CAAMoonMaxDeclinationsDetails2* CAAMoonMaxDeclinations2_Calculate(double StartJD, double EndJD, double StepInterval, CAAMoonMaxDeclinations2::Algorithm algorithm, int* count) {
		auto res = CAAMoonMaxDeclinations2::Calculate(StartJD, EndJD, StepInterval, algorithm);
		*count = static_cast<int>(res.size());
		auto data = new CAAMoonMaxDeclinationsDetails2[*count];
		for (auto i = 0; i < *count; i++) data[i] = res[i];
		return data;
	}
	AAPLUS_EXPORT_LIB void CAAMoonMaxDeclinations2_DestroyData(CAAMoonMaxDeclinationsDetails2* data) {
		delete[] data;
	}

	/* CAAMoonNodes export functions */
	AAPLUS_EXPORT_LIB double CAAMoonNodes_K(double Year) { return CAAMoonNodes::K(Year); }
	AAPLUS_EXPORT_LIB double CAAMoonNodes_PassageThroNode(double k) { return CAAMoonNodes::PassageThroNode(k); }

	/* CAAMoonNodes2 export functions */
	AAPLUS_EXPORT_LIB CAAMoonNodesDetails2* CAAMoonNodes2_Calculate(double StartJD, double EndJD, double StepInterval, CAAMoonNodes2::Algorithm algorithm, int* count) {
		auto res = CAAMoonNodes2::Calculate(StartJD, EndJD, StepInterval, algorithm);
		*count = static_cast<int>(res.size());
		auto data = new CAAMoonNodesDetails2[*count];
		for (auto i = 0; i < *count; i++) data[i] = res[i];
		return data;
	}
	AAPLUS_EXPORT_LIB void CAAMoonNodes2_DestroyData(CAAMoonNodesDetails2* data) {
		delete[] data;
	}

	/* CAAMoonPerigeeApogee export functions */
	AAPLUS_EXPORT_LIB double CAAMoonPerigeeApogee_K(double Year) { return CAAMoonPerigeeApogee::K(Year); }
	AAPLUS_EXPORT_LIB double CAAMoonPerigeeApogee_MeanPerigee(double k) { return CAAMoonPerigeeApogee::MeanPerigee(k); }
	AAPLUS_EXPORT_LIB double CAAMoonPerigeeApogee_MeanApogee(double k) { return CAAMoonPerigeeApogee::MeanApogee(k); }
	AAPLUS_EXPORT_LIB double CAAMoonPerigeeApogee_TruePerigee(double k) { return CAAMoonPerigeeApogee::TruePerigee(k); }
	AAPLUS_EXPORT_LIB double CAAMoonPerigeeApogee_TrueApogee(double k) { return CAAMoonPerigeeApogee::TrueApogee(k); }
	AAPLUS_EXPORT_LIB double CAAMoonPerigeeApogee_PerigeeParallax(double k) { return CAAMoonPerigeeApogee::PerigeeParallax(k); }
	AAPLUS_EXPORT_LIB double CAAMoonPerigeeApogee_ApogeeParallax(double k) { return CAAMoonPerigeeApogee::ApogeeParallax(k); }

	/* CAAMoonPerigeeApogee2 export functions */
	AAPLUS_EXPORT_LIB CAAMoonPerigeeApogeeDetails2* CAAMoonPerigeeApogee2_Calculate(double StartJD, double EndJD, double StepInterval, CAAMoonPerigeeApogee2::Algorithm algorithm, int* count) {
		auto res = CAAMoonPerigeeApogee2::Calculate(StartJD, EndJD, StepInterval, algorithm);
		*count = static_cast<int>(res.size());
		auto data = new CAAMoonPerigeeApogeeDetails2[*count];
		for (auto i = 0; i < *count; i++) data[i] = res[i];
		return data;
	}
	AAPLUS_EXPORT_LIB void CAAMoonPerigeeApogee2_DestroyData(CAAMoonPerigeeApogeeDetails2* data) {
		delete[] data;
	}

	/* CAAMoonPhases export functions */
	AAPLUS_EXPORT_LIB double CAAMoonPhases_K(double Year) { return CAAMoonPhases::K(Year); }
	AAPLUS_EXPORT_LIB double CAAMoonPhases_MeanPhase(double k) { return CAAMoonPhases::MeanPhase(k); }
	AAPLUS_EXPORT_LIB double CAAMoonPhases_TruePhase(double k) { return CAAMoonPhases::TruePhase(k); }

	/* CAAMoonPhases2 export functions */
	AAPLUS_EXPORT_LIB CAAMoonPhasesDetails2* CAAMoonPhases2_Calculate(double StartJD, double EndJD, double StepInterval, CAAMoonPhases2::Algorithm algorithm, int* count) {
		auto res = CAAMoonPhases2::Calculate(StartJD, EndJD, StepInterval, algorithm);
		*count = static_cast<int>(res.size());
		auto data = new CAAMoonPhasesDetails2[*count];
		for (auto i = 0; i < *count; i++) data[i] = res[i];
		return data;
	}
	AAPLUS_EXPORT_LIB void CAAMoonPhases2_DestroyData(CAAMoonPhasesDetails2* data) {
		delete[] data;
	}

	/* CAAMoslemCalendar export functions */
	AAPLUS_EXPORT_LIB CAACalendarDate CAAMoslemCalendar_MoslemToJulian(long Year, long Month, long Day) { return CAAMoslemCalendar::MoslemToJulian(Year, Month, Day); }
	AAPLUS_EXPORT_LIB CAACalendarDate CAAMoslemCalendar_JulianToMoslem(long Year, long Month, long Day) { return CAAMoslemCalendar::JulianToMoslem(Year, Month, Day); }
	AAPLUS_EXPORT_LIB bool CAAMoslemCalendar_IsLeap(long Year) { return CAAMoslemCalendar::IsLeap(Year); }

	/* CAANearParabolic export functions */
	AAPLUS_EXPORT_LIB CAANearParabolicObjectDetails CAANearParabolic_Calculate(double JD, const CAANearParabolicObjectElements& elements, bool bHighPrecision) { return CAANearParabolic::Calculate(JD, elements, bHighPrecision); }
	AAPLUS_EXPORT_LIB double CAANearParabolic_cbrt(double x) { return CAANearParabolic::cbrt(x); }
	AAPLUS_EXPORT_LIB void CAANearParabolic_CalculateTrueAnomalyAndRadius(double JD, const CAANearParabolicObjectElements& elements, double& v, double& r) { return CAANearParabolic::CalculateTrueAnomalyAndRadius(JD, elements, v, r); }

	/* CAANeptune export functions */
	AAPLUS_EXPORT_LIB double CAANeptune_EclipticLongitude(double JD, bool bHighPrecision) { return CAANeptune::EclipticLongitude(JD, bHighPrecision); }
	AAPLUS_EXPORT_LIB double CAANeptune_EclipticLatitude(double JD, bool bHighPrecision) { return CAANeptune::EclipticLatitude(JD, bHighPrecision); }
	AAPLUS_EXPORT_LIB double CAANeptune_RadiusVector(double JD, bool bHighPrecision) { return CAANeptune::RadiusVector(JD, bHighPrecision); }

	/* CAANodes export functions */
	AAPLUS_EXPORT_LIB CAANodeObjectDetails CAANodes_PassageThroAscendingNode(const CAAEllipticalObjectElements& elements) { return CAANodes::PassageThroAscendingNode(elements); }
	AAPLUS_EXPORT_LIB CAANodeObjectDetails CAANodes_PassageThroDescendingNode(const CAAEllipticalObjectElements& elements) { return CAANodes::PassageThroDescendingNode(elements); }
	AAPLUS_EXPORT_LIB CAANodeObjectDetails CAANodes_PassageThroAscendingNode_2(const CAAParabolicObjectElements& elements) { return CAANodes::PassageThroAscendingNode(elements); }
	AAPLUS_EXPORT_LIB CAANodeObjectDetails CAANodes_PassageThroDescendingNode_2(const CAAParabolicObjectElements& elements) { return CAANodes::PassageThroDescendingNode(elements); }

	/* CAANutation export functions */
	AAPLUS_EXPORT_LIB double CAANutation_NutationInLongitude(double JD) { return CAANutation::NutationInLongitude(JD); }
	AAPLUS_EXPORT_LIB double CAANutation_NutationInObliquity(double JD) { return CAANutation::NutationInObliquity(JD); }
	AAPLUS_EXPORT_LIB double CAANutation_NutationInRightAscension(double Alpha, double Delta, double Obliquity, double NutationInLongitude, double NutationInObliquity) { return CAANutation::NutationInRightAscension(Alpha, Delta, Obliquity, NutationInLongitude, NutationInObliquity); }
	AAPLUS_EXPORT_LIB double CAANutation_NutationInDeclination(double Alpha, double Obliquity, double NutationInLongitude, double NutationInObliquity) { return CAANutation::NutationInDeclination(Alpha, Obliquity, NutationInLongitude, NutationInObliquity); }
	AAPLUS_EXPORT_LIB double CAANutation_MeanObliquityOfEcliptic(double JD) { return CAANutation::MeanObliquityOfEcliptic(JD); }
	AAPLUS_EXPORT_LIB double CAANutation_TrueObliquityOfEcliptic(double JD) { return CAANutation::TrueObliquityOfEcliptic(JD); }

	/* CAAParabolic export functions */
	AAPLUS_EXPORT_LIB double CAAParabolic_CalculateBarkers(double W, double epsilon) { return CAAParabolic::CalculateBarkers(W, epsilon); }
	AAPLUS_EXPORT_LIB CAAParabolicObjectDetails CAAParabolic_Calculate(double JD, const CAAParabolicObjectElements& elements, bool bHighPrecision, double epsilon) { return CAAParabolic::Calculate(JD, elements, bHighPrecision, epsilon); }

	/* CAAParallactic export functions */
	AAPLUS_EXPORT_LIB double CAAParallactic_ParallacticAngle(double HourAngle, double Latitude, double delta) { return CAAParallactic::ParallacticAngle(HourAngle, Latitude, delta); }
	AAPLUS_EXPORT_LIB double CAAParallactic_EclipticLongitudeOnHorizon(double LocalSiderealTime, double ObliquityOfEcliptic, double Latitude) { return CAAParallactic::EclipticLongitudeOnHorizon(LocalSiderealTime, ObliquityOfEcliptic, Latitude); }
	AAPLUS_EXPORT_LIB double CAAParallactic_AngleBetweenEclipticAndHorizon(double LocalSiderealTime, double ObliquityOfEcliptic, double Latitude) { return CAAParallactic::AngleBetweenEclipticAndHorizon(LocalSiderealTime, ObliquityOfEcliptic, Latitude); }
	AAPLUS_EXPORT_LIB double CAAParallactic_AngleBetweenNorthCelestialPoleAndNorthPoleOfEcliptic(double Lambda, double Beta, double ObliquityOfEcliptic) { return CAAParallactic::AngleBetweenNorthCelestialPoleAndNorthPoleOfEcliptic(Lambda, Beta, ObliquityOfEcliptic); }

	/* CAAParallax export functions */
	AAPLUS_EXPORT_LIB CAA2DCoordinate CAAParallax_Equatorial2TopocentricDelta(double Alpha, double Delta, double Distance, double Longitude, double Latitude, double Height, double JD) { return CAAParallax::Equatorial2TopocentricDelta(Alpha, Delta, Distance, Longitude, Latitude, Height, JD); }
	AAPLUS_EXPORT_LIB CAA2DCoordinate CAAParallax_Equatorial2Topocentric(double Alpha, double Delta, double Distance, double Longitude, double Latitude, double Height, double JD) { return CAAParallax::Equatorial2Topocentric(Alpha, Delta, Distance, Longitude, Latitude, Height, JD); }
	AAPLUS_EXPORT_LIB CAATopocentricEclipticDetails CAAParallax_Ecliptic2Topocentric(double Lambda, double Beta, double Semidiameter, double Distance, double Epsilon, double Latitude, double Height, double JD) { return CAAParallax::Ecliptic2Topocentric(Lambda, Beta, Semidiameter, Distance, Epsilon, Latitude, Height, JD); }
	AAPLUS_EXPORT_LIB double CAAParallax_ParallaxToDistance(double Parallax) { return CAAParallax::ParallaxToDistance(Parallax); }
	AAPLUS_EXPORT_LIB double CAAParallax_DistanceToParallax(double Distance) { return CAAParallax::DistanceToParallax(Distance); }

	/* CAAPhysicalJupiter export functions */
	AAPLUS_EXPORT_LIB CAAPhysicalJupiterDetails CAAPhysicalJupiter_Calculate(double JD, bool bHighPrecision) { return CAAPhysicalJupiter::Calculate(JD, bHighPrecision); }

	/* CAAPhysicalMars export functions */
	AAPLUS_EXPORT_LIB CAAPhysicalMarsDetails CAAPhysicalMars_Calculate(double JD, bool bHighPrecision) { return CAAPhysicalMars::Calculate(JD, bHighPrecision); }

	/* CAAPhysicalMoon export functions */
	AAPLUS_EXPORT_LIB CAAPhysicalMoonDetails CAAPhysicalMoon_CalculateGeocentric(double JD) { return CAAPhysicalMoon::CalculateGeocentric(JD); }
	AAPLUS_EXPORT_LIB CAAPhysicalMoonDetails CAAPhysicalMoon_CalculateTopocentric(double JD, double Longitude, double Latitude) { return CAAPhysicalMoon::CalculateTopocentric(JD, Longitude, Latitude); }
	AAPLUS_EXPORT_LIB CAASelenographicMoonDetails CAAPhysicalMoon_CalculateSelenographicPositionOfSun(double JD, bool bHighPrecision) { return CAAPhysicalMoon::CalculateSelenographicPositionOfSun(JD, bHighPrecision); }
	AAPLUS_EXPORT_LIB double CAAPhysicalMoon_AltitudeOfSun(double JD, double Longitude, double Latitude, bool bHighPrecision) { return CAAPhysicalMoon::AltitudeOfSun(JD, Longitude, Latitude, bHighPrecision); }
	AAPLUS_EXPORT_LIB double CAAPhysicalMoon_TimeOfSunrise(double JD, double Longitude, double Latitude, bool bHighPrecision) { return CAAPhysicalMoon::TimeOfSunrise(JD, Longitude, Latitude, bHighPrecision); }
	AAPLUS_EXPORT_LIB double CAAPhysicalMoon_TimeOfSunset(double JD, double Longitude, double Latitude, bool bHighPrecision) { return CAAPhysicalMoon::TimeOfSunset(JD, Longitude, Latitude, bHighPrecision); }

	/* CAAPhysicalSun export functions */
	AAPLUS_EXPORT_LIB CAAPhysicalSunDetails CAAPhysicalSun_Calculate(double JD, bool bHighPrecision) { return CAAPhysicalSun::Calculate(JD, bHighPrecision); }
	AAPLUS_EXPORT_LIB double CAAPhysicalSun_TimeOfStartOfRotation(long C) { return CAAPhysicalSun::TimeOfStartOfRotation(C); }

	/* CAAPlanetaryPhenomena export functions */
	AAPLUS_EXPORT_LIB double CAAPlanetaryPhenomena_K(double Year, CAAPlanetaryPhenomena::Planet planet, CAAPlanetaryPhenomena::Type type) { return CAAPlanetaryPhenomena::K(Year, planet, type); }
	AAPLUS_EXPORT_LIB double CAAPlanetaryPhenomena_Mean(double k, CAAPlanetaryPhenomena::Planet planet, CAAPlanetaryPhenomena::Type type) { return CAAPlanetaryPhenomena::Mean(k, planet, type); }
	AAPLUS_EXPORT_LIB double CAAPlanetaryPhenomena_True(double k, CAAPlanetaryPhenomena::Planet planet, CAAPlanetaryPhenomena::Type type) { return CAAPlanetaryPhenomena::True(k, planet, type); }
	AAPLUS_EXPORT_LIB double CAAPlanetaryPhenomena_ElongationValue(double k, CAAPlanetaryPhenomena::Planet planet, bool bEastern) { return CAAPlanetaryPhenomena::ElongationValue(k, planet, bEastern); }

	/* CAAPlanetaryPhenomena2 export functions */
	AAPLUS_EXPORT_LIB CAAPlanetaryPhenomenaDetails2* CAAPlanetaryPhenomena2_Calculate(double StartJD, double EndJD, CAAPlanetaryPhenomena2::Object object, double StepInterval, bool bHighPrecision, int* count) {
		auto res = CAAPlanetaryPhenomena2::Calculate(StartJD, EndJD, object, StepInterval, bHighPrecision);
		*count = static_cast<int>(res.size());
		auto data = new CAAPlanetaryPhenomenaDetails2[*count];
		for (auto i = 0; i < *count; i++) data[i] = res[i];
		return data;
	}
	AAPLUS_EXPORT_LIB void CAAPlanetaryPhenomena2_DestroyData(CAAPlanetaryPhenomenaDetails2* data) {
		delete[] data;
	}

	/* CAAPlanetPerihelionAphelion export functions */
	AAPLUS_EXPORT_LIB double CAAPlanetPerihelionAphelion_MercuryK(double Year) { return CAAPlanetPerihelionAphelion::MercuryK(Year); }
	AAPLUS_EXPORT_LIB double CAAPlanetPerihelionAphelion_Mercury(double k) { return CAAPlanetPerihelionAphelion::Mercury(k); }
	AAPLUS_EXPORT_LIB double CAAPlanetPerihelionAphelion_VenusK(double Year) { return CAAPlanetPerihelionAphelion::VenusK(Year); }
	AAPLUS_EXPORT_LIB double CAAPlanetPerihelionAphelion_Venus(double k) { return CAAPlanetPerihelionAphelion::Venus(k); }
	AAPLUS_EXPORT_LIB double CAAPlanetPerihelionAphelion_EarthK(double Year) { return CAAPlanetPerihelionAphelion::EarthK(Year); }
	AAPLUS_EXPORT_LIB double CAAPlanetPerihelionAphelion_EarthPerihelion(double k, bool bBarycentric) { return CAAPlanetPerihelionAphelion::EarthPerihelion(k, bBarycentric); }
	AAPLUS_EXPORT_LIB double CAAPlanetPerihelionAphelion_EarthAphelion(double k, bool bBarycentric) { return CAAPlanetPerihelionAphelion::EarthAphelion(k, bBarycentric); }
	AAPLUS_EXPORT_LIB double CAAPlanetPerihelionAphelion_MarsK(double Year) { return CAAPlanetPerihelionAphelion::MarsK(Year); }
	AAPLUS_EXPORT_LIB double CAAPlanetPerihelionAphelion_Mars(double k) { return CAAPlanetPerihelionAphelion::Mars(k); }
	AAPLUS_EXPORT_LIB double CAAPlanetPerihelionAphelion_JupiterK(double Year) { return CAAPlanetPerihelionAphelion::JupiterK(Year); }
	AAPLUS_EXPORT_LIB double CAAPlanetPerihelionAphelion_Jupiter(double k) { return CAAPlanetPerihelionAphelion::Jupiter(k); }
	AAPLUS_EXPORT_LIB double CAAPlanetPerihelionAphelion_SaturnK(double Year) { return CAAPlanetPerihelionAphelion::SaturnK(Year); }
	AAPLUS_EXPORT_LIB double CAAPlanetPerihelionAphelion_Saturn(double k) { return CAAPlanetPerihelionAphelion::Saturn(k); }
	AAPLUS_EXPORT_LIB double CAAPlanetPerihelionAphelion_UranusK(double Year) { return CAAPlanetPerihelionAphelion::UranusK(Year); }
	AAPLUS_EXPORT_LIB double CAAPlanetPerihelionAphelion_Uranus(double k) { return CAAPlanetPerihelionAphelion::Uranus(k); }
	AAPLUS_EXPORT_LIB double CAAPlanetPerihelionAphelion_NeptuneK(double Year) { return CAAPlanetPerihelionAphelion::NeptuneK(Year); }
	AAPLUS_EXPORT_LIB double CAAPlanetPerihelionAphelion_Neptune(double k) { return CAAPlanetPerihelionAphelion::Neptune(k); }

	/* CAAPlanetPerihelionAphelion2 export functions */
	AAPLUS_EXPORT_LIB CAAPlanetPerihelionAphelionDetails2* CAAPlanetPerihelionAphelion2_Calculate(double StartJD, double EndJD, CAAPlanetPerihelionAphelion2::Object object, double StepInterval, bool bHighPrecision, int* count) {
		auto res = CAAPlanetPerihelionAphelion2::Calculate(StartJD, EndJD, object, StepInterval, bHighPrecision);
		*count = static_cast<int>(res.size());
		auto data = new CAAPlanetPerihelionAphelionDetails2[*count];
		for (auto i = 0; i < *count; i++) data[i] = res[i];
		return data;
	}
	AAPLUS_EXPORT_LIB void CAAPlanetPerihelionAphelion2_DestroyData(CAAPlanetPerihelionAphelionDetails2* data) {
		delete[] data;
	}

	/* CAAPluto export functions */
	AAPLUS_EXPORT_LIB double CAAPluto_EclipticLongitude(double JD) { return CAAPluto::EclipticLongitude(JD); }
	AAPLUS_EXPORT_LIB double CAAPluto_EclipticLatitude(double JD) { return CAAPluto::EclipticLatitude(JD); }
	AAPLUS_EXPORT_LIB double CAAPluto_RadiusVector(double JD) { return CAAPluto::RadiusVector(JD); }

	/* CAAPrecession export functions */
	AAPLUS_EXPORT_LIB CAA2DCoordinate CAAPrecession_PrecessEquatorial(double Alpha, double Delta, double JD0, double JD) { return CAAPrecession::PrecessEquatorial(Alpha, Delta, JD0, JD); }
	AAPLUS_EXPORT_LIB CAA2DCoordinate CAAPrecession_PrecessEquatorialFK4(double Alpha, double Delta, double JD0, double JD) { return CAAPrecession::PrecessEquatorialFK4(Alpha, Delta, JD0, JD); }
	AAPLUS_EXPORT_LIB CAA2DCoordinate CAAPrecession_PrecessEcliptic(double Lambda, double Beta, double JD0, double JD) { return CAAPrecession::PrecessEcliptic(Lambda, Beta, JD0, JD); }
	AAPLUS_EXPORT_LIB CAA2DCoordinate CAAPrecession_EquatorialPMToEcliptic(double Alpha, double Delta, double Beta, double PMAlpha, double PMDelta, double Epsilon) { return CAAPrecession::EquatorialPMToEcliptic(Alpha, Delta, Beta, PMAlpha, PMDelta, Epsilon); }
	AAPLUS_EXPORT_LIB CAA2DCoordinate CAAPrecession_AdjustPositionUsingUniformProperMotion(double t, double Alpha, double Delta, double PMAlpha, double PMDelta) { return CAAPrecession::AdjustPositionUsingUniformProperMotion(t, Alpha, Delta, PMAlpha, PMDelta); }
	AAPLUS_EXPORT_LIB CAA2DCoordinate CAAPrecession_AdjustPositionUsingMotionInSpace(double r, double deltar, double t, double Alpha, double Delta, double PMAlpha, double PMDelta) { return CAAPrecession::AdjustPositionUsingMotionInSpace(r, deltar, t, Alpha, Delta, PMAlpha, PMDelta); }

	/* CAARefraction export functions */
	AAPLUS_EXPORT_LIB double CAARefraction_RefractionFromApparent(double Altitude, double Pressure, double Temperature) { return CAARefraction::RefractionFromApparent(Altitude, Pressure, Temperature); }
	AAPLUS_EXPORT_LIB double CAARefraction_RefractionFromTrue(double Altitude, double Pressure, double Temperature) { return CAARefraction::RefractionFromTrue(Altitude, Pressure, Temperature); }

	/* CAARiseTransitSet export functions */
	AAPLUS_EXPORT_LIB CAARiseTransitSetDetails CAARiseTransitSet_Calculate(double JD, double Alpha1, double Delta1, double Alpha2, double Delta2, double Alpha3, double Delta3, double Longitude, double Latitude, double h0) { return CAARiseTransitSet::Calculate(JD, Alpha1, Delta1, Alpha2, Delta2, Alpha3, Delta3, Longitude, Latitude, h0); }
	AAPLUS_EXPORT_LIB void CAARiseTransitSet_CorrectRAValuesForInterpolation(double& Alpha1, double& Alpha2, double& Alpha3) { return CAARiseTransitSet::CorrectRAValuesForInterpolation(Alpha1, Alpha2, Alpha3); }

	/* CAARiseTransitSet2 export functions */
	AAPLUS_EXPORT_LIB CAARiseTransitSetDetails2* CAARiseTransitSet2_Calculate(double StartJD, double EndJD, CAARiseTransitSet2::Object object, double Longitude, double Latitude, double h0, double StepInterval, bool bHighPrecision, int* count) {
		auto res = CAARiseTransitSet2::Calculate(StartJD, EndJD, object, Longitude, Latitude, h0, StepInterval, bHighPrecision);
		*count = static_cast<int>(res.size());
		auto data = new CAARiseTransitSetDetails2[*count];
		for (auto i = 0; i < *count; i++) data[i] = res[i];
		return data;
	}
	AAPLUS_EXPORT_LIB CAARiseTransitSetDetails2* CAARiseTransitSet2_CalculateMoon(double StartJD, double EndJD, double Longitude, double Latitude, double RefractionAtHorizon, double StepInterval, CAARiseTransitSet2::MoonAlgorithm algorithm, int* count) {
		auto res = CAARiseTransitSet2::CalculateMoon(StartJD, EndJD, Longitude, Latitude, RefractionAtHorizon, StepInterval, algorithm);
		*count = static_cast<int>(res.size());
		auto data = new CAARiseTransitSetDetails2[*count];
		for (auto i = 0; i < *count; i++) data[i] = res[i];
		return data;
	}
	AAPLUS_EXPORT_LIB CAARiseTransitSetDetails2* CAARiseTransitSet2_CalculateStationary(double StartJD, double EndJD, double Alpha, double Delta, double Longitude, double Latitude, double h0, double StepInterval, int* count) {
		auto res = CAARiseTransitSet2::CalculateStationary(StartJD, EndJD, Alpha, Delta, Longitude, Latitude, h0, StepInterval);
		*count = static_cast<int>(res.size());
		auto data = new CAARiseTransitSetDetails2[*count];
		for (auto i = 0; i < *count; i++) data[i] = res[i];
		return data;
	}
	AAPLUS_EXPORT_LIB void CAARiseTransitSet2_DestroyData(CAARiseTransitSetDetails2* data) {
		delete[] data;
	}

	/* CAASaturn export functions */
	AAPLUS_EXPORT_LIB double CAASaturn_EclipticLongitude(double JD, bool bHighPrecision) { return CAASaturn::EclipticLongitude(JD, bHighPrecision); }
	AAPLUS_EXPORT_LIB double CAASaturn_EclipticLatitude(double JD, bool bHighPrecision) { return CAASaturn::EclipticLatitude(JD, bHighPrecision); }
	AAPLUS_EXPORT_LIB double CAASaturn_RadiusVector(double JD, bool bHighPrecision) { return CAASaturn::RadiusVector(JD, bHighPrecision); }

	/* CAASaturnMoons export functions */
	AAPLUS_EXPORT_LIB CAASaturnMoonsDetails CAASaturnMoons_Calculate(double JD, bool bHighPrecision) { return CAASaturnMoons::Calculate(JD, bHighPrecision); }

	/* CAASaturnRings export functions */
	AAPLUS_EXPORT_LIB CAASaturnRingDetails CAASaturnRings_Calculate(double JD, bool bHighPrecision) { return CAASaturnRings::Calculate(JD, bHighPrecision); }

	/* CAASidereal export functions */
	AAPLUS_EXPORT_LIB double CAASidereal_MeanGreenwichSiderealTime(double JD) { return CAASidereal::MeanGreenwichSiderealTime(JD); }
	AAPLUS_EXPORT_LIB double CAASidereal_ApparentGreenwichSiderealTime(double JD) { return CAASidereal::ApparentGreenwichSiderealTime(JD); }

	/* CAAStellarMagnitudes export functions */
	AAPLUS_EXPORT_LIB double CAAStellarMagnitudes_CombinedMagnitude(double m1, double m2) { return CAAStellarMagnitudes::CombinedMagnitude(m1, m2); }
	AAPLUS_EXPORT_LIB double CAAStellarMagnitudes_CombinedMagnitude_2(int Magnitudes, const double* pMagnitudes) { return CAAStellarMagnitudes::CombinedMagnitude(Magnitudes, pMagnitudes); }
	AAPLUS_EXPORT_LIB double CAAStellarMagnitudes_BrightnessRatio(double m1, double m2) { return CAAStellarMagnitudes::BrightnessRatio(m1, m2); }
	AAPLUS_EXPORT_LIB double CAAStellarMagnitudes_MagnitudeDifference(double brightnessRatio) { return CAAStellarMagnitudes::MagnitudeDifference(brightnessRatio); }

	/* CAASun export functions */
	AAPLUS_EXPORT_LIB double CAASun_GeometricEclipticLongitude(double JD, bool bHighPrecision) { return CAASun::GeometricEclipticLongitude(JD, bHighPrecision); }
	AAPLUS_EXPORT_LIB double CAASun_GeometricEclipticLatitude(double JD, bool bHighPrecision) { return CAASun::GeometricEclipticLatitude(JD, bHighPrecision); }
	AAPLUS_EXPORT_LIB double CAASun_GeometricEclipticLongitudeJ2000(double JD, bool bHighPrecision) { return CAASun::GeometricEclipticLongitudeJ2000(JD, bHighPrecision); }
	AAPLUS_EXPORT_LIB double CAASun_GeometricEclipticLatitudeJ2000(double JD, bool bHighPrecision) { return CAASun::GeometricEclipticLatitudeJ2000(JD, bHighPrecision); }
	AAPLUS_EXPORT_LIB double CAASun_GeometricFK5EclipticLongitude(double JD, bool bHighPrecision) { return CAASun::GeometricFK5EclipticLongitude(JD, bHighPrecision); }
	AAPLUS_EXPORT_LIB double CAASun_GeometricFK5EclipticLatitude(double JD, bool bHighPrecision) { return CAASun::GeometricFK5EclipticLatitude(JD, bHighPrecision); }
	AAPLUS_EXPORT_LIB double CAASun_ApparentEclipticLongitude(double JD, bool bHighPrecision) { return CAASun::ApparentEclipticLongitude(JD, bHighPrecision); }
	AAPLUS_EXPORT_LIB double CAASun_ApparentEclipticLatitude(double JD, bool bHighPrecision) { return CAASun::ApparentEclipticLatitude(JD, bHighPrecision); }
	AAPLUS_EXPORT_LIB double CAASun_VariationGeometricEclipticLongitude(double JD) { return CAASun::VariationGeometricEclipticLongitude(JD); }
	AAPLUS_EXPORT_LIB CAA3DCoordinate CAASun_EquatorialRectangularCoordinatesMeanEquinox(double JD, bool bHighPrecision) { return CAASun::EquatorialRectangularCoordinatesMeanEquinox(JD, bHighPrecision); }
	AAPLUS_EXPORT_LIB CAA3DCoordinate CAASun_EclipticRectangularCoordinatesJ2000(double JD, bool bHighPrecision) { return CAASun::EclipticRectangularCoordinatesJ2000(JD, bHighPrecision); }
	AAPLUS_EXPORT_LIB CAA3DCoordinate CAASun_EquatorialRectangularCoordinatesJ2000(double JD, bool bHighPrecision) { return CAASun::EquatorialRectangularCoordinatesJ2000(JD, bHighPrecision); }
	AAPLUS_EXPORT_LIB CAA3DCoordinate CAASun_EquatorialRectangularCoordinatesB1950(double JD, bool bHighPrecision) { return CAASun::EquatorialRectangularCoordinatesB1950(JD, bHighPrecision); }
	AAPLUS_EXPORT_LIB CAA3DCoordinate CAASun_EquatorialRectangularCoordinatesAnyEquinox(double JD, double JDEquinox, bool bHighPrecision) { return CAASun::EquatorialRectangularCoordinatesAnyEquinox(JD, JDEquinox, bHighPrecision); }

	/* CAAUranus export functions */
	AAPLUS_EXPORT_LIB double CAAUranus_EclipticLongitude(double JD, bool bHighPrecision) { return CAAUranus::EclipticLongitude(JD, bHighPrecision); }
	AAPLUS_EXPORT_LIB double CAAUranus_EclipticLatitude(double JD, bool bHighPrecision) { return CAAUranus::EclipticLatitude(JD, bHighPrecision); }
	AAPLUS_EXPORT_LIB double CAAUranus_RadiusVector(double JD, bool bHighPrecision) { return CAAUranus::RadiusVector(JD, bHighPrecision); }

	/* CAAVenus export functions */
	AAPLUS_EXPORT_LIB double CAAVenus_EclipticLongitude(double JD, bool bHighPrecision) { return CAAVenus::EclipticLongitude(JD, bHighPrecision); }
	AAPLUS_EXPORT_LIB double CAAVenus_EclipticLatitude(double JD, bool bHighPrecision) { return CAAVenus::EclipticLatitude(JD, bHighPrecision); }
	AAPLUS_EXPORT_LIB double CAAVenus_RadiusVector(double JD, bool bHighPrecision) { return CAAVenus::RadiusVector(JD, bHighPrecision); }

	/* CAAVSOP2013 export functions */
	AAPLUS_EXPORT_LIB double CAAVSOP2013_CalculateMeanMotion(CAAVSOP2013::Planet planet, double a) { return CAAVSOP2013::CalculateMeanMotion(planet, a); }
	AAPLUS_EXPORT_LIB CAAEllipticalObjectElements CAAVSOP2013_OrbitToElements(double JD, CAAVSOP2013::Planet planet, const CAAVSOP2013Orbit& orbit) { return CAAVSOP2013::OrbitToElements(JD, planet, orbit); }
	AAPLUS_EXPORT_LIB CAAVSOP2013Position CAAVSOP2013_Ecliptic2Equatorial(const CAAVSOP2013Position& value) { return CAAVSOP2013::Ecliptic2Equatorial(value); }
	
	/* CAAVSOP2013 extra */
	AAPLUS_EXPORT_LIB void* CAAVSOP2013_Create() { return new CAAVSOP2013(); }
	AAPLUS_EXPORT_LIB CAAVSOP2013Position CAAVSOP2013_Calculate(void* self, CAAVSOP2013::Planet planet, double JD) { return static_cast<CAAVSOP2013*>(self)->Calculate(planet, JD); }
	AAPLUS_EXPORT_LIB CAAVSOP2013Orbit CAAVSOP2013_CalculateOrbit(void* self, CAAVSOP2013::Planet planet, double JD) { return static_cast<CAAVSOP2013*>(self)->CalculateOrbit(planet, JD); }
	AAPLUS_EXPORT_LIB auto* CAAVSOP2013_GetBinaryFilesDirectory(void* self) { return static_cast<CAAVSOP2013*>(self)->GetBinaryFilesDirectory(); }
	AAPLUS_EXPORT_LIB void CAAVSOP2013_SetBinaryFilesDirectory(void* self, const std::filesystem::path::value_type* pszBinaryFilesDirectory) { static_cast<CAAVSOP2013*>(self)->SetBinaryFilesDirectory(pszBinaryFilesDirectory); }
	AAPLUS_EXPORT_LIB void CAAVSOP2013_Destroy(void* self) { delete self; }

	/* CAAVSOP87 export functions */
	AAPLUS_EXPORT_LIB double CAAVSOP87_Calculate(double JD, const VSOP87Coefficient2* pTable, size_t nTableSize, bool bAngle) { return CAAVSOP87::Calculate(JD, pTable, nTableSize, bAngle); }
	AAPLUS_EXPORT_LIB double CAAVSOP87_Calculate_Dash(double JD, const VSOP87Coefficient2* pTable, size_t nTableSize) { return CAAVSOP87::Calculate_Dash(JD, pTable, nTableSize); }

	/* CAAVSOP87A_Earth export functions */
	AAPLUS_EXPORT_LIB double CAAVSOP87A_Earth_X(double JD) { return CAAVSOP87A_Earth::X(JD); }
	AAPLUS_EXPORT_LIB double CAAVSOP87A_Earth_X_DASH(double JD) { return CAAVSOP87A_Earth::X_DASH(JD); }
	AAPLUS_EXPORT_LIB double CAAVSOP87A_Earth_Y(double JD) { return CAAVSOP87A_Earth::Y(JD); }
	AAPLUS_EXPORT_LIB double CAAVSOP87A_Earth_Y_DASH(double JD) { return CAAVSOP87A_Earth::Y_DASH(JD); }
	AAPLUS_EXPORT_LIB double CAAVSOP87A_Earth_Z(double JD) { return CAAVSOP87A_Earth::Z(JD); }
	AAPLUS_EXPORT_LIB double CAAVSOP87A_Earth_Z_DASH(double JD) { return CAAVSOP87A_Earth::Z_DASH(JD); }

	/* CAAVSOP87A_EMB export functions */
	AAPLUS_EXPORT_LIB double CAAVSOP87A_EMB_X(double JD) { return CAAVSOP87A_EMB::X(JD); }
	AAPLUS_EXPORT_LIB double CAAVSOP87A_EMB_X_DASH(double JD) { return CAAVSOP87A_EMB::X_DASH(JD); }
	AAPLUS_EXPORT_LIB double CAAVSOP87A_EMB_Y(double JD) { return CAAVSOP87A_EMB::Y(JD); }
	AAPLUS_EXPORT_LIB double CAAVSOP87A_EMB_Y_DASH(double JD) { return CAAVSOP87A_EMB::Y_DASH(JD); }
	AAPLUS_EXPORT_LIB double CAAVSOP87A_EMB_Z(double JD) { return CAAVSOP87A_EMB::Z(JD); }
	AAPLUS_EXPORT_LIB double CAAVSOP87A_EMB_Z_DASH(double JD) { return CAAVSOP87A_EMB::Z_DASH(JD); }

	/* CAAVSOP87A_Jupiter export functions */
	AAPLUS_EXPORT_LIB double CAAVSOP87A_Jupiter_X(double JD) { return CAAVSOP87A_Jupiter::X(JD); }
	AAPLUS_EXPORT_LIB double CAAVSOP87A_Jupiter_X_DASH(double JD) { return CAAVSOP87A_Jupiter::X_DASH(JD); }
	AAPLUS_EXPORT_LIB double CAAVSOP87A_Jupiter_Y(double JD) { return CAAVSOP87A_Jupiter::Y(JD); }
	AAPLUS_EXPORT_LIB double CAAVSOP87A_Jupiter_Y_DASH(double JD) { return CAAVSOP87A_Jupiter::Y_DASH(JD); }
	AAPLUS_EXPORT_LIB double CAAVSOP87A_Jupiter_Z(double JD) { return CAAVSOP87A_Jupiter::Z(JD); }
	AAPLUS_EXPORT_LIB double CAAVSOP87A_Jupiter_Z_DASH(double JD) { return CAAVSOP87A_Jupiter::Z_DASH(JD); }

	/* CAAVSOP87A_Mars export functions */
	AAPLUS_EXPORT_LIB double CAAVSOP87A_Mars_X(double JD) { return CAAVSOP87A_Mars::X(JD); }
	AAPLUS_EXPORT_LIB double CAAVSOP87A_Mars_X_DASH(double JD) { return CAAVSOP87A_Mars::X_DASH(JD); }
	AAPLUS_EXPORT_LIB double CAAVSOP87A_Mars_Y(double JD) { return CAAVSOP87A_Mars::Y(JD); }
	AAPLUS_EXPORT_LIB double CAAVSOP87A_Mars_Y_DASH(double JD) { return CAAVSOP87A_Mars::Y_DASH(JD); }
	AAPLUS_EXPORT_LIB double CAAVSOP87A_Mars_Z(double JD) { return CAAVSOP87A_Mars::Z(JD); }
	AAPLUS_EXPORT_LIB double CAAVSOP87A_Mars_Z_DASH(double JD) { return CAAVSOP87A_Mars::Z_DASH(JD); }

	/* CAAVSOP87A_Mercury export functions */
	AAPLUS_EXPORT_LIB double CAAVSOP87A_Mercury_X(double JD) { return CAAVSOP87A_Mercury::X(JD); }
	AAPLUS_EXPORT_LIB double CAAVSOP87A_Mercury_X_DASH(double JD) { return CAAVSOP87A_Mercury::X_DASH(JD); }
	AAPLUS_EXPORT_LIB double CAAVSOP87A_Mercury_Y(double JD) { return CAAVSOP87A_Mercury::Y(JD); }
	AAPLUS_EXPORT_LIB double CAAVSOP87A_Mercury_Y_DASH(double JD) { return CAAVSOP87A_Mercury::Y_DASH(JD); }
	AAPLUS_EXPORT_LIB double CAAVSOP87A_Mercury_Z(double JD) { return CAAVSOP87A_Mercury::Z(JD); }
	AAPLUS_EXPORT_LIB double CAAVSOP87A_Mercury_Z_DASH(double JD) { return CAAVSOP87A_Mercury::Z_DASH(JD); }

	/* CAAVSOP87A_Neptune export functions */
	AAPLUS_EXPORT_LIB double CAAVSOP87A_Neptune_X(double JD) { return CAAVSOP87A_Neptune::X(JD); }
	AAPLUS_EXPORT_LIB double CAAVSOP87A_Neptune_X_DASH(double JD) { return CAAVSOP87A_Neptune::X_DASH(JD); }
	AAPLUS_EXPORT_LIB double CAAVSOP87A_Neptune_Y(double JD) { return CAAVSOP87A_Neptune::Y(JD); }
	AAPLUS_EXPORT_LIB double CAAVSOP87A_Neptune_Y_DASH(double JD) { return CAAVSOP87A_Neptune::Y_DASH(JD); }
	AAPLUS_EXPORT_LIB double CAAVSOP87A_Neptune_Z(double JD) { return CAAVSOP87A_Neptune::Z(JD); }
	AAPLUS_EXPORT_LIB double CAAVSOP87A_Neptune_Z_DASH(double JD) { return CAAVSOP87A_Neptune::Z_DASH(JD); }

	/* CAAVSOP87A_Saturn export functions */
	AAPLUS_EXPORT_LIB double CAAVSOP87A_Saturn_X(double JD) { return CAAVSOP87A_Saturn::X(JD); }
	AAPLUS_EXPORT_LIB double CAAVSOP87A_Saturn_X_DASH(double JD) { return CAAVSOP87A_Saturn::X_DASH(JD); }
	AAPLUS_EXPORT_LIB double CAAVSOP87A_Saturn_Y(double JD) { return CAAVSOP87A_Saturn::Y(JD); }
	AAPLUS_EXPORT_LIB double CAAVSOP87A_Saturn_Y_DASH(double JD) { return CAAVSOP87A_Saturn::Y_DASH(JD); }
	AAPLUS_EXPORT_LIB double CAAVSOP87A_Saturn_Z(double JD) { return CAAVSOP87A_Saturn::Z(JD); }
	AAPLUS_EXPORT_LIB double CAAVSOP87A_Saturn_Z_DASH(double JD) { return CAAVSOP87A_Saturn::Z_DASH(JD); }

	/* CAAVSOP87A_Uranus export functions */
	AAPLUS_EXPORT_LIB double CAAVSOP87A_Uranus_X(double JD) { return CAAVSOP87A_Uranus::X(JD); }
	AAPLUS_EXPORT_LIB double CAAVSOP87A_Uranus_X_DASH(double JD) { return CAAVSOP87A_Uranus::X_DASH(JD); }
	AAPLUS_EXPORT_LIB double CAAVSOP87A_Uranus_Y(double JD) { return CAAVSOP87A_Uranus::Y(JD); }
	AAPLUS_EXPORT_LIB double CAAVSOP87A_Uranus_Y_DASH(double JD) { return CAAVSOP87A_Uranus::Y_DASH(JD); }
	AAPLUS_EXPORT_LIB double CAAVSOP87A_Uranus_Z(double JD) { return CAAVSOP87A_Uranus::Z(JD); }
	AAPLUS_EXPORT_LIB double CAAVSOP87A_Uranus_Z_DASH(double JD) { return CAAVSOP87A_Uranus::Z_DASH(JD); }

	/* CAAVSOP87A_Venus export functions */
	AAPLUS_EXPORT_LIB double CAAVSOP87A_Venus_X(double JD) { return CAAVSOP87A_Venus::X(JD); }
	AAPLUS_EXPORT_LIB double CAAVSOP87A_Venus_X_DASH(double JD) { return CAAVSOP87A_Venus::X_DASH(JD); }
	AAPLUS_EXPORT_LIB double CAAVSOP87A_Venus_Y(double JD) { return CAAVSOP87A_Venus::Y(JD); }
	AAPLUS_EXPORT_LIB double CAAVSOP87A_Venus_Y_DASH(double JD) { return CAAVSOP87A_Venus::Y_DASH(JD); }
	AAPLUS_EXPORT_LIB double CAAVSOP87A_Venus_Z(double JD) { return CAAVSOP87A_Venus::Z(JD); }
	AAPLUS_EXPORT_LIB double CAAVSOP87A_Venus_Z_DASH(double JD) { return CAAVSOP87A_Venus::Z_DASH(JD); }

	/* CAAVSOP87B_Earth export functions */
	AAPLUS_EXPORT_LIB double CAAVSOP87B_Earth_L(double JD) { return CAAVSOP87B_Earth::L(JD); }
	AAPLUS_EXPORT_LIB double CAAVSOP87B_Earth_L_DASH(double JD) { return CAAVSOP87B_Earth::L_DASH(JD); }
	AAPLUS_EXPORT_LIB double CAAVSOP87B_Earth_B(double JD) { return CAAVSOP87B_Earth::B(JD); }
	AAPLUS_EXPORT_LIB double CAAVSOP87B_Earth_B_DASH(double JD) { return CAAVSOP87B_Earth::B_DASH(JD); }
	AAPLUS_EXPORT_LIB double CAAVSOP87B_Earth_R(double JD) { return CAAVSOP87B_Earth::R(JD); }
	AAPLUS_EXPORT_LIB double CAAVSOP87B_Earth_R_DASH(double JD) { return CAAVSOP87B_Earth::R_DASH(JD); }

	/* CAAVSOP87B_Jupiter export functions */
	AAPLUS_EXPORT_LIB double CAAVSOP87B_Jupiter_L(double JD) { return CAAVSOP87B_Jupiter::L(JD); }
	AAPLUS_EXPORT_LIB double CAAVSOP87B_Jupiter_L_DASH(double JD) { return CAAVSOP87B_Jupiter::L_DASH(JD); }
	AAPLUS_EXPORT_LIB double CAAVSOP87B_Jupiter_B(double JD) { return CAAVSOP87B_Jupiter::B(JD); }
	AAPLUS_EXPORT_LIB double CAAVSOP87B_Jupiter_B_DASH(double JD) { return CAAVSOP87B_Jupiter::B_DASH(JD); }
	AAPLUS_EXPORT_LIB double CAAVSOP87B_Jupiter_R(double JD) { return CAAVSOP87B_Jupiter::R(JD); }
	AAPLUS_EXPORT_LIB double CAAVSOP87B_Jupiter_R_DASH(double JD) { return CAAVSOP87B_Jupiter::R_DASH(JD); }

	/* CAAVSOP87B_Mars export functions */
	AAPLUS_EXPORT_LIB double CAAVSOP87B_Mars_L(double JD) { return CAAVSOP87B_Mars::L(JD); }
	AAPLUS_EXPORT_LIB double CAAVSOP87B_Mars_L_DASH(double JD) { return CAAVSOP87B_Mars::L_DASH(JD); }
	AAPLUS_EXPORT_LIB double CAAVSOP87B_Mars_B(double JD) { return CAAVSOP87B_Mars::B(JD); }
	AAPLUS_EXPORT_LIB double CAAVSOP87B_Mars_B_DASH(double JD) { return CAAVSOP87B_Mars::B_DASH(JD); }
	AAPLUS_EXPORT_LIB double CAAVSOP87B_Mars_R(double JD) { return CAAVSOP87B_Mars::R(JD); }
	AAPLUS_EXPORT_LIB double CAAVSOP87B_Mars_R_DASH(double JD) { return CAAVSOP87B_Mars::R_DASH(JD); }

	/* CAAVSOP87B_Mercury export functions */
	AAPLUS_EXPORT_LIB double CAAVSOP87B_Mercury_L(double JD) { return CAAVSOP87B_Mercury::L(JD); }
	AAPLUS_EXPORT_LIB double CAAVSOP87B_Mercury_L_DASH(double JD) { return CAAVSOP87B_Mercury::L_DASH(JD); }
	AAPLUS_EXPORT_LIB double CAAVSOP87B_Mercury_B(double JD) { return CAAVSOP87B_Mercury::B(JD); }
	AAPLUS_EXPORT_LIB double CAAVSOP87B_Mercury_B_DASH(double JD) { return CAAVSOP87B_Mercury::B_DASH(JD); }
	AAPLUS_EXPORT_LIB double CAAVSOP87B_Mercury_R(double JD) { return CAAVSOP87B_Mercury::R(JD); }
	AAPLUS_EXPORT_LIB double CAAVSOP87B_Mercury_R_DASH(double JD) { return CAAVSOP87B_Mercury::R_DASH(JD); }

	/* CAAVSOP87B_Neptune export functions */
	AAPLUS_EXPORT_LIB double CAAVSOP87B_Neptune_L(double JD) { return CAAVSOP87B_Neptune::L(JD); }
	AAPLUS_EXPORT_LIB double CAAVSOP87B_Neptune_L_DASH(double JD) { return CAAVSOP87B_Neptune::L_DASH(JD); }
	AAPLUS_EXPORT_LIB double CAAVSOP87B_Neptune_B(double JD) { return CAAVSOP87B_Neptune::B(JD); }
	AAPLUS_EXPORT_LIB double CAAVSOP87B_Neptune_B_DASH(double JD) { return CAAVSOP87B_Neptune::B_DASH(JD); }
	AAPLUS_EXPORT_LIB double CAAVSOP87B_Neptune_R(double JD) { return CAAVSOP87B_Neptune::R(JD); }
	AAPLUS_EXPORT_LIB double CAAVSOP87B_Neptune_R_DASH(double JD) { return CAAVSOP87B_Neptune::R_DASH(JD); }

	/* CAAVSOP87B_Saturn export functions */
	AAPLUS_EXPORT_LIB double CAAVSOP87B_Saturn_L(double JD) { return CAAVSOP87B_Saturn::L(JD); }
	AAPLUS_EXPORT_LIB double CAAVSOP87B_Saturn_L_DASH(double JD) { return CAAVSOP87B_Saturn::L_DASH(JD); }
	AAPLUS_EXPORT_LIB double CAAVSOP87B_Saturn_B(double JD) { return CAAVSOP87B_Saturn::B(JD); }
	AAPLUS_EXPORT_LIB double CAAVSOP87B_Saturn_B_DASH(double JD) { return CAAVSOP87B_Saturn::B_DASH(JD); }
	AAPLUS_EXPORT_LIB double CAAVSOP87B_Saturn_R(double JD) { return CAAVSOP87B_Saturn::R(JD); }
	AAPLUS_EXPORT_LIB double CAAVSOP87B_Saturn_R_DASH(double JD) { return CAAVSOP87B_Saturn::R_DASH(JD); }

	/* CAAVSOP87B_Uranus export functions */
	AAPLUS_EXPORT_LIB double CAAVSOP87B_Uranus_L(double JD) { return CAAVSOP87B_Uranus::L(JD); }
	AAPLUS_EXPORT_LIB double CAAVSOP87B_Uranus_L_DASH(double JD) { return CAAVSOP87B_Uranus::L_DASH(JD); }
	AAPLUS_EXPORT_LIB double CAAVSOP87B_Uranus_B(double JD) { return CAAVSOP87B_Uranus::B(JD); }
	AAPLUS_EXPORT_LIB double CAAVSOP87B_Uranus_B_DASH(double JD) { return CAAVSOP87B_Uranus::B_DASH(JD); }
	AAPLUS_EXPORT_LIB double CAAVSOP87B_Uranus_R(double JD) { return CAAVSOP87B_Uranus::R(JD); }
	AAPLUS_EXPORT_LIB double CAAVSOP87B_Uranus_R_DASH(double JD) { return CAAVSOP87B_Uranus::R_DASH(JD); }

	/* CAAVSOP87B_Venus export functions */
	AAPLUS_EXPORT_LIB double CAAVSOP87B_Venus_L(double JD) { return CAAVSOP87B_Venus::L(JD); }
	AAPLUS_EXPORT_LIB double CAAVSOP87B_Venus_L_DASH(double JD) { return CAAVSOP87B_Venus::L_DASH(JD); }
	AAPLUS_EXPORT_LIB double CAAVSOP87B_Venus_B(double JD) { return CAAVSOP87B_Venus::B(JD); }
	AAPLUS_EXPORT_LIB double CAAVSOP87B_Venus_B_DASH(double JD) { return CAAVSOP87B_Venus::B_DASH(JD); }
	AAPLUS_EXPORT_LIB double CAAVSOP87B_Venus_R(double JD) { return CAAVSOP87B_Venus::R(JD); }
	AAPLUS_EXPORT_LIB double CAAVSOP87B_Venus_R_DASH(double JD) { return CAAVSOP87B_Venus::R_DASH(JD); }

	/* CAAVSOP87C_Earth export functions */
	AAPLUS_EXPORT_LIB double CAAVSOP87C_Earth_X(double JD) { return CAAVSOP87C_Earth::X(JD); }
	AAPLUS_EXPORT_LIB double CAAVSOP87C_Earth_X_DASH(double JD) { return CAAVSOP87C_Earth::X_DASH(JD); }
	AAPLUS_EXPORT_LIB double CAAVSOP87C_Earth_Y(double JD) { return CAAVSOP87C_Earth::Y(JD); }
	AAPLUS_EXPORT_LIB double CAAVSOP87C_Earth_Y_DASH(double JD) { return CAAVSOP87C_Earth::Y_DASH(JD); }
	AAPLUS_EXPORT_LIB double CAAVSOP87C_Earth_Z(double JD) { return CAAVSOP87C_Earth::Z(JD); }
	AAPLUS_EXPORT_LIB double CAAVSOP87C_Earth_Z_DASH(double JD) { return CAAVSOP87C_Earth::Z_DASH(JD); }

	/* CAAVSOP87C_Jupiter export functions */
	AAPLUS_EXPORT_LIB double CAAVSOP87C_Jupiter_X(double JD) { return CAAVSOP87C_Jupiter::X(JD); }
	AAPLUS_EXPORT_LIB double CAAVSOP87C_Jupiter_X_DASH(double JD) { return CAAVSOP87C_Jupiter::X_DASH(JD); }
	AAPLUS_EXPORT_LIB double CAAVSOP87C_Jupiter_Y(double JD) { return CAAVSOP87C_Jupiter::Y(JD); }
	AAPLUS_EXPORT_LIB double CAAVSOP87C_Jupiter_Y_DASH(double JD) { return CAAVSOP87C_Jupiter::Y_DASH(JD); }
	AAPLUS_EXPORT_LIB double CAAVSOP87C_Jupiter_Z(double JD) { return CAAVSOP87C_Jupiter::Z(JD); }
	AAPLUS_EXPORT_LIB double CAAVSOP87C_Jupiter_Z_DASH(double JD) { return CAAVSOP87C_Jupiter::Z_DASH(JD); }

	/* CAAVSOP87C_Mars export functions */
	AAPLUS_EXPORT_LIB double CAAVSOP87C_Mars_X(double JD) { return CAAVSOP87C_Mars::X(JD); }
	AAPLUS_EXPORT_LIB double CAAVSOP87C_Mars_X_DASH(double JD) { return CAAVSOP87C_Mars::X_DASH(JD); }
	AAPLUS_EXPORT_LIB double CAAVSOP87C_Mars_Y(double JD) { return CAAVSOP87C_Mars::Y(JD); }
	AAPLUS_EXPORT_LIB double CAAVSOP87C_Mars_Y_DASH(double JD) { return CAAVSOP87C_Mars::Y_DASH(JD); }
	AAPLUS_EXPORT_LIB double CAAVSOP87C_Mars_Z(double JD) { return CAAVSOP87C_Mars::Z(JD); }
	AAPLUS_EXPORT_LIB double CAAVSOP87C_Mars_Z_DASH(double JD) { return CAAVSOP87C_Mars::Z_DASH(JD); }

	/* CAAVSOP87C_Mercury export functions */
	AAPLUS_EXPORT_LIB double CAAVSOP87C_Mercury_X(double JD) { return CAAVSOP87C_Mercury::X(JD); }
	AAPLUS_EXPORT_LIB double CAAVSOP87C_Mercury_X_DASH(double JD) { return CAAVSOP87C_Mercury::X_DASH(JD); }
	AAPLUS_EXPORT_LIB double CAAVSOP87C_Mercury_Y(double JD) { return CAAVSOP87C_Mercury::Y(JD); }
	AAPLUS_EXPORT_LIB double CAAVSOP87C_Mercury_Y_DASH(double JD) { return CAAVSOP87C_Mercury::Y_DASH(JD); }
	AAPLUS_EXPORT_LIB double CAAVSOP87C_Mercury_Z(double JD) { return CAAVSOP87C_Mercury::Z(JD); }
	AAPLUS_EXPORT_LIB double CAAVSOP87C_Mercury_Z_DASH(double JD) { return CAAVSOP87C_Mercury::Z_DASH(JD); }

	/* CAAVSOP87C_Neptune export functions */
	AAPLUS_EXPORT_LIB double CAAVSOP87C_Neptune_X(double JD) { return CAAVSOP87C_Neptune::X(JD); }
	AAPLUS_EXPORT_LIB double CAAVSOP87C_Neptune_X_DASH(double JD) { return CAAVSOP87C_Neptune::X_DASH(JD); }
	AAPLUS_EXPORT_LIB double CAAVSOP87C_Neptune_Y(double JD) { return CAAVSOP87C_Neptune::Y(JD); }
	AAPLUS_EXPORT_LIB double CAAVSOP87C_Neptune_Y_DASH(double JD) { return CAAVSOP87C_Neptune::Y_DASH(JD); }
	AAPLUS_EXPORT_LIB double CAAVSOP87C_Neptune_Z(double JD) { return CAAVSOP87C_Neptune::Z(JD); }
	AAPLUS_EXPORT_LIB double CAAVSOP87C_Neptune_Z_DASH(double JD) { return CAAVSOP87C_Neptune::Z_DASH(JD); }

	/* CAAVSOP87C_Saturn export functions */
	AAPLUS_EXPORT_LIB double CAAVSOP87C_Saturn_X(double JD) { return CAAVSOP87C_Saturn::X(JD); }
	AAPLUS_EXPORT_LIB double CAAVSOP87C_Saturn_X_DASH(double JD) { return CAAVSOP87C_Saturn::X_DASH(JD); }
	AAPLUS_EXPORT_LIB double CAAVSOP87C_Saturn_Y(double JD) { return CAAVSOP87C_Saturn::Y(JD); }
	AAPLUS_EXPORT_LIB double CAAVSOP87C_Saturn_Y_DASH(double JD) { return CAAVSOP87C_Saturn::Y_DASH(JD); }
	AAPLUS_EXPORT_LIB double CAAVSOP87C_Saturn_Z(double JD) { return CAAVSOP87C_Saturn::Z(JD); }
	AAPLUS_EXPORT_LIB double CAAVSOP87C_Saturn_Z_DASH(double JD) { return CAAVSOP87C_Saturn::Z_DASH(JD); }

	/* CAAVSOP87C_Uranus export functions */
	AAPLUS_EXPORT_LIB double CAAVSOP87C_Uranus_X(double JD) { return CAAVSOP87C_Uranus::X(JD); }
	AAPLUS_EXPORT_LIB double CAAVSOP87C_Uranus_X_DASH(double JD) { return CAAVSOP87C_Uranus::X_DASH(JD); }
	AAPLUS_EXPORT_LIB double CAAVSOP87C_Uranus_Y(double JD) { return CAAVSOP87C_Uranus::Y(JD); }
	AAPLUS_EXPORT_LIB double CAAVSOP87C_Uranus_Y_DASH(double JD) { return CAAVSOP87C_Uranus::Y_DASH(JD); }
	AAPLUS_EXPORT_LIB double CAAVSOP87C_Uranus_Z(double JD) { return CAAVSOP87C_Uranus::Z(JD); }
	AAPLUS_EXPORT_LIB double CAAVSOP87C_Uranus_Z_DASH(double JD) { return CAAVSOP87C_Uranus::Z_DASH(JD); }

	/* CAAVSOP87C_Venus export functions */
	AAPLUS_EXPORT_LIB double CAAVSOP87C_Venus_X(double JD) { return CAAVSOP87C_Venus::X(JD); }
	AAPLUS_EXPORT_LIB double CAAVSOP87C_Venus_X_DASH(double JD) { return CAAVSOP87C_Venus::X_DASH(JD); }
	AAPLUS_EXPORT_LIB double CAAVSOP87C_Venus_Y(double JD) { return CAAVSOP87C_Venus::Y(JD); }
	AAPLUS_EXPORT_LIB double CAAVSOP87C_Venus_Y_DASH(double JD) { return CAAVSOP87C_Venus::Y_DASH(JD); }
	AAPLUS_EXPORT_LIB double CAAVSOP87C_Venus_Z(double JD) { return CAAVSOP87C_Venus::Z(JD); }
	AAPLUS_EXPORT_LIB double CAAVSOP87C_Venus_Z_DASH(double JD) { return CAAVSOP87C_Venus::Z_DASH(JD); }

	/* CAAVSOP87D_Earth export functions */
	AAPLUS_EXPORT_LIB double CAAVSOP87D_Earth_L(double JD) { return CAAVSOP87D_Earth::L(JD); }
	AAPLUS_EXPORT_LIB double CAAVSOP87D_Earth_L_DASH(double JD) { return CAAVSOP87D_Earth::L_DASH(JD); }
	AAPLUS_EXPORT_LIB double CAAVSOP87D_Earth_B(double JD) { return CAAVSOP87D_Earth::B(JD); }
	AAPLUS_EXPORT_LIB double CAAVSOP87D_Earth_B_DASH(double JD) { return CAAVSOP87D_Earth::B_DASH(JD); }
	AAPLUS_EXPORT_LIB double CAAVSOP87D_Earth_R(double JD) { return CAAVSOP87D_Earth::R(JD); }
	AAPLUS_EXPORT_LIB double CAAVSOP87D_Earth_R_DASH(double JD) { return CAAVSOP87D_Earth::R_DASH(JD); }

	/* CAAVSOP87D_Jupiter export functions */
	AAPLUS_EXPORT_LIB double CAAVSOP87D_Jupiter_L(double JD) { return CAAVSOP87D_Jupiter::L(JD); }
	AAPLUS_EXPORT_LIB double CAAVSOP87D_Jupiter_L_DASH(double JD) { return CAAVSOP87D_Jupiter::L_DASH(JD); }
	AAPLUS_EXPORT_LIB double CAAVSOP87D_Jupiter_B(double JD) { return CAAVSOP87D_Jupiter::B(JD); }
	AAPLUS_EXPORT_LIB double CAAVSOP87D_Jupiter_B_DASH(double JD) { return CAAVSOP87D_Jupiter::B_DASH(JD); }
	AAPLUS_EXPORT_LIB double CAAVSOP87D_Jupiter_R(double JD) { return CAAVSOP87D_Jupiter::R(JD); }
	AAPLUS_EXPORT_LIB double CAAVSOP87D_Jupiter_R_DASH(double JD) { return CAAVSOP87D_Jupiter::R_DASH(JD); }

	/* CAAVSOP87D_Mars export functions */
	AAPLUS_EXPORT_LIB double CAAVSOP87D_Mars_L(double JD) { return CAAVSOP87D_Mars::L(JD); }
	AAPLUS_EXPORT_LIB double CAAVSOP87D_Mars_L_DASH(double JD) { return CAAVSOP87D_Mars::L_DASH(JD); }
	AAPLUS_EXPORT_LIB double CAAVSOP87D_Mars_B(double JD) { return CAAVSOP87D_Mars::B(JD); }
	AAPLUS_EXPORT_LIB double CAAVSOP87D_Mars_B_DASH(double JD) { return CAAVSOP87D_Mars::B_DASH(JD); }
	AAPLUS_EXPORT_LIB double CAAVSOP87D_Mars_R(double JD) { return CAAVSOP87D_Mars::R(JD); }
	AAPLUS_EXPORT_LIB double CAAVSOP87D_Mars_R_DASH(double JD) { return CAAVSOP87D_Mars::R_DASH(JD); }

	/* CAAVSOP87D_Mercury export functions */
	AAPLUS_EXPORT_LIB double CAAVSOP87D_Mercury_L(double JD) { return CAAVSOP87D_Mercury::L(JD); }
	AAPLUS_EXPORT_LIB double CAAVSOP87D_Mercury_L_DASH(double JD) { return CAAVSOP87D_Mercury::L_DASH(JD); }
	AAPLUS_EXPORT_LIB double CAAVSOP87D_Mercury_B(double JD) { return CAAVSOP87D_Mercury::B(JD); }
	AAPLUS_EXPORT_LIB double CAAVSOP87D_Mercury_B_DASH(double JD) { return CAAVSOP87D_Mercury::B_DASH(JD); }
	AAPLUS_EXPORT_LIB double CAAVSOP87D_Mercury_R(double JD) { return CAAVSOP87D_Mercury::R(JD); }
	AAPLUS_EXPORT_LIB double CAAVSOP87D_Mercury_R_DASH(double JD) { return CAAVSOP87D_Mercury::R_DASH(JD); }

	/* CAAVSOP87D_Neptune export functions */
	AAPLUS_EXPORT_LIB double CAAVSOP87D_Neptune_L(double JD) { return CAAVSOP87D_Neptune::L(JD); }
	AAPLUS_EXPORT_LIB double CAAVSOP87D_Neptune_L_DASH(double JD) { return CAAVSOP87D_Neptune::L_DASH(JD); }
	AAPLUS_EXPORT_LIB double CAAVSOP87D_Neptune_B(double JD) { return CAAVSOP87D_Neptune::B(JD); }
	AAPLUS_EXPORT_LIB double CAAVSOP87D_Neptune_B_DASH(double JD) { return CAAVSOP87D_Neptune::B_DASH(JD); }
	AAPLUS_EXPORT_LIB double CAAVSOP87D_Neptune_R(double JD) { return CAAVSOP87D_Neptune::R(JD); }
	AAPLUS_EXPORT_LIB double CAAVSOP87D_Neptune_R_DASH(double JD) { return CAAVSOP87D_Neptune::R_DASH(JD); }

	/* CAAVSOP87D_Saturn export functions */
	AAPLUS_EXPORT_LIB double CAAVSOP87D_Saturn_L(double JD) { return CAAVSOP87D_Saturn::L(JD); }
	AAPLUS_EXPORT_LIB double CAAVSOP87D_Saturn_L_DASH(double JD) { return CAAVSOP87D_Saturn::L_DASH(JD); }
	AAPLUS_EXPORT_LIB double CAAVSOP87D_Saturn_B(double JD) { return CAAVSOP87D_Saturn::B(JD); }
	AAPLUS_EXPORT_LIB double CAAVSOP87D_Saturn_B_DASH(double JD) { return CAAVSOP87D_Saturn::B_DASH(JD); }
	AAPLUS_EXPORT_LIB double CAAVSOP87D_Saturn_R(double JD) { return CAAVSOP87D_Saturn::R(JD); }
	AAPLUS_EXPORT_LIB double CAAVSOP87D_Saturn_R_DASH(double JD) { return CAAVSOP87D_Saturn::R_DASH(JD); }

	/* CAAVSOP87D_Uranus export functions */
	AAPLUS_EXPORT_LIB double CAAVSOP87D_Uranus_L(double JD) { return CAAVSOP87D_Uranus::L(JD); }
	AAPLUS_EXPORT_LIB double CAAVSOP87D_Uranus_L_DASH(double JD) { return CAAVSOP87D_Uranus::L_DASH(JD); }
	AAPLUS_EXPORT_LIB double CAAVSOP87D_Uranus_B(double JD) { return CAAVSOP87D_Uranus::B(JD); }
	AAPLUS_EXPORT_LIB double CAAVSOP87D_Uranus_B_DASH(double JD) { return CAAVSOP87D_Uranus::B_DASH(JD); }
	AAPLUS_EXPORT_LIB double CAAVSOP87D_Uranus_R(double JD) { return CAAVSOP87D_Uranus::R(JD); }
	AAPLUS_EXPORT_LIB double CAAVSOP87D_Uranus_R_DASH(double JD) { return CAAVSOP87D_Uranus::R_DASH(JD); }

	/* CAAVSOP87D_Venus export functions */
	AAPLUS_EXPORT_LIB double CAAVSOP87D_Venus_L(double JD) { return CAAVSOP87D_Venus::L(JD); }
	AAPLUS_EXPORT_LIB double CAAVSOP87D_Venus_L_DASH(double JD) { return CAAVSOP87D_Venus::L_DASH(JD); }
	AAPLUS_EXPORT_LIB double CAAVSOP87D_Venus_B(double JD) { return CAAVSOP87D_Venus::B(JD); }
	AAPLUS_EXPORT_LIB double CAAVSOP87D_Venus_B_DASH(double JD) { return CAAVSOP87D_Venus::B_DASH(JD); }
	AAPLUS_EXPORT_LIB double CAAVSOP87D_Venus_R(double JD) { return CAAVSOP87D_Venus::R(JD); }
	AAPLUS_EXPORT_LIB double CAAVSOP87D_Venus_R_DASH(double JD) { return CAAVSOP87D_Venus::R_DASH(JD); }

	/* CAAVSOP87E_Earth export functions */
	AAPLUS_EXPORT_LIB double CAAVSOP87E_Earth_X(double JD) { return CAAVSOP87E_Earth::X(JD); }
	AAPLUS_EXPORT_LIB double CAAVSOP87E_Earth_X_DASH(double JD) { return CAAVSOP87E_Earth::X_DASH(JD); }
	AAPLUS_EXPORT_LIB double CAAVSOP87E_Earth_Y(double JD) { return CAAVSOP87E_Earth::Y(JD); }
	AAPLUS_EXPORT_LIB double CAAVSOP87E_Earth_Y_DASH(double JD) { return CAAVSOP87E_Earth::Y_DASH(JD); }
	AAPLUS_EXPORT_LIB double CAAVSOP87E_Earth_Z(double JD) { return CAAVSOP87E_Earth::Z(JD); }
	AAPLUS_EXPORT_LIB double CAAVSOP87E_Earth_Z_DASH(double JD) { return CAAVSOP87E_Earth::Z_DASH(JD); }

	/* CAAVSOP87E_Jupiter export functions */
	AAPLUS_EXPORT_LIB double CAAVSOP87E_Jupiter_X(double JD) { return CAAVSOP87E_Jupiter::X(JD); }
	AAPLUS_EXPORT_LIB double CAAVSOP87E_Jupiter_X_DASH(double JD) { return CAAVSOP87E_Jupiter::X_DASH(JD); }
	AAPLUS_EXPORT_LIB double CAAVSOP87E_Jupiter_Y(double JD) { return CAAVSOP87E_Jupiter::Y(JD); }
	AAPLUS_EXPORT_LIB double CAAVSOP87E_Jupiter_Y_DASH(double JD) { return CAAVSOP87E_Jupiter::Y_DASH(JD); }
	AAPLUS_EXPORT_LIB double CAAVSOP87E_Jupiter_Z(double JD) { return CAAVSOP87E_Jupiter::Z(JD); }
	AAPLUS_EXPORT_LIB double CAAVSOP87E_Jupiter_Z_DASH(double JD) { return CAAVSOP87E_Jupiter::Z_DASH(JD); }

	/* CAAVSOP87E_Mars export functions */
	AAPLUS_EXPORT_LIB double CAAVSOP87E_Mars_X(double JD) { return CAAVSOP87E_Mars::X(JD); }
	AAPLUS_EXPORT_LIB double CAAVSOP87E_Mars_X_DASH(double JD) { return CAAVSOP87E_Mars::X_DASH(JD); }
	AAPLUS_EXPORT_LIB double CAAVSOP87E_Mars_Y(double JD) { return CAAVSOP87E_Mars::Y(JD); }
	AAPLUS_EXPORT_LIB double CAAVSOP87E_Mars_Y_DASH(double JD) { return CAAVSOP87E_Mars::Y_DASH(JD); }
	AAPLUS_EXPORT_LIB double CAAVSOP87E_Mars_Z(double JD) { return CAAVSOP87E_Mars::Z(JD); }
	AAPLUS_EXPORT_LIB double CAAVSOP87E_Mars_Z_DASH(double JD) { return CAAVSOP87E_Mars::Z_DASH(JD); }

	/* CAAVSOP87E_Mercury export functions */
	AAPLUS_EXPORT_LIB double CAAVSOP87E_Mercury_X(double JD) { return CAAVSOP87E_Mercury::X(JD); }
	AAPLUS_EXPORT_LIB double CAAVSOP87E_Mercury_X_DASH(double JD) { return CAAVSOP87E_Mercury::X_DASH(JD); }
	AAPLUS_EXPORT_LIB double CAAVSOP87E_Mercury_Y(double JD) { return CAAVSOP87E_Mercury::Y(JD); }
	AAPLUS_EXPORT_LIB double CAAVSOP87E_Mercury_Y_DASH(double JD) { return CAAVSOP87E_Mercury::Y_DASH(JD); }
	AAPLUS_EXPORT_LIB double CAAVSOP87E_Mercury_Z(double JD) { return CAAVSOP87E_Mercury::Z(JD); }
	AAPLUS_EXPORT_LIB double CAAVSOP87E_Mercury_Z_DASH(double JD) { return CAAVSOP87E_Mercury::Z_DASH(JD); }

	/* CAAVSOP87E_Neptune export functions */
	AAPLUS_EXPORT_LIB double CAAVSOP87E_Neptune_X(double JD) { return CAAVSOP87E_Neptune::X(JD); }
	AAPLUS_EXPORT_LIB double CAAVSOP87E_Neptune_X_DASH(double JD) { return CAAVSOP87E_Neptune::X_DASH(JD); }
	AAPLUS_EXPORT_LIB double CAAVSOP87E_Neptune_Y(double JD) { return CAAVSOP87E_Neptune::Y(JD); }
	AAPLUS_EXPORT_LIB double CAAVSOP87E_Neptune_Y_DASH(double JD) { return CAAVSOP87E_Neptune::Y_DASH(JD); }
	AAPLUS_EXPORT_LIB double CAAVSOP87E_Neptune_Z(double JD) { return CAAVSOP87E_Neptune::Z(JD); }
	AAPLUS_EXPORT_LIB double CAAVSOP87E_Neptune_Z_DASH(double JD) { return CAAVSOP87E_Neptune::Z_DASH(JD); }

	/* CAAVSOP87E_Saturn export functions */
	AAPLUS_EXPORT_LIB double CAAVSOP87E_Saturn_X(double JD) { return CAAVSOP87E_Saturn::X(JD); }
	AAPLUS_EXPORT_LIB double CAAVSOP87E_Saturn_X_DASH(double JD) { return CAAVSOP87E_Saturn::X_DASH(JD); }
	AAPLUS_EXPORT_LIB double CAAVSOP87E_Saturn_Y(double JD) { return CAAVSOP87E_Saturn::Y(JD); }
	AAPLUS_EXPORT_LIB double CAAVSOP87E_Saturn_Y_DASH(double JD) { return CAAVSOP87E_Saturn::Y_DASH(JD); }
	AAPLUS_EXPORT_LIB double CAAVSOP87E_Saturn_Z(double JD) { return CAAVSOP87E_Saturn::Z(JD); }
	AAPLUS_EXPORT_LIB double CAAVSOP87E_Saturn_Z_DASH(double JD) { return CAAVSOP87E_Saturn::Z_DASH(JD); }

	/* CAAVSOP87E_Sun export functions */
	AAPLUS_EXPORT_LIB double CAAVSOP87E_Sun_X(double JD) { return CAAVSOP87E_Sun::X(JD); }
	AAPLUS_EXPORT_LIB double CAAVSOP87E_Sun_X_DASH(double JD) { return CAAVSOP87E_Sun::X_DASH(JD); }
	AAPLUS_EXPORT_LIB double CAAVSOP87E_Sun_Y(double JD) { return CAAVSOP87E_Sun::Y(JD); }
	AAPLUS_EXPORT_LIB double CAAVSOP87E_Sun_Y_DASH(double JD) { return CAAVSOP87E_Sun::Y_DASH(JD); }
	AAPLUS_EXPORT_LIB double CAAVSOP87E_Sun_Z(double JD) { return CAAVSOP87E_Sun::Z(JD); }
	AAPLUS_EXPORT_LIB double CAAVSOP87E_Sun_Z_DASH(double JD) { return CAAVSOP87E_Sun::Z_DASH(JD); }

	/* CAAVSOP87E_Uranus export functions */
	AAPLUS_EXPORT_LIB double CAAVSOP87E_Uranus_X(double JD) { return CAAVSOP87E_Uranus::X(JD); }
	AAPLUS_EXPORT_LIB double CAAVSOP87E_Uranus_X_DASH(double JD) { return CAAVSOP87E_Uranus::X_DASH(JD); }
	AAPLUS_EXPORT_LIB double CAAVSOP87E_Uranus_Y(double JD) { return CAAVSOP87E_Uranus::Y(JD); }
	AAPLUS_EXPORT_LIB double CAAVSOP87E_Uranus_Y_DASH(double JD) { return CAAVSOP87E_Uranus::Y_DASH(JD); }
	AAPLUS_EXPORT_LIB double CAAVSOP87E_Uranus_Z(double JD) { return CAAVSOP87E_Uranus::Z(JD); }
	AAPLUS_EXPORT_LIB double CAAVSOP87E_Uranus_Z_DASH(double JD) { return CAAVSOP87E_Uranus::Z_DASH(JD); }

	/* CAAVSOP87E_Venus export functions */
	AAPLUS_EXPORT_LIB double CAAVSOP87E_Venus_X(double JD) { return CAAVSOP87E_Venus::X(JD); }
	AAPLUS_EXPORT_LIB double CAAVSOP87E_Venus_X_DASH(double JD) { return CAAVSOP87E_Venus::X_DASH(JD); }
	AAPLUS_EXPORT_LIB double CAAVSOP87E_Venus_Y(double JD) { return CAAVSOP87E_Venus::Y(JD); }
	AAPLUS_EXPORT_LIB double CAAVSOP87E_Venus_Y_DASH(double JD) { return CAAVSOP87E_Venus::Y_DASH(JD); }
	AAPLUS_EXPORT_LIB double CAAVSOP87E_Venus_Z(double JD) { return CAAVSOP87E_Venus::Z(JD); }
	AAPLUS_EXPORT_LIB double CAAVSOP87E_Venus_Z_DASH(double JD) { return CAAVSOP87E_Venus::Z_DASH(JD); }

	/* CAAVSOP87_EMB export functions */
	AAPLUS_EXPORT_LIB double CAAVSOP87_EMB_A(double JD) { return CAAVSOP87_EMB::A(JD); }
	AAPLUS_EXPORT_LIB double CAAVSOP87_EMB_L(double JD) { return CAAVSOP87_EMB::L(JD); }
	AAPLUS_EXPORT_LIB double CAAVSOP87_EMB_K(double JD) { return CAAVSOP87_EMB::K(JD); }
	AAPLUS_EXPORT_LIB double CAAVSOP87_EMB_H(double JD) { return CAAVSOP87_EMB::H(JD); }
	AAPLUS_EXPORT_LIB double CAAVSOP87_EMB_Q(double JD) { return CAAVSOP87_EMB::Q(JD); }
	AAPLUS_EXPORT_LIB double CAAVSOP87_EMB_P(double JD) { return CAAVSOP87_EMB::P(JD); }

	/* CAAVSOP87_Jupiter export functions */
	AAPLUS_EXPORT_LIB double CAAVSOP87_Jupiter_A(double JD) { return CAAVSOP87_Jupiter::A(JD); }
	AAPLUS_EXPORT_LIB double CAAVSOP87_Jupiter_L(double JD) { return CAAVSOP87_Jupiter::L(JD); }
	AAPLUS_EXPORT_LIB double CAAVSOP87_Jupiter_K(double JD) { return CAAVSOP87_Jupiter::K(JD); }
	AAPLUS_EXPORT_LIB double CAAVSOP87_Jupiter_H(double JD) { return CAAVSOP87_Jupiter::H(JD); }
	AAPLUS_EXPORT_LIB double CAAVSOP87_Jupiter_Q(double JD) { return CAAVSOP87_Jupiter::Q(JD); }
	AAPLUS_EXPORT_LIB double CAAVSOP87_Jupiter_P(double JD) { return CAAVSOP87_Jupiter::P(JD); }

	/* CAAVSOP87_Mars export functions */
	AAPLUS_EXPORT_LIB double CAAVSOP87_Mars_A(double JD) { return CAAVSOP87_Mars::A(JD); }
	AAPLUS_EXPORT_LIB double CAAVSOP87_Mars_L(double JD) { return CAAVSOP87_Mars::L(JD); }
	AAPLUS_EXPORT_LIB double CAAVSOP87_Mars_K(double JD) { return CAAVSOP87_Mars::K(JD); }
	AAPLUS_EXPORT_LIB double CAAVSOP87_Mars_H(double JD) { return CAAVSOP87_Mars::H(JD); }
	AAPLUS_EXPORT_LIB double CAAVSOP87_Mars_Q(double JD) { return CAAVSOP87_Mars::Q(JD); }
	AAPLUS_EXPORT_LIB double CAAVSOP87_Mars_P(double JD) { return CAAVSOP87_Mars::P(JD); }

	/* CAAVSOP87_Mercury export functions */
	AAPLUS_EXPORT_LIB double CAAVSOP87_Mercury_A(double JD) { return CAAVSOP87_Mercury::A(JD); }
	AAPLUS_EXPORT_LIB double CAAVSOP87_Mercury_L(double JD) { return CAAVSOP87_Mercury::L(JD); }
	AAPLUS_EXPORT_LIB double CAAVSOP87_Mercury_K(double JD) { return CAAVSOP87_Mercury::K(JD); }
	AAPLUS_EXPORT_LIB double CAAVSOP87_Mercury_H(double JD) { return CAAVSOP87_Mercury::H(JD); }
	AAPLUS_EXPORT_LIB double CAAVSOP87_Mercury_Q(double JD) { return CAAVSOP87_Mercury::Q(JD); }
	AAPLUS_EXPORT_LIB double CAAVSOP87_Mercury_P(double JD) { return CAAVSOP87_Mercury::P(JD); }

	/* CAAVSOP87_Neptune export functions */
	AAPLUS_EXPORT_LIB double CAAVSOP87_Neptune_A(double JD) { return CAAVSOP87_Neptune::A(JD); }
	AAPLUS_EXPORT_LIB double CAAVSOP87_Neptune_L(double JD) { return CAAVSOP87_Neptune::L(JD); }
	AAPLUS_EXPORT_LIB double CAAVSOP87_Neptune_K(double JD) { return CAAVSOP87_Neptune::K(JD); }
	AAPLUS_EXPORT_LIB double CAAVSOP87_Neptune_H(double JD) { return CAAVSOP87_Neptune::H(JD); }
	AAPLUS_EXPORT_LIB double CAAVSOP87_Neptune_Q(double JD) { return CAAVSOP87_Neptune::Q(JD); }
	AAPLUS_EXPORT_LIB double CAAVSOP87_Neptune_P(double JD) { return CAAVSOP87_Neptune::P(JD); }

	/* CAAVSOP87_Saturn export functions */
	AAPLUS_EXPORT_LIB double CAAVSOP87_Saturn_A(double JD) { return CAAVSOP87_Saturn::A(JD); }
	AAPLUS_EXPORT_LIB double CAAVSOP87_Saturn_L(double JD) { return CAAVSOP87_Saturn::L(JD); }
	AAPLUS_EXPORT_LIB double CAAVSOP87_Saturn_K(double JD) { return CAAVSOP87_Saturn::K(JD); }
	AAPLUS_EXPORT_LIB double CAAVSOP87_Saturn_H(double JD) { return CAAVSOP87_Saturn::H(JD); }
	AAPLUS_EXPORT_LIB double CAAVSOP87_Saturn_Q(double JD) { return CAAVSOP87_Saturn::Q(JD); }
	AAPLUS_EXPORT_LIB double CAAVSOP87_Saturn_P(double JD) { return CAAVSOP87_Saturn::P(JD); }

	/* CAAVSOP87_Uranus export functions */
	AAPLUS_EXPORT_LIB double CAAVSOP87_Uranus_A(double JD) { return CAAVSOP87_Uranus::A(JD); }
	AAPLUS_EXPORT_LIB double CAAVSOP87_Uranus_L(double JD) { return CAAVSOP87_Uranus::L(JD); }
	AAPLUS_EXPORT_LIB double CAAVSOP87_Uranus_K(double JD) { return CAAVSOP87_Uranus::K(JD); }
	AAPLUS_EXPORT_LIB double CAAVSOP87_Uranus_H(double JD) { return CAAVSOP87_Uranus::H(JD); }
	AAPLUS_EXPORT_LIB double CAAVSOP87_Uranus_Q(double JD) { return CAAVSOP87_Uranus::Q(JD); }
	AAPLUS_EXPORT_LIB double CAAVSOP87_Uranus_P(double JD) { return CAAVSOP87_Uranus::P(JD); }

	/* CAAVSOP87_Venus export functions */
	AAPLUS_EXPORT_LIB double CAAVSOP87_Venus_A(double JD) { return CAAVSOP87_Venus::A(JD); }
	AAPLUS_EXPORT_LIB double CAAVSOP87_Venus_L(double JD) { return CAAVSOP87_Venus::L(JD); }
	AAPLUS_EXPORT_LIB double CAAVSOP87_Venus_K(double JD) { return CAAVSOP87_Venus::K(JD); }
	AAPLUS_EXPORT_LIB double CAAVSOP87_Venus_H(double JD) { return CAAVSOP87_Venus::H(JD); }
	AAPLUS_EXPORT_LIB double CAAVSOP87_Venus_Q(double JD) { return CAAVSOP87_Venus::Q(JD); }
	AAPLUS_EXPORT_LIB double CAAVSOP87_Venus_P(double JD) { return CAAVSOP87_Venus::P(JD); }

}

#endif // __CWRAPPER_H__
