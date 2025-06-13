using System;
using System.Diagnostics;
using System.Runtime.InteropServices;
using static AAPlus.AADate;
using static AAPlus.AAElliptical;
using static AAPlus.AAParabolic;

namespace AAPlus {
    [StructLayout(LayoutKind.Sequential)]
    public struct AA2DCoordinate {
        public double X;
        public double Y;
    }

    [StructLayout(LayoutKind.Sequential)]
    public struct AA3DCoordinate {
        public double X;
        public double Y;
        public double Z;
    }

    public class AAPlus {
        private const string LibName = "caaplus";

        [DllImport(LibName, EntryPoint = "CAAPlus_Version")]
        private static extern IntPtr _Version();

        [DllImport(LibName, EntryPoint = "CAAPlus_VersionNumber")]
        public static extern int VersionNumber();

        public static string Version() => Marshal.PtrToStringAnsi(_Version());
    }

    public class AAAberration {
        private const string LibName = "caaplus";

        [DllImport(LibName, EntryPoint = "CAAAberration_EarthVelocity")]
        public static extern AA3DCoordinate EarthVelocity(double JD, bool bHighPrecision);

        [DllImport(LibName, EntryPoint = "CAAAberration_EclipticAberration")]
        public static extern AA2DCoordinate EclipticAberration(double Alpha, double Delta, double JD, bool bHighPrecision);

        [DllImport(LibName, EntryPoint = "CAAAberration_EquatorialAberration")]
        public static extern AA2DCoordinate EquatorialAberration(double Lambda, double Beta, double JD, bool bHighPrecision);

    }

    public class AAAngularSeparation {
        private const string LibName = "caaplus";

        [DllImport(LibName, EntryPoint = "CAAAngularSeparation_Separation")]
        public static extern double Separation(double Alpha1, double Delta1, double Alpha2, double Delta2);

        [DllImport(LibName, EntryPoint = "CAAAngularSeparation_PositionAngle")]
        public static extern double PositionAngle(double Alpha1, double Delta1, double Alpha2, double Delta2);

        [DllImport(LibName, EntryPoint = "CAAAngularSeparation_DistanceFromGreatArc")]
        public static extern double DistanceFromGreatArc(double Alpha1, double Delta1, double Alpha2, double Delta2, double Alpha3, double Delta3);

        [DllImport(LibName, EntryPoint = "CAAAngularSeparation_SmallestCircle")]
        public static extern double SmallestCircle(double Alpha1, double Delta1, double Alpha2, double Delta2, double Alpha3, double Delta3, out bool bType1);

    }

    public class AABinaryStar {
        private const string LibName = "caaplus";

        [StructLayout(LayoutKind.Sequential)]
        public struct AABinaryStarDetails {
            public double r;
            public double Theta;
            public double Rho;
            public double x;
            public double y;
        }

        [DllImport(LibName, EntryPoint = "CAABinaryStar_Calculate")]
        public static extern AABinaryStarDetails Calculate(double t, double P, double T, double e, double a, double i, double omega, double w);

        [DllImport(LibName, EntryPoint = "CAABinaryStar_ApparentEccentricity")]
        public static extern double ApparentEccentricity(double e, double i, double w);

    }

    public class AACoordinateTransformation {
        private const string LibName = "caaplus";

        [DllImport(LibName, EntryPoint = "CAACoordinateTransformation_Equatorial2Ecliptic")]
        public static extern AA2DCoordinate Equatorial2Ecliptic(double Alpha, double Delta, double Epsilon);

        [DllImport(LibName, EntryPoint = "CAACoordinateTransformation_Ecliptic2Equatorial")]
        public static extern AA2DCoordinate Ecliptic2Equatorial(double Lambda, double Beta, double Epsilon);

        [DllImport(LibName, EntryPoint = "CAACoordinateTransformation_Equatorial2Horizontal")]
        public static extern AA2DCoordinate Equatorial2Horizontal(double LocalHourAngle, double Delta, double Latitude);

        [DllImport(LibName, EntryPoint = "CAACoordinateTransformation_Horizontal2Equatorial")]
        public static extern AA2DCoordinate Horizontal2Equatorial(double A, double h, double Latitude);

        [DllImport(LibName, EntryPoint = "CAACoordinateTransformation_Equatorial2Galactic")]
        public static extern AA2DCoordinate Equatorial2Galactic(double Alpha, double Delta);

        [DllImport(LibName, EntryPoint = "CAACoordinateTransformation_Galactic2Equatorial")]
        public static extern AA2DCoordinate Galactic2Equatorial(double l, double b);

        [DllImport(LibName, EntryPoint = "CAACoordinateTransformation_DegreesToRadians")]
        public static extern double DegreesToRadians(double Degrees);

        [DllImport(LibName, EntryPoint = "CAACoordinateTransformation_RadiansToDegrees")]
        public static extern double RadiansToDegrees(double Radians);

        [DllImport(LibName, EntryPoint = "CAACoordinateTransformation_RadiansToHours")]
        public static extern double RadiansToHours(double Radians);

        [DllImport(LibName, EntryPoint = "CAACoordinateTransformation_HoursToRadians")]
        public static extern double HoursToRadians(double Hours);

        [DllImport(LibName, EntryPoint = "CAACoordinateTransformation_HoursToDegrees")]
        public static extern double HoursToDegrees(double Hours);

        [DllImport(LibName, EntryPoint = "CAACoordinateTransformation_DegreesToHours")]
        public static extern double DegreesToHours(double Degrees);

        [DllImport(LibName, EntryPoint = "CAACoordinateTransformation_PI")]
        public static extern double PI();

        [DllImport(LibName, EntryPoint = "CAACoordinateTransformation_MapTo0To360Range")]
        public static extern double MapTo0To360Range(double Degrees);

        [DllImport(LibName, EntryPoint = "CAACoordinateTransformation_MapToMinus90To90Range")]
        public static extern double MapToMinus90To90Range(double Degrees);

        [DllImport(LibName, EntryPoint = "CAACoordinateTransformation_MapTo0To24Range")]
        public static extern double MapTo0To24Range(double HourAngle);

        [DllImport(LibName, EntryPoint = "CAACoordinateTransformation_MapTo0To2PIRange")]
        public static extern double MapTo0To2PIRange(double Angle);

        [DllImport(LibName, EntryPoint = "CAACoordinateTransformation_DMSToDegrees")]
        public static extern double DMSToDegrees(double Degrees, double Minutes, double Seconds, bool bPositive);

        /// <summary>
        /// Formats decimal degrees as a DMS string with customizable separator characters.
        /// </summary>
        public static string Degrees2DMS(double Degrees, char DegDelim = '°', char MinDelim = '′', char SecDelim = '″', char FracDelim = '.') {
            var IsNegative = false;
            if (Degrees < 0) {
                Degrees = -Degrees;
                IsNegative = true;
            }

            var WholeDeg = Math.Truncate(Degrees);
            var DDD = WholeDeg.ToString().PadLeft(2, '0');

            var Minutes = (Degrees - WholeDeg) * 60.0;
            var WholeMin = Math.Truncate(Minutes);
            var MM = WholeMin.ToString().PadLeft(2, '0');

            var Seconds = (Minutes - WholeMin) * 60.0;
            var WholeSec = Math.Truncate(Seconds);
            var SS = WholeSec.ToString().PadLeft(2, '0');

            var Fracs = (Seconds - WholeSec) * 1000.0;
            var WholeFracs = Math.Truncate(Fracs);

            var result = $"{DDD}{DegDelim}{MM}{MinDelim}{SS}{FracDelim}{WholeFracs}{SecDelim}";
            if (IsNegative) result = $"-{result}";

            return result;
        }

        /// <summary>
        /// Formats decimal hours as a HMS string with customizable separator characters.
        /// </summary>
        public static string Hours2HMS(double Hours, char HourDelim = ':', char MinDelim = ':') {
            Debug.Assert(Hours >= 0.0, "Argument \"Hours\" must be a nonnegative number!");

            var WholeHour = Math.Truncate(Hours);
            var HH = WholeHour.ToString().PadLeft(2, '0');

            var Minutes = (Hours - WholeHour) * 60.0;
            var WholeMin = Math.Truncate(Minutes);
            var MM = WholeMin.ToString().PadLeft(2, '0');

            var Seconds = (Minutes - WholeMin) * 60.0;
            var WholeSec = Math.Truncate(Seconds);
            var SS = WholeSec.ToString().PadLeft(2, '0');

            return $"{HH}{HourDelim}{MM}{MinDelim}{SS}";
        }
    }

    public class AADate : IDisposable {
        private const string LibName = "caaplus";
        private IntPtr _ptr = IntPtr.Zero;
        private bool disposedValue;

        /// <summary>
        /// Initializes a new <b>AADate</b> instance using date and time parts.
        /// </summary>
        public AADate(long year, long month, double day, double hour, double minute, double second, bool IsGregorian) {
            _ptr = Create(year, month, day, hour, minute, second, IsGregorian);
        }

        /// <summary>
        /// Initializes a new <b>AADate</b> instance using <b>System.DateTime</b> in UTC timeframe.
        /// </summary>
        public AADate(DateTime date, bool IsGregorian = true) {
            #if DEBUG
            Debug.Assert(date.Kind == DateTimeKind.Utc, "Argument \"date\" must be in UTC timeframe!");
            #else
            Trace.Assert(date.Kind == DateTimeKind.Utc, "Argument \"date\" must be in UTC timeframe!");
            #endif
            _ptr = Create(date.Year, date.Month, date.Day, date.Hour, date.Minute, date.Second, IsGregorian);
        }

        [Flags]
        public enum DOW : int {
            SUNDAY = 0,
            MONDAY = 1,
            TUESDAY = 2,
            WEDNESDAY = 3,
            THURSDAY = 4,
            FRIDAY = 5,
            SATURDAY = 6,
        }

        [StructLayout(LayoutKind.Sequential)]
        public struct AACalendarDate {
            public long Year;
            public long Month;
            public long Day;
        }

        #region Public native methods
        [DllImport(LibName, EntryPoint = "CAADate_DateToJD")]
        public static extern double DateToJD(long Year, long Month, double Day, bool bGregorianCalendar);

        [DllImport(LibName, EntryPoint = "CAADate_IsLeap")]
        [return: MarshalAs(UnmanagedType.U1)]
        public static extern bool IsLeap(long Year, bool bGregorianCalendar);

        [DllImport(LibName, EntryPoint = "CAADate_DayOfYearToDayAndMonth")]
        public static extern void DayOfYearToDayAndMonth(long DayOfYear, bool bLeap, out long DayOfMonth, out long Month);

        [DllImport(LibName, EntryPoint = "CAADate_JulianToGregorian")]
        public static extern AACalendarDate JulianToGregorian(long Year, long Month, long Day);

        [DllImport(LibName, EntryPoint = "CAADate_GregorianToJulian")]
        public static extern AACalendarDate GregorianToJulian(long Year, long Month, long Day);

        [DllImport(LibName, EntryPoint = "CAADate_INT")]
        public static extern long INT(double value);

        [DllImport(LibName, EntryPoint = "CAADate_AfterPapalReform")]
        [return: MarshalAs(UnmanagedType.U1)]
        public static extern bool AfterPapalReform(long Year, long Month, double Day);

        [DllImport(LibName, EntryPoint = "CAADate_AfterPapalReform_2")]
        [return: MarshalAs(UnmanagedType.U1)]
        public static extern bool AfterPapalReform_2(double JD);

        [DllImport(LibName, EntryPoint = "CAADate_DayOfYear")]
        public static extern double DayOfYear(double JD, long Year, bool bGregorianCalendar);

        [DllImport(LibName, EntryPoint = "CAADate_DaysInMonth")]
        public static extern long DaysInMonth(long Month, bool bLeap);

        [DllImport(LibName, EntryPoint = "CAADate_JDToDateParts")]
        public static extern void JDToDateParts(double JD, bool IsGregorian, out long year, out long month, out long day, out long hour, out long minute, out double second);
        #endregion

        #region Private native methods
        [DllImport(LibName, EntryPoint = "CAADate_Create")]
        private static extern IntPtr Create(long year, long month, double day, double hour, double minute, double second, bool IsGregorian);

        [DllImport(LibName, EntryPoint = "CAADate_Get")]
        private static extern void Get(IntPtr self, out long year, out long month, out long day, out long hour, out long minute, out double second);

        [DllImport(LibName, EntryPoint = "CAADate_Set")]
        private static extern void Set(IntPtr self, long year, long month, double day, double hour, double minute, double second, bool IsGregorian);

        [DllImport(LibName, EntryPoint = "CAADate_DayOfWeek")]
        private static extern DOW _DayOfWeek(IntPtr self);

        [DllImport(LibName, EntryPoint = "CAADate_DaysInYear")]
        private static extern long _DaysInYear(IntPtr self);

        [DllImport(LibName, EntryPoint = "CAADate_FractionalYear")]
        private static extern double _FractionalYear(IntPtr self);

        [DllImport(LibName, EntryPoint = "CAADate_InGregorianCalendar")]
        [return: MarshalAs(UnmanagedType.U1)]
        private static extern bool _InGregorianCalendar(IntPtr self);

        [DllImport(LibName, EntryPoint = "CAADate_Leap")]
        [return: MarshalAs(UnmanagedType.U1)]
        private static extern bool _Leap(IntPtr self);

        [DllImport(LibName, EntryPoint = "CAADate_SetInGregorianCalendar")]
        private static extern void SetInGregorianCalendar(IntPtr self, bool IsGregorian);

        [DllImport(LibName, EntryPoint = "CAADate_Julian")]
        private static extern double _Julian(IntPtr self);

        [DllImport(LibName, EntryPoint = "CAADate_Destroy")]
        private static extern void Destroy(IntPtr self);
        #endregion

        public void Get(out long year, out long month, out long day, out long hour, out long minute, out double second) => Get(_ptr, out year, out month, out day, out hour, out minute, out second);
        public void Set(long year, long month, double day, double hour, double minute, double second, bool IsGregorian) => Set(_ptr, year, month, day, hour, minute, second, IsGregorian);
        public DOW DayOfWeek => _DayOfWeek(_ptr);
        public long DaysInYear => _DaysInYear(_ptr);
        public double FractionalYear => _FractionalYear(_ptr);
        public bool InGregorianCalendar => _InGregorianCalendar(_ptr);
        public bool Leap => _Leap(_ptr);
        public void SetInGregorianCalendar(bool IsGregorian) => SetInGregorianCalendar(_ptr, IsGregorian);
        public double Julian => _Julian(_ptr);

        /// <summary>
        /// Converts <b>System.DateTime</b> to Julian Day number while keeps UTC.
        /// </summary>
        public static double DateTimeUTC2JD(DateTime date, bool IsGregorian = true) {
            #if DEBUG
            Debug.Assert(date.Kind == DateTimeKind.Utc, "Argument \"date\" must be in UTC timeframe!");
            #else
            Trace.Assert(date.Kind == DateTimeKind.Utc, "Argument \"date\" must be in UTC timeframe!");
            #endif
            return DateToJD(date.Year, date.Month, date.Day + date.TimeOfDay.TotalDays, IsGregorian);
        }

        /// <summary>
        /// Converts Julian Day number in TT timeframe to <b>System.DateTime</b> in UTC timeframe.
        /// </summary>
        public static DateTime TT2DateTimeUTC(double TimeTT) {
            var TimeUTC = AADynamicalTime.TT2UTC(TimeTT);
            JDToDateParts(TimeUTC, true, out long year, out long month, out long day, out long hour, out long minute, out double second);
            return new DateTime((int)year, (int)month, (int)day, (int)hour, (int)minute, (int)second, DateTimeKind.Utc);
        }

        /// <summary>
        /// Converts <b>System.DateTime</b> in UTC timeframe to TT timeframe JD number.
        /// </summary>
        public static double DateTimeUTC2TT(DateTime date, bool IsGregorian = true) => AADynamicalTime.UTC2TT(DateTimeUTC2JD(date, IsGregorian));

        protected virtual void Dispose(bool disposing) {
            if (!disposedValue) {
                // if (disposing) { }

                if (_ptr != IntPtr.Zero) {
                    Destroy(_ptr);
                    _ptr = IntPtr.Zero;
                }
                disposedValue = true;
            }
        }

        // Do not change this code. Put cleanup code in 'Dispose(bool disposing)' method
        ~AADate() => Dispose(disposing: false);

        public void Dispose() {
            // Do not change this code. Put cleanup code in 'Dispose(bool disposing)' method
            Dispose(disposing: true);
            GC.SuppressFinalize(this);
        }
    }

    public class AADiameters {
        private const string LibName = "caaplus";

        [DllImport(LibName, EntryPoint = "CAADiameters_SunSemidiameterA")]
        public static extern double SunSemidiameterA(double Delta);

        [DllImport(LibName, EntryPoint = "CAADiameters_MercurySemidiameterA")]
        public static extern double MercurySemidiameterA(double Delta);

        [DllImport(LibName, EntryPoint = "CAADiameters_VenusSemidiameterA")]
        public static extern double VenusSemidiameterA(double Delta);

        [DllImport(LibName, EntryPoint = "CAADiameters_MarsSemidiameterA")]
        public static extern double MarsSemidiameterA(double Delta);

        [DllImport(LibName, EntryPoint = "CAADiameters_JupiterEquatorialSemidiameterA")]
        public static extern double JupiterEquatorialSemidiameterA(double Delta);

        [DllImport(LibName, EntryPoint = "CAADiameters_JupiterPolarSemidiameterA")]
        public static extern double JupiterPolarSemidiameterA(double Delta);

        [DllImport(LibName, EntryPoint = "CAADiameters_SaturnEquatorialSemidiameterA")]
        public static extern double SaturnEquatorialSemidiameterA(double Delta);

        [DllImport(LibName, EntryPoint = "CAADiameters_SaturnPolarSemidiameterA")]
        public static extern double SaturnPolarSemidiameterA(double Delta);

        [DllImport(LibName, EntryPoint = "CAADiameters_UranusSemidiameterA")]
        public static extern double UranusSemidiameterA(double Delta);

        [DllImport(LibName, EntryPoint = "CAADiameters_NeptuneSemidiameterA")]
        public static extern double NeptuneSemidiameterA(double Delta);

        [DllImport(LibName, EntryPoint = "CAADiameters_MercurySemidiameterB")]
        public static extern double MercurySemidiameterB(double Delta);

        [DllImport(LibName, EntryPoint = "CAADiameters_VenusSemidiameterB")]
        public static extern double VenusSemidiameterB(double Delta);

        [DllImport(LibName, EntryPoint = "CAADiameters_MarsSemidiameterB")]
        public static extern double MarsSemidiameterB(double Delta);

        [DllImport(LibName, EntryPoint = "CAADiameters_JupiterEquatorialSemidiameterB")]
        public static extern double JupiterEquatorialSemidiameterB(double Delta);

        [DllImport(LibName, EntryPoint = "CAADiameters_JupiterPolarSemidiameterB")]
        public static extern double JupiterPolarSemidiameterB(double Delta);

        [DllImport(LibName, EntryPoint = "CAADiameters_SaturnEquatorialSemidiameterB")]
        public static extern double SaturnEquatorialSemidiameterB(double Delta);

        [DllImport(LibName, EntryPoint = "CAADiameters_SaturnPolarSemidiameterB")]
        public static extern double SaturnPolarSemidiameterB(double Delta);

        [DllImport(LibName, EntryPoint = "CAADiameters_UranusSemidiameterB")]
        public static extern double UranusSemidiameterB(double Delta);

        [DllImport(LibName, EntryPoint = "CAADiameters_NeptuneSemidiameterB")]
        public static extern double NeptuneSemidiameterB(double Delta);

        [DllImport(LibName, EntryPoint = "CAADiameters_PlutoSemidiameterB")]
        public static extern double PlutoSemidiameterB(double Delta);

        [DllImport(LibName, EntryPoint = "CAADiameters_ApparentAsteroidDiameter")]
        public static extern double ApparentAsteroidDiameter(double Delta, double d);

        [DllImport(LibName, EntryPoint = "CAADiameters_GeocentricMoonSemidiameter")]
        public static extern double GeocentricMoonSemidiameter(double Delta);

        [DllImport(LibName, EntryPoint = "CAADiameters_ApparentSaturnPolarSemidiameterA")]
        public static extern double ApparentSaturnPolarSemidiameterA(double Delta, double B);

        [DllImport(LibName, EntryPoint = "CAADiameters_ApparentSaturnPolarSemidiameterB")]
        public static extern double ApparentSaturnPolarSemidiameterB(double Delta, double B);

        [DllImport(LibName, EntryPoint = "CAADiameters_TopocentricMoonSemidiameter")]
        public static extern double TopocentricMoonSemidiameter(double DistanceDelta, double Delta, double H, double Latitude, double Height);

        [DllImport(LibName, EntryPoint = "CAADiameters_AsteroidDiameter")]
        public static extern double AsteroidDiameter(double H, double A);

    }

    public class AADynamicalTime {
        private const string LibName = "caaplus";

        [UnmanagedFunctionPointer(CallingConvention.Cdecl, SetLastError = true)]
        public delegate double DELTAT_PROC(double JD);

        [DllImport(LibName, EntryPoint = "CAADynamicalTime_SetUserDefinedDeltaT")]
        public static extern DELTAT_PROC SetUserDefinedDeltaT(DELTAT_PROC pProc);

        [DllImport(LibName, EntryPoint = "CAADynamicalTime_DeltaT")]
        public static extern double DeltaT(double JD);

        [DllImport(LibName, EntryPoint = "CAADynamicalTime_CumulativeLeapSeconds")]
        public static extern double CumulativeLeapSeconds(double JD);

        [DllImport(LibName, EntryPoint = "CAADynamicalTime_TT2UTC")]
        public static extern double TT2UTC(double JD);

        [DllImport(LibName, EntryPoint = "CAADynamicalTime_UTC2TT")]
        public static extern double UTC2TT(double JD);

        [DllImport(LibName, EntryPoint = "CAADynamicalTime_TT2TAI")]
        public static extern double TT2TAI(double JD);

        [DllImport(LibName, EntryPoint = "CAADynamicalTime_TAI2TT")]
        public static extern double TAI2TT(double JD);

        [DllImport(LibName, EntryPoint = "CAADynamicalTime_TT2UT1")]
        public static extern double TT2UT1(double JD);

        [DllImport(LibName, EntryPoint = "CAADynamicalTime_UT12TT")]
        public static extern double UT12TT(double JD);

        [DllImport(LibName, EntryPoint = "CAADynamicalTime_UT1MinusUTC")]
        public static extern double UT1MinusUTC(double JD);

    }

    public class AAEarth {
        private const string LibName = "caaplus";

        [DllImport(LibName, EntryPoint = "CAAEarth_EclipticLongitude")]
        public static extern double EclipticLongitude(double JD, bool bHighPrecision);

        [DllImport(LibName, EntryPoint = "CAAEarth_EclipticLatitude")]
        public static extern double EclipticLatitude(double JD, bool bHighPrecision);

        [DllImport(LibName, EntryPoint = "CAAEarth_RadiusVector")]
        public static extern double RadiusVector(double JD, bool bHighPrecision);

        [DllImport(LibName, EntryPoint = "CAAEarth_SunMeanAnomaly")]
        public static extern double SunMeanAnomaly(double JD);

        [DllImport(LibName, EntryPoint = "CAAEarth_Eccentricity")]
        public static extern double Eccentricity(double JD);

        [DllImport(LibName, EntryPoint = "CAAEarth_EclipticLongitudeJ2000")]
        public static extern double EclipticLongitudeJ2000(double JD, bool bHighPrecision);

        [DllImport(LibName, EntryPoint = "CAAEarth_EclipticLatitudeJ2000")]
        public static extern double EclipticLatitudeJ2000(double JD, bool bHighPrecision);

    }

    public class AAEaster {
        private const string LibName = "caaplus";

        [StructLayout(LayoutKind.Sequential)]
        public struct AAEasterDetails {
            public uint Month;
            public uint Day;
        }

        [DllImport(LibName, EntryPoint = "CAAEaster_Calculate")]
        public static extern AAEasterDetails Calculate(int nYear, bool GregorianCalendar);
    }

    public class AAEclipses {
        private const string LibName = "caaplus";

        [Flags]
        public enum Flagz : uint {
            TOTAL_ECLIPSE = 0x01,
            ANNULAR_ECLIPSE = 0x02,
            ANNULAR_TOTAL_ECLIPSE = 0x04,
            CENTRAL_ECLIPSE = 0x08,
            PARTIAL_ECLIPSE = 0x10,
            NON_CENTRAL_ECLIPSE = 0x20
        }

        [StructLayout(LayoutKind.Sequential)]
        public struct AASolarEclipseDetails {
            public Flagz Flags;
            public double TimeOfMaximumEclipse;
            public double F;
            public double u;
            public double gamma;
            public double GreatestMagnitude;
        }

        [StructLayout(LayoutKind.Sequential)]
        public struct AALunarEclipseDetails {
            [MarshalAs(UnmanagedType.U1)] public bool bEclipse;
            public double TimeOfMaximumEclipse;
            public double F;
            public double u;
            public double gamma;
            public double PenumbralRadii;
            public double UmbralRadii;
            public double PenumbralMagnitude;
            public double UmbralMagnitude;
            public double PartialPhaseSemiDuration;
            public double TotalPhaseSemiDuration;
            public double PartialPhasePenumbraSemiDuration;
        }

        [DllImport(LibName, EntryPoint = "CAAEclipses_CalculateSolar")]
        public static extern AASolarEclipseDetails CalculateSolar(double k);

        [DllImport(LibName, EntryPoint = "CAAEclipses_CalculateLunar")]
        public static extern AALunarEclipseDetails CalculateLunar(double k);

    }

    public class AAEclipticalElements {
        private const string LibName = "caaplus";

        [StructLayout(LayoutKind.Sequential)]
        public struct AAEclipticalElementDetails {
            public double i;
            public double w;
            public double omega;
        }

        [DllImport(LibName, EntryPoint = "CAAEclipticalElements_Calculate")]
        public static extern AAEclipticalElementDetails Calculate(double i0, double w0, double omega0, double JD0, double JD);

        [DllImport(LibName, EntryPoint = "CAAEclipticalElements_FK4B1950ToFK5J2000")]
        public static extern AAEclipticalElementDetails FK4B1950ToFK5J2000(double i0, double w0, double omega0);

    }

    public class AAElementsPlanetaryOrbit {
        private const string LibName = "caaplus";

        [DllImport(LibName, EntryPoint = "CAAElementsPlanetaryOrbit_MercuryMeanLongitude")]
        public static extern double MercuryMeanLongitude(double JD);

        [DllImport(LibName, EntryPoint = "CAAElementsPlanetaryOrbit_MercurySemimajorAxis")]
        public static extern double MercurySemimajorAxis(double JD);

        [DllImport(LibName, EntryPoint = "CAAElementsPlanetaryOrbit_MercuryEccentricity")]
        public static extern double MercuryEccentricity(double JD);

        [DllImport(LibName, EntryPoint = "CAAElementsPlanetaryOrbit_MercuryInclination")]
        public static extern double MercuryInclination(double JD);

        [DllImport(LibName, EntryPoint = "CAAElementsPlanetaryOrbit_MercuryLongitudeAscendingNode")]
        public static extern double MercuryLongitudeAscendingNode(double JD);

        [DllImport(LibName, EntryPoint = "CAAElementsPlanetaryOrbit_MercuryLongitudePerihelion")]
        public static extern double MercuryLongitudePerihelion(double JD);

        [DllImport(LibName, EntryPoint = "CAAElementsPlanetaryOrbit_VenusMeanLongitude")]
        public static extern double VenusMeanLongitude(double JD);

        [DllImport(LibName, EntryPoint = "CAAElementsPlanetaryOrbit_VenusSemimajorAxis")]
        public static extern double VenusSemimajorAxis(double JD);

        [DllImport(LibName, EntryPoint = "CAAElementsPlanetaryOrbit_VenusEccentricity")]
        public static extern double VenusEccentricity(double JD);

        [DllImport(LibName, EntryPoint = "CAAElementsPlanetaryOrbit_VenusInclination")]
        public static extern double VenusInclination(double JD);

        [DllImport(LibName, EntryPoint = "CAAElementsPlanetaryOrbit_VenusLongitudeAscendingNode")]
        public static extern double VenusLongitudeAscendingNode(double JD);

        [DllImport(LibName, EntryPoint = "CAAElementsPlanetaryOrbit_VenusLongitudePerihelion")]
        public static extern double VenusLongitudePerihelion(double JD);

        [DllImport(LibName, EntryPoint = "CAAElementsPlanetaryOrbit_EarthMeanLongitude")]
        public static extern double EarthMeanLongitude(double JD);

        [DllImport(LibName, EntryPoint = "CAAElementsPlanetaryOrbit_EarthSemimajorAxis")]
        public static extern double EarthSemimajorAxis(double JD);

        [DllImport(LibName, EntryPoint = "CAAElementsPlanetaryOrbit_EarthEccentricity")]
        public static extern double EarthEccentricity(double JD);

        [DllImport(LibName, EntryPoint = "CAAElementsPlanetaryOrbit_EarthInclination")]
        public static extern double EarthInclination(double JD);

        [DllImport(LibName, EntryPoint = "CAAElementsPlanetaryOrbit_EarthLongitudePerihelion")]
        public static extern double EarthLongitudePerihelion(double JD);

        [DllImport(LibName, EntryPoint = "CAAElementsPlanetaryOrbit_MarsMeanLongitude")]
        public static extern double MarsMeanLongitude(double JD);

        [DllImport(LibName, EntryPoint = "CAAElementsPlanetaryOrbit_MarsSemimajorAxis")]
        public static extern double MarsSemimajorAxis(double JD);

        [DllImport(LibName, EntryPoint = "CAAElementsPlanetaryOrbit_MarsEccentricity")]
        public static extern double MarsEccentricity(double JD);

        [DllImport(LibName, EntryPoint = "CAAElementsPlanetaryOrbit_MarsInclination")]
        public static extern double MarsInclination(double JD);

        [DllImport(LibName, EntryPoint = "CAAElementsPlanetaryOrbit_MarsLongitudeAscendingNode")]
        public static extern double MarsLongitudeAscendingNode(double JD);

        [DllImport(LibName, EntryPoint = "CAAElementsPlanetaryOrbit_MarsLongitudePerihelion")]
        public static extern double MarsLongitudePerihelion(double JD);

        [DllImport(LibName, EntryPoint = "CAAElementsPlanetaryOrbit_JupiterMeanLongitude")]
        public static extern double JupiterMeanLongitude(double JD);

        [DllImport(LibName, EntryPoint = "CAAElementsPlanetaryOrbit_JupiterSemimajorAxis")]
        public static extern double JupiterSemimajorAxis(double JD);

        [DllImport(LibName, EntryPoint = "CAAElementsPlanetaryOrbit_JupiterEccentricity")]
        public static extern double JupiterEccentricity(double JD);

        [DllImport(LibName, EntryPoint = "CAAElementsPlanetaryOrbit_JupiterInclination")]
        public static extern double JupiterInclination(double JD);

        [DllImport(LibName, EntryPoint = "CAAElementsPlanetaryOrbit_JupiterLongitudeAscendingNode")]
        public static extern double JupiterLongitudeAscendingNode(double JD);

        [DllImport(LibName, EntryPoint = "CAAElementsPlanetaryOrbit_JupiterLongitudePerihelion")]
        public static extern double JupiterLongitudePerihelion(double JD);

        [DllImport(LibName, EntryPoint = "CAAElementsPlanetaryOrbit_SaturnMeanLongitude")]
        public static extern double SaturnMeanLongitude(double JD);

        [DllImport(LibName, EntryPoint = "CAAElementsPlanetaryOrbit_SaturnSemimajorAxis")]
        public static extern double SaturnSemimajorAxis(double JD);

        [DllImport(LibName, EntryPoint = "CAAElementsPlanetaryOrbit_SaturnEccentricity")]
        public static extern double SaturnEccentricity(double JD);

        [DllImport(LibName, EntryPoint = "CAAElementsPlanetaryOrbit_SaturnInclination")]
        public static extern double SaturnInclination(double JD);

        [DllImport(LibName, EntryPoint = "CAAElementsPlanetaryOrbit_SaturnLongitudeAscendingNode")]
        public static extern double SaturnLongitudeAscendingNode(double JD);

        [DllImport(LibName, EntryPoint = "CAAElementsPlanetaryOrbit_SaturnLongitudePerihelion")]
        public static extern double SaturnLongitudePerihelion(double JD);

        [DllImport(LibName, EntryPoint = "CAAElementsPlanetaryOrbit_UranusMeanLongitude")]
        public static extern double UranusMeanLongitude(double JD);

        [DllImport(LibName, EntryPoint = "CAAElementsPlanetaryOrbit_UranusSemimajorAxis")]
        public static extern double UranusSemimajorAxis(double JD);

        [DllImport(LibName, EntryPoint = "CAAElementsPlanetaryOrbit_UranusEccentricity")]
        public static extern double UranusEccentricity(double JD);

        [DllImport(LibName, EntryPoint = "CAAElementsPlanetaryOrbit_UranusInclination")]
        public static extern double UranusInclination(double JD);

        [DllImport(LibName, EntryPoint = "CAAElementsPlanetaryOrbit_UranusLongitudeAscendingNode")]
        public static extern double UranusLongitudeAscendingNode(double JD);

        [DllImport(LibName, EntryPoint = "CAAElementsPlanetaryOrbit_UranusLongitudePerihelion")]
        public static extern double UranusLongitudePerihelion(double JD);

        [DllImport(LibName, EntryPoint = "CAAElementsPlanetaryOrbit_NeptuneMeanLongitude")]
        public static extern double NeptuneMeanLongitude(double JD);

        [DllImport(LibName, EntryPoint = "CAAElementsPlanetaryOrbit_NeptuneSemimajorAxis")]
        public static extern double NeptuneSemimajorAxis(double JD);

        [DllImport(LibName, EntryPoint = "CAAElementsPlanetaryOrbit_NeptuneEccentricity")]
        public static extern double NeptuneEccentricity(double JD);

        [DllImport(LibName, EntryPoint = "CAAElementsPlanetaryOrbit_NeptuneInclination")]
        public static extern double NeptuneInclination(double JD);

        [DllImport(LibName, EntryPoint = "CAAElementsPlanetaryOrbit_NeptuneLongitudeAscendingNode")]
        public static extern double NeptuneLongitudeAscendingNode(double JD);

        [DllImport(LibName, EntryPoint = "CAAElementsPlanetaryOrbit_NeptuneLongitudePerihelion")]
        public static extern double NeptuneLongitudePerihelion(double JD);

        [DllImport(LibName, EntryPoint = "CAAElementsPlanetaryOrbit_MercuryMeanLongitudeJ2000")]
        public static extern double MercuryMeanLongitudeJ2000(double JD);

        [DllImport(LibName, EntryPoint = "CAAElementsPlanetaryOrbit_MercuryInclinationJ2000")]
        public static extern double MercuryInclinationJ2000(double JD);

        [DllImport(LibName, EntryPoint = "CAAElementsPlanetaryOrbit_MercuryLongitudeAscendingNodeJ2000")]
        public static extern double MercuryLongitudeAscendingNodeJ2000(double JD);

        [DllImport(LibName, EntryPoint = "CAAElementsPlanetaryOrbit_MercuryLongitudePerihelionJ2000")]
        public static extern double MercuryLongitudePerihelionJ2000(double JD);

        [DllImport(LibName, EntryPoint = "CAAElementsPlanetaryOrbit_VenusMeanLongitudeJ2000")]
        public static extern double VenusMeanLongitudeJ2000(double JD);

        [DllImport(LibName, EntryPoint = "CAAElementsPlanetaryOrbit_VenusInclinationJ2000")]
        public static extern double VenusInclinationJ2000(double JD);

        [DllImport(LibName, EntryPoint = "CAAElementsPlanetaryOrbit_VenusLongitudeAscendingNodeJ2000")]
        public static extern double VenusLongitudeAscendingNodeJ2000(double JD);

        [DllImport(LibName, EntryPoint = "CAAElementsPlanetaryOrbit_VenusLongitudePerihelionJ2000")]
        public static extern double VenusLongitudePerihelionJ2000(double JD);

        [DllImport(LibName, EntryPoint = "CAAElementsPlanetaryOrbit_EarthMeanLongitudeJ2000")]
        public static extern double EarthMeanLongitudeJ2000(double JD);

        [DllImport(LibName, EntryPoint = "CAAElementsPlanetaryOrbit_EarthInclinationJ2000")]
        public static extern double EarthInclinationJ2000(double JD);

        [DllImport(LibName, EntryPoint = "CAAElementsPlanetaryOrbit_EarthLongitudeAscendingNodeJ2000")]
        public static extern double EarthLongitudeAscendingNodeJ2000(double JD);

        [DllImport(LibName, EntryPoint = "CAAElementsPlanetaryOrbit_EarthLongitudePerihelionJ2000")]
        public static extern double EarthLongitudePerihelionJ2000(double JD);

        [DllImport(LibName, EntryPoint = "CAAElementsPlanetaryOrbit_MarsMeanLongitudeJ2000")]
        public static extern double MarsMeanLongitudeJ2000(double JD);

        [DllImport(LibName, EntryPoint = "CAAElementsPlanetaryOrbit_MarsInclinationJ2000")]
        public static extern double MarsInclinationJ2000(double JD);

        [DllImport(LibName, EntryPoint = "CAAElementsPlanetaryOrbit_MarsLongitudeAscendingNodeJ2000")]
        public static extern double MarsLongitudeAscendingNodeJ2000(double JD);

        [DllImport(LibName, EntryPoint = "CAAElementsPlanetaryOrbit_MarsLongitudePerihelionJ2000")]
        public static extern double MarsLongitudePerihelionJ2000(double JD);

        [DllImport(LibName, EntryPoint = "CAAElementsPlanetaryOrbit_JupiterMeanLongitudeJ2000")]
        public static extern double JupiterMeanLongitudeJ2000(double JD);

        [DllImport(LibName, EntryPoint = "CAAElementsPlanetaryOrbit_JupiterInclinationJ2000")]
        public static extern double JupiterInclinationJ2000(double JD);

        [DllImport(LibName, EntryPoint = "CAAElementsPlanetaryOrbit_JupiterLongitudeAscendingNodeJ2000")]
        public static extern double JupiterLongitudeAscendingNodeJ2000(double JD);

        [DllImport(LibName, EntryPoint = "CAAElementsPlanetaryOrbit_JupiterLongitudePerihelionJ2000")]
        public static extern double JupiterLongitudePerihelionJ2000(double JD);

        [DllImport(LibName, EntryPoint = "CAAElementsPlanetaryOrbit_SaturnMeanLongitudeJ2000")]
        public static extern double SaturnMeanLongitudeJ2000(double JD);

        [DllImport(LibName, EntryPoint = "CAAElementsPlanetaryOrbit_SaturnInclinationJ2000")]
        public static extern double SaturnInclinationJ2000(double JD);

        [DllImport(LibName, EntryPoint = "CAAElementsPlanetaryOrbit_SaturnLongitudeAscendingNodeJ2000")]
        public static extern double SaturnLongitudeAscendingNodeJ2000(double JD);

        [DllImport(LibName, EntryPoint = "CAAElementsPlanetaryOrbit_SaturnLongitudePerihelionJ2000")]
        public static extern double SaturnLongitudePerihelionJ2000(double JD);

        [DllImport(LibName, EntryPoint = "CAAElementsPlanetaryOrbit_UranusMeanLongitudeJ2000")]
        public static extern double UranusMeanLongitudeJ2000(double JD);

        [DllImport(LibName, EntryPoint = "CAAElementsPlanetaryOrbit_UranusInclinationJ2000")]
        public static extern double UranusInclinationJ2000(double JD);

        [DllImport(LibName, EntryPoint = "CAAElementsPlanetaryOrbit_UranusLongitudeAscendingNodeJ2000")]
        public static extern double UranusLongitudeAscendingNodeJ2000(double JD);

        [DllImport(LibName, EntryPoint = "CAAElementsPlanetaryOrbit_UranusLongitudePerihelionJ2000")]
        public static extern double UranusLongitudePerihelionJ2000(double JD);

        [DllImport(LibName, EntryPoint = "CAAElementsPlanetaryOrbit_NeptuneMeanLongitudeJ2000")]
        public static extern double NeptuneMeanLongitudeJ2000(double JD);

        [DllImport(LibName, EntryPoint = "CAAElementsPlanetaryOrbit_NeptuneInclinationJ2000")]
        public static extern double NeptuneInclinationJ2000(double JD);

        [DllImport(LibName, EntryPoint = "CAAElementsPlanetaryOrbit_NeptuneLongitudeAscendingNodeJ2000")]
        public static extern double NeptuneLongitudeAscendingNodeJ2000(double JD);

        [DllImport(LibName, EntryPoint = "CAAElementsPlanetaryOrbit_NeptuneLongitudePerihelionJ2000")]
        public static extern double NeptuneLongitudePerihelionJ2000(double JD);

    }

    public class AAElliptical {
        private const string LibName = "caaplus";

        [Flags]
        public enum Object : int {
            SUN = 0,
            MERCURY = 1,
            VENUS = 2,
            MARS = 3,
            JUPITER = 4,
            SATURN = 5,
            URANUS = 6,
            NEPTUNE = 7,
        }

        [StructLayout(LayoutKind.Sequential)]
        public struct AAEllipticalObjectElements {
            public double a;
            public double e;
            public double i;
            public double w;
            public double omega;
            public double JDEquinox;
            public double T;
        }

        [StructLayout(LayoutKind.Sequential)]
        public struct AAEllipticalPlanetaryDetails {
            public double ApparentGeocentricEclipticalLongitude;
            public double ApparentGeocentricEclipticalLatitude;
            public double ApparentGeocentricDistance;
            public double ApparentLightTime;
            public double ApparentGeocentricRA;
            public double ApparentGeocentricDeclination;
            public AA3DCoordinate TrueGeocentricRectangularEcliptical;
            public double TrueHeliocentricEclipticalLongitude;
            public double TrueHeliocentricEclipticalLatitude;
            public double TrueHeliocentricDistance;
            public double TrueGeocentricEclipticalLongitude;
            public double TrueGeocentricEclipticalLatitude;
            public double TrueGeocentricDistance;
            public double TrueLightTime;
            public double TrueGeocentricRA;
            public double TrueGeocentricDeclination;
        }

        [StructLayout(LayoutKind.Sequential)]
        public struct AAEllipticalObjectDetails {
            public AA3DCoordinate HeliocentricRectangularEquatorial;
            public AA3DCoordinate HeliocentricRectangularEcliptical;
            public double HeliocentricEclipticLongitude;
            public double HeliocentricEclipticLatitude;
            public double TrueGeocentricRA;
            public double TrueGeocentricDeclination;
            public double TrueGeocentricDistance;
            public double TrueGeocentricLightTime;
            public double AstrometricGeocentricRA;
            public double AstrometricGeocentricDeclination;
            public double AstrometricGeocentricDistance;
            public double AstrometricGeocentricLightTime;
            public double Elongation;
            public double PhaseAngle;
        }

        [DllImport(LibName, EntryPoint = "CAAElliptical_DistanceToLightTime")]
        public static extern double DistanceToLightTime(double Distance);

        [DllImport(LibName, EntryPoint = "CAAElliptical_Calculate")]
        public static extern AAEllipticalPlanetaryDetails Calculate(double JD, Object _object, bool bHighPrecision);

        [DllImport(LibName, EntryPoint = "CAAElliptical_SemiMajorAxisFromPerihelionDistance")]
        public static extern double SemiMajorAxisFromPerihelionDistance(double q, double e);

        [DllImport(LibName, EntryPoint = "CAAElliptical_MeanMotionFromSemiMajorAxis")]
        public static extern double MeanMotionFromSemiMajorAxis(double a);

        [DllImport(LibName, EntryPoint = "CAAElliptical_Calculate")]
        public static extern AAEllipticalObjectDetails Calculate(double JD, ref AAEllipticalObjectElements elements, bool bHighPrecision);

        [DllImport(LibName, EntryPoint = "CAAElliptical_InstantaneousVelocity")]
        public static extern double InstantaneousVelocity(double r, double a);

        [DllImport(LibName, EntryPoint = "CAAElliptical_VelocityAtPerihelion")]
        public static extern double VelocityAtPerihelion(double e, double a);

        [DllImport(LibName, EntryPoint = "CAAElliptical_VelocityAtAphelion")]
        public static extern double VelocityAtAphelion(double e, double a);

        [DllImport(LibName, EntryPoint = "CAAElliptical_LengthOfEllipse")]
        public static extern double LengthOfEllipse(double e, double a);

        [DllImport(LibName, EntryPoint = "CAAElliptical_CometMagnitude")]
        public static extern double CometMagnitude(double g, double delta, double k, double r);

        [DllImport(LibName, EntryPoint = "CAAElliptical_MinorPlanetMagnitude")]
        public static extern double MinorPlanetMagnitude(double H, double delta, double G, double r, double PhaseAngle);

    }

    public class AAELP2000 {
        private const string LibName = "caaplus";

        [StructLayout(LayoutKind.Sequential)]
        public struct ELP2000MainProblemCoefficient {
            [MarshalAs(UnmanagedType.ByValArray, ArraySubType = UnmanagedType.I4, SizeConst = 4)] public int[] m_I;
            public double m_A;
            [MarshalAs(UnmanagedType.ByValArray, ArraySubType = UnmanagedType.R8, SizeConst = 6)] public double[] m_B;
        }

        [StructLayout(LayoutKind.Sequential)]
        public struct ELP2000EarthTidalMoonRelativisticSolarEccentricityCoefficient {
            public int m_IZ;
            [MarshalAs(UnmanagedType.ByValArray, ArraySubType = UnmanagedType.I4, SizeConst = 4)] public int[] m_I;
            public double m_O;
            public double m_A;
            public double m_P;
        }

        [StructLayout(LayoutKind.Sequential)]
        public struct ELP2000PlanetPertCoefficient {
            [MarshalAs(UnmanagedType.ByValArray, ArraySubType = UnmanagedType.I4, SizeConst = 11)] public int[] m_ip;
            public double m_theta;
            public double m_O;
            public double m_P;
        }

        [DllImport(LibName, EntryPoint = "CAAELP2000_EclipticLongitude")]
        public static extern double EclipticLongitude(double JD);

        [DllImport(LibName, EntryPoint = "CAAELP2000_EclipticLongitude_2")]
        public static extern double EclipticLongitude_2(double[] pT, int nTSize);

        [DllImport(LibName, EntryPoint = "CAAELP2000_EclipticLatitude")]
        public static extern double EclipticLatitude(double JD);

        [DllImport(LibName, EntryPoint = "CAAELP2000_EclipticLatitude_2")]
        public static extern double EclipticLatitude_2(double[] pT, int nTSize);

        [DllImport(LibName, EntryPoint = "CAAELP2000_RadiusVector")]
        public static extern double RadiusVector(double JD);

        [DllImport(LibName, EntryPoint = "CAAELP2000_RadiusVector_2")]
        public static extern double RadiusVector_2(double[] pT, int nTSize);

        [DllImport(LibName, EntryPoint = "CAAELP2000_EclipticRectangularCoordinates")]
        public static extern AA3DCoordinate EclipticRectangularCoordinates(double JD);

        [DllImport(LibName, EntryPoint = "CAAELP2000_EclipticRectangularCoordinatesJ2000")]
        public static extern AA3DCoordinate EclipticRectangularCoordinatesJ2000(double JD);

        [DllImport(LibName, EntryPoint = "CAAELP2000_EquatorialRectangularCoordinatesFK5")]
        public static extern AA3DCoordinate EquatorialRectangularCoordinatesFK5(double JD);

        [DllImport(LibName, EntryPoint = "CAAELP2000_MoonMeanMeanLongitude")]
        public static extern double MoonMeanMeanLongitude(double[] pT, int nTSize);

        [DllImport(LibName, EntryPoint = "CAAELP2000_MoonMeanMeanLongitude_2")]
        public static extern double MoonMeanMeanLongitude_2(double JD);

        [DllImport(LibName, EntryPoint = "CAAELP2000_MeanLongitudeLunarPerigee")]
        public static extern double MeanLongitudeLunarPerigee(double[] pT, int nTSize);

        [DllImport(LibName, EntryPoint = "CAAELP2000_MeanLongitudeLunarPerigee_2")]
        public static extern double MeanLongitudeLunarPerigee_2(double JD);

        [DllImport(LibName, EntryPoint = "CAAELP2000_MeanLongitudeLunarAscendingNode")]
        public static extern double MeanLongitudeLunarAscendingNode(double[] pT, int nTSize);

        [DllImport(LibName, EntryPoint = "CAAELP2000_MeanLongitudeLunarAscendingNode_2")]
        public static extern double MeanLongitudeLunarAscendingNode_2(double JD);

        [DllImport(LibName, EntryPoint = "CAAELP2000_MeanHeliocentricMeanLongitudeEarthMoonBarycentre")]
        public static extern double MeanHeliocentricMeanLongitudeEarthMoonBarycentre(double[] pT, int nTSize);

        [DllImport(LibName, EntryPoint = "CAAELP2000_MeanHeliocentricMeanLongitudeEarthMoonBarycentre_2")]
        public static extern double MeanHeliocentricMeanLongitudeEarthMoonBarycentre_2(double JD);

        [DllImport(LibName, EntryPoint = "CAAELP2000_MeanLongitudeOfPerihelionOfEarthMoonBarycentre")]
        public static extern double MeanLongitudeOfPerihelionOfEarthMoonBarycentre(double[] pT, int nTSize);

        [DllImport(LibName, EntryPoint = "CAAELP2000_MeanLongitudeOfPerihelionOfEarthMoonBarycentre_2")]
        public static extern double MeanLongitudeOfPerihelionOfEarthMoonBarycentre_2(double JD);

        [DllImport(LibName, EntryPoint = "CAAELP2000_MoonMeanSolarElongation")]
        public static extern double MoonMeanSolarElongation(double[] pT, int nTSize);

        [DllImport(LibName, EntryPoint = "CAAELP2000_MoonMeanSolarElongation_2")]
        public static extern double MoonMeanSolarElongation_2(double JD);

        [DllImport(LibName, EntryPoint = "CAAELP2000_SunMeanAnomaly")]
        public static extern double SunMeanAnomaly(double[] pT, int nTSize);

        [DllImport(LibName, EntryPoint = "CAAELP2000_SunMeanAnomaly_2")]
        public static extern double SunMeanAnomaly_2(double JD);

        [DllImport(LibName, EntryPoint = "CAAELP2000_MoonMeanAnomaly")]
        public static extern double MoonMeanAnomaly(double[] pT, int nTSize);

        [DllImport(LibName, EntryPoint = "CAAELP2000_MoonMeanAnomaly_2")]
        public static extern double MoonMeanAnomaly_2(double JD);

        [DllImport(LibName, EntryPoint = "CAAELP2000_MoonMeanArgumentOfLatitude")]
        public static extern double MoonMeanArgumentOfLatitude(double[] pT, int nTSize);

        [DllImport(LibName, EntryPoint = "CAAELP2000_MoonMeanArgumentOfLatitude_2")]
        public static extern double MoonMeanArgumentOfLatitude_2(double JD);

        [DllImport(LibName, EntryPoint = "CAAELP2000_MercuryMeanLongitude")]
        public static extern double MercuryMeanLongitude(double T);

        [DllImport(LibName, EntryPoint = "CAAELP2000_VenusMeanLongitude")]
        public static extern double VenusMeanLongitude(double T);

        [DllImport(LibName, EntryPoint = "CAAELP2000_MarsMeanLongitude")]
        public static extern double MarsMeanLongitude(double T);

        [DllImport(LibName, EntryPoint = "CAAELP2000_JupiterMeanLongitude")]
        public static extern double JupiterMeanLongitude(double T);

        [DllImport(LibName, EntryPoint = "CAAELP2000_SaturnMeanLongitude")]
        public static extern double SaturnMeanLongitude(double T);

        [DllImport(LibName, EntryPoint = "CAAELP2000_UranusMeanLongitude")]
        public static extern double UranusMeanLongitude(double T);

        [DllImport(LibName, EntryPoint = "CAAELP2000_NeptuneMeanLongitude")]
        public static extern double NeptuneMeanLongitude(double T);

    }

    public class AAELPMPP02 {
        private const string LibName = "caaplus";

        [Flags]
        public enum Correction : int {
            Nominal = 0,
            LLR = 1,
            DE405 = 2,
            DE406 = 3,
        }

        [DllImport(LibName, EntryPoint = "CAAELPMPP02_EclipticLongitude")]
        public static extern double EclipticLongitude(double JD, Correction correction, ref double pDerivative);

        [DllImport(LibName, EntryPoint = "CAAELPMPP02_EclipticLongitude_2")]
        public static extern double EclipticLongitude_2(double[] pT, int nTSize, Correction correction, ref double pDerivative);

        [DllImport(LibName, EntryPoint = "CAAELPMPP02_EclipticLatitude")]
        public static extern double EclipticLatitude(double JD, Correction correction, ref double pDerivative);

        [DllImport(LibName, EntryPoint = "CAAELPMPP02_EclipticLatitude_2")]
        public static extern double EclipticLatitude_2(double[] pT, int nTSize, Correction correction, ref double pDerivative);

        [DllImport(LibName, EntryPoint = "CAAELPMPP02_RadiusVector")]
        public static extern double RadiusVector(double JD, Correction correction, ref double pDerivative);

        [DllImport(LibName, EntryPoint = "CAAELPMPP02_RadiusVector_2")]
        public static extern double RadiusVector_2(double[] pT, int nTSize, Correction correction, ref double pDerivative);

        [DllImport(LibName, EntryPoint = "CAAELPMPP02_EclipticRectangularCoordinates")]
        public static extern AA3DCoordinate EclipticRectangularCoordinates(double JD, Correction correction, ref AA3DCoordinate pDerivative);

        [DllImport(LibName, EntryPoint = "CAAELPMPP02_EclipticRectangularCoordinates_2")]
        public static extern AA3DCoordinate EclipticRectangularCoordinates_2(double[] pT, int nTSize, Correction correction, ref AA3DCoordinate pDerivative);

        [DllImport(LibName, EntryPoint = "CAAELPMPP02_EclipticRectangularCoordinatesJ2000")]
        public static extern AA3DCoordinate EclipticRectangularCoordinatesJ2000(double JD, Correction correction, ref AA3DCoordinate pDerivative);

        [DllImport(LibName, EntryPoint = "CAAELPMPP02_EclipticRectangularCoordinatesJ2000_2")]
        public static extern AA3DCoordinate EclipticRectangularCoordinatesJ2000_2(double[] pT, int nTSize, Correction correction, ref AA3DCoordinate pDerivative);

    }

    public class AAEquationOfTime {
        private const string LibName = "caaplus";

        [DllImport(LibName, EntryPoint = "CAAEquationOfTime_Calculate")]
        public static extern double Calculate(double JD, bool bHighPrecision);

    }

    public class AAEquinoxesAndSolstices {
        private const string LibName = "caaplus";

        [DllImport(LibName, EntryPoint = "CAAEquinoxesAndSolstices_NorthwardEquinox")]
        public static extern double NorthwardEquinox(long Year, bool bHighPrecision);

        [DllImport(LibName, EntryPoint = "CAAEquinoxesAndSolstices_NorthernSolstice")]
        public static extern double NorthernSolstice(long Year, bool bHighPrecision);

        [DllImport(LibName, EntryPoint = "CAAEquinoxesAndSolstices_SouthwardEquinox")]
        public static extern double SouthwardEquinox(long Year, bool bHighPrecision);

        [DllImport(LibName, EntryPoint = "CAAEquinoxesAndSolstices_SouthernSolstice")]
        public static extern double SouthernSolstice(long Year, bool bHighPrecision);

        [DllImport(LibName, EntryPoint = "CAAEquinoxesAndSolstices_LengthOfSpring")]
        public static extern double LengthOfSpring(long Year, bool bNorthernHemisphere, bool bHighPrecision);

        [DllImport(LibName, EntryPoint = "CAAEquinoxesAndSolstices_LengthOfSummer")]
        public static extern double LengthOfSummer(long Year, bool bNorthernHemisphere, bool bHighPrecision);

        [DllImport(LibName, EntryPoint = "CAAEquinoxesAndSolstices_LengthOfAutumn")]
        public static extern double LengthOfAutumn(long Year, bool bNorthernHemisphere, bool bHighPrecision);

        [DllImport(LibName, EntryPoint = "CAAEquinoxesAndSolstices_LengthOfWinter")]
        public static extern double LengthOfWinter(long Year, bool bNorthernHemisphere, bool bHighPrecision);

    }

    public class AAEquinoxesAndSolstices2 {
        private const string LibName = "caaplus";

        [Flags]
        public enum Type : int {
            NotDefined = 0,
            NorthwardEquinox = 1,
            NorthernSolstice = 2,
            SouthwardEquinox = 3,
            SouthernSolstice = 4,
        }

        [StructLayout(LayoutKind.Sequential)]
        public struct AAEquinoxSolsticeDetails2 {
            public Type type;
            public double JD;
        }

        [DllImport(LibName, EntryPoint = "CAAEquinoxesAndSolstices2_Calculate")]
        private static extern IntPtr Calculate(double StartJD, double EndJD, double StepInterval, bool bHighPrecision, out int num);

        [DllImport(LibName, EntryPoint = "CAAEquinoxesAndSolstices2_DestroyData")]
        private static extern void DestroyData(IntPtr ptr);

        public static AAEquinoxSolsticeDetails2[] Calculate(double StartJD, double EndJD, double StepInterval, bool bHighPrecision) {
            var ptr = Calculate(StartJD, EndJD, StepInterval, bHighPrecision, out int Count);
            var result = new AAEquinoxSolsticeDetails2[Count];
            var size = Marshal.SizeOf<AAEquinoxSolsticeDetails2>();
            for (var i = 0; i < Count; i++) result[i] = Marshal.PtrToStructure<AAEquinoxSolsticeDetails2>(ptr + i * size);
            DestroyData(ptr);
            return result;
        }
    }

    public class AAFK5 {
        private const string LibName = "caaplus";

        [DllImport(LibName, EntryPoint = "CAAFK5_CorrectionInLongitude")]
        public static extern double CorrectionInLongitude(double Longitude, double Latitude, double JD);

        [DllImport(LibName, EntryPoint = "CAAFK5_CorrectionInLatitude")]
        public static extern double CorrectionInLatitude(double Longitude, double JD);

        [DllImport(LibName, EntryPoint = "CAAFK5_ConvertVSOPToFK5J2000")]
        public static extern AA3DCoordinate ConvertVSOPToFK5J2000(ref AA3DCoordinate value);

        [DllImport(LibName, EntryPoint = "CAAFK5_ConvertVSOPToFK5B1950")]
        public static extern AA3DCoordinate ConvertVSOPToFK5B1950(ref AA3DCoordinate value);

        [DllImport(LibName, EntryPoint = "CAAFK5_ConvertVSOPToFK5AnyEquinox")]
        public static extern AA3DCoordinate ConvertVSOPToFK5AnyEquinox(ref AA3DCoordinate value, double JDEquinox);

    }

    public class AAGalileanMoons {
        private const string LibName = "caaplus";

        [StructLayout(LayoutKind.Sequential)]
        public struct AAGalileanMoonDetail {
            public double MeanLongitude;
            public double TrueLongitude;
            public double TropicalLongitude;
            public double EquatorialLatitude;
            public double r;
            public AA3DCoordinate TrueRectangularCoordinates;
            public AA3DCoordinate ApparentRectangularCoordinates;
            [MarshalAs(UnmanagedType.U1)] public bool bInTransit;
            [MarshalAs(UnmanagedType.U1)] public bool bInOccultation;
            [MarshalAs(UnmanagedType.U1)] public bool bInEclipse;
            [MarshalAs(UnmanagedType.U1)] public bool bInShadowTransit;
        }

        [StructLayout(LayoutKind.Sequential)]
        public struct AAGalileanMoonsDetails {
            public AAGalileanMoonDetail Satellite1;
            public AAGalileanMoonDetail Satellite2;
            public AAGalileanMoonDetail Satellite3;
            public AAGalileanMoonDetail Satellite4;
        }

        [DllImport(LibName, EntryPoint = "CAAGalileanMoons_Calculate")]
        public static extern AAGalileanMoonsDetails Calculate(double JD, bool bHighPrecision);

    }

    public class AAGlobe {
        private const string LibName = "caaplus";

        [DllImport(LibName, EntryPoint = "CAAGlobe_RhoSinThetaPrime")]
        public static extern double RhoSinThetaPrime(double GeographicalLatitude, double Height);

        [DllImport(LibName, EntryPoint = "CAAGlobe_RhoCosThetaPrime")]
        public static extern double RhoCosThetaPrime(double GeographicalLatitude, double Height);

        [DllImport(LibName, EntryPoint = "CAAGlobe_RadiusOfParallelOfLatitude")]
        public static extern double RadiusOfParallelOfLatitude(double GeographicalLatitude);

        [DllImport(LibName, EntryPoint = "CAAGlobe_RadiusOfCurvature")]
        public static extern double RadiusOfCurvature(double GeographicalLatitude);

        [DllImport(LibName, EntryPoint = "CAAGlobe_DistanceBetweenPoints")]
        public static extern double DistanceBetweenPoints(double GeographicalLatitude1, double GeographicalLongitude1, double GeographicalLatitude2, double GeographicalLongitude2);

    }

    public class AAIlluminatedFraction {
        private const string LibName = "caaplus";

        [DllImport(LibName, EntryPoint = "CAAIlluminatedFraction_PhaseAngle")]
        public static extern double PhaseAngle(double r, double R, double Delta);

        [DllImport(LibName, EntryPoint = "CAAIlluminatedFraction_PhaseAngle_2")]
        public static extern double PhaseAngle_2(double R, double R0, double B, double L, double L0, double Delta);

        [DllImport(LibName, EntryPoint = "CAAIlluminatedFraction_PhaseAngleRectangular")]
        public static extern double PhaseAngleRectangular(double x, double y, double z, double B, double L, double Delta);

        [DllImport(LibName, EntryPoint = "CAAIlluminatedFraction_IlluminatedFraction")]
        public static extern double IlluminatedFraction(double PhaseAngle);

        [DllImport(LibName, EntryPoint = "CAAIlluminatedFraction_IlluminatedFraction_2")]
        public static extern double IlluminatedFraction_2(double r, double R, double Delta);

        [DllImport(LibName, EntryPoint = "CAAIlluminatedFraction_MercuryMagnitudeMuller")]
        public static extern double MercuryMagnitudeMuller(double r, double Delta, double i);

        [DllImport(LibName, EntryPoint = "CAAIlluminatedFraction_VenusMagnitudeMuller")]
        public static extern double VenusMagnitudeMuller(double r, double Delta, double i);

        [DllImport(LibName, EntryPoint = "CAAIlluminatedFraction_MarsMagnitudeMuller")]
        public static extern double MarsMagnitudeMuller(double r, double Delta, double i);

        [DllImport(LibName, EntryPoint = "CAAIlluminatedFraction_JupiterMagnitudeMuller")]
        public static extern double JupiterMagnitudeMuller(double r, double Delta);

        [DllImport(LibName, EntryPoint = "CAAIlluminatedFraction_SaturnMagnitudeMuller")]
        public static extern double SaturnMagnitudeMuller(double r, double Delta, double DeltaU, double B);

        [DllImport(LibName, EntryPoint = "CAAIlluminatedFraction_UranusMagnitudeMuller")]
        public static extern double UranusMagnitudeMuller(double r, double Delta);

        [DllImport(LibName, EntryPoint = "CAAIlluminatedFraction_NeptuneMagnitudeMuller")]
        public static extern double NeptuneMagnitudeMuller(double r, double Delta);

        [DllImport(LibName, EntryPoint = "CAAIlluminatedFraction_MercuryMagnitudeAA")]
        public static extern double MercuryMagnitudeAA(double r, double Delta, double i);

        [DllImport(LibName, EntryPoint = "CAAIlluminatedFraction_VenusMagnitudeAA")]
        public static extern double VenusMagnitudeAA(double r, double Delta, double i);

        [DllImport(LibName, EntryPoint = "CAAIlluminatedFraction_MarsMagnitudeAA")]
        public static extern double MarsMagnitudeAA(double r, double Delta, double i);

        [DllImport(LibName, EntryPoint = "CAAIlluminatedFraction_JupiterMagnitudeAA")]
        public static extern double JupiterMagnitudeAA(double r, double Delta, double i);

        [DllImport(LibName, EntryPoint = "CAAIlluminatedFraction_SaturnMagnitudeAA")]
        public static extern double SaturnMagnitudeAA(double r, double Delta, double DeltaU, double B);

        [DllImport(LibName, EntryPoint = "CAAIlluminatedFraction_UranusMagnitudeAA")]
        public static extern double UranusMagnitudeAA(double r, double Delta);

        [DllImport(LibName, EntryPoint = "CAAIlluminatedFraction_NeptuneMagnitudeAA")]
        public static extern double NeptuneMagnitudeAA(double r, double Delta);

        [DllImport(LibName, EntryPoint = "CAAIlluminatedFraction_PlutoMagnitudeAA")]
        public static extern double PlutoMagnitudeAA(double r, double Delta);

    }

    public class AAInterpolate {
        private const string LibName = "caaplus";

        [DllImport(LibName, EntryPoint = "CAAInterpolate_Interpolate")]
        public static extern double Interpolate(double n, double Y1, double Y2, double Y3);

        [DllImport(LibName, EntryPoint = "CAAInterpolate_Interpolate_2")]
        public static extern double Interpolate_2(double n, double Y1, double Y2, double Y3, double Y4, double Y5);

        [DllImport(LibName, EntryPoint = "CAAInterpolate_InterpolateToHalves")]
        public static extern double InterpolateToHalves(double Y1, double Y2, double Y3, double Y4);

        [DllImport(LibName, EntryPoint = "CAAInterpolate_LagrangeInterpolate")]
        public static extern double LagrangeInterpolate(double X, int n, double[] pX, double[] pY);

        [DllImport(LibName, EntryPoint = "CAAInterpolate_Extremum")]
        public static extern double Extremum(double Y1, double Y2, double Y3, out double nm);

        [DllImport(LibName, EntryPoint = "CAAInterpolate_Extremum_2")]
        public static extern double Extremum_2(double Y1, double Y2, double Y3, double Y4, double Y5, out double nm, double epsilon);

        [DllImport(LibName, EntryPoint = "CAAInterpolate_Zero")]
        public static extern double Zero(double Y1, double Y2, double Y3, double epsilon);

        [DllImport(LibName, EntryPoint = "CAAInterpolate_Zero_2")]
        public static extern double Zero_2(double Y1, double Y2, double Y3, double Y4, double Y5, double epsilon);

        [DllImport(LibName, EntryPoint = "CAAInterpolate_Zero2")]
        public static extern double Zero2(double Y1, double Y2, double Y3, double epsilon);

        [DllImport(LibName, EntryPoint = "CAAInterpolate_Zero2_2")]
        public static extern double Zero2_2(double Y1, double Y2, double Y3, double Y4, double Y5, double epsilon);

    }

    public class AAJewishCalendar {
        private const string LibName = "caaplus";

        [DllImport(LibName, EntryPoint = "CAAJewishCalendar_DateOfPesach")]
        public static extern AACalendarDate DateOfPesach(long Year, bool bGregorianCalendar);

        [DllImport(LibName, EntryPoint = "CAAJewishCalendar_IsLeap")]
        [return: MarshalAs(UnmanagedType.U1)]
        public static extern bool IsLeap(long Year);

        [DllImport(LibName, EntryPoint = "CAAJewishCalendar_DaysInYear")]
        public static extern long DaysInYear(long Year);

    }

    public class AAJupiter {
        private const string LibName = "caaplus";

        [DllImport(LibName, EntryPoint = "CAAJupiter_EclipticLongitude")]
        public static extern double EclipticLongitude(double JD, bool bHighPrecision);

        [DllImport(LibName, EntryPoint = "CAAJupiter_EclipticLatitude")]
        public static extern double EclipticLatitude(double JD, bool bHighPrecision);

        [DllImport(LibName, EntryPoint = "CAAJupiter_RadiusVector")]
        public static extern double RadiusVector(double JD, bool bHighPrecision);

    }

    public class AAKepler {
        private const string LibName = "caaplus";

        [DllImport(LibName, EntryPoint = "CAAKepler_Calculate")]
        public static extern double Calculate(double M, double e, int nIterations);

    }

    public class AAMars {
        private const string LibName = "caaplus";

        [DllImport(LibName, EntryPoint = "CAAMars_EclipticLongitude")]
        public static extern double EclipticLongitude(double JD, bool bHighPrecision);

        [DllImport(LibName, EntryPoint = "CAAMars_EclipticLatitude")]
        public static extern double EclipticLatitude(double JD, bool bHighPrecision);

        [DllImport(LibName, EntryPoint = "CAAMars_RadiusVector")]
        public static extern double RadiusVector(double JD, bool bHighPrecision);

    }

    public class AAMercury {
        private const string LibName = "caaplus";

        [DllImport(LibName, EntryPoint = "CAAMercury_EclipticLongitude")]
        public static extern double EclipticLongitude(double JD, bool bHighPrecision);

        [DllImport(LibName, EntryPoint = "CAAMercury_EclipticLatitude")]
        public static extern double EclipticLatitude(double JD, bool bHighPrecision);

        [DllImport(LibName, EntryPoint = "CAAMercury_RadiusVector")]
        public static extern double RadiusVector(double JD, bool bHighPrecision);

    }

    public class AAMoon {
        private const string LibName = "caaplus";

        [DllImport(LibName, EntryPoint = "CAAMoon_MeanLongitude")]
        public static extern double MeanLongitude(double JD);

        [DllImport(LibName, EntryPoint = "CAAMoon_MeanElongation")]
        public static extern double MeanElongation(double JD);

        [DllImport(LibName, EntryPoint = "CAAMoon_MeanAnomaly")]
        public static extern double MeanAnomaly(double JD);

        [DllImport(LibName, EntryPoint = "CAAMoon_ArgumentOfLatitude")]
        public static extern double ArgumentOfLatitude(double JD);

        [DllImport(LibName, EntryPoint = "CAAMoon_MeanLongitudeAscendingNode")]
        public static extern double MeanLongitudeAscendingNode(double JD);

        [DllImport(LibName, EntryPoint = "CAAMoon_MeanLongitudePerigee")]
        public static extern double MeanLongitudePerigee(double JD);

        [DllImport(LibName, EntryPoint = "CAAMoon_TrueLongitudeAscendingNode")]
        public static extern double TrueLongitudeAscendingNode(double JD);

        [DllImport(LibName, EntryPoint = "CAAMoon_EclipticLongitude")]
        public static extern double EclipticLongitude(double JD);

        [DllImport(LibName, EntryPoint = "CAAMoon_EclipticLatitude")]
        public static extern double EclipticLatitude(double JD);

        [DllImport(LibName, EntryPoint = "CAAMoon_RadiusVector")]
        public static extern double RadiusVector(double JD);

        [DllImport(LibName, EntryPoint = "CAAMoon_RadiusVectorToHorizontalParallax")]
        public static extern double RadiusVectorToHorizontalParallax(double RadiusVector);

        [DllImport(LibName, EntryPoint = "CAAMoon_HorizontalParallaxToRadiusVector")]
        public static extern double HorizontalParallaxToRadiusVector(double Parallax);

        /// <summary>
        /// Calculates the Lunar phase angle (between 0 and 360 degress) for the given <b>System.DateTime</b> in UTC.
        /// The returned angle can be used to determine the Moon phase: 0 or 360 degrees - New Moon, more than 0 but less than 90 - Waxing Crescent,
        /// 90 degrees - First Quarter, more than 90 but less the 180 - Waxing Gibbous, 180 degrees - Full Moon, more than 180 but less than 270 - Waning Gibbous,
        /// 270 degrees - Last Quarter, more than 270 but less then 360 - Waning Crescent.
        /// </summary>
        public static double GetLunarPhaseAngle(DateTime date, bool IsGregorian = true) {
            var tt = AADate.DateTimeUTC2TT(date, IsGregorian);
            return AACoordinateTransformation.MapTo0To360Range(EclipticLongitude(tt) - AASun.ApparentEclipticLongitude(tt, true)); 
        }
    }

    public class AAMoonIlluminatedFraction {
        private const string LibName = "caaplus";

        [DllImport(LibName, EntryPoint = "CAAMoonIlluminatedFraction_GeocentricElongation")]
        public static extern double GeocentricElongation(double ObjectAlpha, double ObjectDelta, double SunAlpha, double SunDelta);

        [DllImport(LibName, EntryPoint = "CAAMoonIlluminatedFraction_PhaseAngle")]
        public static extern double PhaseAngle(double GeocentricElongation, double EarthObjectDistance, double EarthSunDistance);

        [DllImport(LibName, EntryPoint = "CAAMoonIlluminatedFraction_IlluminatedFraction")]
        public static extern double IlluminatedFraction(double PhaseAngle);

        [DllImport(LibName, EntryPoint = "CAAMoonIlluminatedFraction_PositionAngle")]
        public static extern double PositionAngle(double Alpha0, double Delta0, double Alpha, double Delta);

    }

    public class AAMoonMaxDeclinations {
        private const string LibName = "caaplus";

        [DllImport(LibName, EntryPoint = "CAAMoonMaxDeclinations_K")]
        public static extern double K(double Year);

        [DllImport(LibName, EntryPoint = "CAAMoonMaxDeclinations_MeanGreatestDeclination")]
        public static extern double MeanGreatestDeclination(double k, bool bNortherly);

        [DllImport(LibName, EntryPoint = "CAAMoonMaxDeclinations_MeanGreatestDeclinationValue")]
        public static extern double MeanGreatestDeclinationValue(double k);

        [DllImport(LibName, EntryPoint = "CAAMoonMaxDeclinations_TrueGreatestDeclination")]
        public static extern double TrueGreatestDeclination(double k, bool bNortherly);

        [DllImport(LibName, EntryPoint = "CAAMoonMaxDeclinations_TrueGreatestDeclinationValue")]
        public static extern double TrueGreatestDeclinationValue(double k, bool bNortherly);

    }

    public class AAMoonMaxDeclinations2 {
        private const string LibName = "caaplus";

        [Flags]
        public enum Type : int {
            NotDefined = 0,
            MaxNorthernDeclination = 1,
            MaxSouthernDeclination = 2,
        }

        [Flags]
        public enum Algorithm : int {
            MeeusTruncated = 0,
            ELP2000 = 1,
        }

        [StructLayout(LayoutKind.Sequential)]
        public struct AAMoonMaxDeclinationsDetails2 {
            public Type type;
            public double JD;
            public double Declination;
            public double RA;
        }

        [DllImport(LibName, EntryPoint = "CAAMoonMaxDeclinations2_Calculate")]
        private static extern IntPtr Calculate(double StartJD, double EndJD, double StepInterval, Algorithm algorithm, out int num);

        [DllImport(LibName, EntryPoint = "CAAMoonMaxDeclinations2_DestroyData")]
        private static extern void DestroyData(IntPtr ptr);

        public static AAMoonMaxDeclinationsDetails2[] Calculate(double StartJD, double EndJD, double StepInterval, Algorithm algorithm) {
            var ptr = Calculate(StartJD, EndJD, StepInterval, algorithm, out int Count);
            var result = new AAMoonMaxDeclinationsDetails2[Count];
            var size = Marshal.SizeOf<AAMoonMaxDeclinationsDetails2>();
            for (var i = 0; i < Count; i++) result[i] = Marshal.PtrToStructure<AAMoonMaxDeclinationsDetails2>(ptr + i * size);
            DestroyData(ptr);
            return result;
        }
    }

    public class AAMoonNodes {
        private const string LibName = "caaplus";

        [DllImport(LibName, EntryPoint = "CAAMoonNodes_K")]
        public static extern double K(double Year);

        [DllImport(LibName, EntryPoint = "CAAMoonNodes_PassageThroNode")]
        public static extern double PassageThroNode(double k);

    }

    public class AAMoonNodes2 {
        private const string LibName = "caaplus";

        [Flags]
        public enum Type : int {
            NotDefined = 0,
            Ascending = 1,
            Descending = 2,
        }

        [Flags]
        public enum Algorithm : int {
            MeeusTruncated = 0,
            ELP2000 = 1,
        }

        [StructLayout(LayoutKind.Sequential)]
        public struct AAMoonNodesDetails2 {
            public Type type;
            public double JD;
        }

        [DllImport(LibName, EntryPoint = "CAAMoonNodes2_Calculate")]
        private static extern IntPtr Calculate(double StartJD, double EndJD, double StepInterval, Algorithm algorithm, out int num);

        [DllImport(LibName, EntryPoint = "CAAMoonNodes2_DestroyData")]
        private static extern void DestroyData(IntPtr ptr);

        public static AAMoonNodesDetails2[] Calculate(double StartJD, double EndJD, double StepInterval, Algorithm algorithm) {
            var ptr = Calculate(StartJD, EndJD, StepInterval, algorithm, out int Count);
            var result = new AAMoonNodesDetails2[Count];
            var size = Marshal.SizeOf<AAMoonNodesDetails2>();
            for (var i = 0; i < Count; i++) result[i] = Marshal.PtrToStructure<AAMoonNodesDetails2>(ptr + i * size);
            DestroyData(ptr);
            return result;
        }
    }

    public class AAMoonPerigeeApogee {
        private const string LibName = "caaplus";

        [DllImport(LibName, EntryPoint = "CAAMoonPerigeeApogee_K")]
        public static extern double K(double Year);

        [DllImport(LibName, EntryPoint = "CAAMoonPerigeeApogee_MeanPerigee")]
        public static extern double MeanPerigee(double k);

        [DllImport(LibName, EntryPoint = "CAAMoonPerigeeApogee_MeanApogee")]
        public static extern double MeanApogee(double k);

        [DllImport(LibName, EntryPoint = "CAAMoonPerigeeApogee_TruePerigee")]
        public static extern double TruePerigee(double k);

        [DllImport(LibName, EntryPoint = "CAAMoonPerigeeApogee_TrueApogee")]
        public static extern double TrueApogee(double k);

        [DllImport(LibName, EntryPoint = "CAAMoonPerigeeApogee_PerigeeParallax")]
        public static extern double PerigeeParallax(double k);

        [DllImport(LibName, EntryPoint = "CAAMoonPerigeeApogee_ApogeeParallax")]
        public static extern double ApogeeParallax(double k);

    }

    public class AAMoonPerigeeApogee2 {
        private const string LibName = "caaplus";

        [Flags]
        public enum Type : int {
            NotDefined = 0,
            Perigee = 1,
            Apogee = 2,
        }

        [Flags]
        public enum Algorithm : int {
            MeeusTruncated = 0,
            ELP2000 = 1,
        }

        [StructLayout(LayoutKind.Sequential)]
        public struct AAMoonPerigeeApogeeDetails2 {
            public Type type;
            public double JD;
            public double Value;
        }

        [DllImport(LibName, EntryPoint = "CAAMoonPerigeeApogee2_Calculate")]
        private static extern IntPtr Calculate(double StartJD, double EndJD, double StepInterval, Algorithm algorithm, out int num);

        [DllImport(LibName, EntryPoint = "CAAMoonPerigeeApogee2_DestroyData")]
        private static extern void DestroyData(IntPtr ptr);

        public static AAMoonPerigeeApogeeDetails2[] Calculate(double StartJD, double EndJD, double StepInterval, Algorithm algorithm) {
            var ptr = Calculate(StartJD, EndJD, StepInterval, algorithm, out int Count);
            var result = new AAMoonPerigeeApogeeDetails2[Count];
            var size = Marshal.SizeOf<AAMoonPerigeeApogeeDetails2>();
            for (var i = 0; i < Count; i++) result[i] = Marshal.PtrToStructure<AAMoonPerigeeApogeeDetails2>(ptr + i * size);
            DestroyData(ptr);
            return result;
        }
    }

    public class AAMoonPhases {
        private const string LibName = "caaplus";

        [DllImport(LibName, EntryPoint = "CAAMoonPhases_K")]
        public static extern double K(double Year);

        [DllImport(LibName, EntryPoint = "CAAMoonPhases_MeanPhase")]
        public static extern double MeanPhase(double k);

        [DllImport(LibName, EntryPoint = "CAAMoonPhases_TruePhase")]
        public static extern double TruePhase(double k);

    }

    public class AAMoonPhases2 {
        private const string LibName = "caaplus";

        [Flags]
        public enum Type : int {
            NotDefined = 0,
            NewMoon = 1,
            FirstQuarter = 2,
            FullMoon = 3,
            LastQuarter = 4,
        }

        [Flags]
        public enum Algorithm : int {
            MeeusTruncated = 0,
            ELP2000 = 1,
        }

        [StructLayout(LayoutKind.Sequential)]
        public struct AAMoonPhasesDetails2 {
            public Type type;
            public double JD;
        }

        [DllImport(LibName, EntryPoint = "CAAMoonPhases2_Calculate")]
        private static extern IntPtr Calculate(double StartJD, double EndJD, double StepInterval, Algorithm algorithm, out int num);

        [DllImport(LibName, EntryPoint = "CAAMoonPhases2_DestroyData")]
        private static extern void DestroyData(IntPtr ptr);

        public static AAMoonPhasesDetails2[] Calculate(double StartJD, double EndJD, double StepInterval, Algorithm algorithm) {
            var ptr = Calculate(StartJD, EndJD, StepInterval, algorithm, out int Count);
            var result = new AAMoonPhasesDetails2[Count];
            var size = Marshal.SizeOf<AAMoonPhasesDetails2>();
            for (var i = 0; i < Count; i++) result[i] = Marshal.PtrToStructure<AAMoonPhasesDetails2>(ptr + i * size);
            DestroyData(ptr);
            return result;
        }
    }

    public class AAMoslemCalendar {
        private const string LibName = "caaplus";

        [DllImport(LibName, EntryPoint = "CAAMoslemCalendar_MoslemToJulian")]
        public static extern AACalendarDate MoslemToJulian(long Year, long Month, long Day);

        [DllImport(LibName, EntryPoint = "CAAMoslemCalendar_JulianToMoslem")]
        public static extern AACalendarDate JulianToMoslem(long Year, long Month, long Day);

        [DllImport(LibName, EntryPoint = "CAAMoslemCalendar_IsLeap")]
        [return: MarshalAs(UnmanagedType.U1)]
        public static extern bool IsLeap(long Year);

    }

    public class AANearParabolic {
        private const string LibName = "caaplus";

        [StructLayout(LayoutKind.Sequential)]
        public struct AANearParabolicObjectElements {
            public double q;
            public double i;
            public double w;
            public double omega;
            public double JDEquinox;
            public double T;
            public double e;
        }

        [StructLayout(LayoutKind.Sequential)]
        public struct AANearParabolicObjectDetails {
            public AA3DCoordinate HeliocentricRectangularEquatorial;
            public AA3DCoordinate HeliocentricRectangularEcliptical;
            public double HeliocentricEclipticLongitude;
            public double HeliocentricEclipticLatitude;
            public double TrueGeocentricRA;
            public double TrueGeocentricDeclination;
            public double TrueGeocentricDistance;
            public double TrueGeocentricLightTime;
            public double AstrometricGeocentricRA;
            public double AstrometricGeocentricDeclination;
            public double AstrometricGeocentricDistance;
            public double AstrometricGeocentricLightTime;
            public double Elongation;
            public double PhaseAngle;
        }

        [DllImport(LibName, EntryPoint = "CAANearParabolic_Calculate")]
        public static extern AANearParabolicObjectDetails Calculate(double JD, ref AANearParabolicObjectElements elements, bool bHighPrecision);

        [DllImport(LibName, EntryPoint = "CAANearParabolic_cbrt")]
        public static extern double cbrt(double x);

        [DllImport(LibName, EntryPoint = "CAANearParabolic_CalculateTrueAnomalyAndRadius")]
        public static extern void CalculateTrueAnomalyAndRadius(double JD, ref AANearParabolicObjectElements elements, out double v, out double r);

    }

    public class AANeptune {
        private const string LibName = "caaplus";

        [DllImport(LibName, EntryPoint = "CAANeptune_EclipticLongitude")]
        public static extern double EclipticLongitude(double JD, bool bHighPrecision);

        [DllImport(LibName, EntryPoint = "CAANeptune_EclipticLatitude")]
        public static extern double EclipticLatitude(double JD, bool bHighPrecision);

        [DllImport(LibName, EntryPoint = "CAANeptune_RadiusVector")]
        public static extern double RadiusVector(double JD, bool bHighPrecision);

    }

    public class AANodes {
        private const string LibName = "caaplus";

        [StructLayout(LayoutKind.Sequential)]
        public struct AANodeObjectDetails {
            public double t;
            public double radius;
        }

        [DllImport(LibName, EntryPoint = "CAANodes_PassageThroAscendingNode")]
        public static extern AANodeObjectDetails PassageThroAscendingNode(ref AAEllipticalObjectElements elements);

        [DllImport(LibName, EntryPoint = "CAANodes_PassageThroDescendingNode")]
        public static extern AANodeObjectDetails PassageThroDescendingNode(ref AAEllipticalObjectElements elements);

        [DllImport(LibName, EntryPoint = "CAANodes_PassageThroAscendingNode_2")]
        public static extern AANodeObjectDetails PassageThroAscendingNode_2(ref AAParabolicObjectElements elements);

        [DllImport(LibName, EntryPoint = "CAANodes_PassageThroDescendingNode_2")]
        public static extern AANodeObjectDetails PassageThroDescendingNode_2(ref AAParabolicObjectElements elements);

    }

    public class AANutation {
        private const string LibName = "caaplus";

        [DllImport(LibName, EntryPoint = "CAANutation_NutationInLongitude")]
        public static extern double NutationInLongitude(double JD);

        [DllImport(LibName, EntryPoint = "CAANutation_NutationInObliquity")]
        public static extern double NutationInObliquity(double JD);

        [DllImport(LibName, EntryPoint = "CAANutation_NutationInRightAscension")]
        public static extern double NutationInRightAscension(double Alpha, double Delta, double Obliquity, double NutationInLongitude, double NutationInObliquity);

        [DllImport(LibName, EntryPoint = "CAANutation_NutationInDeclination")]
        public static extern double NutationInDeclination(double Alpha, double Obliquity, double NutationInLongitude, double NutationInObliquity);

        [DllImport(LibName, EntryPoint = "CAANutation_MeanObliquityOfEcliptic")]
        public static extern double MeanObliquityOfEcliptic(double JD);

        [DllImport(LibName, EntryPoint = "CAANutation_TrueObliquityOfEcliptic")]
        public static extern double TrueObliquityOfEcliptic(double JD);

    }

    public class AAParabolic {
        private const string LibName = "caaplus";

        [StructLayout(LayoutKind.Sequential)]
        public struct AAParabolicObjectElements {
            public double q;
            public double i;
            public double w;
            public double omega;
            public double JDEquinox;
            public double T;
        }

        [StructLayout(LayoutKind.Sequential)]
        public struct AAParabolicObjectDetails {
            public AA3DCoordinate HeliocentricRectangularEquatorial;
            public AA3DCoordinate HeliocentricRectangularEcliptical;
            public double HeliocentricEclipticLongitude;
            public double HeliocentricEclipticLatitude;
            public double TrueGeocentricRA;
            public double TrueGeocentricDeclination;
            public double TrueGeocentricDistance;
            public double TrueGeocentricLightTime;
            public double AstrometricGeocentricRA;
            public double AstrometricGeocentricDeclination;
            public double AstrometricGeocentricDistance;
            public double AstrometricGeocentricLightTime;
            public double Elongation;
            public double PhaseAngle;
        }

        [DllImport(LibName, EntryPoint = "CAAParabolic_CalculateBarkers")]
        public static extern double CalculateBarkers(double W, double epsilon);

        [DllImport(LibName, EntryPoint = "CAAParabolic_Calculate")]
        public static extern AAParabolicObjectDetails Calculate(double JD, ref AAParabolicObjectElements elements, bool bHighPrecision, double epsilon);

    }

    public class AAParallactic {
        private const string LibName = "caaplus";

        [DllImport(LibName, EntryPoint = "CAAParallactic_ParallacticAngle")]
        public static extern double ParallacticAngle(double HourAngle, double Latitude, double delta);

        [DllImport(LibName, EntryPoint = "CAAParallactic_EclipticLongitudeOnHorizon")]
        public static extern double EclipticLongitudeOnHorizon(double LocalSiderealTime, double ObliquityOfEcliptic, double Latitude);

        [DllImport(LibName, EntryPoint = "CAAParallactic_AngleBetweenEclipticAndHorizon")]
        public static extern double AngleBetweenEclipticAndHorizon(double LocalSiderealTime, double ObliquityOfEcliptic, double Latitude);

        [DllImport(LibName, EntryPoint = "CAAParallactic_AngleBetweenNorthCelestialPoleAndNorthPoleOfEcliptic")]
        public static extern double AngleBetweenNorthCelestialPoleAndNorthPoleOfEcliptic(double Lambda, double Beta, double ObliquityOfEcliptic);

    }

    public class AAParallax {
        private const string LibName = "caaplus";

        [StructLayout(LayoutKind.Sequential)]
        public struct AATopocentricEclipticDetails {
            public double Lambda;
            public double Beta;
            public double Semidiameter;
        }

        [DllImport(LibName, EntryPoint = "CAAParallax_Equatorial2TopocentricDelta")]
        public static extern AA2DCoordinate Equatorial2TopocentricDelta(double Alpha, double Delta, double Distance, double Longitude, double Latitude, double Height, double JD);

        [DllImport(LibName, EntryPoint = "CAAParallax_Equatorial2Topocentric")]
        public static extern AA2DCoordinate Equatorial2Topocentric(double Alpha, double Delta, double Distance, double Longitude, double Latitude, double Height, double JD);

        [DllImport(LibName, EntryPoint = "CAAParallax_Ecliptic2Topocentric")]
        public static extern AATopocentricEclipticDetails Ecliptic2Topocentric(double Lambda, double Beta, double Semidiameter, double Distance, double Epsilon, double Latitude, double Height, double JD);

        [DllImport(LibName, EntryPoint = "CAAParallax_ParallaxToDistance")]
        public static extern double ParallaxToDistance(double Parallax);

        [DllImport(LibName, EntryPoint = "CAAParallax_DistanceToParallax")]
        public static extern double DistanceToParallax(double Distance);

    }

    public class AAPhysicalJupiter {
        private const string LibName = "caaplus";

        [StructLayout(LayoutKind.Sequential)]
        public struct AAPhysicalJupiterDetails {
            public double DE;
            public double DS;
            public double Geometricw1;
            public double Geometricw2;
            public double Apparentw1;
            public double Apparentw2;
            public double P;
        }

        [DllImport(LibName, EntryPoint = "CAAPhysicalJupiter_Calculate")]
        public static extern AAPhysicalJupiterDetails Calculate(double JD, bool bHighPrecision);

    }

    public class AAPhysicalMars {
        private const string LibName = "caaplus";

        [StructLayout(LayoutKind.Sequential)]
        public struct AAPhysicalMarsDetails {
            public double DE;
            public double DS;
            public double w;
            public double P;
            public double X;
            public double k;
            public double q;
            public double d;
        }

        [DllImport(LibName, EntryPoint = "CAAPhysicalMars_Calculate")]
        public static extern AAPhysicalMarsDetails Calculate(double JD, bool bHighPrecision);

    }

    public class AAPhysicalMoon {
        private const string LibName = "caaplus";

        [StructLayout(LayoutKind.Sequential)]
        public struct AAPhysicalMoonDetails {
            public double ldash;
            public double bdash;
            public double ldash2;
            public double bdash2;
            public double l;
            public double b;
            public double P;
        }

        [StructLayout(LayoutKind.Sequential)]
        public struct AASelenographicMoonDetails {
            public double l0;
            public double b0;
            public double c0;
        }

        [DllImport(LibName, EntryPoint = "CAAPhysicalMoon_CalculateGeocentric")]
        public static extern AAPhysicalMoonDetails CalculateGeocentric(double JD);

        [DllImport(LibName, EntryPoint = "CAAPhysicalMoon_CalculateTopocentric")]
        public static extern AAPhysicalMoonDetails CalculateTopocentric(double JD, double Longitude, double Latitude);

        [DllImport(LibName, EntryPoint = "CAAPhysicalMoon_CalculateSelenographicPositionOfSun")]
        public static extern AASelenographicMoonDetails CalculateSelenographicPositionOfSun(double JD, bool bHighPrecision);

        [DllImport(LibName, EntryPoint = "CAAPhysicalMoon_AltitudeOfSun")]
        public static extern double AltitudeOfSun(double JD, double Longitude, double Latitude, bool bHighPrecision);

        [DllImport(LibName, EntryPoint = "CAAPhysicalMoon_TimeOfSunrise")]
        public static extern double TimeOfSunrise(double JD, double Longitude, double Latitude, bool bHighPrecision);

        [DllImport(LibName, EntryPoint = "CAAPhysicalMoon_TimeOfSunset")]
        public static extern double TimeOfSunset(double JD, double Longitude, double Latitude, bool bHighPrecision);

    }

    public class AAPhysicalSun {
        private const string LibName = "caaplus";

        [StructLayout(LayoutKind.Sequential)]
        public struct AAPhysicalSunDetails {
            public double P;
            public double B0;
            public double L0;
        }

        [DllImport(LibName, EntryPoint = "CAAPhysicalSun_Calculate")]
        public static extern AAPhysicalSunDetails Calculate(double JD, bool bHighPrecision);

        [DllImport(LibName, EntryPoint = "CAAPhysicalSun_TimeOfStartOfRotation")]
        public static extern double TimeOfStartOfRotation(long C);

    }

    public class AAPlanetaryPhenomena {
        private const string LibName = "caaplus";

        [Flags]
        public enum Planet : int {
            MERCURY = 0,
            VENUS = 1,
            MARS = 2,
            JUPITER = 3,
            SATURN = 4,
            URANUS = 5,
            NEPTUNE = 6,
        }

        [Flags]
        public enum Type : int {
            INFERIOR_CONJUNCTION = 0,
            SUPERIOR_CONJUNCTION = 1,
            OPPOSITION = 2,
            CONJUNCTION = 3,
            EASTERN_ELONGATION = 4,
            WESTERN_ELONGATION = 5,
            STATION1 = 6,
            STATION2 = 7,
        }

        [DllImport(LibName, EntryPoint = "CAAPlanetaryPhenomena_K")]
        public static extern double K(double Year, Planet planet, Type type);

        [DllImport(LibName, EntryPoint = "CAAPlanetaryPhenomena_Mean")]
        public static extern double Mean(double k, Planet planet, Type type);

        [DllImport(LibName, EntryPoint = "CAAPlanetaryPhenomena_True")]
        public static extern double True(double k, Planet planet, Type type);

        [DllImport(LibName, EntryPoint = "CAAPlanetaryPhenomena_ElongationValue")]
        public static extern double ElongationValue(double k, Planet planet, bool bEastern);

    }

    public class AAPlanetaryPhenomena2 {
        private const string LibName = "caaplus";

        [Flags]
        public enum Type : int {
            NotDefined = 0,
            InferiorConjunctionInEclipticLongitude = 1,
            InferiorConjunctionInRA = 2,
            InferiorConjunctionInAngularDistance = 3,
            SuperiorConjunctionInEclipticLongitude = 4,
            SuperiorConjunctionInRA = 5,
            SuperiorConjunctionInAngularDistance = 6,
            GreatestWesternElongationInEclipticLongitude = 7,
            GreatestWesternElongationInRA = 8,
            GreatestWesternElongationInAngularDistance = 9,
            GreatestEasternElongationInEclipticLongitude = 10,
            GreatestEasternElongationInRA = 11,
            GreatestEasternElongationInAngularDistance = 12,
            OppositionInEclipticLongitude = 13,
            OppositionInRA = 14,
            OppositionInAngularDistance = 15,
            ConjunctionInEclipticLongitude = 16,
            ConjunctionInRA = 17,
            ConjunctionInAngularDistance = 18,
            Station1InEclipticLongitude = 19,
            Station1InRA = 20,
            Station2InEclipticLongitude = 21,
            Station2InRA = 22,
            WesternQuadratureInEclipticLongitude = 23,
            WesternQuadratureInRA = 24,
            WesternQuadratureInAngularDistance = 25,
            EasternQuadratureInEclipticLongitude = 26,
            EasternQuadratureInRA = 27,
            EasternQuadratureInAngularDistance = 28,
            MaximumDistance = 29,
            MinimumDistance = 30,
        }

        [Flags]
        public enum Object : int {
            MERCURY = 0,
            VENUS = 1,
            MARS = 2,
            JUPITER = 3,
            SATURN = 4,
            URANUS = 5,
            NEPTUNE = 6,
        }

        [StructLayout(LayoutKind.Sequential)]
        public struct AAPlanetaryPhenomenaDetails2 {
            public Type type;
            public double JD;
            public double Value;
        }

        [DllImport(LibName, EntryPoint = "CAAPlanetaryPhenomena2_Calculate")]
        private static extern IntPtr Calculate(double StartJD, double EndJD, Object _object, double StepInterval, bool bHighPrecision, out int num);

        [DllImport(LibName, EntryPoint = "CAAPlanetaryPhenomena2_DestroyData")]
        private static extern void DestroyData(IntPtr ptr);

        public static AAPlanetaryPhenomenaDetails2[] Calculate(double StartJD, double EndJD, Object _object, double StepInterval, bool bHighPrecision) {
            var ptr = Calculate(StartJD, EndJD, _object, StepInterval, bHighPrecision, out int Count);
            var result = new AAPlanetaryPhenomenaDetails2[Count];
            var size = Marshal.SizeOf<AAPlanetaryPhenomenaDetails2>();
            for (var i = 0; i < Count; i++) result[i] = Marshal.PtrToStructure<AAPlanetaryPhenomenaDetails2>(ptr + i * size);
            DestroyData(ptr);
            return result;
        }
    }

    public class AAPlanetPerihelionAphelion {
        private const string LibName = "caaplus";

        [DllImport(LibName, EntryPoint = "CAAPlanetPerihelionAphelion_MercuryK")]
        public static extern double MercuryK(double Year);

        [DllImport(LibName, EntryPoint = "CAAPlanetPerihelionAphelion_Mercury")]
        public static extern double Mercury(double k);

        [DllImport(LibName, EntryPoint = "CAAPlanetPerihelionAphelion_VenusK")]
        public static extern double VenusK(double Year);

        [DllImport(LibName, EntryPoint = "CAAPlanetPerihelionAphelion_Venus")]
        public static extern double Venus(double k);

        [DllImport(LibName, EntryPoint = "CAAPlanetPerihelionAphelion_EarthK")]
        public static extern double EarthK(double Year);

        [DllImport(LibName, EntryPoint = "CAAPlanetPerihelionAphelion_EarthPerihelion")]
        public static extern double EarthPerihelion(double k, bool bBarycentric);

        [DllImport(LibName, EntryPoint = "CAAPlanetPerihelionAphelion_EarthAphelion")]
        public static extern double EarthAphelion(double k, bool bBarycentric);

        [DllImport(LibName, EntryPoint = "CAAPlanetPerihelionAphelion_MarsK")]
        public static extern double MarsK(double Year);

        [DllImport(LibName, EntryPoint = "CAAPlanetPerihelionAphelion_Mars")]
        public static extern double Mars(double k);

        [DllImport(LibName, EntryPoint = "CAAPlanetPerihelionAphelion_JupiterK")]
        public static extern double JupiterK(double Year);

        [DllImport(LibName, EntryPoint = "CAAPlanetPerihelionAphelion_Jupiter")]
        public static extern double Jupiter(double k);

        [DllImport(LibName, EntryPoint = "CAAPlanetPerihelionAphelion_SaturnK")]
        public static extern double SaturnK(double Year);

        [DllImport(LibName, EntryPoint = "CAAPlanetPerihelionAphelion_Saturn")]
        public static extern double Saturn(double k);

        [DllImport(LibName, EntryPoint = "CAAPlanetPerihelionAphelion_UranusK")]
        public static extern double UranusK(double Year);

        [DllImport(LibName, EntryPoint = "CAAPlanetPerihelionAphelion_Uranus")]
        public static extern double Uranus(double k);

        [DllImport(LibName, EntryPoint = "CAAPlanetPerihelionAphelion_NeptuneK")]
        public static extern double NeptuneK(double Year);

        [DllImport(LibName, EntryPoint = "CAAPlanetPerihelionAphelion_Neptune")]
        public static extern double Neptune(double k);

    }

    public class AAPlanetPerihelionAphelion2 {
        private const string LibName = "caaplus";

        [Flags]
        public enum Type : int {
            NotDefined = 0,
            Perihelion = 1,
            Aphelion = 2,
        }

        [Flags]
        public enum Object : int {
            MERCURY = 0,
            VENUS = 1,
            EARTH = 2,
            MARS = 3,
            JUPITER = 4,
            SATURN = 5,
            URANUS = 6,
            NEPTUNE = 7,
            PLUTO = 8,
        }

        [StructLayout(LayoutKind.Sequential)]
        public struct AAPlanetPerihelionAphelionDetails2 {
            public Type type;
            public double JD;
            public double Value;
        }

        [DllImport(LibName, EntryPoint = "CAAPlanetPerihelionAphelion2_Calculate")]
        private static extern IntPtr Calculate(double StartJD, double EndJD, Object _object, double StepInterval, bool bHighPrecision, out int num);

        [DllImport(LibName, EntryPoint = "CAAPlanetPerihelionAphelion2_DestroyData")]
        private static extern void DestroyData(IntPtr ptr);

        public static AAPlanetPerihelionAphelionDetails2[] Calculate(double StartJD, double EndJD, Object _object, double StepInterval, bool bHighPrecision) {
            var ptr = Calculate(StartJD, EndJD, _object, StepInterval, bHighPrecision, out int Count);
            var result = new AAPlanetPerihelionAphelionDetails2[Count];
            var size = Marshal.SizeOf<AAPlanetPerihelionAphelionDetails2>();
            for (var i = 0; i < Count; i++) result[i] = Marshal.PtrToStructure<AAPlanetPerihelionAphelionDetails2>(ptr + i * size);
            DestroyData(ptr);
            return result;
        }
    }

    public class AAPluto {
        private const string LibName = "caaplus";

        [DllImport(LibName, EntryPoint = "CAAPluto_EclipticLongitude")]
        public static extern double EclipticLongitude(double JD);

        [DllImport(LibName, EntryPoint = "CAAPluto_EclipticLatitude")]
        public static extern double EclipticLatitude(double JD);

        [DllImport(LibName, EntryPoint = "CAAPluto_RadiusVector")]
        public static extern double RadiusVector(double JD);

    }

    public class AAPrecession {
        private const string LibName = "caaplus";

        [DllImport(LibName, EntryPoint = "CAAPrecession_PrecessEquatorial")]
        public static extern AA2DCoordinate PrecessEquatorial(double Alpha, double Delta, double JD0, double JD);

        [DllImport(LibName, EntryPoint = "CAAPrecession_PrecessEquatorialFK4")]
        public static extern AA2DCoordinate PrecessEquatorialFK4(double Alpha, double Delta, double JD0, double JD);

        [DllImport(LibName, EntryPoint = "CAAPrecession_PrecessEcliptic")]
        public static extern AA2DCoordinate PrecessEcliptic(double Lambda, double Beta, double JD0, double JD);

        [DllImport(LibName, EntryPoint = "CAAPrecession_EquatorialPMToEcliptic")]
        public static extern AA2DCoordinate EquatorialPMToEcliptic(double Alpha, double Delta, double Beta, double PMAlpha, double PMDelta, double Epsilon);

        [DllImport(LibName, EntryPoint = "CAAPrecession_AdjustPositionUsingUniformProperMotion")]
        public static extern AA2DCoordinate AdjustPositionUsingUniformProperMotion(double t, double Alpha, double Delta, double PMAlpha, double PMDelta);

        [DllImport(LibName, EntryPoint = "CAAPrecession_AdjustPositionUsingMotionInSpace")]
        public static extern AA2DCoordinate AdjustPositionUsingMotionInSpace(double r, double deltar, double t, double Alpha, double Delta, double PMAlpha, double PMDelta);

    }

    public class AARefraction {
        private const string LibName = "caaplus";

        [DllImport(LibName, EntryPoint = "CAARefraction_RefractionFromApparent")]
        public static extern double RefractionFromApparent(double Altitude, double Pressure, double Temperature);

        [DllImport(LibName, EntryPoint = "CAARefraction_RefractionFromTrue")]
        public static extern double RefractionFromTrue(double Altitude, double Pressure, double Temperature);

    }

    public class AARiseTransitSet {
        private const string LibName = "caaplus";

        [StructLayout(LayoutKind.Sequential)]
        public struct AARiseTransitSetDetails {
            [MarshalAs(UnmanagedType.U1)] public bool bRiseValid;
            public double Rise;
            [MarshalAs(UnmanagedType.U1)] public bool bTransitValid;
            [MarshalAs(UnmanagedType.U1)] public bool bTransitAboveHorizon;
            public double Transit;
            [MarshalAs(UnmanagedType.U1)] public bool bSetValid;
            public double Set;
        }

        [DllImport(LibName, EntryPoint = "CAARiseTransitSet_Calculate")]
        public static extern AARiseTransitSetDetails Calculate(double JD, double Alpha1, double Delta1, double Alpha2, double Delta2, double Alpha3, double Delta3, double Longitude, double Latitude, double h0);

        [DllImport(LibName, EntryPoint = "CAARiseTransitSet_CorrectRAValuesForInterpolation")]
        public static extern void CorrectRAValuesForInterpolation(out double Alpha1, out double Alpha2, out double Alpha3);

    }

    public class AARiseTransitSet2 {
        private const string LibName = "caaplus";

        [Flags]
        public enum Type : int {
            NotDefined = 0,
            Rise = 1,
            Set = 2,
            SouthernTransit = 3,
            NorthernTransit = 4,
            CivilDusk = 5,
            NauticalDusk = 6,
            AstronomicalDusk = 7,
            AstronomicalDawn = 8,
            NauticalDawn = 9,
            CivilDawn = 10,
        }

        [Flags]
        public enum Object : int {
            SUN = 0,
            MOON = 1,
            MERCURY = 2,
            VENUS = 3,
            MARS = 4,
            JUPITER = 5,
            SATURN = 6,
            URANUS = 7,
            NEPTUNE = 8,
            STAR = 9,
        }

        [Flags]
        public enum MoonAlgorithm : int {
            MeeusTruncated = 0,
            ELP2000 = 1,
        }

        [StructLayout(LayoutKind.Sequential)]
        public struct AARiseTransitSetDetails2 {
            public Type type;
            public double JD;
            public double Bearing;
            public double GeometricAltitude;
            [MarshalAs(UnmanagedType.U1)] public bool bAboveHorizon;
        }

        [DllImport(LibName, EntryPoint = "CAARiseTransitSet2_Calculate")]
        private static extern IntPtr Calculate(double StartJD, double EndJD, Object _object, double Longitude, double Latitude, double h0, double StepInterval, bool bHighPrecision, out int num);

        [DllImport(LibName, EntryPoint = "CAARiseTransitSet2_CalculateMoon")]
        private static extern IntPtr CalculateMoon(double StartJD, double EndJD, double Longitude, double Latitude, double RefractionAtHorizon, double StepInterval, MoonAlgorithm algorithm, out int num);

        [DllImport(LibName, EntryPoint = "CAARiseTransitSet2_CalculateStationary")]
        private static extern IntPtr CalculateStationary(double StartJD, double EndJD, double Alpha, double Delta, double Longitude, double Latitude, double h0, double StepInterval, out int num);

        [DllImport(LibName, EntryPoint = "CAARiseTransitSet2_DestroyData")]
        private static extern void DestroyData(IntPtr ptr);

        public static AARiseTransitSetDetails2[] Calculate(double StartJD, double EndJD, Object _object, double Longitude, double Latitude, double h0, double StepInterval, bool bHighPrecision) {
            var ptr = Calculate(StartJD, EndJD, _object, Longitude, Latitude, h0, StepInterval, bHighPrecision, out int Count);
            var result = new AARiseTransitSetDetails2[Count];
            var size = Marshal.SizeOf<AARiseTransitSetDetails2>();
            for (var i = 0; i < Count; i++) result[i] = Marshal.PtrToStructure<AARiseTransitSetDetails2>(ptr + i * size);
            DestroyData(ptr);
            return result;
        }

        public static AARiseTransitSetDetails2[] CalculateMoon(double StartJD, double EndJD, double Longitude, double Latitude, double RefractionAtHorizon, double StepInterval, MoonAlgorithm algorithm) {
            var ptr = CalculateMoon(StartJD, EndJD, Longitude, Latitude, RefractionAtHorizon, StepInterval, algorithm, out int Count);
            var result = new AARiseTransitSetDetails2[Count];
            var size = Marshal.SizeOf<AARiseTransitSetDetails2>();
            for (var i = 0; i < Count; i++) result[i] = Marshal.PtrToStructure<AARiseTransitSetDetails2>(ptr + i * size);
            DestroyData(ptr);
            return result;
        }

        public static AARiseTransitSetDetails2[] CalculateStationary(double StartJD, double EndJD, double Alpha, double Delta, double Longitude, double Latitude, double h0, double StepInterval) {
            var ptr = CalculateStationary(StartJD, EndJD, Alpha, Delta, Longitude, Latitude, h0, StepInterval, out int Count);
            var result = new AARiseTransitSetDetails2[Count];
            var size = Marshal.SizeOf<AARiseTransitSetDetails2>();
            for (var i = 0; i < Count; i++) result[i] = Marshal.PtrToStructure<AARiseTransitSetDetails2>(ptr + i * size);
            DestroyData(ptr);
            return result;
        }
    }

    public class AASaturn {
        private const string LibName = "caaplus";

        [DllImport(LibName, EntryPoint = "CAASaturn_EclipticLongitude")]
        public static extern double EclipticLongitude(double JD, bool bHighPrecision);

        [DllImport(LibName, EntryPoint = "CAASaturn_EclipticLatitude")]
        public static extern double EclipticLatitude(double JD, bool bHighPrecision);

        [DllImport(LibName, EntryPoint = "CAASaturn_RadiusVector")]
        public static extern double RadiusVector(double JD, bool bHighPrecision);

    }

    public class AASaturnMoons {
        private const string LibName = "caaplus";

        [StructLayout(LayoutKind.Sequential)]
        public struct AASaturnMoonDetail {
            public AA3DCoordinate TrueRectangularCoordinates;
            public AA3DCoordinate ApparentRectangularCoordinates;
            [MarshalAs(UnmanagedType.U1)] public bool bInTransit;
            [MarshalAs(UnmanagedType.U1)] public bool bInOccultation;
            [MarshalAs(UnmanagedType.U1)] public bool bInEclipse;
            [MarshalAs(UnmanagedType.U1)] public bool bInShadowTransit;
        }

        [StructLayout(LayoutKind.Sequential)]
        public struct AASaturnMoonsDetails {
            public AASaturnMoonDetail Satellite1;
            public AASaturnMoonDetail Satellite2;
            public AASaturnMoonDetail Satellite3;
            public AASaturnMoonDetail Satellite4;
            public AASaturnMoonDetail Satellite5;
            public AASaturnMoonDetail Satellite6;
            public AASaturnMoonDetail Satellite7;
            public AASaturnMoonDetail Satellite8;
        }

        [DllImport(LibName, EntryPoint = "CAASaturnMoons_Calculate")]
        public static extern AASaturnMoonsDetails Calculate(double JD, bool bHighPrecision);

    }

    public class AASaturnRings {
        private const string LibName = "caaplus";

        [StructLayout(LayoutKind.Sequential)]
        public struct AASaturnRingDetails {
            public double B;
            public double Bdash;
            public double P;
            public double a;
            public double b;
            public double DeltaU;
            public double U1;
            public double U2;
        }

        [DllImport(LibName, EntryPoint = "CAASaturnRings_Calculate")]
        public static extern AASaturnRingDetails Calculate(double JD, bool bHighPrecision);

    }

    public class AASidereal {
        private const string LibName = "caaplus";

        [DllImport(LibName, EntryPoint = "CAASidereal_MeanGreenwichSiderealTime")]
        public static extern double MeanGreenwichSiderealTime(double JD);

        [DllImport(LibName, EntryPoint = "CAASidereal_ApparentGreenwichSiderealTime")]
        public static extern double ApparentGreenwichSiderealTime(double JD);

    }

    public class AAStellarMagnitudes {
        private const string LibName = "caaplus";

        [DllImport(LibName, EntryPoint = "CAAStellarMagnitudes_CombinedMagnitude")]
        public static extern double CombinedMagnitude(double m1, double m2);

        [DllImport(LibName, EntryPoint = "CAAStellarMagnitudes_CombinedMagnitude_2")]
        public static extern double CombinedMagnitude_2(int Magnitudes, double[] pMagnitudes);

        [DllImport(LibName, EntryPoint = "CAAStellarMagnitudes_BrightnessRatio")]
        public static extern double BrightnessRatio(double m1, double m2);

        [DllImport(LibName, EntryPoint = "CAAStellarMagnitudes_MagnitudeDifference")]
        public static extern double MagnitudeDifference(double brightnessRatio);

    }

    public class AASun {
        private const string LibName = "caaplus";

        [DllImport(LibName, EntryPoint = "CAASun_GeometricEclipticLongitude")]
        public static extern double GeometricEclipticLongitude(double JD, bool bHighPrecision);

        [DllImport(LibName, EntryPoint = "CAASun_GeometricEclipticLatitude")]
        public static extern double GeometricEclipticLatitude(double JD, bool bHighPrecision);

        [DllImport(LibName, EntryPoint = "CAASun_GeometricEclipticLongitudeJ2000")]
        public static extern double GeometricEclipticLongitudeJ2000(double JD, bool bHighPrecision);

        [DllImport(LibName, EntryPoint = "CAASun_GeometricEclipticLatitudeJ2000")]
        public static extern double GeometricEclipticLatitudeJ2000(double JD, bool bHighPrecision);

        [DllImport(LibName, EntryPoint = "CAASun_GeometricFK5EclipticLongitude")]
        public static extern double GeometricFK5EclipticLongitude(double JD, bool bHighPrecision);

        [DllImport(LibName, EntryPoint = "CAASun_GeometricFK5EclipticLatitude")]
        public static extern double GeometricFK5EclipticLatitude(double JD, bool bHighPrecision);

        [DllImport(LibName, EntryPoint = "CAASun_ApparentEclipticLongitude")]
        public static extern double ApparentEclipticLongitude(double JD, bool bHighPrecision);

        [DllImport(LibName, EntryPoint = "CAASun_ApparentEclipticLatitude")]
        public static extern double ApparentEclipticLatitude(double JD, bool bHighPrecision);

        [DllImport(LibName, EntryPoint = "CAASun_VariationGeometricEclipticLongitude")]
        public static extern double VariationGeometricEclipticLongitude(double JD);

        [DllImport(LibName, EntryPoint = "CAASun_EquatorialRectangularCoordinatesMeanEquinox")]
        public static extern AA3DCoordinate EquatorialRectangularCoordinatesMeanEquinox(double JD, bool bHighPrecision);

        [DllImport(LibName, EntryPoint = "CAASun_EclipticRectangularCoordinatesJ2000")]
        public static extern AA3DCoordinate EclipticRectangularCoordinatesJ2000(double JD, bool bHighPrecision);

        [DllImport(LibName, EntryPoint = "CAASun_EquatorialRectangularCoordinatesJ2000")]
        public static extern AA3DCoordinate EquatorialRectangularCoordinatesJ2000(double JD, bool bHighPrecision);

        [DllImport(LibName, EntryPoint = "CAASun_EquatorialRectangularCoordinatesB1950")]
        public static extern AA3DCoordinate EquatorialRectangularCoordinatesB1950(double JD, bool bHighPrecision);

        [DllImport(LibName, EntryPoint = "CAASun_EquatorialRectangularCoordinatesAnyEquinox")]
        public static extern AA3DCoordinate EquatorialRectangularCoordinatesAnyEquinox(double JD, double JDEquinox, bool bHighPrecision);

    }

    public class AAUranus {
        private const string LibName = "caaplus";

        [DllImport(LibName, EntryPoint = "CAAUranus_EclipticLongitude")]
        public static extern double EclipticLongitude(double JD, bool bHighPrecision);

        [DllImport(LibName, EntryPoint = "CAAUranus_EclipticLatitude")]
        public static extern double EclipticLatitude(double JD, bool bHighPrecision);

        [DllImport(LibName, EntryPoint = "CAAUranus_RadiusVector")]
        public static extern double RadiusVector(double JD, bool bHighPrecision);

    }

    public class AAVenus {
        private const string LibName = "caaplus";

        [DllImport(LibName, EntryPoint = "CAAVenus_EclipticLongitude")]
        public static extern double EclipticLongitude(double JD, bool bHighPrecision);

        [DllImport(LibName, EntryPoint = "CAAVenus_EclipticLatitude")]
        public static extern double EclipticLatitude(double JD, bool bHighPrecision);

        [DllImport(LibName, EntryPoint = "CAAVenus_RadiusVector")]
        public static extern double RadiusVector(double JD, bool bHighPrecision);

    }

    public class AAVSOP2013 : IDisposable {
        private const string LibName = "caaplus";
        private IntPtr _ptr = IntPtr.Zero;
        private bool disposedValue;

        public AAVSOP2013() {
            _ptr = Create();
        }

        [Flags]
        public enum Planet : int {
            MERCURY = 0,
            VENUS = 1,
            EARTH_MOON_BARYCENTER = 2,
            MARS = 3,
            JUPITER = 4,
            SATURN = 5,
            URANUS = 6,
            NEPTUNE = 7,
            PLUTO = 8
        }

        [StructLayout(LayoutKind.Sequential)]
        public struct AAVSOP2013Orbit {
            public double a;
            public double lambda;
            public double k;
            public double h;
            public double q;
            public double p;
        }

        [StructLayout(LayoutKind.Sequential)]
        public struct AAVSOP2013Position {
            public double X;
            public double Y;
            public double Z;
            public double X_DASH;
            public double Y_DASH;
            public double Z_DASH;
        }

        #region Public native methods
        [DllImport(LibName, EntryPoint = "CAAVSOP2013_CalculateMeanMotion")]
        public static extern double CalculateMeanMotion(Planet planet, double a);

        [DllImport(LibName, EntryPoint = "CAAVSOP2013_OrbitToElements")]
        public static extern AAEllipticalObjectElements OrbitToElements(double JD, Planet planet, ref AAVSOP2013Orbit orbit);

        [DllImport(LibName, EntryPoint = "CAAVSOP2013_Ecliptic2Equatorial")]
        public static extern AAVSOP2013Position Ecliptic2Equatorial(ref AAVSOP2013Position value);
        #endregion

        #region Private native methods
        [DllImport(LibName, EntryPoint = "CAAVSOP2013_Create")]
        private static extern IntPtr Create();

        [DllImport(LibName, CharSet = CharSet.Ansi, EntryPoint = "CAAVSOP2013_GetBinaryFilesDirectory")]
        private static extern IntPtr GetBinaryFilesDirectory(IntPtr ptr);

        [DllImport(LibName, CharSet = CharSet.Ansi, EntryPoint = "CAAVSOP2013_SetBinaryFilesDirectory")]
        private static extern void SetBinaryFilesDirectory(IntPtr ptr, IntPtr dir);

        [DllImport(LibName, EntryPoint = "CAAVSOP2013_Destroy")]
        private static extern void Destroy(IntPtr ptr);
        #endregion

        public string GetBinaryFilesDirectory() => Marshal.PtrToStringAnsi(GetBinaryFilesDirectory(_ptr));

        public void SetBinaryFilesDirectory(string dir) {
            var StrPtr = Marshal.StringToHGlobalAnsi(dir);
            SetBinaryFilesDirectory(_ptr, StrPtr);
            Marshal.FreeHGlobal(StrPtr);
        }

        protected virtual void Dispose(bool disposing) {
            if (!disposedValue) {
                // if (disposing) { }

                if (_ptr != IntPtr.Zero) {
                    Destroy(_ptr);
                    _ptr = IntPtr.Zero;
                }
                disposedValue = true;
            }
        }

        // Do not change this code. Put cleanup code in 'Dispose(bool disposing)' method
        ~AAVSOP2013() => Dispose(disposing: false);

        public void Dispose() {
            // Do not change this code. Put cleanup code in 'Dispose(bool disposing)' method
            Dispose(disposing: true);
            GC.SuppressFinalize(this);
        }
    }

    public class AAVSOP87 {
        private const string LibName = "caaplus";

        [StructLayout(LayoutKind.Sequential)]
        public struct VSOP87Coefficient {
            public double A;
            public double B;
            public double C;
        }

        [StructLayout(LayoutKind.Sequential)]
        public struct VSOP87Coefficient2 {
            IntPtr pCoefficients; // array of VSOP87Coefficient (see above)
            public int nCoefficientsSize;
        }

        [DllImport(LibName, EntryPoint = "CAAVSOP87_Calculate")]
        public static extern double Calculate(double JD, VSOP87Coefficient2[] pTable, int nTableSize, bool bAngle);

        [DllImport(LibName, EntryPoint = "CAAVSOP87_Calculate_Dash")]
        public static extern double Calculate_Dash(double JD, VSOP87Coefficient2[] pTable, int nTableSize);

    }

    public class AAVSOP87A_Earth {
        private const string LibName = "caaplus";

        [DllImport(LibName, EntryPoint = "CAAVSOP87A_Earth_X")]
        public static extern double Earth_X(double JD);

        [DllImport(LibName, EntryPoint = "CAAVSOP87A_Earth_X_DASH")]
        public static extern double Earth_X_DASH(double JD);

        [DllImport(LibName, EntryPoint = "CAAVSOP87A_Earth_Y")]
        public static extern double Earth_Y(double JD);

        [DllImport(LibName, EntryPoint = "CAAVSOP87A_Earth_Y_DASH")]
        public static extern double Earth_Y_DASH(double JD);

        [DllImport(LibName, EntryPoint = "CAAVSOP87A_Earth_Z")]
        public static extern double Earth_Z(double JD);

        [DllImport(LibName, EntryPoint = "CAAVSOP87A_Earth_Z_DASH")]
        public static extern double Earth_Z_DASH(double JD);

    }

    public class AAVSOP87A_EMB {
        private const string LibName = "caaplus";

        [DllImport(LibName, EntryPoint = "CAAVSOP87A_EMB_X")]
        public static extern double EMB_X(double JD);

        [DllImport(LibName, EntryPoint = "CAAVSOP87A_EMB_X_DASH")]
        public static extern double EMB_X_DASH(double JD);

        [DllImport(LibName, EntryPoint = "CAAVSOP87A_EMB_Y")]
        public static extern double EMB_Y(double JD);

        [DllImport(LibName, EntryPoint = "CAAVSOP87A_EMB_Y_DASH")]
        public static extern double EMB_Y_DASH(double JD);

        [DllImport(LibName, EntryPoint = "CAAVSOP87A_EMB_Z")]
        public static extern double EMB_Z(double JD);

        [DllImport(LibName, EntryPoint = "CAAVSOP87A_EMB_Z_DASH")]
        public static extern double EMB_Z_DASH(double JD);

    }

    public class AAVSOP87A_Jupiter {
        private const string LibName = "caaplus";

        [DllImport(LibName, EntryPoint = "CAAVSOP87A_Jupiter_X")]
        public static extern double Jupiter_X(double JD);

        [DllImport(LibName, EntryPoint = "CAAVSOP87A_Jupiter_X_DASH")]
        public static extern double Jupiter_X_DASH(double JD);

        [DllImport(LibName, EntryPoint = "CAAVSOP87A_Jupiter_Y")]
        public static extern double Jupiter_Y(double JD);

        [DllImport(LibName, EntryPoint = "CAAVSOP87A_Jupiter_Y_DASH")]
        public static extern double Jupiter_Y_DASH(double JD);

        [DllImport(LibName, EntryPoint = "CAAVSOP87A_Jupiter_Z")]
        public static extern double Jupiter_Z(double JD);

        [DllImport(LibName, EntryPoint = "CAAVSOP87A_Jupiter_Z_DASH")]
        public static extern double Jupiter_Z_DASH(double JD);

    }

    public class AAVSOP87A_Mars {
        private const string LibName = "caaplus";

        [DllImport(LibName, EntryPoint = "CAAVSOP87A_Mars_X")]
        public static extern double Mars_X(double JD);

        [DllImport(LibName, EntryPoint = "CAAVSOP87A_Mars_X_DASH")]
        public static extern double Mars_X_DASH(double JD);

        [DllImport(LibName, EntryPoint = "CAAVSOP87A_Mars_Y")]
        public static extern double Mars_Y(double JD);

        [DllImport(LibName, EntryPoint = "CAAVSOP87A_Mars_Y_DASH")]
        public static extern double Mars_Y_DASH(double JD);

        [DllImport(LibName, EntryPoint = "CAAVSOP87A_Mars_Z")]
        public static extern double Mars_Z(double JD);

        [DllImport(LibName, EntryPoint = "CAAVSOP87A_Mars_Z_DASH")]
        public static extern double Mars_Z_DASH(double JD);

    }

    public class AAVSOP87A_Mercury {
        private const string LibName = "caaplus";

        [DllImport(LibName, EntryPoint = "CAAVSOP87A_Mercury_X")]
        public static extern double Mercury_X(double JD);

        [DllImport(LibName, EntryPoint = "CAAVSOP87A_Mercury_X_DASH")]
        public static extern double Mercury_X_DASH(double JD);

        [DllImport(LibName, EntryPoint = "CAAVSOP87A_Mercury_Y")]
        public static extern double Mercury_Y(double JD);

        [DllImport(LibName, EntryPoint = "CAAVSOP87A_Mercury_Y_DASH")]
        public static extern double Mercury_Y_DASH(double JD);

        [DllImport(LibName, EntryPoint = "CAAVSOP87A_Mercury_Z")]
        public static extern double Mercury_Z(double JD);

        [DllImport(LibName, EntryPoint = "CAAVSOP87A_Mercury_Z_DASH")]
        public static extern double Mercury_Z_DASH(double JD);

    }

    public class AAVSOP87A_Neptune {
        private const string LibName = "caaplus";

        [DllImport(LibName, EntryPoint = "CAAVSOP87A_Neptune_X")]
        public static extern double Neptune_X(double JD);

        [DllImport(LibName, EntryPoint = "CAAVSOP87A_Neptune_X_DASH")]
        public static extern double Neptune_X_DASH(double JD);

        [DllImport(LibName, EntryPoint = "CAAVSOP87A_Neptune_Y")]
        public static extern double Neptune_Y(double JD);

        [DllImport(LibName, EntryPoint = "CAAVSOP87A_Neptune_Y_DASH")]
        public static extern double Neptune_Y_DASH(double JD);

        [DllImport(LibName, EntryPoint = "CAAVSOP87A_Neptune_Z")]
        public static extern double Neptune_Z(double JD);

        [DllImport(LibName, EntryPoint = "CAAVSOP87A_Neptune_Z_DASH")]
        public static extern double Neptune_Z_DASH(double JD);

    }

    public class AAVSOP87A_Saturn {
        private const string LibName = "caaplus";

        [DllImport(LibName, EntryPoint = "CAAVSOP87A_Saturn_X")]
        public static extern double Saturn_X(double JD);

        [DllImport(LibName, EntryPoint = "CAAVSOP87A_Saturn_X_DASH")]
        public static extern double Saturn_X_DASH(double JD);

        [DllImport(LibName, EntryPoint = "CAAVSOP87A_Saturn_Y")]
        public static extern double Saturn_Y(double JD);

        [DllImport(LibName, EntryPoint = "CAAVSOP87A_Saturn_Y_DASH")]
        public static extern double Saturn_Y_DASH(double JD);

        [DllImport(LibName, EntryPoint = "CAAVSOP87A_Saturn_Z")]
        public static extern double Saturn_Z(double JD);

        [DllImport(LibName, EntryPoint = "CAAVSOP87A_Saturn_Z_DASH")]
        public static extern double Saturn_Z_DASH(double JD);

    }

    public class AAVSOP87A_Uranus {
        private const string LibName = "caaplus";

        [DllImport(LibName, EntryPoint = "CAAVSOP87A_Uranus_X")]
        public static extern double Uranus_X(double JD);

        [DllImport(LibName, EntryPoint = "CAAVSOP87A_Uranus_X_DASH")]
        public static extern double Uranus_X_DASH(double JD);

        [DllImport(LibName, EntryPoint = "CAAVSOP87A_Uranus_Y")]
        public static extern double Uranus_Y(double JD);

        [DllImport(LibName, EntryPoint = "CAAVSOP87A_Uranus_Y_DASH")]
        public static extern double Uranus_Y_DASH(double JD);

        [DllImport(LibName, EntryPoint = "CAAVSOP87A_Uranus_Z")]
        public static extern double Uranus_Z(double JD);

        [DllImport(LibName, EntryPoint = "CAAVSOP87A_Uranus_Z_DASH")]
        public static extern double Uranus_Z_DASH(double JD);

    }

    public class AAVSOP87A_Venus {
        private const string LibName = "caaplus";

        [DllImport(LibName, EntryPoint = "CAAVSOP87A_Venus_X")]
        public static extern double Venus_X(double JD);

        [DllImport(LibName, EntryPoint = "CAAVSOP87A_Venus_X_DASH")]
        public static extern double Venus_X_DASH(double JD);

        [DllImport(LibName, EntryPoint = "CAAVSOP87A_Venus_Y")]
        public static extern double Venus_Y(double JD);

        [DllImport(LibName, EntryPoint = "CAAVSOP87A_Venus_Y_DASH")]
        public static extern double Venus_Y_DASH(double JD);

        [DllImport(LibName, EntryPoint = "CAAVSOP87A_Venus_Z")]
        public static extern double Venus_Z(double JD);

        [DllImport(LibName, EntryPoint = "CAAVSOP87A_Venus_Z_DASH")]
        public static extern double Venus_Z_DASH(double JD);

    }

    public class AAVSOP87B_Earth {
        private const string LibName = "caaplus";

        [DllImport(LibName, EntryPoint = "CAAVSOP87B_Earth_L")]
        public static extern double Earth_L(double JD);

        [DllImport(LibName, EntryPoint = "CAAVSOP87B_Earth_L_DASH")]
        public static extern double Earth_L_DASH(double JD);

        [DllImport(LibName, EntryPoint = "CAAVSOP87B_Earth_B")]
        public static extern double Earth_B(double JD);

        [DllImport(LibName, EntryPoint = "CAAVSOP87B_Earth_B_DASH")]
        public static extern double Earth_B_DASH(double JD);

        [DllImport(LibName, EntryPoint = "CAAVSOP87B_Earth_R")]
        public static extern double Earth_R(double JD);

        [DllImport(LibName, EntryPoint = "CAAVSOP87B_Earth_R_DASH")]
        public static extern double Earth_R_DASH(double JD);

    }

    public class AAVSOP87B_Jupiter {
        private const string LibName = "caaplus";

        [DllImport(LibName, EntryPoint = "CAAVSOP87B_Jupiter_L")]
        public static extern double Jupiter_L(double JD);

        [DllImport(LibName, EntryPoint = "CAAVSOP87B_Jupiter_L_DASH")]
        public static extern double Jupiter_L_DASH(double JD);

        [DllImport(LibName, EntryPoint = "CAAVSOP87B_Jupiter_B")]
        public static extern double Jupiter_B(double JD);

        [DllImport(LibName, EntryPoint = "CAAVSOP87B_Jupiter_B_DASH")]
        public static extern double Jupiter_B_DASH(double JD);

        [DllImport(LibName, EntryPoint = "CAAVSOP87B_Jupiter_R")]
        public static extern double Jupiter_R(double JD);

        [DllImport(LibName, EntryPoint = "CAAVSOP87B_Jupiter_R_DASH")]
        public static extern double Jupiter_R_DASH(double JD);

    }

    public class AAVSOP87B_Mars {
        private const string LibName = "caaplus";

        [DllImport(LibName, EntryPoint = "CAAVSOP87B_Mars_L")]
        public static extern double Mars_L(double JD);

        [DllImport(LibName, EntryPoint = "CAAVSOP87B_Mars_L_DASH")]
        public static extern double Mars_L_DASH(double JD);

        [DllImport(LibName, EntryPoint = "CAAVSOP87B_Mars_B")]
        public static extern double Mars_B(double JD);

        [DllImport(LibName, EntryPoint = "CAAVSOP87B_Mars_B_DASH")]
        public static extern double Mars_B_DASH(double JD);

        [DllImport(LibName, EntryPoint = "CAAVSOP87B_Mars_R")]
        public static extern double Mars_R(double JD);

        [DllImport(LibName, EntryPoint = "CAAVSOP87B_Mars_R_DASH")]
        public static extern double Mars_R_DASH(double JD);

    }

    public class AAVSOP87B_Mercury {
        private const string LibName = "caaplus";

        [DllImport(LibName, EntryPoint = "CAAVSOP87B_Mercury_L")]
        public static extern double Mercury_L(double JD);

        [DllImport(LibName, EntryPoint = "CAAVSOP87B_Mercury_L_DASH")]
        public static extern double Mercury_L_DASH(double JD);

        [DllImport(LibName, EntryPoint = "CAAVSOP87B_Mercury_B")]
        public static extern double Mercury_B(double JD);

        [DllImport(LibName, EntryPoint = "CAAVSOP87B_Mercury_B_DASH")]
        public static extern double Mercury_B_DASH(double JD);

        [DllImport(LibName, EntryPoint = "CAAVSOP87B_Mercury_R")]
        public static extern double Mercury_R(double JD);

        [DllImport(LibName, EntryPoint = "CAAVSOP87B_Mercury_R_DASH")]
        public static extern double Mercury_R_DASH(double JD);

    }

    public class AAVSOP87B_Neptune {
        private const string LibName = "caaplus";

        [DllImport(LibName, EntryPoint = "CAAVSOP87B_Neptune_L")]
        public static extern double Neptune_L(double JD);

        [DllImport(LibName, EntryPoint = "CAAVSOP87B_Neptune_L_DASH")]
        public static extern double Neptune_L_DASH(double JD);

        [DllImport(LibName, EntryPoint = "CAAVSOP87B_Neptune_B")]
        public static extern double Neptune_B(double JD);

        [DllImport(LibName, EntryPoint = "CAAVSOP87B_Neptune_B_DASH")]
        public static extern double Neptune_B_DASH(double JD);

        [DllImport(LibName, EntryPoint = "CAAVSOP87B_Neptune_R")]
        public static extern double Neptune_R(double JD);

        [DllImport(LibName, EntryPoint = "CAAVSOP87B_Neptune_R_DASH")]
        public static extern double Neptune_R_DASH(double JD);

    }

    public class AAVSOP87B_Saturn {
        private const string LibName = "caaplus";

        [DllImport(LibName, EntryPoint = "CAAVSOP87B_Saturn_L")]
        public static extern double Saturn_L(double JD);

        [DllImport(LibName, EntryPoint = "CAAVSOP87B_Saturn_L_DASH")]
        public static extern double Saturn_L_DASH(double JD);

        [DllImport(LibName, EntryPoint = "CAAVSOP87B_Saturn_B")]
        public static extern double Saturn_B(double JD);

        [DllImport(LibName, EntryPoint = "CAAVSOP87B_Saturn_B_DASH")]
        public static extern double Saturn_B_DASH(double JD);

        [DllImport(LibName, EntryPoint = "CAAVSOP87B_Saturn_R")]
        public static extern double Saturn_R(double JD);

        [DllImport(LibName, EntryPoint = "CAAVSOP87B_Saturn_R_DASH")]
        public static extern double Saturn_R_DASH(double JD);

    }

    public class AAVSOP87B_Uranus {
        private const string LibName = "caaplus";

        [DllImport(LibName, EntryPoint = "CAAVSOP87B_Uranus_L")]
        public static extern double Uranus_L(double JD);

        [DllImport(LibName, EntryPoint = "CAAVSOP87B_Uranus_L_DASH")]
        public static extern double Uranus_L_DASH(double JD);

        [DllImport(LibName, EntryPoint = "CAAVSOP87B_Uranus_B")]
        public static extern double Uranus_B(double JD);

        [DllImport(LibName, EntryPoint = "CAAVSOP87B_Uranus_B_DASH")]
        public static extern double Uranus_B_DASH(double JD);

        [DllImport(LibName, EntryPoint = "CAAVSOP87B_Uranus_R")]
        public static extern double Uranus_R(double JD);

        [DllImport(LibName, EntryPoint = "CAAVSOP87B_Uranus_R_DASH")]
        public static extern double Uranus_R_DASH(double JD);

    }

    public class AAVSOP87B_Venus {
        private const string LibName = "caaplus";

        [DllImport(LibName, EntryPoint = "CAAVSOP87B_Venus_L")]
        public static extern double Venus_L(double JD);

        [DllImport(LibName, EntryPoint = "CAAVSOP87B_Venus_L_DASH")]
        public static extern double Venus_L_DASH(double JD);

        [DllImport(LibName, EntryPoint = "CAAVSOP87B_Venus_B")]
        public static extern double Venus_B(double JD);

        [DllImport(LibName, EntryPoint = "CAAVSOP87B_Venus_B_DASH")]
        public static extern double Venus_B_DASH(double JD);

        [DllImport(LibName, EntryPoint = "CAAVSOP87B_Venus_R")]
        public static extern double Venus_R(double JD);

        [DllImport(LibName, EntryPoint = "CAAVSOP87B_Venus_R_DASH")]
        public static extern double Venus_R_DASH(double JD);

    }

    public class AAVSOP87C_Earth {
        private const string LibName = "caaplus";

        [DllImport(LibName, EntryPoint = "CAAVSOP87C_Earth_X")]
        public static extern double Earth_X(double JD);

        [DllImport(LibName, EntryPoint = "CAAVSOP87C_Earth_X_DASH")]
        public static extern double Earth_X_DASH(double JD);

        [DllImport(LibName, EntryPoint = "CAAVSOP87C_Earth_Y")]
        public static extern double Earth_Y(double JD);

        [DllImport(LibName, EntryPoint = "CAAVSOP87C_Earth_Y_DASH")]
        public static extern double Earth_Y_DASH(double JD);

        [DllImport(LibName, EntryPoint = "CAAVSOP87C_Earth_Z")]
        public static extern double Earth_Z(double JD);

        [DllImport(LibName, EntryPoint = "CAAVSOP87C_Earth_Z_DASH")]
        public static extern double Earth_Z_DASH(double JD);

    }

    public class AAVSOP87C_Jupiter {
        private const string LibName = "caaplus";

        [DllImport(LibName, EntryPoint = "CAAVSOP87C_Jupiter_X")]
        public static extern double Jupiter_X(double JD);

        [DllImport(LibName, EntryPoint = "CAAVSOP87C_Jupiter_X_DASH")]
        public static extern double Jupiter_X_DASH(double JD);

        [DllImport(LibName, EntryPoint = "CAAVSOP87C_Jupiter_Y")]
        public static extern double Jupiter_Y(double JD);

        [DllImport(LibName, EntryPoint = "CAAVSOP87C_Jupiter_Y_DASH")]
        public static extern double Jupiter_Y_DASH(double JD);

        [DllImport(LibName, EntryPoint = "CAAVSOP87C_Jupiter_Z")]
        public static extern double Jupiter_Z(double JD);

        [DllImport(LibName, EntryPoint = "CAAVSOP87C_Jupiter_Z_DASH")]
        public static extern double Jupiter_Z_DASH(double JD);

    }

    public class AAVSOP87C_Mars {
        private const string LibName = "caaplus";

        [DllImport(LibName, EntryPoint = "CAAVSOP87C_Mars_X")]
        public static extern double Mars_X(double JD);

        [DllImport(LibName, EntryPoint = "CAAVSOP87C_Mars_X_DASH")]
        public static extern double Mars_X_DASH(double JD);

        [DllImport(LibName, EntryPoint = "CAAVSOP87C_Mars_Y")]
        public static extern double Mars_Y(double JD);

        [DllImport(LibName, EntryPoint = "CAAVSOP87C_Mars_Y_DASH")]
        public static extern double Mars_Y_DASH(double JD);

        [DllImport(LibName, EntryPoint = "CAAVSOP87C_Mars_Z")]
        public static extern double Mars_Z(double JD);

        [DllImport(LibName, EntryPoint = "CAAVSOP87C_Mars_Z_DASH")]
        public static extern double Mars_Z_DASH(double JD);

    }

    public class AAVSOP87C_Mercury {
        private const string LibName = "caaplus";

        [DllImport(LibName, EntryPoint = "CAAVSOP87C_Mercury_X")]
        public static extern double Mercury_X(double JD);

        [DllImport(LibName, EntryPoint = "CAAVSOP87C_Mercury_X_DASH")]
        public static extern double Mercury_X_DASH(double JD);

        [DllImport(LibName, EntryPoint = "CAAVSOP87C_Mercury_Y")]
        public static extern double Mercury_Y(double JD);

        [DllImport(LibName, EntryPoint = "CAAVSOP87C_Mercury_Y_DASH")]
        public static extern double Mercury_Y_DASH(double JD);

        [DllImport(LibName, EntryPoint = "CAAVSOP87C_Mercury_Z")]
        public static extern double Mercury_Z(double JD);

        [DllImport(LibName, EntryPoint = "CAAVSOP87C_Mercury_Z_DASH")]
        public static extern double Mercury_Z_DASH(double JD);

    }

    public class AAVSOP87C_Neptune {
        private const string LibName = "caaplus";

        [DllImport(LibName, EntryPoint = "CAAVSOP87C_Neptune_X")]
        public static extern double Neptune_X(double JD);

        [DllImport(LibName, EntryPoint = "CAAVSOP87C_Neptune_X_DASH")]
        public static extern double Neptune_X_DASH(double JD);

        [DllImport(LibName, EntryPoint = "CAAVSOP87C_Neptune_Y")]
        public static extern double Neptune_Y(double JD);

        [DllImport(LibName, EntryPoint = "CAAVSOP87C_Neptune_Y_DASH")]
        public static extern double Neptune_Y_DASH(double JD);

        [DllImport(LibName, EntryPoint = "CAAVSOP87C_Neptune_Z")]
        public static extern double Neptune_Z(double JD);

        [DllImport(LibName, EntryPoint = "CAAVSOP87C_Neptune_Z_DASH")]
        public static extern double Neptune_Z_DASH(double JD);

    }

    public class AAVSOP87C_Saturn {
        private const string LibName = "caaplus";

        [DllImport(LibName, EntryPoint = "CAAVSOP87C_Saturn_X")]
        public static extern double Saturn_X(double JD);

        [DllImport(LibName, EntryPoint = "CAAVSOP87C_Saturn_X_DASH")]
        public static extern double Saturn_X_DASH(double JD);

        [DllImport(LibName, EntryPoint = "CAAVSOP87C_Saturn_Y")]
        public static extern double Saturn_Y(double JD);

        [DllImport(LibName, EntryPoint = "CAAVSOP87C_Saturn_Y_DASH")]
        public static extern double Saturn_Y_DASH(double JD);

        [DllImport(LibName, EntryPoint = "CAAVSOP87C_Saturn_Z")]
        public static extern double Saturn_Z(double JD);

        [DllImport(LibName, EntryPoint = "CAAVSOP87C_Saturn_Z_DASH")]
        public static extern double Saturn_Z_DASH(double JD);

    }

    public class AAVSOP87C_Uranus {
        private const string LibName = "caaplus";

        [DllImport(LibName, EntryPoint = "CAAVSOP87C_Uranus_X")]
        public static extern double Uranus_X(double JD);

        [DllImport(LibName, EntryPoint = "CAAVSOP87C_Uranus_X_DASH")]
        public static extern double Uranus_X_DASH(double JD);

        [DllImport(LibName, EntryPoint = "CAAVSOP87C_Uranus_Y")]
        public static extern double Uranus_Y(double JD);

        [DllImport(LibName, EntryPoint = "CAAVSOP87C_Uranus_Y_DASH")]
        public static extern double Uranus_Y_DASH(double JD);

        [DllImport(LibName, EntryPoint = "CAAVSOP87C_Uranus_Z")]
        public static extern double Uranus_Z(double JD);

        [DllImport(LibName, EntryPoint = "CAAVSOP87C_Uranus_Z_DASH")]
        public static extern double Uranus_Z_DASH(double JD);

    }

    public class AAVSOP87C_Venus {
        private const string LibName = "caaplus";

        [DllImport(LibName, EntryPoint = "CAAVSOP87C_Venus_X")]
        public static extern double Venus_X(double JD);

        [DllImport(LibName, EntryPoint = "CAAVSOP87C_Venus_X_DASH")]
        public static extern double Venus_X_DASH(double JD);

        [DllImport(LibName, EntryPoint = "CAAVSOP87C_Venus_Y")]
        public static extern double Venus_Y(double JD);

        [DllImport(LibName, EntryPoint = "CAAVSOP87C_Venus_Y_DASH")]
        public static extern double Venus_Y_DASH(double JD);

        [DllImport(LibName, EntryPoint = "CAAVSOP87C_Venus_Z")]
        public static extern double Venus_Z(double JD);

        [DllImport(LibName, EntryPoint = "CAAVSOP87C_Venus_Z_DASH")]
        public static extern double Venus_Z_DASH(double JD);

    }

    public class AAVSOP87D_Earth {
        private const string LibName = "caaplus";

        [DllImport(LibName, EntryPoint = "CAAVSOP87D_Earth_L")]
        public static extern double Earth_L(double JD);

        [DllImport(LibName, EntryPoint = "CAAVSOP87D_Earth_L_DASH")]
        public static extern double Earth_L_DASH(double JD);

        [DllImport(LibName, EntryPoint = "CAAVSOP87D_Earth_B")]
        public static extern double Earth_B(double JD);

        [DllImport(LibName, EntryPoint = "CAAVSOP87D_Earth_B_DASH")]
        public static extern double Earth_B_DASH(double JD);

        [DllImport(LibName, EntryPoint = "CAAVSOP87D_Earth_R")]
        public static extern double Earth_R(double JD);

        [DllImport(LibName, EntryPoint = "CAAVSOP87D_Earth_R_DASH")]
        public static extern double Earth_R_DASH(double JD);

    }

    public class AAVSOP87D_Jupiter {
        private const string LibName = "caaplus";

        [DllImport(LibName, EntryPoint = "CAAVSOP87D_Jupiter_L")]
        public static extern double Jupiter_L(double JD);

        [DllImport(LibName, EntryPoint = "CAAVSOP87D_Jupiter_L_DASH")]
        public static extern double Jupiter_L_DASH(double JD);

        [DllImport(LibName, EntryPoint = "CAAVSOP87D_Jupiter_B")]
        public static extern double Jupiter_B(double JD);

        [DllImport(LibName, EntryPoint = "CAAVSOP87D_Jupiter_B_DASH")]
        public static extern double Jupiter_B_DASH(double JD);

        [DllImport(LibName, EntryPoint = "CAAVSOP87D_Jupiter_R")]
        public static extern double Jupiter_R(double JD);

        [DllImport(LibName, EntryPoint = "CAAVSOP87D_Jupiter_R_DASH")]
        public static extern double Jupiter_R_DASH(double JD);

    }

    public class AAVSOP87D_Mars {
        private const string LibName = "caaplus";

        [DllImport(LibName, EntryPoint = "CAAVSOP87D_Mars_L")]
        public static extern double Mars_L(double JD);

        [DllImport(LibName, EntryPoint = "CAAVSOP87D_Mars_L_DASH")]
        public static extern double Mars_L_DASH(double JD);

        [DllImport(LibName, EntryPoint = "CAAVSOP87D_Mars_B")]
        public static extern double Mars_B(double JD);

        [DllImport(LibName, EntryPoint = "CAAVSOP87D_Mars_B_DASH")]
        public static extern double Mars_B_DASH(double JD);

        [DllImport(LibName, EntryPoint = "CAAVSOP87D_Mars_R")]
        public static extern double Mars_R(double JD);

        [DllImport(LibName, EntryPoint = "CAAVSOP87D_Mars_R_DASH")]
        public static extern double Mars_R_DASH(double JD);

    }

    public class AAVSOP87D_Mercury {
        private const string LibName = "caaplus";

        [DllImport(LibName, EntryPoint = "CAAVSOP87D_Mercury_L")]
        public static extern double Mercury_L(double JD);

        [DllImport(LibName, EntryPoint = "CAAVSOP87D_Mercury_L_DASH")]
        public static extern double Mercury_L_DASH(double JD);

        [DllImport(LibName, EntryPoint = "CAAVSOP87D_Mercury_B")]
        public static extern double Mercury_B(double JD);

        [DllImport(LibName, EntryPoint = "CAAVSOP87D_Mercury_B_DASH")]
        public static extern double Mercury_B_DASH(double JD);

        [DllImport(LibName, EntryPoint = "CAAVSOP87D_Mercury_R")]
        public static extern double Mercury_R(double JD);

        [DllImport(LibName, EntryPoint = "CAAVSOP87D_Mercury_R_DASH")]
        public static extern double Mercury_R_DASH(double JD);

    }

    public class AAVSOP87D_Neptune {
        private const string LibName = "caaplus";

        [DllImport(LibName, EntryPoint = "CAAVSOP87D_Neptune_L")]
        public static extern double Neptune_L(double JD);

        [DllImport(LibName, EntryPoint = "CAAVSOP87D_Neptune_L_DASH")]
        public static extern double Neptune_L_DASH(double JD);

        [DllImport(LibName, EntryPoint = "CAAVSOP87D_Neptune_B")]
        public static extern double Neptune_B(double JD);

        [DllImport(LibName, EntryPoint = "CAAVSOP87D_Neptune_B_DASH")]
        public static extern double Neptune_B_DASH(double JD);

        [DllImport(LibName, EntryPoint = "CAAVSOP87D_Neptune_R")]
        public static extern double Neptune_R(double JD);

        [DllImport(LibName, EntryPoint = "CAAVSOP87D_Neptune_R_DASH")]
        public static extern double Neptune_R_DASH(double JD);

    }

    public class AAVSOP87D_Saturn {
        private const string LibName = "caaplus";

        [DllImport(LibName, EntryPoint = "CAAVSOP87D_Saturn_L")]
        public static extern double Saturn_L(double JD);

        [DllImport(LibName, EntryPoint = "CAAVSOP87D_Saturn_L_DASH")]
        public static extern double Saturn_L_DASH(double JD);

        [DllImport(LibName, EntryPoint = "CAAVSOP87D_Saturn_B")]
        public static extern double Saturn_B(double JD);

        [DllImport(LibName, EntryPoint = "CAAVSOP87D_Saturn_B_DASH")]
        public static extern double Saturn_B_DASH(double JD);

        [DllImport(LibName, EntryPoint = "CAAVSOP87D_Saturn_R")]
        public static extern double Saturn_R(double JD);

        [DllImport(LibName, EntryPoint = "CAAVSOP87D_Saturn_R_DASH")]
        public static extern double Saturn_R_DASH(double JD);

    }

    public class AAVSOP87D_Uranus {
        private const string LibName = "caaplus";

        [DllImport(LibName, EntryPoint = "CAAVSOP87D_Uranus_L")]
        public static extern double Uranus_L(double JD);

        [DllImport(LibName, EntryPoint = "CAAVSOP87D_Uranus_L_DASH")]
        public static extern double Uranus_L_DASH(double JD);

        [DllImport(LibName, EntryPoint = "CAAVSOP87D_Uranus_B")]
        public static extern double Uranus_B(double JD);

        [DllImport(LibName, EntryPoint = "CAAVSOP87D_Uranus_B_DASH")]
        public static extern double Uranus_B_DASH(double JD);

        [DllImport(LibName, EntryPoint = "CAAVSOP87D_Uranus_R")]
        public static extern double Uranus_R(double JD);

        [DllImport(LibName, EntryPoint = "CAAVSOP87D_Uranus_R_DASH")]
        public static extern double Uranus_R_DASH(double JD);

    }

    public class AAVSOP87D_Venus {
        private const string LibName = "caaplus";

        [DllImport(LibName, EntryPoint = "CAAVSOP87D_Venus_L")]
        public static extern double Venus_L(double JD);

        [DllImport(LibName, EntryPoint = "CAAVSOP87D_Venus_L_DASH")]
        public static extern double Venus_L_DASH(double JD);

        [DllImport(LibName, EntryPoint = "CAAVSOP87D_Venus_B")]
        public static extern double Venus_B(double JD);

        [DllImport(LibName, EntryPoint = "CAAVSOP87D_Venus_B_DASH")]
        public static extern double Venus_B_DASH(double JD);

        [DllImport(LibName, EntryPoint = "CAAVSOP87D_Venus_R")]
        public static extern double Venus_R(double JD);

        [DllImport(LibName, EntryPoint = "CAAVSOP87D_Venus_R_DASH")]
        public static extern double Venus_R_DASH(double JD);

    }

    public class AAVSOP87E_Earth {
        private const string LibName = "caaplus";

        [DllImport(LibName, EntryPoint = "CAAVSOP87E_Earth_X")]
        public static extern double Earth_X(double JD);

        [DllImport(LibName, EntryPoint = "CAAVSOP87E_Earth_X_DASH")]
        public static extern double Earth_X_DASH(double JD);

        [DllImport(LibName, EntryPoint = "CAAVSOP87E_Earth_Y")]
        public static extern double Earth_Y(double JD);

        [DllImport(LibName, EntryPoint = "CAAVSOP87E_Earth_Y_DASH")]
        public static extern double Earth_Y_DASH(double JD);

        [DllImport(LibName, EntryPoint = "CAAVSOP87E_Earth_Z")]
        public static extern double Earth_Z(double JD);

        [DllImport(LibName, EntryPoint = "CAAVSOP87E_Earth_Z_DASH")]
        public static extern double Earth_Z_DASH(double JD);

    }

    public class AAVSOP87E_Jupiter {
        private const string LibName = "caaplus";

        [DllImport(LibName, EntryPoint = "CAAVSOP87E_Jupiter_X")]
        public static extern double Jupiter_X(double JD);

        [DllImport(LibName, EntryPoint = "CAAVSOP87E_Jupiter_X_DASH")]
        public static extern double Jupiter_X_DASH(double JD);

        [DllImport(LibName, EntryPoint = "CAAVSOP87E_Jupiter_Y")]
        public static extern double Jupiter_Y(double JD);

        [DllImport(LibName, EntryPoint = "CAAVSOP87E_Jupiter_Y_DASH")]
        public static extern double Jupiter_Y_DASH(double JD);

        [DllImport(LibName, EntryPoint = "CAAVSOP87E_Jupiter_Z")]
        public static extern double Jupiter_Z(double JD);

        [DllImport(LibName, EntryPoint = "CAAVSOP87E_Jupiter_Z_DASH")]
        public static extern double Jupiter_Z_DASH(double JD);

    }

    public class AAVSOP87E_Mars {
        private const string LibName = "caaplus";

        [DllImport(LibName, EntryPoint = "CAAVSOP87E_Mars_X")]
        public static extern double Mars_X(double JD);

        [DllImport(LibName, EntryPoint = "CAAVSOP87E_Mars_X_DASH")]
        public static extern double Mars_X_DASH(double JD);

        [DllImport(LibName, EntryPoint = "CAAVSOP87E_Mars_Y")]
        public static extern double Mars_Y(double JD);

        [DllImport(LibName, EntryPoint = "CAAVSOP87E_Mars_Y_DASH")]
        public static extern double Mars_Y_DASH(double JD);

        [DllImport(LibName, EntryPoint = "CAAVSOP87E_Mars_Z")]
        public static extern double Mars_Z(double JD);

        [DllImport(LibName, EntryPoint = "CAAVSOP87E_Mars_Z_DASH")]
        public static extern double Mars_Z_DASH(double JD);

    }

    public class AAVSOP87E_Mercury {
        private const string LibName = "caaplus";

        [DllImport(LibName, EntryPoint = "CAAVSOP87E_Mercury_X")]
        public static extern double Mercury_X(double JD);

        [DllImport(LibName, EntryPoint = "CAAVSOP87E_Mercury_X_DASH")]
        public static extern double Mercury_X_DASH(double JD);

        [DllImport(LibName, EntryPoint = "CAAVSOP87E_Mercury_Y")]
        public static extern double Mercury_Y(double JD);

        [DllImport(LibName, EntryPoint = "CAAVSOP87E_Mercury_Y_DASH")]
        public static extern double Mercury_Y_DASH(double JD);

        [DllImport(LibName, EntryPoint = "CAAVSOP87E_Mercury_Z")]
        public static extern double Mercury_Z(double JD);

        [DllImport(LibName, EntryPoint = "CAAVSOP87E_Mercury_Z_DASH")]
        public static extern double Mercury_Z_DASH(double JD);

    }

    public class AAVSOP87E_Neptune {
        private const string LibName = "caaplus";

        [DllImport(LibName, EntryPoint = "CAAVSOP87E_Neptune_X")]
        public static extern double Neptune_X(double JD);

        [DllImport(LibName, EntryPoint = "CAAVSOP87E_Neptune_X_DASH")]
        public static extern double Neptune_X_DASH(double JD);

        [DllImport(LibName, EntryPoint = "CAAVSOP87E_Neptune_Y")]
        public static extern double Neptune_Y(double JD);

        [DllImport(LibName, EntryPoint = "CAAVSOP87E_Neptune_Y_DASH")]
        public static extern double Neptune_Y_DASH(double JD);

        [DllImport(LibName, EntryPoint = "CAAVSOP87E_Neptune_Z")]
        public static extern double Neptune_Z(double JD);

        [DllImport(LibName, EntryPoint = "CAAVSOP87E_Neptune_Z_DASH")]
        public static extern double Neptune_Z_DASH(double JD);

    }

    public class AAVSOP87E_Saturn {
        private const string LibName = "caaplus";

        [DllImport(LibName, EntryPoint = "CAAVSOP87E_Saturn_X")]
        public static extern double Saturn_X(double JD);

        [DllImport(LibName, EntryPoint = "CAAVSOP87E_Saturn_X_DASH")]
        public static extern double Saturn_X_DASH(double JD);

        [DllImport(LibName, EntryPoint = "CAAVSOP87E_Saturn_Y")]
        public static extern double Saturn_Y(double JD);

        [DllImport(LibName, EntryPoint = "CAAVSOP87E_Saturn_Y_DASH")]
        public static extern double Saturn_Y_DASH(double JD);

        [DllImport(LibName, EntryPoint = "CAAVSOP87E_Saturn_Z")]
        public static extern double Saturn_Z(double JD);

        [DllImport(LibName, EntryPoint = "CAAVSOP87E_Saturn_Z_DASH")]
        public static extern double Saturn_Z_DASH(double JD);

    }

    public class AAVSOP87E_Sun {
        private const string LibName = "caaplus";

        [DllImport(LibName, EntryPoint = "CAAVSOP87E_Sun_X")]
        public static extern double Sun_X(double JD);

        [DllImport(LibName, EntryPoint = "CAAVSOP87E_Sun_X_DASH")]
        public static extern double Sun_X_DASH(double JD);

        [DllImport(LibName, EntryPoint = "CAAVSOP87E_Sun_Y")]
        public static extern double Sun_Y(double JD);

        [DllImport(LibName, EntryPoint = "CAAVSOP87E_Sun_Y_DASH")]
        public static extern double Sun_Y_DASH(double JD);

        [DllImport(LibName, EntryPoint = "CAAVSOP87E_Sun_Z")]
        public static extern double Sun_Z(double JD);

        [DllImport(LibName, EntryPoint = "CAAVSOP87E_Sun_Z_DASH")]
        public static extern double Sun_Z_DASH(double JD);

    }

    public class AAVSOP87E_Uranus {
        private const string LibName = "caaplus";

        [DllImport(LibName, EntryPoint = "CAAVSOP87E_Uranus_X")]
        public static extern double Uranus_X(double JD);

        [DllImport(LibName, EntryPoint = "CAAVSOP87E_Uranus_X_DASH")]
        public static extern double Uranus_X_DASH(double JD);

        [DllImport(LibName, EntryPoint = "CAAVSOP87E_Uranus_Y")]
        public static extern double Uranus_Y(double JD);

        [DllImport(LibName, EntryPoint = "CAAVSOP87E_Uranus_Y_DASH")]
        public static extern double Uranus_Y_DASH(double JD);

        [DllImport(LibName, EntryPoint = "CAAVSOP87E_Uranus_Z")]
        public static extern double Uranus_Z(double JD);

        [DllImport(LibName, EntryPoint = "CAAVSOP87E_Uranus_Z_DASH")]
        public static extern double Uranus_Z_DASH(double JD);

    }

    public class AAVSOP87E_Venus {
        private const string LibName = "caaplus";

        [DllImport(LibName, EntryPoint = "CAAVSOP87E_Venus_X")]
        public static extern double Venus_X(double JD);

        [DllImport(LibName, EntryPoint = "CAAVSOP87E_Venus_X_DASH")]
        public static extern double Venus_X_DASH(double JD);

        [DllImport(LibName, EntryPoint = "CAAVSOP87E_Venus_Y")]
        public static extern double Venus_Y(double JD);

        [DllImport(LibName, EntryPoint = "CAAVSOP87E_Venus_Y_DASH")]
        public static extern double Venus_Y_DASH(double JD);

        [DllImport(LibName, EntryPoint = "CAAVSOP87E_Venus_Z")]
        public static extern double Venus_Z(double JD);

        [DllImport(LibName, EntryPoint = "CAAVSOP87E_Venus_Z_DASH")]
        public static extern double Venus_Z_DASH(double JD);

    }

    public class AAVSOP87_EMB {
        private const string LibName = "caaplus";

        [DllImport(LibName, EntryPoint = "CAAVSOP87_EMB_A")]
        public static extern double EMB_A(double JD);

        [DllImport(LibName, EntryPoint = "CAAVSOP87_EMB_L")]
        public static extern double EMB_L(double JD);

        [DllImport(LibName, EntryPoint = "CAAVSOP87_EMB_K")]
        public static extern double EMB_K(double JD);

        [DllImport(LibName, EntryPoint = "CAAVSOP87_EMB_H")]
        public static extern double EMB_H(double JD);

        [DllImport(LibName, EntryPoint = "CAAVSOP87_EMB_Q")]
        public static extern double EMB_Q(double JD);

        [DllImport(LibName, EntryPoint = "CAAVSOP87_EMB_P")]
        public static extern double EMB_P(double JD);

    }

    public class AAVSOP87_Jupiter {
        private const string LibName = "caaplus";

        [DllImport(LibName, EntryPoint = "CAAVSOP87_Jupiter_A")]
        public static extern double Jupiter_A(double JD);

        [DllImport(LibName, EntryPoint = "CAAVSOP87_Jupiter_L")]
        public static extern double Jupiter_L(double JD);

        [DllImport(LibName, EntryPoint = "CAAVSOP87_Jupiter_K")]
        public static extern double Jupiter_K(double JD);

        [DllImport(LibName, EntryPoint = "CAAVSOP87_Jupiter_H")]
        public static extern double Jupiter_H(double JD);

        [DllImport(LibName, EntryPoint = "CAAVSOP87_Jupiter_Q")]
        public static extern double Jupiter_Q(double JD);

        [DllImport(LibName, EntryPoint = "CAAVSOP87_Jupiter_P")]
        public static extern double Jupiter_P(double JD);

    }

    public class AAVSOP87_Mars {
        private const string LibName = "caaplus";

        [DllImport(LibName, EntryPoint = "CAAVSOP87_Mars_A")]
        public static extern double Mars_A(double JD);

        [DllImport(LibName, EntryPoint = "CAAVSOP87_Mars_L")]
        public static extern double Mars_L(double JD);

        [DllImport(LibName, EntryPoint = "CAAVSOP87_Mars_K")]
        public static extern double Mars_K(double JD);

        [DllImport(LibName, EntryPoint = "CAAVSOP87_Mars_H")]
        public static extern double Mars_H(double JD);

        [DllImport(LibName, EntryPoint = "CAAVSOP87_Mars_Q")]
        public static extern double Mars_Q(double JD);

        [DllImport(LibName, EntryPoint = "CAAVSOP87_Mars_P")]
        public static extern double Mars_P(double JD);

    }

    public class AAVSOP87_Mercury {
        private const string LibName = "caaplus";

        [DllImport(LibName, EntryPoint = "CAAVSOP87_Mercury_A")]
        public static extern double Mercury_A(double JD);

        [DllImport(LibName, EntryPoint = "CAAVSOP87_Mercury_L")]
        public static extern double Mercury_L(double JD);

        [DllImport(LibName, EntryPoint = "CAAVSOP87_Mercury_K")]
        public static extern double Mercury_K(double JD);

        [DllImport(LibName, EntryPoint = "CAAVSOP87_Mercury_H")]
        public static extern double Mercury_H(double JD);

        [DllImport(LibName, EntryPoint = "CAAVSOP87_Mercury_Q")]
        public static extern double Mercury_Q(double JD);

        [DllImport(LibName, EntryPoint = "CAAVSOP87_Mercury_P")]
        public static extern double Mercury_P(double JD);

    }

    public class AAVSOP87_Neptune {
        private const string LibName = "caaplus";

        [DllImport(LibName, EntryPoint = "CAAVSOP87_Neptune_A")]
        public static extern double Neptune_A(double JD);

        [DllImport(LibName, EntryPoint = "CAAVSOP87_Neptune_L")]
        public static extern double Neptune_L(double JD);

        [DllImport(LibName, EntryPoint = "CAAVSOP87_Neptune_K")]
        public static extern double Neptune_K(double JD);

        [DllImport(LibName, EntryPoint = "CAAVSOP87_Neptune_H")]
        public static extern double Neptune_H(double JD);

        [DllImport(LibName, EntryPoint = "CAAVSOP87_Neptune_Q")]
        public static extern double Neptune_Q(double JD);

        [DllImport(LibName, EntryPoint = "CAAVSOP87_Neptune_P")]
        public static extern double Neptune_P(double JD);

    }

    public class AAVSOP87_Saturn {
        private const string LibName = "caaplus";

        [DllImport(LibName, EntryPoint = "CAAVSOP87_Saturn_A")]
        public static extern double Saturn_A(double JD);

        [DllImport(LibName, EntryPoint = "CAAVSOP87_Saturn_L")]
        public static extern double Saturn_L(double JD);

        [DllImport(LibName, EntryPoint = "CAAVSOP87_Saturn_K")]
        public static extern double Saturn_K(double JD);

        [DllImport(LibName, EntryPoint = "CAAVSOP87_Saturn_H")]
        public static extern double Saturn_H(double JD);

        [DllImport(LibName, EntryPoint = "CAAVSOP87_Saturn_Q")]
        public static extern double Saturn_Q(double JD);

        [DllImport(LibName, EntryPoint = "CAAVSOP87_Saturn_P")]
        public static extern double Saturn_P(double JD);

    }

    public class AAVSOP87_Uranus {
        private const string LibName = "caaplus";

        [DllImport(LibName, EntryPoint = "CAAVSOP87_Uranus_A")]
        public static extern double Uranus_A(double JD);

        [DllImport(LibName, EntryPoint = "CAAVSOP87_Uranus_L")]
        public static extern double Uranus_L(double JD);

        [DllImport(LibName, EntryPoint = "CAAVSOP87_Uranus_K")]
        public static extern double Uranus_K(double JD);

        [DllImport(LibName, EntryPoint = "CAAVSOP87_Uranus_H")]
        public static extern double Uranus_H(double JD);

        [DllImport(LibName, EntryPoint = "CAAVSOP87_Uranus_Q")]
        public static extern double Uranus_Q(double JD);

        [DllImport(LibName, EntryPoint = "CAAVSOP87_Uranus_P")]
        public static extern double Uranus_P(double JD);

    }

    public class AAVSOP87_Venus {
        private const string LibName = "caaplus";

        [DllImport(LibName, EntryPoint = "CAAVSOP87_Venus_A")]
        public static extern double Venus_A(double JD);

        [DllImport(LibName, EntryPoint = "CAAVSOP87_Venus_L")]
        public static extern double Venus_L(double JD);

        [DllImport(LibName, EntryPoint = "CAAVSOP87_Venus_K")]
        public static extern double Venus_K(double JD);

        [DllImport(LibName, EntryPoint = "CAAVSOP87_Venus_H")]
        public static extern double Venus_H(double JD);

        [DllImport(LibName, EntryPoint = "CAAVSOP87_Venus_Q")]
        public static extern double Venus_Q(double JD);

        [DllImport(LibName, EntryPoint = "CAAVSOP87_Venus_P")]
        public static extern double Venus_P(double JD);

    }

}
