/*
Module : AASaturn.cpp
Purpose: Implementation for the algorithms which obtain the heliocentric position of Saturn
Created: PJN / 29-12-2003
History: PJN / 31-05-2004 1) In CAASaturn::EclipticLongitude the g_L5SaturnCoefficients[] were 
                          not included. Thanks to Brian Orme for reporting this problem.
                          2) In CAASaturn::EclipticLatitude the g_B5SaturnCoefficients[] were
                          not included. Thanks to Brian Orme for reporting this problem.
                          3) In CAASaturn::RadiusVector the g_R5SaturnCoefficients[] were not 
                          included. Thanks to Brian Orme for reporting this problem.
         PJN / 18-03-2012 1. All global "g_*" tables are now const. Thanks to Roger Dahl for reporting this 
                          issue when compiling AA+ on ARM.
         PJN / 04-08-2013 1. Fixed a transcription error in the twenty ninth coefficient used to calculate 
                          the B2 term for the ecliptic latitude of Saturn. Thanks to Isaac Clark for 
                          reporting this issue. Spot tests indicate that this change only affected the 
                          ecliptic latitude in the twelfth decimal place.
                          2. Updated copyright details
         PJN / 16-09-2015 1. CAASaturn::EclipticLongitude, EclipticLatitude & RadiusVector now include a
                          "bool bHighPrecision" parameter which if set to true means the code uses the full
                          VSOP87 theory rather than the truncated theory as presented in Meeus's book.
         PJN / 01-08-2017 1. Fixed up alignment of lookup tables in AASaturn.cpp module
         PJN / 18-08-2019 1. Fixed some further compiler warnings when using VC 2019 Preview v16.3.0 Preview 2.0
         PJN / 13-04-2020 1. Reworked C arrays to use std::array
         PJN / 07-07-2022 1. Updated all the code in AASaturn.cpp to use C++ uniform initialization for all
                          variable declarations.

Copyright (c) 2003 - 2025 by PJ Naughter (Web: www.naughter.com, Email: pjna@naughter.com)

All rights reserved.

Copyright / Usage Details:

You are allowed to include the source code in any product (commercial, shareware, freeware or otherwise) 
when your product is released in binary form. You are allowed to modify the source code in any way you want 
except you cannot modify the copyright details at the top of each module. If you want to distribute source 
code with your application, then you are only allowed to distribute versions released by the author. This is 
to maintain a single distribution point for the source code.

*/


//////////////////// Includes /////////////////////////////////////////////////

#include "stdafx.h"
#include "AASaturn.h"
#include "AACoordinateTransformation.h"
#ifndef AAPLUS_NO_VSOP87
#include "AAVSOP87D_SAT.h"
#endif //#ifndef AAPLUS_NO_VSOP87
#include <cmath>
#include <array>


//////////////////// Macros / Defines /////////////////////////////////////////

#ifdef _MSC_VER
#pragma warning(disable : 26446 26482 26485)
#endif //#ifdef _MSC_VER

struct VSOP87Coefficient
{
  double A;
  double B;
  double C;
};

constexpr std::array<VSOP87Coefficient, 90> g_L0SaturnCoefficients
{ {
  { 87401354, 0,          0            },
  { 11107660, 3.96205090, 213.29909544 },
  { 1414151,  4.5858152,  7.1135470    },
  { 398379,   0.521120,   206.185548   },
  { 350769,   3.303299,   426.598191   },
  { 206816,   0.246584,   103.092774   },
  { 79271,    3.84007,    220.41264    },
  { 23990,    4.66977,    110.20632    },
  { 16574,    0.43719,    419.48464    },
  { 15820,    0.93809,    632.78374    },
  { 15054,    2.71670,    639.89729    },
  { 14907,    5.76903,    316.39187    },
  { 14610,    1.56519,    3.93215      },
  { 13160,    4.44891,    14.22709     },
  { 13005,    5.98119,    11.04570     },
  { 10725,    3.12940,    202.25340    },
  { 6126,     1.7633,     277.0350     },
  { 5863,     0.2366,     529.6910     },
  { 5228,     4.2078,     3.1814       },
  { 5020,     3.1779,     433.7117     },
  { 4593,     0.6198,     199.0720     },
  { 4006,     2.2448,     63.7359      },
  { 3874,     3.2228,     138.5175     },
  { 3269,     0.7749,     949.1756     },
  { 2954,     0.9828,     95.9792      },
  { 2461,     2.0316,     735.8765     },
  { 1758,     3.2658,     522.5774     },
  { 1640,     5.5050,     846.0828     },
  { 1581,     4.3727,     309.2783     },
  { 1391,     4.0233,     323.5054     },
  { 1124,     2.8373,     415.5525     },
  { 1087,     4.1834,     2.4477       },
  { 1017,     3.7170,     227.5262     },
  { 957,      0.507,      1265.567     },
  { 853,      3.421,      175.166      },
  { 849,      3.191,      209.367      },
  { 789,      5.007,      0.963        },
  { 749,      2.144,      853.196      },
  { 744,      5.253,      224.345      },
  { 687,      1.747,      1052.268     },
  { 654,      1.599,      0.048        },
  { 634,      2.299,      412.371      },
  { 625,      0.970,      210.118      },
  { 580,      3.093,      74.782       },
  { 546,      2.127,      350.332      },
  { 543,      1.518,      9.561        },
  { 530,      4.449,      117.320      },
  { 478,      2.965,      137.033      },
  { 474,      5.475,      742.990      },
  { 452,      1.044,      490.334      },
  { 449,      1.290,      127.472      },
  { 372,      2.278,      217.231      },
  { 355,      3.013,      838.969      },
  { 347,      1.539,      340.771      },
  { 343,      0.246,      0.521        },
  { 330,      0.247,      1581.959     },
  { 322,      0.961,      203.738      },
  { 322,      2.572,      647.011      },
  { 309,      3.495,      216.480      },
  { 287,      2.370,      351.817      },
  { 278,      0.400,      211.815      },
  { 249,      1.470,      1368.660     },
  { 227,      4.910,      12.530       },
  { 220,      4.204,      200.769      },
  { 209,      1.345,      625.670      },
  { 208,      0.483,      1162.475     },
  { 208,      1.283,      39.357       },
  { 204,      6.011,      265.989      },
  { 185,      3.503,      149.563      },
  { 184,      0.973,      4.193        },
  { 182,      5.491,      2.921        },
  { 174,      1.863,      0.751        },
  { 165,      0.440,      5.417        },
  { 149,      5.736,      52.690       },
  { 148,      1.535,      5.629        },
  { 146,      6.231,      195.140      },
  { 140,      4.295,      21.341       },
  { 131,      4.068,      10.295       },
  { 125,      6.277,      1898.351     },
  { 122,      1.976,      4.666        },
  { 118,      5.341,      554.070      },
  { 117,      2.679,      1155.361     },
  { 114,      5.594,      1059.382     },
  { 112,      1.105,      191.208      },
  { 110,      0.166,      1.484        },
  { 109,      3.438,      536.805      },
  { 107,      4.012,      956.289      },
  { 104,      2.192,      88.866       },
  { 103,      1.197,      1685.052     },
  { 101,      4.965,      269.921      }
} };

constexpr std::array<VSOP87Coefficient, 79> g_L1SaturnCoefficients
{ {
  { 21354295596.0, 0,         0           },
  { 1296855,       1.8282054, 213.2990954 },
  { 564348,        2.885001,  7.113547    },
  { 107679,        2.277699,  206.185548  },
  { 98323,         1.08070,   426.59819   },
  { 40255,         2.04128,   220.41264   },
  { 19942,         1.27955,   103.09277   },
  { 10512,         2.74880,   14.22709    },
  { 6939,          0.4049,    639.8973    },
  { 4803,          2.4419,    419.4846    },
  { 4056,          2.9217,    110.2063    },
  { 3769,          3.6497,    3.9322      },
  { 3385,          2.4169,    3.1814      },
  { 3302,          1.2626,    433.7117    },
  { 3071,          2.3274,    199.0720    },
  { 1953,          3.5639,    11.0457     },
  { 1249,          2.6280,    95.9792     },
  { 922,           1.961,     227.526     },
  { 706,           4.417,     529.691     },
  { 650,           6.174,     202.253     },
  { 628,           6.111,     309.278     },
  { 487,           6.040,     853.196     },
  { 479,           4.988,     522.577     },
  { 468,           4.617,     63.736      },
  { 417,           2.117,     323.505     },
  { 408,           1.299,     209.367     },
  { 352,           2.317,     632.784     },
  { 344,           3.959,     412.371     },
  { 340,           3.634,     316.392     },
  { 336,           3.772,     735.877     },
  { 332,           2.861,     210.118     },
  { 289,           2.733,     117.320     },
  { 281,           5.744,     2.448       },
  { 266,           0.543,     647.011     },
  { 230,           1.644,     216.480     },
  { 192,           2.965,     224.345     },
  { 173,           4.077,     846.083     },
  { 167,           2.597,     21.341      },
  { 136,           2.286,     10.295      },
  { 131,           3.441,     742.990     },
  { 128,           4.095,     217.231     },
  { 109,           6.161,     415.552     },
  { 98,            4.73,      838.97      },
  { 94,            3.48,      1052.27     },
  { 92,            3.95,      88.87       },
  { 87,            1.22,      440.83      },
  { 83,            3.11,      625.67      },
  { 78,            6.24,      302.16      },
  { 67,            0.29,      4.67        },
  { 66,            5.65,      9.56        },
  { 62,            4.29,      127.47      },
  { 62,            1.83,      195.14      },
  { 58,            2.48,      191.96      },
  { 57,            5.02,      137.03      },
  { 55,            0.28,      74.78       },
  { 54,            5.13,      490.33      },
  { 51,            1.46,      536.80      },
  { 47,            1.18,      149.56      },
  { 47,            5.15,      515.46      },
  { 46,            2.23,      956.29      },
  { 44,            2.71,      5.42        },
  { 40,            0.41,      269.92      },
  { 40,            3.89,      728.76      },
  { 38,            0.65,      422.67      },
  { 38,            2.53,      12.53       },
  { 37,            3.78,      2.92        },
  { 35,            6.08,      5.63        },
  { 34,            3.21,      1368.66     },
  { 33,            4.64,      277.03      },
  { 33,            5.43,      1066.50     },
  { 33,            0.30,      351.82      },
  { 32,            4.39,      1155.36     },
  { 31,            2.43,      52.69       },
  { 30,            2.84,      203.00      },
  { 30,            6.19,      284.15      },
  { 30,            3.39,      1059.38     },
  { 29,            2.03,      330.62      },
  { 28,            2.74,      265.99      },
  { 26,            4.51,      340.77      }
} };

constexpr std::array<VSOP87Coefficient, 63> g_L2SaturnCoefficients
{ {
  { 116441, 1.179879, 7.113547  },
  { 91921,  0.07425,  213.29910 },
  { 90592,  0,	      0         },
  { 15277,  4.06492,  206.18555 },
  { 10631,  0.25778,  220.41264 },
  { 10605,  5.40964,  426.59819 },
  { 4265,   1.0460,   14.2271   },
  { 1216,   2.9186,   103.0928  },
  { 1165,   4.6094,   639.8973  },
  { 1082,   5.6913,   433.7117  },
  { 1045,   4.0421,   199.0720  },
  { 1020,   0.6337,   3.1814    },
  { 634,    4.388,    419.485   },
  { 549,    5.573,    3.932     },
  { 457,    1.268,    110.206   },
  { 425,    0.209,    227.526   },
  { 274,    4.288,    95.979    },
  { 162,    1.381,    11.046    },
  { 129,    1.566,    309.278   },
  { 117,    3.881,    853.196   },
  { 105,    4.900,    647.011   },
  { 101,    0.893,    21.341    },
  { 96,     2.91,     316.39    },
  { 95,     5.63,     412.37    },
  { 85,     5.73,     209.37    },
  { 83,     6.05,     216.48    },
  { 82,     1.02,     117.32    },
  { 75,     4.76,     210.12    },
  { 67,     0.46,     522.58    },
  { 66,     0.48,     10.29     },
  { 64,     0.35,     323.51    },
  { 61,     4.88,     632.78    },
  { 53,     2.75,     529.69    },
  { 46,     5.69,     440.83    },
  { 45,     1.67,     202.25    },
  { 42,     5.71,     88.87     },
  { 32,     0.07,     63.74     },
  { 32,     1.67,     302.16    },
  { 31,     4.16,     191.96    },
  { 27,     0.83,     224.34    },
  { 25,     5.66,     735.88    },
  { 20,     5.94,     217.23    },
  { 18,     4.90,     625.67    },
  { 17,     1.63,     742.99    },
  { 16,     0.58,     515.46    },
  { 14,     0.21,     838.97    },
  { 14,     3.76,     195.14    },
  { 12,     4.72,     203.00    },
  { 12,     0.13,     234.64    },
  { 12,     3.12,     846.08    },
  { 11,     5.92,     536.80    },
  { 11,     5.60,     728.76    },
  { 11,     3.20,     1066.50   },
  { 10,     4.99,     422.67    },
  { 10,     0.26,     330.62    },
  { 10,     4.15,     860.31    },
  { 9,      0.46,     956.29    },
  { 8,      2.14,     269.92    },
  { 8,      5.25,     429.78    },
  { 8,      4.03,     9.56      },
  { 7,      5.40,     1052.27   },
  { 6,      4.46,     284.15    },
  { 6,      5.93,     405.26    }
} };

constexpr std::array<VSOP87Coefficient, 48> g_L3SaturnCoefficients
{ {
  { 16039, 5.73945, 7.11355  },
  { 4250,  4.5854,  213.2991 },
  { 1907,  4.7608,  220.4126 },
  { 1466,  5.9133,  206.1855 },
  { 1162,  5.6197,  14.2271  },
  { 1067,  3.6082,  426.5982 },
  { 239,   3.861,   433.712  },
  { 237,   5.768,   199.072  },
  { 166,   5.116,   3.181    },
  { 151,   2.736,   639.897  },
  { 131,   4.743,   227.526  },
  { 63,    0.23,    419.48   },
  { 62,    4.74,    103.09   },
  { 40,    5.47,    21.34    },
  { 40,    5.96,    95.98    },
  { 39,    5.83,    110.21   },
  { 28,    3.01,    647.01   },
  { 25,    0.99,    3.93     },
  { 19,    1.92,    853.20   },
  { 18,    4.97,    10.29    },
  { 18,    1.03,    412.37   },
  { 18,    4.20,    216.48   },
  { 18,    3.32,    309.28   },
  { 16,    3.90,    440.83   },
  { 16,    5.62,    117.32   },
  { 13,    1.18,    88.87    },
  { 11,    5.58,    11.05    },
  { 11,    5.93,    191.96   },
  { 10,    3.95,    209.37   },
  { 9,     3.39,    302.16   },
  { 8,     4.88,    323.51   },
  { 7,     0.38,    632.78   },
  { 6,     2.25,    522.58   },
  { 6,     1.06,    210.12   },
  { 5,     4.64,    234.64   },
  { 4,     3.14,    0        },
  { 4,     2.31,    515.46   },
  { 3,     2.20,    860.31   },
  { 3,     0.59,    529.69   },
  { 3,     4.93,    224.34   },
  { 3,     0.42,    625.67   },
  { 2,     4.77,    330.62   },
  { 2,     3.35,    429.78   },
  { 2,     3.20,    202.25   },
  { 2,     1.19,    1066.50  },
  { 2,     1.35,    405.26   },
  { 2,     4.16,    223.59   },
  { 2,     3.07,    654.12   }
} };

constexpr std::array<VSOP87Coefficient, 27> g_L4SaturnCoefficients
{ {
  { 1662, 3.9983, 7.1135  },
  { 257,  2.984,  220.413 },
  { 236,  3.902,  14.227  },
  { 149,  2.741,  213.299 },
  { 114,  3.142,  0       },
  { 110,  1.515,  206.186 },
  { 68,   1.72,   426.60  },
  { 40,   2.05,   433.71  },
  { 38,   1.24,   199.07  },
  { 31,   3.01,   227.53  },
  { 15,   0.83,   639.90  },
  { 9,    3.71,   21.34   },
  { 6,    2.42,   419.48  },
  { 6,    1.16,   647.01  },
  { 4,    1.45,   95.98   },
  { 4,    2.12,   440.83  },
  { 3,    4.09,   110.21  },
  { 3,    2.77,   412.37  },
  { 3,    3.01,   88.87   },
  { 3,    0.00,   853.20  },
  { 3,    0.39,   103.09  },
  { 2,    3.78,   117.32  },
  { 2,    2.83,   234.64  },
  { 2,    5.08,   309.28  },
  { 2,    2.24,   216.48  },
  { 2,    5.19,   302.16  },
  { 1,    1.55,   191.96  }
} };

constexpr std::array<VSOP87Coefficient, 12> g_L5SaturnCoefficients
{ {
  { 124, 2.259, 7.114  },
  { 34,  2.16,  14.23  },
  { 28,  1.20,  220.41 },
  { 6,   1.22,  227.53 },
  { 5,   0.24,  433.71 },
  { 4,   6.23,  426.60 },
  { 3,   2.97,  199.07 },
  { 3,   4.29,  206.19 },
  { 2,   6.25,  213.30 },
  { 1,   5.28,  639.90 },
  { 1,   0.24,  440.83 },
  { 1,   3.14,  0      }
} };

constexpr std::array<VSOP87Coefficient, 34> g_B0SaturnCoefficients
{ {
  { 4330678, 3.6028443, 213.2990954 },
  { 240348,  2.852385,  426.598191  },
  { 84746,   0,         0           },
  { 34116,   0.57297,   206.18555   },
  { 30863,   3.48442,   220.41264   },
  { 14734,   2.11847,   639.89729   },
  { 9917,    5.7900,    419.4846    },
  { 6994,    4.7360,    7.1135      },
  { 4808,    5.4331,    316.3919    },
  { 4788,    4.9651,    110.2063    },
  { 3432,    2.7326,    433.7117    },
  { 1506,    6.0130,    103.0928    },
  { 1060,    5.6310,    529.6910    },
  { 969,     5.204,     632.784     },
  { 942,     1.396,     853.196     },
  { 708,     3.803,     323.505     },
  { 552,     5.131,     202.253     },
  { 400,     3.359,     227.526     },
  { 319,     3.626,     209.367     },
  { 316,     1.997,     647.011     },
  { 314,     0.465,     217.231     },
  { 284,     4.886,     224.345     },
  { 236,     2.139,     11.046      },
  { 215,     5.950,     846.083     },
  { 209,     2.120,     415.552     },
  { 207,     0.730,     199.072     },
  { 179,     2.954,     63.736      },
  { 141,     0.644,     490.334     },
  { 139,     4.595,     14.227      },
  { 139,     1.998,     735.877     },
  { 135,     5.245,     742.990     },
  { 122,     3.115,     522.577     },
  { 116,     3.109,     216.480     },
  { 114,     0.963,     210.118     }
} };

constexpr std::array<VSOP87Coefficient, 32> g_B1SaturnCoefficients
{ {
  { 397555, 5.332900, 213.299095 },
  { 49479,  3.14159,  0          },
  { 18572,  6.09919,  426.59819  },
  { 14801,  2.30586,  206.18555  },
  { 9644,   1.6967,   220.4126   },
  { 3757,   1.2543,   419.4846   },
  { 2717,   5.9117,   639.8973   },
  { 1455,   0.8516,   433.7117   },
  { 1291,   2.9177,   7.1135     },
  { 853,    0.436,    316.392    },
  { 298,    0.919,    632.784    },
  { 292,    5.316,    853.196    },
  { 284,    1.619,    227.526    },
  { 275,    3.889,    103.093    },
  { 172,    0.052,    647.011    },
  { 166,    2.444,    199.072    },
  { 158,    5.209,    110.206    },
  { 128,    1.207,    529.691    },
  { 110,    2.457,    217.231    },
  { 82,     2.76,     210.12     },
  { 81,     2.86,     14.23      },
  { 69,     1.66,     202.25     },
  { 65,     1.26,     216.48     },
  { 61,     1.25,     209.37     },
  { 59,     1.82,     323.51     },
  { 46,     0.82,     440.83     },
  { 36,     1.82,     224.34     },
  { 34,     2.84,     117.32     },
  { 33,     1.31,     412.37     },
  { 32,     1.19,     846.08     },
  { 27,     4.65,     1066.50    },
  { 27,     4.44,     11.05      }
} };

constexpr std::array<VSOP87Coefficient, 29> g_B2SaturnCoefficients
{ {
  { 20630, 0.50482, 213.29910 },
  { 3720,  3.9983,  206.1855  },
  { 1627,  6.1819,  220.4126  },
  { 1346,  0,       0         },
  { 706,   3.039,   419.485   },
  { 365,   5.099,   426.598   },
  { 330,   5.279,   433.712   },
  { 219,   3.828,   639.897   },
  { 139,   1.043,   7.114     },
  { 104,   6.157,   227.526   },
  { 93,    1.98,    316.39    },
  { 71,    4.15,    199.07    },
  { 52,    2.88,    632.78    },
  { 49,    4.43,    647.01    },
  { 41,    3.16,    853.20    },
  { 29,    4.53,    210.12    },
  { 24,    1.12,    14.23     },
  { 21,    4.35,    217.23    },
  { 20,    5.31,    440.83    },
  { 18,    0.85,    110.21    },
  { 17,    5.68,    216.48    },
  { 16,    4.26,    103.09    },
  { 14,    3.00,    412.37    },
  { 12,    2.53,    529.69    },
  { 8,     3.32,    202.25    },
  { 7,     5.56,    209.37    },
  { 7,     0.29,    323.51    },
  { 6,     1.16,    117.32    },
  { 6,     3.61,    860.31    }
} };

constexpr std::array<VSOP87Coefficient, 21> g_B3SaturnCoefficients
{ {
  { 666, 1.990, 213.299 },
  { 632, 5.698, 206.186 },
  { 398, 0,     0       },
  { 188, 4.338, 220.413 },
  { 92,  4.84,  419.48  },
  { 52,  3.42,  433.71  },
  { 42,  2.38,  426.60  },
  { 26,  4.40,  227.53  },
  { 21,  5.85,  199.07  },
  { 18,  1.99,  639.90  },
  { 11,  5.37,  7.11    },
  { 10,  2.55,  647.01  },
  { 7,   3.46,  316.39  },
  { 6,   4.80,  632.78  },
  { 6,   0.02,  210.12  },
  { 6,   3.52,  440.83  },
  { 5,   5.64,  14.23   },
  { 5,   1.22,  853.20  },
  { 4,   4.71,  412.37  },
  { 3,   0.63,  103.09  },
  { 2,   3.72,  216.48  }
} };

constexpr std::array<VSOP87Coefficient, 12> g_B4SaturnCoefficients
{ {
  { 80, 1.12, 206.19 },
  { 32, 3.12, 213.30 },
  { 17, 2.48, 220.41 },
  { 12, 3.14, 0      },
  { 9,  0.38, 419.48 },
  { 6,  1.56, 433.71 },
  { 5,  2.63, 227.53 },
  { 5,  1.28, 199.07 },
  { 1,  1.43, 426.60 },
  { 1,  0.67, 647.01 },
  { 1,  1.72, 440.83 },
  { 1,  6.18, 639.90 }
} };

constexpr std::array<VSOP87Coefficient, 2> g_B5SaturnCoefficients
{ {
  { 8, 2.82, 206.19 },
  { 1, 0.51, 220.41 }
} };

constexpr std::array<VSOP87Coefficient, 44> g_R0SaturnCoefficients
{ {
  { 955758136, 0,          0            },
  { 52921382,  2.39226220, 213.29909544 },
  { 1873680,   5.2354961,  206.1855484  },
  { 1464664,   1.6476305,  426.5981909  },
  { 821891,    5.935200,   316.391870   },
  { 547507,    5.015326,   103.092774   },
  { 371684,    2.271148,   220.412642   },
  { 361778,    3.139043,   7.113547     },
  { 140618,    5.704067,   632.783739   },
  { 108975,    3.293136,   110.206321   },
  { 69007,     5.94100,    419.48464    },
  { 61053,     0.94038,    639.89729    },
  { 48913,     1.55733,    202.25340    },
  { 34144,     0.19519,    277.03499    },
  { 32402,     5.47085,    949.17561    },
  { 20937,     0.46349,    735.87651    },
  { 20839,     1.52103,    433.71174    },
  { 20747,     5.33256,    199.07200    },
  { 15298,     3.05944,    529.69097    },
  { 14296,     2.60434,    323.50542    },
  { 12884,     1.64892,    138.51750    },
  { 11993,     5.98051,    846.08283    },
  { 11380,     1.73106,    522.57742    },
  { 9796,      5.2048,     1265.5675    },
  { 7753,      5.8519,     95.9792      },
  { 6771,      3.0043,     14.2271      },
  { 6466,      0.1773,     1052.2684    },
  { 5850,      1.4552,     415.5525     },
  { 5307,      0.5974,     63.7359      },
  { 4696,      2.1492,     227.5262     },
  { 4044,      1.6401,     209.3669     },
  { 3688,      0.7802,     412.3711     },
  { 3461,      1.8509,     175.1661     },
  { 3420,      4.9455,     1581.9593    },
  { 3401,      0.5539,     350.3321     },
  { 3376,      3.6953,     224.3448     },
  { 2976,      5.6847,     210.1177     },
  { 2885,      1.3876,     838.9693     },
  { 2881,      0.1796,     853.1964     },
  { 2508,      3.5385,     742.9901     },
  { 2448,      6.1841,     1368.6603    },
  { 2406,      2.9656,     117.3199     },
  { 2174,      0.0151,     340.7709     },
  { 2024,      5.0541,     11.0457      }
} };

constexpr std::array<VSOP87Coefficient, 38> g_R1SaturnCoefficients
{ {
  { 6182981, 0.2584352, 213.2990954 },
  { 506578,  0.711147,  206.185548  },
  { 341394,  5.796358,  426.598191  },
  { 188491,  0.472157,  220.412642  },
  { 186262,  3.141593,  0           },
  { 143891,  1.407449,  7.113547    },
  { 49621,   6.01744,   103.09277   },
  { 20928,   5.09246,   639.89729   },
  { 19953,   1.17560,   419.48464   },
  { 18840,   1.60820,   110.20632   },
  { 13877,   0.75886,   199.07200   },
  { 12893,   5.94330,   433.71174   },
  { 5397,    1.2885,    14.2271     },
  { 4869,    0.8679,    323.5054    },
  { 4247,    0.3930,    227.5262    },
  { 3252,    1.2585,    95.9792     },
  { 3081,    3.4366,    522.5774    },
  { 2909,    4.6068,    202.2534    },
  { 2856,    2.1673,    735.8765    },
  { 1988,    2.4505,    412.3711    },
  { 1941,    6.0239,    209.3669    },
  { 1581,    1.2919,    210.1177    },
  { 1340,    4.3080,    853.1964    },
  { 1316,    1.2530,    117.3199    },
  { 1203,    1.8665,    316.3919    },
  { 1091,    0.0753,    216.4805    },
  { 966,     0.480,     632.784     },
  { 954,     5.152,     647.011     },
  { 898,     0.983,     529.691     },
  { 882,     1.885,     1052.268    },
  { 874,     1.402,     224.345     },
  { 785,     3.064,     838.969     },
  { 740,     1.382,     625.670     },
  { 658,     4.144,     309.278     },
  { 650,     1.725,     742.990     },
  { 613,     3.033,     63.736      },
  { 599,     2.549,     217.231     },
  { 503,     2.130,     3.932       }
} };

constexpr std::array<VSOP87Coefficient, 32> g_R2SaturnCoefficients
{ {
  { 436902, 4.786717, 213.299095 },
  { 71923,  2.50070,  206.18555  },
  { 49767,  4.97168,  220.41264  },
  { 43221,  3.86940,  426.59819  },
  { 29646,  5.96310,  7.11355    },
  { 4721,   2.4753,   199.0720   },
  { 4142,   4.1067,   433.7117   },
  { 3789,   3.0977,   639.8973   },
  { 2964,   1.3721,   103.0928   },
  { 2556,   2.8507,   419.4846   },
  { 2327,   0,	      0          },
  { 2208,   6.2759,   110.2063   },
  { 2188,   5.8555,   14.2271    },
  { 1957,   4.9245,   227.5262   },
  { 924,    5.464,    323.505    },
  { 706,    2.971,    95.979     },
  { 546,    4.129,    412.371    },
  { 431,    5.178,    522.577    },
  { 405,    4.173,    209.367    },
  { 391,    4.481,    216.480    },
  { 374,    5.834,    117.320    },
  { 361,    3.277,    647.011    },
  { 356,    3.192,    210.118    },
  { 326,    2.269,    853.196    },
  { 207,    4.022,    735.877    },
  { 204,    0.088,    202.253    },
  { 180,    3.597,    632.784    },
  { 178,    4.097,    440.825    },
  { 154,    3.135,    625.670    },
  { 148,    0.136,    302.165    },
  { 133,    2.594,    191.958    },
  { 132,    5.933,    309.278    }
} };

constexpr std::array<VSOP87Coefficient, 28> g_R3SaturnCoefficients
{ {
  { 20315, 3.02187, 213.29910 },
  { 8924,  3.1914,  220.4126  },
  { 6909,  4.3517,  206.1855  },
  { 4087,  4.2241,  7.1135    },
  { 3879,  2.0106,  426.5982  },
  { 1071,  4.2036,  199.0720  },
  { 907,   2.283,   433.712   },
  { 606,   3.175,   227.526   },
  { 597,   4.135,   14.227    },
  { 483,   1.173,   639.897   },
  { 393,   0,       0         },
  { 229,   4.698,   419.485   },
  { 188,   4.590,   110.206   },
  { 150,   3.202,   103.093   },
  { 121,   3.768,   323.505   },
  { 102,   4.710,   95.979    },
  { 101,   5.819,   412.371   },
  { 93,    1.44,    647.01    },
  { 84,    2.63,    216.48    },
  { 73,    4.15,    117.32    },
  { 62,    2.31,    440.83    },
  { 55,    0.31,    853.20    },
  { 50,    2.39,    209.37    },
  { 45,    4.37,    191.96    },
  { 41,    0.69,    522.58    },
  { 40,    1.84,    302.16    },
  { 38,    5.94,    88.87     },
  { 32,    4.01,    21.34     }
} };

constexpr std::array<VSOP87Coefficient, 23> g_R4SaturnCoefficients
{ {
  { 1202, 1.4150, 220.4126 },
  { 708,  1.162,  213.299  },
  { 516,  6.240,  206.186  },
  { 427,  2.469,  7.114    },
  { 268,  0.187,  426.598  },
  { 170,  5.959,  199.072  },
  { 150,  0.480,  433.712  },
  { 145,  1.442,  227.526  },
  { 121,  2.405,  14.227   },
  { 47,   5.57,   639.90   },
  { 19,   5.86,   647.01   },
  { 17,   0.53,   440.83   },
  { 16,   2.90,   110.21   },
  { 15,   0.30,   419.48   },
  { 14,   1.30,   412.37   },
  { 13,   2.09,   323.51   },
  { 11,   0.22,   95.98    },
  { 11,   2.46,   117.32   },
  { 10,   3.14,   0        },
  { 9,    1.56,   88.87    },
  { 9,    2.28,   21.34    },
  { 9,    0.68,   216.48   },
  { 8,    1.27,   234.64   }
} };

constexpr std::array<VSOP87Coefficient, 18> g_R5SaturnCoefficients
{ {
  { 129, 5.913, 220.413 },
  { 32,  0.69,  7.11    },
  { 27,  5.91,  227.53  },
  { 20,  4.95,  433.71  },
  { 20,  0.67,  14.23   },
  { 14,  2.67,  206.19  },
  { 14,  1.46,  199.07  },
  { 13,  4.59,  426.60  },
  { 7,   4.63,  213.30  },
  { 5,   3.61,  639.90  },
  { 4,   4.90,  440.83  },
  { 3,   4.07,  647.01  },
  { 3,   4.66,  191.96  },
  { 3,   0.49,  323.51  },
  { 3,   3.18,  419.48  },
  { 2,   3.70,  88.87   },
  { 2,   3.32,  95.98   },
  { 2,   0.56,  117.32  }
} };


//////////////////// Implementation ///////////////////////////////////////////

double CAASaturn::EclipticLongitude(double JD, bool bHighPrecision) noexcept
{
#ifndef AAPLUS_NO_VSOP87
  if (bHighPrecision)
    return CAACoordinateTransformation::MapTo0To360Range(CAACoordinateTransformation::RadiansToDegrees(CAAVSOP87D_Saturn::L(JD)));
#else
  UNREFERENCED_PARAMETER(bHighPrecision);
#endif //#ifndef AAPLUS_NO_VSOP87

  const double rho{(JD - 2451545)/365250};
  const double rhosquared{rho*rho};
  const double rhocubed{rhosquared*rho};
  const double rho4{rhocubed*rho};
  const double rho5{rho4*rho};

  //Calculate L0
  double L0{0};
  for (const auto& L0Coefficient : g_L0SaturnCoefficients)
    L0 += (L0Coefficient.A*cos(L0Coefficient.B + (L0Coefficient.C*rho)));

  //Calculate L1
  double L1{0};
  for (const auto& L1Coefficient : g_L1SaturnCoefficients)
    L1 += (L1Coefficient.A*cos(L1Coefficient.B + (L1Coefficient.C*rho)));

  //Calculate L2
  double L2{0};
  for (const auto& L2Coefficient : g_L2SaturnCoefficients)
    L2 += (L2Coefficient.A*cos(L2Coefficient.B + (L2Coefficient.C*rho)));

  //Calculate L3
  double L3{0};
  for (const auto& L3Coefficient : g_L3SaturnCoefficients)
    L3 += (L3Coefficient.A*cos(L3Coefficient.B + (L3Coefficient.C*rho)));

  //Calculate L4
  double L4{0};
  for (const auto& L4Coefficient : g_L4SaturnCoefficients)
    L4 += (L4Coefficient.A*cos(L4Coefficient.B + (L4Coefficient.C*rho)));

  //Calculate L5
  double L5{0};
  for (const auto& L5Coefficient : g_L5SaturnCoefficients)
    L5 += (L5Coefficient.A*cos(L5Coefficient.B + (L5Coefficient.C*rho)));

  double value{(L0 + (L1*rho) + (L2*rhosquared) + (L3*rhocubed) + (L4*rho4) + (L5*rho5))/100000000};

  //convert results back to degrees
  value = CAACoordinateTransformation::MapTo0To360Range(CAACoordinateTransformation::RadiansToDegrees(value));
  return value;
}

double CAASaturn::EclipticLatitude(double JD, bool bHighPrecision) noexcept
{
#ifndef AAPLUS_NO_VSOP87
  if (bHighPrecision)
    return CAACoordinateTransformation::MapToMinus90To90Range(CAACoordinateTransformation::RadiansToDegrees(CAAVSOP87D_Saturn::B(JD)));
#else
  UNREFERENCED_PARAMETER(bHighPrecision);
#endif //#ifndef AAPLUS_NO_VSOP87

  const double rho{(JD - 2451545)/365250};
  const double rhosquared{rho*rho};
  const double rhocubed{rhosquared*rho};
  const double rho4{rhocubed*rho};
  const double rho5{rho4*rho};

  //Calculate B0
  double B0{0};
  for (const auto& B0Coefficient : g_B0SaturnCoefficients)
    B0 += (B0Coefficient.A*cos(B0Coefficient.B + (B0Coefficient.C*rho)));

  //Calculate B1
  double B1{0};
  for (const auto& B1Coefficient : g_B1SaturnCoefficients)
    B1 += (B1Coefficient.A*cos(B1Coefficient.B + (B1Coefficient.C*rho)));

  //Calculate B2
  double B2{0};
  for (const auto& B2Coefficient : g_B2SaturnCoefficients)
    B2 += (B2Coefficient.A*cos(B2Coefficient.B + (B2Coefficient.C*rho)));

  //Calculate B3
  double B3{0};
  for (const auto& B3Coefficient : g_B3SaturnCoefficients)
    B3 += (B3Coefficient.A*cos(B3Coefficient.B + (B3Coefficient.C*rho)));

  //Calculate B4
  double B4{0};
  for (const auto& B4Coefficient : g_B4SaturnCoefficients)
    B4 += (B4Coefficient.A*cos(B4Coefficient.B + (B4Coefficient.C*rho)));

  //Calculate B5
  double B5{0};
  for (const auto& B5Coefficient : g_B5SaturnCoefficients)
    B5 += (B5Coefficient.A*cos(B5Coefficient.B + (B5Coefficient.C*rho)));

  double value{(B0 + (B1*rho) + (B2*rhosquared) + (B3*rhocubed) + (B4*rho4) + (B5*rho5))/100000000};

  //convert results back to degrees
  value = CAACoordinateTransformation::MapToMinus90To90Range(CAACoordinateTransformation::RadiansToDegrees(value));
  return value;
}

double CAASaturn::RadiusVector(double JD, bool bHighPrecision) noexcept
{
#ifndef AAPLUS_NO_VSOP87
  if (bHighPrecision)
    return CAAVSOP87D_Saturn::R(JD);
#else
  UNREFERENCED_PARAMETER(bHighPrecision);
#endif //#ifndef AAPLUS_NO_VSOP87

  const double rho{(JD - 2451545)/365250};
  const double rhosquared{rho*rho};
  const double rhocubed{rhosquared*rho};
  const double rho4{rhocubed*rho};
  const double rho5{rho4*rho};

  //Calculate R0
  double R0{0};
  for (const auto& R0Coefficient : g_R0SaturnCoefficients)
    R0 += (R0Coefficient.A*cos(R0Coefficient.B + (R0Coefficient.C*rho)));

  //Calculate R1
  double R1{0};
  for (const auto& R1Coefficient : g_R1SaturnCoefficients)
    R1 += (R1Coefficient.A*cos(R1Coefficient.B + (R1Coefficient.C*rho)));

  //Calculate R2
  double R2{0};
  for (const auto& R2Coefficient : g_R2SaturnCoefficients)
    R2 += (R2Coefficient.A*cos(R2Coefficient.B + (R2Coefficient.C*rho)));

  //Calculate R3
  double R3{0};
  for (const auto& R3Coefficient : g_R3SaturnCoefficients)
    R3 += (R3Coefficient.A*cos(R3Coefficient.B + (R3Coefficient.C*rho)));

  //Calculate R4
  double R4{0};
  for (const auto& R4Coefficient : g_R4SaturnCoefficients)
    R4 += (R4Coefficient.A*cos(R4Coefficient.B + (R4Coefficient.C*rho)));

  //Calculate R5
  double R5{0};
  for (const auto& R5Coefficient : g_R5SaturnCoefficients)
    R5 += (R5Coefficient.A*cos(R5Coefficient.B + (R5Coefficient.C*rho)));

  return (R0 + (R1*rho) + (R2*rhosquared) + (R3*rhocubed) + (R4*rho4) + (R5*rho5))/100000000;
}
