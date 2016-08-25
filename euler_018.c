#include <math.h>
#include <omp.h>
#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>

double walltime(double *t0);

int tri[120] = {75, 95, 64, 17, 47, 82, 18, 35, 87, 10, 20, 4, 82, 47, 65, 19, 1, 23, 75, 3, 34, 88, 2, 77, 73, 7, 63, 67, 99, 65, 4, 28, 6, 16, 70, 92, 41, 41, 26, 56, 83, 40, 80, 70, 33, 41, 48, 72, 33, 47, 32, 37, 16, 94, 29, 53, 71, 44, 65, 25, 43, 91, 52, 97, 51, 14, 70, 11, 33, 28, 77, 73, 17, 78, 39, 68, 17, 57, 91, 71, 52, 38, 17, 14, 91, 43, 58, 50, 27, 29, 48, 63, 66, 4, 68, 89, 53, 67, 30, 73, 16, 69, 87, 40, 31, 4, 62, 98, 27, 23, 9, 70, 98, 73, 93, 38, 53, 60, 4, 23}; 

int main (int argc, char *argv[]) 
{
    int ii,jj,tid,index,nthreads;

    double sum,
           max,
           start,
           elapsed,
           nroutes,
           zero=0;

    start = walltime(&zero);

    long int route, nroute;

    #pragma omp parallel private(ii,jj,sum,max,tid,index,route,nroute) \
                         share(nthreads,nroutes)
    {
        tid = omp_get_thread_num();
        if (tid == 0) {
            nthreads = omp_get_num_threads();
            nroutes = (2^14) / nthreads;
        }

        route = tid*nroutes;
        nroute = (long)(nroutes+1);

        for (ii=0; ii<nroute; ii++) {
            index = 0;
            sum = 0;
            for (jj=0; jj<15; jj++) {
                sum += tri[index];
                index += 1 + jj + (int)(((bool)route)[jj]);
            }
            if (sum>max)
                max=sum;
            route++;
        }
        print("thread %d max %d\n",tid,max);
    }

    elapsed = walltime(&start);

    printf("Calculation took %f seconds\n",elapsed);

    return EXIT_SUCCESS;
}

