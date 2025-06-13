using AAPlus;
using System.Diagnostics;
using System.Text;

namespace test {
    internal class Program {
        static void Main(string[] args) {
            Console.OutputEncoding = Encoding.UTF8;
            Console.WriteLine("AAPlus C# wrapper test");

            var ver = AAPlus.AAPlus.Version();
            Console.WriteLine($"Library version: {ver}");
            Console.WriteLine($"Version number: {AAPlus.AAPlus.VersionNumber()}");
            Console.WriteLine();

            var jd = AADate.DateToJD(2000L, 1L, 1.5, true); // 2000.jan.1 - 12:00:00
            Debug.Assert(jd == 2451545.0, "JD calculation error");
            Console.WriteLine($"JD at [2000.jan.1 - 12:00:00]: {jd}");

            jd = AADate.DateTimeUTC2JD(new DateTime(2000, 1, 1, 12, 0, 0, DateTimeKind.Utc));
            Debug.Assert(jd == 2451545.0, "JD calculation error");
            Console.WriteLine($"JD at [2000.jan.1 - 12:00:00]: {jd}");

            var now = DateTime.UtcNow;
            var Formatted = $"{now:yyyy-MMM-dd HH:mm:ss}";

            jd = AADate.DateTimeUTC2JD(now);
            Console.WriteLine($"GMST: {AACoordinateTransformation.Hours2HMS(AASidereal.MeanGreenwichSiderealTime(jd))}");
            Console.WriteLine($"GAST: {AACoordinateTransformation.Hours2HMS(AASidereal.ApparentGreenwichSiderealTime(jd))}");
            Console.WriteLine();

            Console.WriteLine($"Details for current date: {Formatted} UTC");
            using (var dt1 = new AADate(now)) {
                dt1.Get(out long year, out long month, out long day, out long hour, out long minute, out double second);
                Console.WriteLine($"Day of week:         {dt1.DayOfWeek}");
                Console.WriteLine($"Days in this year:   {dt1.DaysInYear}");
                Console.WriteLine($"Fractional year:     {dt1.FractionalYear:F5}");
                Console.WriteLine($"JD number:           {dt1.Julian}");
                Console.WriteLine($"Is this year leap:   {dt1.Leap}");
                Console.WriteLine($"Is a Gregorian date: {dt1.InGregorianCalendar}");
            }
            Console.WriteLine($"Leap 2025: {AADate.IsLeap(2025, true)}");
            Console.WriteLine();

            var MarchEquinoxTT = AAEquinoxesAndSolstices.NorthwardEquinox(2025, true);
            var meq = AADate.TT2DateTimeUTC(MarchEquinoxTT);
            Console.WriteLine($"2025 March Equinox occurs on {meq:yyyy.MMM.dd} at {meq:HH:mm:ss} UTC");
            Console.WriteLine();

            var startJD = AADate.DateTimeUTC2TT(new DateTime(2025, 1, 1, 12, 0, 0, DateTimeKind.Utc));
            var endJD = AADate.DateTimeUTC2TT(new DateTime(2025, 12, 31, 23, 59, 59, DateTimeKind.Utc));
            var result = AAEquinoxesAndSolstices2.Calculate(startJD, endJD, 0.007, true);
            Console.WriteLine($"Equnixoes and solstices in the year 2025: {result.Length}");

            foreach (var item in result) {
                Console.WriteLine($"Event type:                      {item.type}");
                //Console.WriteLine($"Occurs on:   {item.JD}");
                var dt = AADate.TT2DateTimeUTC(item.JD);
                Console.WriteLine($"Occurs on:                       {dt:yyyy-MMM-dd HH:mm:ss} UTC");
                Console.WriteLine();
            }

            var easter = AAEaster.Calculate(2025, true);
            Console.WriteLine($"2025 Easter occurs at: {easter.Month}.{easter.Day}.");
            Console.WriteLine();

            var MPStartJD = AADate.DateTimeUTC2TT(new DateTime(2025, 5, 1, 12, 0, 0, DateTimeKind.Utc));
            var MPEndJD = AADate.DateTimeUTC2TT(new DateTime(2025, 5, 31, 0, 0, 0, DateTimeKind.Utc));
            var result2 = AAMoonPhases2.Calculate(MPStartJD, MPEndJD, 1.0, AAMoonPhases2.Algorithm.ELP2000);
            Console.WriteLine($"Moon phases in May 2025: {result2.Length}");

            foreach (var item in result2) {
                Console.WriteLine($"Type:      {item.type}");
                var dt = AADate.TT2DateTimeUTC(item.JD);
                Console.WriteLine($"Occurs on: {dt:yyyy-MMM-dd HH:mm:ss} UTC");
                Console.WriteLine();
            }

            Console.WriteLine("AAAberration test:");
            var EarthVelocity = AAAberration.EarthVelocity(AADate.DateTimeUTC2TT(now), true);
            Console.WriteLine($"Earth velocity X: {EarthVelocity.X * 10e-8} AU/day");
            Console.WriteLine($"Earth velocity Y: {EarthVelocity.Y * 10e-8} AU/day");
            Console.WriteLine($"Earth velocity Z: {EarthVelocity.Z * 10e-8} AU/day");
            Console.WriteLine();

            Console.WriteLine("AAVSOP2013 test:");
            using (var inst = new AAVSOP2013()) {
                inst.SetBinaryFilesDirectory(@"C:\Temp1");
                var dir = inst.GetBinaryFilesDirectory();
                Console.WriteLine($"Directory: {dir}");
            }
            Console.WriteLine();

            Console.WriteLine($"Degrees to DMS conversion: 275.2947 degrees = {AACoordinateTransformation.Degrees2DMS(275.2947)}");
            Console.WriteLine($"Hours to HMS conversion: 23.9999 hours = {AACoordinateTransformation.Hours2HMS(23.9999)}");
            Console.WriteLine();

            Console.WriteLine("Calculate Rise/Transit/Set of the Moon for current time at Bratislava/Slovakia:");
            // Bratislava/Slovakia coordinates: 48° 08′ 41″ N, 17° 06′ 46″ E
            var GeoLat = AACoordinateTransformation.DMSToDegrees(48, 8, 41, true);
            var GeoLon = AACoordinateTransformation.DMSToDegrees(17, 6, 46, false); // East longitude should be a negative number!
            var now2 = now.Date; // we only need the date part WITHOUT the fractions of the day
            var TTNow = AADate.DateTimeUTC2TT(now2);
            var coo1 = AACoordinateTransformation.Ecliptic2Equatorial(AAMoon.EclipticLongitude(TTNow - 1), AAMoon.EclipticLatitude(TTNow - 1), AANutation.TrueObliquityOfEcliptic(TTNow - 1));
            var coo2 = AACoordinateTransformation.Ecliptic2Equatorial(AAMoon.EclipticLongitude(TTNow), AAMoon.EclipticLatitude(TTNow), AANutation.TrueObliquityOfEcliptic(TTNow));
            var coo3 = AACoordinateTransformation.Ecliptic2Equatorial(AAMoon.EclipticLongitude(TTNow + 1), AAMoon.EclipticLatitude(TTNow + 1), AANutation.TrueObliquityOfEcliptic(TTNow + 1));
            var det = AARiseTransitSet.Calculate(TTNow, coo1.X, coo1.Y, coo2.X, coo2.Y, coo3.X, coo3.Y, GeoLon, GeoLat, 0.125);
            if (det.bRiseValid) Console.WriteLine($"Moon rises at:                  {AACoordinateTransformation.Hours2HMS(det.Rise)} UTC");
            if (det.bTransitValid) {
                var TransitType = det.bTransitAboveHorizon ? "above" : "below";
                Console.WriteLine($"Moon transits {TransitType} horizon at: {AACoordinateTransformation.Hours2HMS(det.Transit)} UTC");
            }
            if (det.bSetValid) Console.WriteLine($"Moon sets at:                   {AACoordinateTransformation.Hours2HMS(det.Set)} UTC");
            Console.WriteLine();

            var angle = AAMoon.GetLunarPhaseAngle(now);
            var msg = "Lunar phase";
            if (angle == 0 || angle == 360) msg = "New Moon";
            else if (angle > 0 && angle < 90) msg = "Waxing Crescent";
            else if (angle == 90) msg = "First Quarter";
            else if (angle > 90 && angle < 180) msg = "Waxing Gibbous";
            else if (angle == 180) msg = "Full Moon";
            else if (angle > 180 && angle < 270) msg = "Waning Gibbous";
            else if (angle == 270) msg = "Last Quarter";
            else if (angle > 270 && angle < 360) msg = "Waning Crescent";
            Console.WriteLine($"Lunar phase angle now: {angle:F3} degrees => {msg}");
            Console.WriteLine();

            var JDNowTT = AADate.DateTimeUTC2TT(now);
            var VenusDetails = AAElliptical.Calculate(JDNowTT, AAElliptical.Object.VENUS, true);
            Console.WriteLine("Venus apparent geocentric ecliptic coordinates now (UTC):"); // Used in planetarium software and for visual observation predictions.
            Console.WriteLine($"\tLongitude (λ): {AACoordinateTransformation.Degrees2DMS(VenusDetails.ApparentGeocentricEclipticalLongitude)}");
            Console.WriteLine($"\tLatitude  (β): {AACoordinateTransformation.Degrees2DMS(VenusDetails.ApparentGeocentricEclipticalLatitude)}");
            Console.WriteLine();

            Console.WriteLine("Venus true geocentric ecliptic coordinates now (UTC):"); // Used in precise orbital mechanics or ephemerides generation.
            Console.WriteLine($"\tLongitude (λ): {AACoordinateTransformation.Degrees2DMS(VenusDetails.TrueGeocentricEclipticalLongitude)}");
            Console.WriteLine($"\tLatitude  (β): {AACoordinateTransformation.Degrees2DMS(VenusDetails.TrueGeocentricEclipticalLatitude)}");
            Console.WriteLine();

            Console.WriteLine("Venus true heliocentric ecliptic coordinates now (UTC):");
            Console.WriteLine($"\tLongitude (λ): {AACoordinateTransformation.Degrees2DMS(VenusDetails.TrueHeliocentricEclipticalLongitude)}");
            Console.WriteLine($"\tLatitude  (β): {AACoordinateTransformation.Degrees2DMS(VenusDetails.TrueHeliocentricEclipticalLatitude)}");
            Console.WriteLine();

            var VenusSemiDia = AADiameters.VenusSemidiameterA(VenusDetails.ApparentGeocentricDistance) / 3600.0; // arcseconds => degrees
            var eps = AANutation.TrueObliquityOfEcliptic(JDNowTT);
            var VenusTopo = AAParallax.Ecliptic2Topocentric(VenusDetails.ApparentGeocentricEclipticalLongitude, VenusDetails.ApparentGeocentricEclipticalLatitude, VenusSemiDia, VenusDetails.ApparentGeocentricDistance, eps, GeoLat, 111, JDNowTT);
            Console.WriteLine("Venus topocentric ecliptic coordinates now (UTC):");
            Console.WriteLine($"\tLongitude (λ): {AACoordinateTransformation.Degrees2DMS(VenusTopo.Lambda)}");
            Console.WriteLine($"\tLatitude  (β): {AACoordinateTransformation.Degrees2DMS(VenusTopo.Beta)}");
            Console.WriteLine();

            Console.WriteLine($"True obliquity of the Ecliptic now (UTC): {AACoordinateTransformation.Degrees2DMS(eps)}");
            Console.WriteLine();

            Console.WriteLine("Earth heliocentric ecliptic coordinates now (UTC):");
            // Longitude: 180° at March Equinox; 0° at September Equinox
            Console.WriteLine($"\tLongitude (λ): {AACoordinateTransformation.Degrees2DMS(AAEarth.EclipticLongitude(JDNowTT, true))}");
            Console.WriteLine($"\tLatitude  (β): {AACoordinateTransformation.Degrees2DMS(AAEarth.EclipticLatitude(JDNowTT, true))}");
            Console.WriteLine();

            var mk = 0.5; // must be
            using (var date1 = new AADate(now)) mk += Math.Truncate(AAMoonPhases.K(date1.FractionalYear));
            while (true) {
                var lec = AAEclipses.CalculateLunar(mk);
                if (lec.bEclipse) {
                    Console.WriteLine($"Maximum of next lunar eclipse occurs on {AADate.TT2DateTimeUTC(lec.TimeOfMaximumEclipse):yyyy-MMM-dd HH:mm:ss} UTC");
                    Console.WriteLine();
                    break;
                }
                mk += 1.0;
                Console.WriteLine($"mk = {mk}");
            }

            var planet = AAPlanetaryPhenomena.Planet.VENUS;
            var evt = AAPlanetaryPhenomena.Type.INFERIOR_CONJUNCTION;
            var vk = 0.0;
            using (var date1 = new AADate(now)) vk = Math.Truncate(AAPlanetaryPhenomena.K(date1.FractionalYear, planet, evt));
            while (true) {
                var EvtDate = AADate.TT2DateTimeUTC(AAPlanetaryPhenomena.True(vk, planet, evt));
                if (EvtDate >= DateTime.UtcNow) {
                    Console.WriteLine($"Venus next {evt} occurs on {EvtDate:yyyy-MMM-dd HH:mm:ss} UTC");
                    break;
                }
                vk += 1.0;
            }
        }
    }
}
