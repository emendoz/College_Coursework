/* program to time several sorting algorithms on data sets of various sizes
 */

#include <stdio.h>
#include <stdlib.h>   // for malloc, free
#include <time.h>     // for time
#include <stdbool.h>

/**********************************************************************
* Name: Erika Garnica Mendoza                                         *
* Assignment name: Comparison of Sorts                                *
* Assignment for March 16th, 2022                                     *
***********************************************************************/

/* *****************************************************************************************************************************************
* Academic honesty certification:                                                                                                          *
*   Written/online sources used:                                                                                                           *
*     - Program sort-comparisons.c by Henry m Walker from CS 415 Lab                                                                       * 
*     - CS415 Insertion Sort Reading (https://blue.cs.sonoma.edu/~hwalker/courses/415-sonoma.sp22/readings/reading-insertion-sort.php)     *          
*     - CS415 Quicksort Reading      (https://blue.cs.sonoma.edu/~hwalker/courses/415-sonoma.sp22/readings/reading-quicksort.php)          *
*     - CS415 Lecture for March 14 on more efficient code styles                                                                           *
*     - Merge sort: (https://www.geeksforgeeks.org/merge-sort/)                                                                            *
*     - Heap sort: (https://www.geeksforgeeks.org/heap-sort/)                                                                              *
*     [include textbook(s), CS 415 labs or readings;                                                                                       *
*       complete citations for Web or other written sources]                                                                               *
*   Help obtained                                                                                                                          *
*     [indicate names of instructor, class mentors                                                                                         *
*      or evening tutors, consulted according to class policy;                                                                             *
*      write "none" if none of these sources used]                                                                                         *
*   My signature below confirms that the above list of sources                                                                             *
*   is complete AND that I have not talked to anyone else                                                                                  *
*   (e.g., CSC 415 students) about the solution to this problem                                                                            *
*                                                                                                                                          *
*   Signature: Erika Garnica Mendoza                                                                                                       *
*******************************************************************************************************************************************/


/* Straight Selection sort */
void straightSelection (int a [ ], int n) {
   int i, j, smallIndex;
   int temp;
   // put largest remaining element in a[i]
   for (i = n-1; i >= 0; i--) {
      // find largest in a[i..n-1]
      smallIndex = i;
      for (j = i-1; j >= 0; j--) {
         if (a[smallIndex] < a[j])
            smallIndex = j;
     }
     // swap smallest to a[i]
     temp = a[smallIndex];
     a[smallIndex] = a[i];
     a[i] = temp;
   }
}

/* Insertion sort */
void insertionSort (int a [], int n) {
   for (int i = 1; i < n; i++) {
      int item = a[i];
      int j = i-1;
      while ((j >= 0) && a[j] > item){
         a[j+1] = a[j];
         j--;
      }
      a[j+1] = item;
   }
}

/* Insertion sort */
void insertionSort (int a [], int n) {
   for (int i = 1; i < n; i++) {
      int item = a[i];
      int j = i-1;
      while ((j >= 0) && a[j] > item){
         a[j+1] = a[j];
         j--;
      }
      a[j+1] = item;
   }
}

void merge(int arr[], int l, int m, int r)
{
    int i, j, k;
    int n1 = m - l + 1;
    int n2 = r - m;
  
    /* create temp arrays */
    int L[n1], R[n2];
  
    /* Copy data to temp arrays L[] and R[] */
    for (i = 0; i < n1; i++)
        L[i] = arr[l + i];
    for (j = 0; j < n2; j++)
        R[j] = arr[m + 1 + j];
  
    /* Merge the temp arrays back into arr[l..r]*/
    i = 0; // Initial index of first subarray
    j = 0; // Initial index of second subarray
    k = l; // Initial index of merged subarray
    while (i < n1 && j < n2) {
        if (L[i] <= R[j]) {
            arr[k] = L[i];
            i++;
        }
        else {
            arr[k] = R[j];
            j++;
        }
        k++;
    }
  
    /* Copy the remaining elements of L[], if there
    are any */
    while (i < n1) {
        arr[k] = L[i];
        i++;
        k++;
    }
  
    /* Copy the remaining elements of R[], if there
    are any */
    while (j < n2) {
        arr[k] = R[j];
        j++;
        k++;
    }
}

/* Merge sort */
void mergeSort(int arr[], int l, int r)
{
    if (l < r) {
        // Same as (l+r)/2, but avoids overflow for
        // large l and h
        int m = l + (r - l) / 2;
  
        // Sort first and second halves
        mergeSort(arr, l, m);
        mergeSort(arr, m + 1, r);
  
        merge(arr, l, m, r);
    }
}

// To heapify a subtree rooted with node i which is
// an index in arr[]. n is size of heap
void heapify(int a [], int n, int i)
{
  int largest = i; // Initialize largest as root
  int l = 2 * i + 1; // left = 2*i + 1
  int r = 2 * i + 2; // right = 2*i + 2

  // If left child is larger than root
  if (l < n && a[l] > a[largest])
      largest = l;

  // If right child is larger than largest so far
  if (r < n && a[r] > a[largest])
      largest = r;

  // If largest is not root
  if (largest != i) {
      int temp = a[i];
      a[i] = a[largest];
      a[largest] = temp;

      // Recursively heapify the affected sub-tree
      heapify(a, n, largest);
  }
}

/* Heap sort */
void heapSort(int a [], int n) {

  // Build heap (rearrange array)
  for (int i = n / 2 - 1; i >= 0; i--)
      heapify(a, n, i);

  // One by one extract an element from heap
  for (int i = n - 1; i > 0; i--) {
      // Move current root to end
      int temp = a[0];
      a[0] = a[i];
      a[i] = temp;

      // call max heapify on the reduced heap
      heapify(a, i, 0);
  }
}

/* Quicksort Helper */
void quicksortHelper (int a [], int first, int last) {
    int left = first + 1;
    int right = last;
    int temp;

    while (right >= left) {
        // search left to find small array item
        while ((right >= left) && (a[first] <= a[right]))
            right--;
        // search right to find large array item
        while ((right >= left) && (a[first] >= a[left]))
            left++;
        // swap large left item and small right item, if needed
        if (right > left) {
            temp = a[left];
            a[left] = a[right];
            a[right] = temp;
        }
    }
    // put a[first] in its place
    temp = a[first];
    a[first] = a[right];
    a[right] = temp;

    // recursively apply algorithm to a[first]..a[right-1] 
    // and a[right+1]..a[last], provided these segments contain >= 2 items
    if (first < right-1)
        quicksortHelper (a, first, right-1);
    if (right+1 < last)
        quicksortHelper (a, right+1, last);   
}

/* Quicksort */
void quicksort (int a [], int n) {
   // method to sort using the quicksort
   quicksortHelper (a, 0, n-1);
}

/* Version 1: Standard Partition, swapping only as needed */
int partition (int a [], int left, int right) {
   int pivot = a[left];
   int leftSpot = left + 1;
   int rightSpot = right;
   int temp;

   while(leftSpot <= rightSpot) {
      while( (leftSpot <= rightSpot) && (a[rightSpot] >= pivot))
         rightSpot--;
      while( (leftSpot <= rightSpot) && (a[leftSpot] <= pivot))
         leftSpot++;
      
      // if misplaced small and large values found, swap them
      if(leftSpot < rightSpot) {
         temp = a[leftSpot];
         a[leftSpot] = a[rightSpot];
         a[rightSpot] = temp;
         leftSpot++;
         rightSpot--;
      }
   }

   // swap a[left] with the biggest small value
   temp = a[left];
   a[left] = a[rightSpot];
   a[rightSpot] = temp;
   return rightSpot;
}

void IMPquicksortHelper(int a [], int left, int right) {
   // check base case
   if(left >= right) {
      return;
   }

   int pivot = partition(a, left, right);

   // elements less than pivot
   quicksortHelper(a, left, pivot);

   // elements of a larger value than pivot
   quicksortHelper(a, pivot + 1, right);
}

/* IMP Quicksort */
void quicksortIMP (int a [], int n) {
   IMPquicksortHelper(a, 0, n - 1);
}

/* driver program for testing and timing sorting algorithms
 */
int main ( ) {
  // print headings
  printf ("               Data Set                   Times\n");
  printf ("Algorithm        Size     Ascending Order   Random Order  Descending Order\n");

  int size;
  for (size = 10000; size <= 160000; size *= 2) {
      // create control data set arrays
     int * asc = (int *) malloc (size * sizeof(int));   //array with ascending data
     int * ran = (int *) malloc (size * sizeof(int));   //array with random data
     int * des = (int *) malloc (size * sizeof(int));   // array with descending data
     
     int i;
     for (i = 0; i < size; i++) {
        asc[i] = 2*i;
        ran[i] = rand();
        des[i] = 2*(size - i - 1); 
     } 

     // timing variables
     clock_t start_time, end_time;
     double elapsed_time;

     // copy to test arrays
     int * tempAsc = malloc (size * sizeof(int));
     int * tempRan = malloc (size * sizeof(int));
     int * tempDes = malloc (size * sizeof(int));

      // Resetting temp arrays back to normal
     for (i = 0; i < size; i++) {
        tempAsc[i] = asc[i];
        tempRan[i] = ran[i];
        tempDes[i] = des[i];
     }
 
     // timing for straight selection sort
     printf ("Selection sort %7d", size);
     // ascending data
     start_time = clock ();
     straightSelection (tempAsc, size);
     end_time = clock();
     elapsed_time = (end_time - start_time) / (double) CLOCKS_PER_SEC;
     printf ("%14.1lf", elapsed_time);

     // random data
     start_time = clock ();
     straightSelection (tempRan, size);
     end_time = clock();
     elapsed_time = (end_time - start_time) / (double) CLOCKS_PER_SEC;
     printf ("%15.1lf", elapsed_time);
     
     // descending data
     start_time = clock ();
     straightSelection (tempDes, size);
     end_time = clock();
     elapsed_time = (end_time - start_time) / (double) CLOCKS_PER_SEC;
     printf ("%15.1lf", elapsed_time);

     printf ("\n");

      // Resetting temp arrays back to normal
     for (i = 0; i < size; i++) {
        tempAsc[i] = asc[i];
        tempRan[i] = ran[i];
        tempDes[i] = des[i];
     }

     // timing for Insertion sort
     printf ("Insertion sort %7d", size);
     // ascending data
     start_time = clock ();
     insertionSort (tempAsc, size);
     end_time = clock();
     elapsed_time = (end_time - start_time) / (double) CLOCKS_PER_SEC;
     printf ("%14.1lf", elapsed_time);

     // random data
     start_time = clock ();
     insertionSort (tempRan, size);
     end_time = clock();
     elapsed_time = (end_time - start_time) / (double) CLOCKS_PER_SEC;
     printf ("%15.1lf", elapsed_time);
     
     // descending data
     start_time = clock ();
     insertionSort (tempDes, size);
     end_time = clock();
     elapsed_time = (end_time - start_time) / (double) CLOCKS_PER_SEC;
     printf ("%15.1lf", elapsed_time);
     
     printf ("\n");

      // Resetting temp arrays back to normal
     for (i = 0; i < size; i++) {
        tempAsc[i] = asc[i];
        tempRan[i] = ran[i];
        tempDes[i] = des[i];
     }

    // timing for Merge sort
    printf ("Merge sort %11d", size);
    // ascending data
    start_time = clock ();
    mergeSort(tempAsc, 0, size - 1);
    end_time = clock();
    elapsed_time = (end_time - start_time) / (double) CLOCKS_PER_SEC;
    printf ("%14.1lf", elapsed_time);

    // random data
    start_time = clock ();
    mergeSort(tempRan, 0, size - 1);
    end_time = clock();
    elapsed_time = (end_time - start_time) / (double) CLOCKS_PER_SEC;
    printf ("%15.1lf", elapsed_time);
     
    // descending data
    start_time = clock ();
    mergeSort(tempDes, 0, size - 1);
    end_time = clock();
    elapsed_time = (end_time - start_time) / (double) CLOCKS_PER_SEC;
    printf ("%15.1lf", elapsed_time);
     
    printf ("\n");

      // Resetting temp arrays back to normal
     for (i = 0; i < size; i++) {
        tempAsc[i] = asc[i];
        tempRan[i] = ran[i];
        tempDes[i] = des[i];
     }

    // timing for Heap sort
    printf ("Heap sort %12d", size);
    // ascending data
    start_time = clock ();
    heapSort (tempAsc, size);
    end_time = clock();
    elapsed_time = (end_time - start_time) / (double) CLOCKS_PER_SEC;
    printf ("%14.1lf", elapsed_time);

    // random data
    start_time = clock ();
    heapSort (tempRan, size);
    end_time = clock();
    elapsed_time = (end_time - start_time) / (double) CLOCKS_PER_SEC;
    printf ("%15.1lf", elapsed_time);
     
    // descending data
    start_time = clock ();
    heapSort (tempDes, size);
    end_time = clock();
    elapsed_time = (end_time - start_time) / (double) CLOCKS_PER_SEC;
    printf ("%15.1lf", elapsed_time);
     
    printf ("\n");

      // Resetting temp arrays back to normal
     for (i = 0; i < size; i++) {
        tempAsc[i] = asc[i];
        tempRan[i] = ran[i];
        tempDes[i] = des[i];
     }

    // timing for Quicksort 
    printf ("Quicksort %12d", size);
    // ascending data
    start_time = clock ();
    quicksort (tempAsc, size);
    end_time = clock();
    elapsed_time = (end_time - start_time) / (double) CLOCKS_PER_SEC;
    printf ("%14.1lf", elapsed_time);

    // random data
    start_time = clock ();
    quicksort (tempRan, size);
    end_time = clock();
    elapsed_time = (end_time - start_time) / (double) CLOCKS_PER_SEC;
    printf ("%15.1lf", elapsed_time);
     
    // descending data
    start_time = clock ();
    quicksort (tempDes, size);
    end_time = clock();
    elapsed_time = (end_time - start_time) / (double) CLOCKS_PER_SEC;
    printf ("%15.1lf", elapsed_time);
     
    printf ("\n");

      // Resetting temp arrays back to normal
     for (i = 0; i < size; i++) {
        tempAsc[i] = asc[i];
        tempRan[i] = ran[i];
        tempDes[i] = des[i];
     }

    // timing for IMP Quicksort 
    printf ("IMP Quicksort %8d", size);
    // ascending data
    start_time = clock ();
    quicksortIMP (tempAsc, size);
    end_time = clock();
    elapsed_time = (end_time - start_time) / (double) CLOCKS_PER_SEC;
    printf ("%14.1lf", elapsed_time);

    // random data
    start_time = clock ();
    quicksortIMP (tempRan, size);
    end_time = clock();
    elapsed_time = (end_time - start_time) / (double) CLOCKS_PER_SEC;
    printf ("%15.1lf", elapsed_time);
     
    // descending data
    start_time = clock ();
    quicksortIMP (tempDes, size);
    end_time = clock();
    elapsed_time = (end_time - start_time) / (double) CLOCKS_PER_SEC;
    printf ("%15.1lf", elapsed_time);
     
    printf ("\n \n");

     /* print results of sorting (ascending/random/descending data)
     for (i = 0; i < 15; i++) {
       printf ("%10d  %10d  %10d\n", tempAsc[i], tempRan[i], tempDes[i]);
     }
     */

     // clean up copies of test arrays
     free (tempAsc);
     free (tempRan);
     free (tempDes);

     // clean up original test arrays
     free (asc);
     free (ran);
     free (des);
     
  } // end of loop for testing procedures with different array sizes

  return 0;
}
