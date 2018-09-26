#include<iostream>
#include<stdlib.h>
using namespace std;
int main()
{
  srand(time(0));
  int i,j;
  i=1+rand()%10;
  cout<<"Я загадала число! Отгадайте..."<<endl;
  cout<<"Итак, ваше число: ";
  cin>>j;
  if (i==j)
    cout<<"Поздравляю, Вы отгадали"<<endl;
  else
   {
    cout<<"Сожалею, но Вы проиграли...."<<endl;
    cout<<"Я загадала число: "<<i<<endl;
    cout<<"Ребята, снимите-ка с него шкуру"<<endl;
   }
  return 0;
}
