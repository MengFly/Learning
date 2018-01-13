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

//����vector��ֵ
double median(vector<double> vec)
{
    //Ϊvector�ı�������һ������
    typedef vector<double>::size_type vec_sz;
    vec_sz size = vec.size();
    //��������Ƿ�Ϊ��
    if(size == 0) {
        throw domain_error("median of an empty vector");
    }
    //����
    sort(vec.begin(), vec.end());

    //�����Ȼ�����������������С�����������Ϊ����������vector::size_type
    vec_sz mid = size / 2;

    return size % 2 == 0 ? (vec[mid-1] + vec[mid])/2 : vec[mid];
}

//�����ܳɼ�
double grade(double midterm, double final, double homework)
{
    return 0.2*midterm + 0.4*final + 0.4*homework;
}

/**�����ܳɼ�
    const ��֤�����ǲ����hw���κθı�ֵ�Ĳ���
    ���磺
    const vector<double> &hw1 = hw;
    ������hw1����hw������˵hw1��hw��һ������������const��֤��hw1��ֻ���ġ�
    ʹ�����ֲ�������߳���Ч�ʵ�һ����Ҫ�ֶ�
    ��Ϊvector��string�ĸ��ƻ�����ʱ�䡣
    */
double grade(double midterm, double final, const vector<double>& hw)
{
    return grade(midterm, final, median(hw));
}


//����vector��ƽ��ֵ
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


/**��ȡ��ͥ��ҵ�ɼ�
    ��������ʹ��&����Ϊ����Ҫ�ı������ֵ������Ҫ����ϵͳ�Բ������и���
*/
istream& read_hw(istream &in, vector<double> &hw)
{
    if(in) {
        //���ԭ�ȵ�����
        hw.clear();

        //��ȡ��ͥ��ҵ�ɼ�
        double x;
        while(in >> x) {
            hw.push_back(x);
        }
        //�������ʹ���붯������һ��ѧ����Ч
        in.clear();
    }
    return in;
}

//��ȡѧ����Ϣ
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
    //��������ѧ������
    cout << "Please enter your first name:";
    string name;
    cin >> name;
    cout << "Hello, " << name << "!" << endl;

    //���󲢶������к���ĩ�ĳɼ�
    cout << "Please enter your midterm and final exam grades:";
    double midterm, final;
    cin >> midterm >> final;

    //�����û������ͥ��ҵ�ɼ�
    cout << "Enter all your home work grades."
        "followed by end-of-file:";
    vector<double> homework;

    //�����ͥ��ҵ�ɼ�
    read_hw(cin, homework);

    //������ԵĻ������������ܳɼ�
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
