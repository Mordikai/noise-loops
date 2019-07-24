// Can confirm, perlin works just fine. Now to get the module working...

#include "perlin.h"
#include <stdlib.h>
#include <stdio.h>
#include <math.h>

int main(int argc, char const *argv[])
{
	double input = (double)atof(argv[1]);
	for (double x = 0; x < input; x += 0.1)
	{
		for (double y = 0; y < input; y += 0.1)
		{
			for (double z = 0; z < input; z += 0.1)
		    {
				for (double w = 0; w < input; w += 0.1)
		    	{
		    		double n = noise(x, y, z, w);
		    		int nfloor;
		    		if(n<0){
		    			nfloor = (int)(n*(-75.0));
		    			for (int i=0; i<(75-nfloor); ++i)
			    			printf(" ");
			    	}
		    		else
		    		{
		    			for (int i=0; i<75; ++i)
			    			printf(" ");
			    		nfloor = (int)(n*75.0);
			    	}
			    	for (int i=0; i<nfloor; ++i)
			    			printf("#");
			    	printf("\n");
		    	}
		    }
		}
	}
	
	return 0;
}