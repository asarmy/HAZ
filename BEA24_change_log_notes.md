# Changes made by Jeff B on 19 Jan 2024

## 1) gc2.f: made Global_T and Global_U passed out.  
- haz_main2.f: include Global_T and Global_U in call to GC2 subroutine 

> DONE

- cldist.f: CalcDist subroutine list of arguments

> DONE

- cldist.f: CalcDist add Global_T and Global_U to declarations passed out

> DONE; also added to CalcDist and Directivity subroutine calls in `01_HAZ_MAIN2.f`

> A note on `cldist.f`: new subroutines (new relative to `14_CLDIST.f`) appear not to be used in 
> Jeff B files nor the other HAZ files, so they are not moved over: CalcPlaneDist, CalcPlaneDist2

- Note, T and U have origin at the first along strike coordinate of the rupture surface trace, that 
  Global_U is converted to Bea23 U (origin at hypocenter loc) in the directivity.f sub as described 
  below. 

> Global_U and Global_T are part of internal calculations in GC2, so we only need to pass them out

## 2) haz_main2.f: include Global_T, Global_U in the call to Directivity subroutine
- added an if statement for dirflag equal to 40 or 41 (the Bea23 dirflags). Requires M>=6 and T>=0.1
- This uses 100 along strike hypocenters and just 1 down dip since Bea23 does not change with 
  hypocenter depth.
- For other dirflags the code is unchanged.
- Note, as Bea23 is only for strike-slip ruptures, the fault file directivity flag should be used to 
  identify which faults to apply the model. In the future, we can add to the above if statement so 
  that only SS ruptures use the directivity model.

> DONE

> A note on `haz_main2.f`: `TVZ_DIST` block isn't in `01_HAZ_MAIN2.f`, so it is not moved over.

## 3) declare1.h: add Global_T and Global_U 
	
> DONE

## 4) Directivity.f: can replace with new file.  Changes include:
- add Global_T, Global_U in the arguments

> DONE

- add Global_T, Global_U to 'real' declarations, plus others: U, T, Smax1, Smax2, Version

> DONE

- add dirflag .eq. 40 and dirflag .eq. 41 to CheckDir

> DONE

- added a whole new block of code for dirflag=40,41 (Bea23 model). includes call to ruptdirct2023 
  subroutine.
  
> DONE except it is `ruptdirct2024`; it is in `directivity_bea24.f`

- Note, this implementation is inefficent because it repeats the fG calculation for every period (it 
  is period independent). In a future update of Haz this can be cleaned up. 

## 5) directivity_bea24.f 
- This subroutine calculates the median and variability adjustment for the 2023 model. Use it with 
  dirflag=40 or 41
	
> DONE (included in src directory)

> Note that previous minimum period was 0.5, changed to 0.1 for BEA24.

> Note that other 2013 vintage Bayless models (31, 32; FN and FP) in `Directivity.f` were not added 
> to `16_Directivity.f`.

> Call to `interp` replaced with `S24_interp`

## 6) add directivity_bea24.f and directivity_bea24.o to makefile

> DONE (happens automatically with `cmake .. -G "MSYS Makefiles"`)
