#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <float.h>
#include <string.h>
#define POWER 2 // should be 2 size behind the maximum power

// get whole and decimal part
char* getPart(char* whole);
// transform whole part in long double array
long double* wholeArray(char *num, long long *len);
// transform decimal part in long double array
long double* decArray(char *dec, long long len);
// transform whole and decimal part from long double arrays to a string
char* toStringFormat(
  long double* whole, long long wLen,
  long double* dec, long long dLen);
// add 2 numbers
char* add(char* num1, char* num2);
// substracte 2 numbers
char* sub(char* num1, char* num2);
// divide 2 numbers
char* division(char* num1, char* num2);

int main(int argc, char const *argv[])
{
  /* the highest number in IEEE754 80bits
  should be 0  111111111111110 11111111111111111111111111111111111111111111111111111111111111
            s  exponent 15bits     mantissa 64 bits
  because if exponent = 11111111 the result is whether NaN or infinity depending on the mantissa
  */

  // calculate exponent - bias
  int e = pow(2, 15) - 2 -(pow(2, 14) -1);

  // calculate mantissa + 1
  long double m = 1;
  // it should be up to -64 but m is rounded to 2
  // which result in maxFloating being inf
  // so we chose the most precise which is -52
  for (int j = -1; j >= -52; j--)
  {
    m += powl(2, j);
  }

  long double maxFloating = powl(2, e) * m;
  printf("E = %d\n", e);
  printf("M = %.52Lf\n", m);
  printf("maxFloat = %Le\n", maxFloating); // calculated float max
  printf("LDBL_MAX defined by the float.h library = %Le\n", LDBL_MAX);
  printf("\n\n\n");
// -------------------------------------------------------
  if(argc > 1)
  {
  }
  char arg1[] = "5000";
  char arg2[] = "2000";
  char *num1 = malloc (sizeof (char) * strlen(arg1));
  char *num2 = malloc (sizeof (char) * strlen(arg2));
  if (num1 == NULL || num2 == NULL) {
    printf("Failed to allocate memory space.");
    return 0;
  }
  strcpy(num1, arg1);
  strcpy(num2, arg2);

  printf("%s\n", arg1);
  printf("+\n");
  printf("%s\n", arg2);
  printf("---------\n");
  printf("%s\n\n", add(num1, num2));
  // -------------------------------------------------------
  strcpy(num1, arg1);
  strcpy(num2, arg2);
  printf("%s\n", num1);
  printf("-\n");
  printf("%s\n", num2);
  printf("---------\n");
  printf("%s\n\n",sub(arg1, arg2));


  return 1;
}
// functions start here

char* getPart(char* num)
{
  strtok(num, ".");
  char *dec = strtok(NULL, ".");
  return dec != NULL ? dec : "0000";
}

long double* wholeArray(char *num, long long *len)
{
  long double *result = malloc (sizeof (long double) * (*len));
  // if failed
  if (result == NULL) {
    printf("Failed to allocate memory space.");
    return NULL;
  }
  int sign = 0;
  if(num[0] == '-')
    sign = 1;
  long long index = 0;
  for(long long i = strlen(num)-1; i >= sign; i--)
  {
    result[index] = 0;
    for(int power = 0; power < POWER; power++)
    {
      if(i < 0)
        break;
      result[index] += (num[i]-'0') * pow(10, power);
      if(power < POWER-1)
        i--;
    }
    index++;
  }
  if(sign == 1)
  {
    result[index-1] = result[index-1]* -1;
    (*len)--;
  }
  return result;

}

long double* decArray(char *dec, long long len)
{
  long double *result = malloc (sizeof (long double) * len);
  // if failed
  if (result == NULL) {
    printf("Failed to allocate memory space.");
    return NULL;
  }

  long long index = 0;
  for(long long i = 0; i <strlen(dec); i++)
  {
    result[index] = 0;
    for(int power = POWER-1; power >= 0; power--)
    {
      if(i >= strlen(dec))
        break;
      result[index] += (dec[i]-'0') * pow(10, power);
      if(power > 0)
        i++;
    }
    index++;
  }
  return result;
}
// transform long double array format into string
char* toStringFormat( long double* whole, long long wLen, long double* dec, long long dLen)
{
  int sign = 0;
  long long index = 0;
  if(whole[wLen-1]<0)
  {
    sign = 1;
  }
  char* result = malloc (sizeof (char)* POWER * (wLen+dLen) + 1 + sign);
  if (result == NULL)
  {
    printf("Failed to allocate memory space.");
    return NULL;
  }
  if (sign>0)
  {
    whole[wLen-1] = whole[wLen-1] * -1;
    sprintf(&result[index], "-");
    index++;
  }
  // display whole part
  for(long long i = wLen-1; i >= 0; i--)
  {
    char first = 1;
    char didFirst = 0;
    // add 0
    if((whole[i] < powl(10, POWER-1)))
    {
      long long f = 0;
      while( whole[i] < powl(10, POWER-1-f))
      {
        if(first == 0)
        {

          sprintf(&result[index], "0");

          index++;
        }
        f++;
        didFirst = 1;
      }
      if(didFirst == 1)
        first = 0;
      sprintf(&result[index], "%0.Lf", whole[i]);
      index+=f;
    }
    else
    {
      sprintf(&result[index], "%0.Lf", whole[i]);
      index += POWER;
    }
  }
  // add the dot "."
  sprintf(&result[index],".");
  index++;
  // display decimal
  for(long long j = dLen-1; j >= 0; j--)
  {
    // prevent single 0
    if(dec[j] == 0)
    {
      for (long long k = 0; k < POWER; k++)
      {
        sprintf(&result[index+k], "0");
      }
    }
    else
    {
      sprintf(&result[index],"%.0Lf", dec[j]);
    }
    index += POWER;
  }
  return result;
}

// addition
char* add(char* num1, char* num2)
{
  // get whole and decimal part of each number
  char * dec1 = getPart(num1);
  char * dec2 = getPart(num2);

  // calculate length of each long double array
  long long w1Len = strlen(num1)/POWER + strlen(num1) % POWER;
  long long w2Len = strlen(num2)/POWER + strlen(num2) % POWER;
  long long d1Len = strlen(dec1)/POWER + strlen(dec1) % POWER;
  long long d2Len = strlen(dec2)/POWER + strlen(dec2) % POWER;

  long double temp;
  int carry = 0;
  long long wLen = w1Len > w2Len ? w1Len : w2Len;
  long long dLen = d1Len > d2Len ? d1Len : d2Len;

  // array to store the result
  long double *whole = (long double*)malloc (sizeof (long double) * wLen+1);
  long double *decimal = (long double*)malloc (sizeof (long double) * dLen+1);
  long double *w1 = (long double*)malloc (sizeof (long double)*w1Len);
  long double *w2 = (long double*)malloc (sizeof (long double)*w2Len);
  long double *d1 = (long double*)malloc (sizeof (long double)*d1Len);
  long double *d2 = (long double*)malloc (sizeof (long double)*d2Len);
  // if failed
  if (
    whole == NULL || decimal == NULL
    || w1 == NULL || d1 == NULL
    || w2 == NULL || d2 == NULL) {
    printf("Failed to allocate memory space.");
    return NULL;
  }
  // transform each part into long double array
  // array to store the result

  w1 = wholeArray(num1, &w1Len);
  w2 = wholeArray(num2, &w2Len);
  d1 = decArray(dec1, d1Len);
  d2 = decArray(dec2, d2Len);
  int sign = 1;
  if(w1[w1Len-1]<0 && w2[w2Len-1]<0)
  {
    w1[w1Len-1] = w1[w1Len-1] * -1;
    w2[w2Len-1] = w2[w2Len-1] * -1;
    sign = -1;
  }
  // calculate decimal part
  long long di = 0;
  for(long long i = dLen -1; i >= 0; i--)
  {
    temp = 0;
    if(carry > 0)
    {
      temp += carry;
      carry = 0; // reset carry
    }
    if(i < d1Len)
      temp += d1[i];
    if(i < d2Len)
      temp += d2[i];
    if(temp >= powl(10, POWER))
    {
        carry = (int) (temp/powl(10, POWER));
        temp = temp - (carry * powl(10, POWER));
    }
    decimal[di] = temp;
    di++;
  }
  // calculate whole part
  long long wi = 0;
  for(long long j = 0; j < wLen; j++)
  {
    temp = 0;
    if(carry > 0)
    {
      temp += carry;
      carry = 0; // reset carry
    }
    if(j < w1Len)
      temp += w1[j];
    if(j < w2Len)
      temp += w2[j];
    if(temp >= powl(10, POWER))
    {
        carry = (int) (temp/powl(10, POWER));
        temp = temp - (carry * powl(10, POWER));
    }
    whole[wi] = temp;
    wi++;

  }
  if(carry > 0)
  {
    whole[wi] = carry;
    wi++;
  }
  whole[wi-1] = whole[wi-1]*sign;
  return toStringFormat(whole, wi, decimal, di);
}

// substraction
char* sub(char* num1, char* num2)
{
  // get whole and decimal part of each number
  char * dec1 = getPart(num1);
  char * dec2 = getPart(num2);

  // calculate length of each long double array
  long long w1Len = strlen(num1)/POWER + strlen(num1) % POWER;
  long long w2Len = strlen(num2)/POWER + strlen(num2) % POWER;
  long long d1Len = strlen(dec1)/POWER + strlen(dec1) % POWER;
  long long d2Len = strlen(dec2)/POWER + strlen(dec2) % POWER;

  long double temp;
  int carry = 0;
  long long wLen = w1Len > w2Len ? w1Len : w2Len;
  long long dLen = d1Len > d2Len ? d1Len : d2Len;
  int sign = 1;

  // array to store the result
  long double *whole = (long double*)malloc (sizeof (long double) * wLen+1);
  long double *decimal = (long double*)malloc (sizeof (long double) * dLen+1);
  long double *w1 = (long double*)malloc (sizeof (long double)*w1Len);
  long double *w2 = (long double*)malloc (sizeof (long double)*w2Len);
  long double *d1 = (long double*)malloc (sizeof (long double)*d1Len);
  long double *d2 = (long double*)malloc (sizeof (long double)*d2Len);
  // if failed
  if (
    whole == NULL || decimal == NULL
    || w1 == NULL || d1 == NULL
    || w2 == NULL || d2 == NULL) {
    printf("Failed to allocate memory space.");
    return NULL;
  }

  // transform each part into long double array
  // array to store the result

  w1 = wholeArray(num1, &w1Len);
  w2 = wholeArray(num2, &w2Len);
  d1 = decArray(dec1, d1Len);
  d2 = decArray(dec2, d2Len);

  // compare num1 and num2 to determine who should be substracted

  if(w2Len > w1Len)
  {
    long double *temp = w1;
    w1 = w2;
    w2 = temp;
    sign = -1;
  }
  else if(w2Len == w1Len)
  {
    for( long long i = 0; i < w2Len; i++)
    {
      if(w1[i]>w2[i])
        break;
      if(w2[i]>w1[i])
      {
        long double *temp = w1;
        w1 = w2;
        w2 = temp;
        sign = -1;
        break;
      }
    }
  }

  // calculate decimal part
  long long di = 0;
  for(long long i = dLen -1; i >= 0; i--)
  {
    temp = 0;
    if(carry > 0)
    {
      temp -= carry;
      carry = 0; // reset carry
    }
    if(i < d1Len)
      temp += d1[i];
    if(i < d2Len)
    {
      if(temp < d2[i])
      {
        temp += powl(10, POWER);
        carry = 1;
      }
      temp -= d2[i];
    }
    decimal[di] = temp;
    di++;
  }
  // calculate whole part
  long long wi = 0;
  for(long long j = 0; j < wLen; j++)
  {
    temp = 0;
    if(carry > 0)
    {
      temp -= carry;
      carry = 0; // reset carry
    }
    if(j < w1Len)
      temp += w1[j];
    if(j < w2Len)
    {
      if(temp < w2[j])
      {
        temp += powl(10, POWER);
        carry = 1;
      }
      temp -= w2[j];
    }
    whole[wi] = temp;
    wi++;
  }
  whole[wi-1] = whole[wi-1] * sign;
  return toStringFormat(whole, wi, decimal, di);
}

// division
char* division(char* num1, char* num2)
{
  long long num1Len = strlen(num1);
  long long num2Len = strlen(num2);
  long double *result = malloc (sizeof (long double) * num1Len);
  // if failed
  if (result == NULL) {
    printf("Failed to allocate memory space.");
    return NULL;
  }
  int stop = 0;
  if(stop > 0)
  {
    while(num1Len>num2Len)
    {
      printf("%s\n", sub(num1, num2));
      num1 = sub(num1, num2);
    }
  }
  return "result";
}
