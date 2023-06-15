/* This is a plugin for surge that optionally forbids
   adjacent oxygen atoms. */

#define HELPTEXT2 \
" This version forbids adjacent oxygen atoms if -Y is given.\nAnd removes molecules with K(2,3).\n"


#define SURGEPLUGIN_STEP0 \
 { int ii,jj; \
   for (jj = n; --jj >= 1; ) \
   for (ii = jj; --ii >= 0; ) \
       if (POPCOUNT(g[ii] & g[jj]) >= 3) return 1; }\


static _Boolean Yswitch = FALSE;
#define SURGEPLUGIN_SWITCHES  SWBOOLEAN('Y',Yswitch)

static int oxygenindex = -1;
#define SURGEPLUGIN_STEP2 \
 if (oxygenindex < 0) oxygenindex = elementindex("O"); \
 if (Yswitch) { int ii; for (ii = 0; ii < ne; ++ii) \
   if (vcol[edge[ii].x] == oxygenindex \
    && vcol[edge[ii].y] == oxygenindex) return; }
