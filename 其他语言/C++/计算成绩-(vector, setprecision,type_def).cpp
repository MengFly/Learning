#include<iostream>
//ios����������streamsize������������������������ʾ����
#include<ios>
//�����˿�����setprecision,�������������������ָ�������������Чλ��
//��һ�����õĿ�������endl,����Ϊ�˷��㣬c++�ѿ�����������iostream��
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
        //�������ļ���������ʱ�������Windowsϵͳ����Ctrl + z
        homework.push_back(x);
    }

    //typedef Ϊһ���������Ͷ���һ��������
    typedef vector<double>::size_type vec_sz;
    vec_sz size = homework.size();

    if(size == 0) {
        cout << endl << "You must enter your grades " << "Please try again" << endl;
        return 1;
    }

    sort(homework.begin(), homework.end());

    // �����ͥ��ҵ��ֵ
    vec_sz mid = size/2;
    double median;
    median = (size % 2 == 0) ? (homework[mid] + homework[mid-1])/2 : homework[mid];

    //��ǰ����е�����ĸ��������ȣ���Ϊ����Ҫ�ı�����ľ��ȣ�����������֮ǰ����ȡ��ǰ����ľ��ȣ����������֮�������ó�ԭ��
    streamsize prec = cout.precision();
    //setprecision()��ָ����ӡ�ĸ�������λ���ܺͣ�����С����ǰ��С��������
    //����setprecision(4) ���մ�ӡ��һ�����ֿ�����1.235������1.23
    cout << "Your final grade is " << setprecision(4)
        << 0.2 * midterm + 0.4 * final + 0.4 * median
        << setprecision(prec) << endl;

    cout << "Your final grade is "
        << 0.2 * midterm + 0.4 * final + 0.4 * median << endl;

    return 0;
}

