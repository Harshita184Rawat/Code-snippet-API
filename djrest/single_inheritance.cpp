#include<iostream>
using namespace std;


class parent
{
    private:
    int a,b,c;
    public:
    int add(int a, int b)
    {
        c=a+b;
        return c;
    }
    parent()
    {
        a=20, b=49;
    }
}

class child: public parent
{
    result=add();
    void show_result()
    {
        cout<<"Result of addition is"<<result;
    }

}

int main()
{
    parent P1;
    P1.add();
    return 0;
}

