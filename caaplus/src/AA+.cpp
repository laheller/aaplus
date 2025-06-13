/*
Module : AAA+.cpp
Purpose: Implementation for the CAAPlus class
Created: PJN / 08-05-2025
History: PJN / 08-05-2025 1. Initial creation of the new class. Thanks to Armando DiCianno for prompting
                          this update.

Copyright (c) 2025 by PJ Naughter (Web: www.naughter.com, Email: pjna@naughter.com)

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

#ifdef CWRAPPER
#include "CWrapper.h"
#else
#include "AA+.h"
#endif

//////////////////// Implementation ///////////////////////////////////////////

const char* CAAPlus::Version() noexcept
{
  return AAPLUS_VERSION;
}

int CAAPlus::VersionNumber() noexcept
{
  return AAPLUS_VERSION_NUMBER;
}
