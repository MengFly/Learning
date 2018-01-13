#include<iostream>
//ios定义了类型streamsize。输入输出库用这个类型来表示长度
#include<ios>
//定义了控制器setprecision,这个控制器可以让我们指明输出包含的有效位数
//另一个常用的控制器是endl,但是为了方便，c++把控制器放在了iostream中
#include<iomanip>
#include<string>
#include<vector>
#include<algorithm>

using std::cin;
using std::cout;
using std::endl;
using std::setprecision;
using std::string;
using std::streamsize;
using std::vector;
using std::sort;

int main()
{
    cout << "Please enter your first name:";
    string name;
    cin >> name;

    cout << "Please enter your midterm and final exam grades:";
    double midterm, final;
    cin >> midterm >> final;

    cout << "Enter all your homework grades, "
    " followed by end-of-file:";

    vector<double> homework;
    double x;
    while(cin >> x) {
        //当输入文件结束符的时候结束，Windows系统中是Ctrl + z
        homework.push_back(x);
    }

    //typedef 为一个数据类型定义一个新名字
    typedef vector<double>::size_type vec_sz;
    vec_sz size = homework.size();

    if(size == 0) {
        cout << endl << "You must enter your grades " << "Please try again" << endl;
        return 1;
    }

    sort(homework.begin(), homework.end());

    // 计算家庭作业中值
    vec_sz mid = size/2;
    double median;
    median = (size % 2 == 0) ? (homework[mid] + homework[mid-1])/2 : homework[mid];

    //当前输出行的输出的浮点数精度，因为我们要改变输出的精度，所以在设置之前来获取当前输出的精度，在设置完成之后再设置成原样
    streamsize prec = cout.precision();
    //setprecision()是指定打印的浮点数的位数总和，包括小数点前和小数点后面的
    //例如setprecision(4) 最终打印的一个数字可能是1.235而不是1.23
    cout << "Your final grade is " << setprecision(4)
        << 0.2 * midterm + 0.4 * final + 0.4 * median
        << setprecision(prec) << endl;

    cout << "Your final grade is "
        << 0.2 * midterm + 0.4 * final + 0.4 * median << endl;

    return 0;
}

