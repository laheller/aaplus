from aaplus import *

# test aaplus library version
print(f"AAPlus version #1: {AAPlus.Version()}")
print(f"AAPlus version #2: {AAPlus.VersionNumber()}")
print()

# test January 1st 2000, 12:00:00 Julian Day number
jd = AADate.DateToJD(2000, 1, 1.5, True)
assert jd == 2451545.0

# test Python datetime to JD
now = datetime.now(timezone.utc)
jd = AADate.DateTimeUTC2JD(now)
tt = AADate.DateTimeUTC2TT(now)
print(f'Current UTC date/time expressed as Julian Day number: {jd}')
print()

print(f'Greenwich mean sidereal time:     {AACoordinateTransformation.Hours2HMS(AASidereal.MeanGreenwichSiderealTime(jd))}')
print(f'Greenwich apparent sidereal time: {AACoordinateTransformation.Hours2HMS(AASidereal.ApparentGreenwichSiderealTime(jd))}')
print()

# various tests for the current date/time 
aadate = AADate(now.year, now.month, now.day, now.hour, now.minute, now.second, True)
parts = aadate.Get()
print(f"Details for the current date/time: {parts['Year']}-{parts['Month']}-{parts['Day']} {parts['Hour']}:{parts['Minute']}:{parts['Second']:.3f} UTC")
print(f'Day of week: {aadate.DayOfWeek()}')
print(f'Days in this year: {aadate.DaysInYear()}')
print(f'Fractional year: {aadate.FractionalYear()}')
print(f'JD number: {aadate.Julian()}')
print(f'Is this year leap: {aadate.Leap()}')
print(f'Is a Gregorian date: {aadate.InGregorianCalendar()}')

DayNum = 66
res = AADate.DayOfYearToDayAndMonth(DayNum, False)
print(f"The {DayNum}. day of the year is on {res['DayOfMonth']}. of {Months(res['Month']).name}.")
print()

# get the 2025 March Equinox time
MarchEquinoxTT = AAEquinoxesAndSolstices.NorthwardEquinox(2025, True)
parts = AADate.JDToDateParts(AADynamicalTime.TT2UTC(MarchEquinoxTT), True)
print(f"2025 March Equinox occurs on {AADate.TT2DateTimeUTC(MarchEquinoxTT).strftime('%Y-%b-%d %H:%M:%S')} UTC")
print()

# get 2025 equinoxes and solstices dates
startJD = AADate.DateTimeUTC2TT(datetime(year=2025, month=1, day=1, hour=12, minute=0, second=0, tzinfo=timezone.utc))
endJD = AADate.DateTimeUTC2TT(datetime(year=2025, month=12, day=31, hour=23, minute=59, second=59, tzinfo=timezone.utc))
list = AAEquinoxesAndSolstices2.Calculate(startJD, endJD)
for x in list:
    print(f'Type: {AAEquinoxesAndSolstices2.Type(x.type).name}')
    print(f"When: {AADate.TT2DateTimeUTC(x.JD).strftime('%Y-%b-%d %H:%M:%S')} UTC")
    print()

# get 2025 Easter date
easter = AAEaster.Calculate(2025)
print(f'2025 Easter occurs on: {easter.Month}. {easter.Day}.')
print()

# calculate Moon phases during May 2025
MPStartJD = AADate.DateTimeUTC2TT(datetime(year=2025, month=5, day=1, hour=12, minute=0, second=0, tzinfo=timezone.utc))
MPEndJD = AADate.DateTimeUTC2TT(datetime(year=2025, month=5, day=31, hour=0, minute=0, second=0, tzinfo=timezone.utc))
list = AAMoonPhases2.Calculate(MPStartJD, MPEndJD, 0.007, AAMoonPhases2.Algorithm.ELP2000)
for x in list:
    print(f'Type: {AAMoonPhases2.Type(x.type).name}')
    print(f"When: {AADate.TT2DateTimeUTC(x.JD).strftime('%Y-%b-%d %H:%M:%S')} UTC")
    print()

# Earth velocity test
ev = AAAberration.EarthVelocity(tt, True)
print(f'Earth velocity X: {ev.X * 10e-8} AU/day')
print(f'Earth velocity Y: {ev.Y * 10e-8} AU/day')
print(f'Earth velocity Z: {ev.Z * 10e-8} AU/day')
print()

# Mercury elliptical parameters test
elem = AAElliptical.AAEllipticalObjectElements(0.38709831000000, 0.205636952745891, 7.00544937793475, 214.033155488883, 48.6334292020304, tt, tt)
det = AAElliptical.Calculate_2(tt, elem)
print(f'TrueGeocentricDistance: {det.TrueGeocentricDistance}')
print()

# test the AAVSOP2013 class
inst = AAVSOP2013()
inst.SetBinaryFilesDirectory('C:\\Ladsi1')
dir = inst.GetBinaryFilesDirectory()
print(f'Directory: {dir}')
print()

# Degrees2DMS and Hours2HMS conversion tests
deg = 275.2947
print(f'Degrees to DMS conversion: {deg} degrees = {AACoordinateTransformation.Degrees2DMS(deg)}')
hrs = 23.9999
print(f'Hours to HMS conversion: {hrs} hours = {AACoordinateTransformation.Hours2HMS(hrs)}')
print()

# calculate rise/transit/set of the Moon for current time at Bratislava/Slovakia
GeoLat = AACoordinateTransformation.DMSToDegrees(48, 8, 41, True)
GeoLon = AACoordinateTransformation.DMSToDegrees(17, 6, 46, False) # East longitude should be a negative number!
now2 = datetime.combine(now.date(), datetime.min.time(), timezone.utc) # take only the date part
TTnow = AADate.DateTimeUTC2TT(now2)
coo1 = AACoordinateTransformation.Ecliptic2Equatorial(AAMoon.EclipticLongitude(TTnow - 1), AAMoon.EclipticLatitude(TTnow - 1), AANutation.TrueObliquityOfEcliptic(TTnow - 1))
coo2 = AACoordinateTransformation.Ecliptic2Equatorial(AAMoon.EclipticLongitude(TTnow), AAMoon.EclipticLatitude(TTnow), AANutation.TrueObliquityOfEcliptic(TTnow))
coo3 = AACoordinateTransformation.Ecliptic2Equatorial(AAMoon.EclipticLongitude(TTnow + 1), AAMoon.EclipticLatitude(TTnow + 1), AANutation.TrueObliquityOfEcliptic(TTnow + 1))
det = AARiseTransitSet.Calculate(TTnow, coo1.X, coo1.Y, coo2.X, coo2.Y, coo3.X, coo3.Y, GeoLon, GeoLat, 0.125)
if det.bRiseValid:
    print(f'Moon rises at: {AACoordinateTransformation.Hours2HMS(det.Rise)} UTC')
if det.bTransitValid:
    TransitType = 'above' if det.bTransitAboveHorizon else 'below'
    print(f'Moon transits {TransitType} horizon at: {AACoordinateTransformation.Hours2HMS(det.Transit)} UTC')
if det.bSetValid:
    print(f'Moon sets at: {AACoordinateTransformation.Hours2HMS(det.Set)} UTC')
print()

# calculate Moon phase
angle = AAMoon.GetLunarPhaseAngle(now)
msg = 'Lunar phase'
if angle == 0 or angle == 360:
    msg = 'New Moon'
elif angle > 0 and angle < 90:
    msg = 'Waxing Crescent'
elif angle == 90:
    msg = 'First Quarter'
elif angle > 90 and angle < 180:
    msg = 'Waxing Gibbous'
elif angle == 180:
    msg = 'Full Moon'
elif angle > 180 and angle < 270:
    msg = 'Waning Gibbous'
elif angle == 270:
    msg = 'Last Quarter'
elif angle > 270 and angle < 360:
    msg = 'Waning Crescent'
else:
    msg = 'N/A'
print(f'Lunar phase angle now: {angle:.3f} degrees => {msg}')
print()

# calculate various Venus ecliptic coordinates
venus_details = AAElliptical.Calculate(tt, AAElliptical.Object.VENUS, True)

# Apparent - used in planetarium software and for visual observation predictions
print('Venus apparent geocentric ecliptic coordinates now (UTC):')
print(f'\tLongitude (λ): {AACoordinateTransformation.Degrees2DMS(venus_details.ApparentGeocentricEclipticalLongitude)}')
print(f'\tLatitude (β):  {AACoordinateTransformation.Degrees2DMS(venus_details.ApparentGeocentricEclipticalLatitude)}')

# True - used in precise orbital mechanics or ephemerides generation
print('Venus true geocentric ecliptic coordinates now (UTC):')
print(f'\tLongitude (λ): {AACoordinateTransformation.Degrees2DMS(venus_details.TrueGeocentricEclipticalLongitude)}')
print(f'\tLatitude (β):  {AACoordinateTransformation.Degrees2DMS(venus_details.TrueGeocentricEclipticalLatitude)}')

print('Venus true heliocentric ecliptic coordinates now (UTC):')
print(f'\tLongitude (λ): {AACoordinateTransformation.Degrees2DMS(venus_details.TrueHeliocentricEclipticalLongitude)}')
print(f'\tLatitude (β):  {AACoordinateTransformation.Degrees2DMS(venus_details.TrueHeliocentricEclipticalLatitude)}')

sd = AADiameters.VenusSemidiameterA(venus_details.ApparentGeocentricDistance) / 3600
eps = AANutation.TrueObliquityOfEcliptic(tt)
venus_topo = AAParallax.Ecliptic2Topocentric(
    venus_details.ApparentGeocentricEclipticalLongitude,
    venus_details.ApparentGeocentricEclipticalLatitude,
    sd,
    venus_details.ApparentGeocentricDistance,
    eps,
    GeoLat,
    111,
    tt)
print('Venus topocentric ecliptic coordinates now (UTC):')
print(f'\tLongitude (λ): {AACoordinateTransformation.Degrees2DMS(venus_topo.Lambda)}')
print(f'\tLatitude (β):  {AACoordinateTransformation.Degrees2DMS(venus_topo.Beta)}')
print()

print(f'True obliquity of the Ecliptic now (UTC): {AACoordinateTransformation.Degrees2DMS(eps)}')
print()

print('Earth heliocentric ecliptic coordinates now (UTC):')
# Longitude: 180° at March Equinox; 0° at September Equinox
print(f'\tLongitude (λ): {AACoordinateTransformation.Degrees2DMS(AAEarth.EclipticLongitude(tt, True))}')
print(f'\tLatitude (β):  {AACoordinateTransformation.Degrees2DMS(AAEarth.EclipticLatitude(tt, True))}')
print()

# calculate the next Lunar eclipse event
mk = 0.5 + math.trunc(AAMoonPhases.K(aadate.FractionalYear())) # + 0.5 is required!
while True:
    lec = AAEclipses.CalculateLunar(mk)
    if lec.bEclipse:
        print(f"Maximum of the next Lunar eclipse occurs on {AADate.TT2DateTimeUTC(lec.TimeOfMaximumEclipse).strftime('%Y-%b-%d %H:%M:%S')} UTC")
        print()
        break
    mk += 1.0
    print(f'mk = {mk}')
print()

# calculate the next Venus inferior conjuction
planet = AAPlanetaryPhenomena.Planet.VENUS
evt = AAPlanetaryPhenomena.Type.INFERIOR_CONJUNCTION
vk = math.trunc(AAPlanetaryPhenomena.K(aadate.FractionalYear(), planet, evt))
while True:
    EvtDate = AADate.TT2DateTimeUTC(AAPlanetaryPhenomena._True(vk, planet, evt))
    if EvtDate > now:
        print(f"Venus next {evt.name} occurs on {EvtDate.strftime('%Y-%b-%d %H:%M:%S')} UTC")
        break
    vk += 1.0

print('Done!')