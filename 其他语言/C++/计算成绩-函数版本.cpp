#include<iostream>
#include<vector>
#include<algorithm>
#include<string>
#include<ios>
#include<stdexcept>
#include<iomanip>

using std::vector;
using std::istream;
using std::cout;
using std::cin;
using std::endl;
using std::string;
using std::setprecision;
using std::streamsize;
using std::domain_error;


struct Student_info {
    string name;
    double midterm, final;
    vector<double> homework;

};

//查找vector中值
double median(vector<double> vec)
{
    //为vector的变量设置一个别名
    typedef vector<double>::size_type vec_sz;
    vec_sz size = vec.size();
    //检查向量是否为空
    if(size == 0) {
        throw domain_error("median of an empty vector");
    }
    //排序
    sort(vec.begin(), vec.end());

    //这个必然是整数，不会出现是小数的情况，因为它的类型是vector::size_type
    vec_sz mid = size / 2;

    return size % 2 == 0 ? (vec[mid-1] + vec[mid])/2 : vec[mid];
}

//计算总成绩
double grade(double midterm, double final, double homework)
{
    return 0.2*midterm + 0.4*final + 0.4*homework;
}

/**计算总成绩
    const 保证了我们不会对hw做任何改变值的操作
    例如：
    const vector<double> &hw1 = hw;
    在这里hw1就是hw，或者说hw1是hw的一个别名，但是const保证了hw1是只读的。
    使用这种参数是提高程序效率的一种重要手段
    因为vector和string的复制会消耗时间。
    */
double grade(double midterm, double final, const vector<double>& hw)
{
    return grade(midterm, final, median(hw));
}


//查找vector的平均值
double mean(vector<double> &vec)
{
    vector<double>::size_type size = vec.size();

    if(size == 0) {
        return 0;
    }

    double sum = 0;
    for(int i = 0; i < size; i ++) {
        sum += vec[i];
    }
    return sum/size;
}


/**读取家庭作业成绩
    这里我们使用&是因为我们要改变参数的值，所以要避免系统对参数进行复制
*/
istream& read_hw(istream &in, vector<double> &hw)
{
    if(in) {
        //清除原先的内容
        hw.clear();

        //读取家庭作业成绩
        double x;
        while(in >> x) {
            hw.push_back(x);
        }
        //清除流以使输入动作对下一个学生有效
        in.clear();
    }
    return in;
}

//读取学生信息
istream& read(istream& is, Student_info& s)
{
    is >> s.name >> s.midterm >> s.final;

    read_hw(is, s.homework);
    return is;
}

vector<double> emptyvec()
{
    vector<double> v;
    return v;
}

int main()
{
    //请求输入学生姓名
    cout << "Please enter your first name:";
    string name;
    cin >> name;
    cout << "Hello, " << name << "!" << endl;

    //请求并读入其中和期末的成绩
    cout << "Please enter your midterm and final exam grades:";
    double midterm, final;
    cin >> midterm >> final;

    //请求用户输入家庭作业成绩
    cout << "Enter all your home work grades."
        "followed by end-of-file:";
    vector<double> homework;

    //读入家庭作业成绩
    read_hw(cin, homework);

    //如果可以的话，计算生成总成绩
    try {
        double final_grade = grade(midterm, final, homework);
        streamsize prec = cout.precision();
        cout << "Your final grade is " << setprecision(3)
            << final_grade << setprecision(prec) << endl;
    } catch(domain_error) {
        cout << endl << "You must enter your grades."
            << "Please try again." << endl;
        return 1;
    }
    return 0;
}
