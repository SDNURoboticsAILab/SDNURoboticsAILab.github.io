# C++ 中的数据类型范围及其宏

在竞争性编程中，通常需要将变量赋值为数据类型所能容纳的最大值或最小值。然而，记住这些大而精确的数字是一项困难的任务。因此，C++ 提供了一些宏来表示这些数字，这样可以直接将它们赋值给变量，而不必实际输入整个数字。以下是一些宏的列表：

<table><thead><tr><th style="width: 116.667px;"><p dir="ltr"><span>数据类型</span></p>
</th><th style="width: 116.667px;"><p dir="ltr"><span>范围 </span></p>
</th><th style="width: 116.667px;"><p dir="ltr"><span>宏的最小值 </span></p>
</th><th style="width: 116.667px;"><p dir="ltr"><span>宏的最大值 </span></p>
</th></tr></thead><tbody><tr><th style="width: 140px;"><p dir="ltr"><span> char </span></p>
</th><td style="width: 140px;"><p dir="ltr"><span>-128 to +127  </span></p><div id="GFG_AD_Desktop_InContent_ATF_336x280" style="text-align:center; max-height: 280px;"></div><div id="GFG_AD_gfg_mobile_336x280_1" style="margin: 5px 0;"></div>
</td><td style="width: 140px;"><p dir="ltr"><span>CHAR_MIN </span></p>
</td><td style="width: 140px;"><p dir="ltr"><span>CHAR_MAX </span></p>
</td></tr><tr><th style="width: 116.667px;"><p dir="ltr"><span>short char </span></p>
</th><td style="width: 116.667px;"><p dir="ltr"><span>-128 to +127 </span></p>
</td><td style="width: 116.667px;"><p dir="ltr"><span>SCHAR_MIN </span></p>
</td><td style="width: 116.667px;"><p dir="ltr"><span>SCHAR_MAX</span></p>
</td></tr><tr><th style="width: 116.667px;"><p dir="ltr"><span>unsigned char  </span></p>
</th><td style="width: 116.667px;"><p dir="ltr"><span>0 to 255  </span></p>
</td><td style="width: 116.667px;">
<p><span>—</span></p>
</td><td style="width: 116.667px;"><p dir="ltr"><span>UCHAR_MAX </span></p>
</td></tr><tr><th style="width: 116.667px;"><p dir="ltr"><span>short int </span></p>
</th><td style="width: 116.667px;"><p dir="ltr"><span>-32768 to +32767  </span></p>
</td><td style="width: 116.667px;"><p dir="ltr"><span>SHRT_MIN </span></p>
</td><td style="width: 116.667px;"><p dir="ltr"><span>SHRT_MAX                  </span></p>
</td></tr><tr><th style="width: 116.667px;"><p dir="ltr"><span>unsigned short int </span></p>
</th><td style="width: 116.667px;"><p dir="ltr"><span>0 to 65535 </span></p>
</td><td style="width: 116.667px;">
<p><span>—</span></p>
</td><td style="width: 116.667px;"><p dir="ltr"><span>USHRT_MAX</span></p>
</td></tr><tr><th style="width: 116.667px;"><p dir="ltr"><span>int </span></p>
</th><td style="width: 116.667px;"><p dir="ltr"><span>-2147483648 to +2147483647 </span></p>
</td><td style="width: 116.667px;"><p dir="ltr"><span>INT_MIN </span></p>
</td><td style="width: 116.667px;"><p dir="ltr"><span>INT_MAX                   </span></p>
</td></tr><tr><th style="width: 116.667px;"><p dir="ltr"><span>unsigned int </span></p>
</th><td style="width: 116.667px;"><p dir="ltr"><span>0 to 4294967295 </span></p>
</td><td style="width: 116.667px;">
<p><span>—</span></p>
</td><td style="width: 116.667px;"><p dir="ltr"><span>UINT_MAX </span></p>
</td></tr><tr><th style="width: 116.667px;"><p dir="ltr"><span>long int </span></p>
</th><td style="width: 116.667px;"><p dir="ltr"><span>-9223372036854775808 to +9223372036854775807</span></p>
</td><td style="width: 116.667px;"><p dir="ltr"><span>LONG_MIN </span></p>
</td><td style="width: 116.667px;"><p dir="ltr"><span>LONG_MAX</span></p>
</td></tr><tr><th style="width: 116.667px;"><p dir="ltr"><span>unsigned long int</span></p>
</th><td style="width: 116.667px;"><p dir="ltr"><span>0 to 18446744073709551615</span></p>
</td><td style="width: 116.667px;">
<p><span>—</span></p>
</td><td style="width: 116.667px;"><p dir="ltr"><span>ULONG_MAX</span></p>
</td></tr><tr><th style="width: 116.667px;"><p dir="ltr"><span>long long int</span></p>
</th><td style="width: 116.667px;"><p dir="ltr"><span>-9223372036854775808 to +9223372036854775807</span></p>
</td><td style="width: 116.667px;"><p dir="ltr"><span>LLONG_MIN</span></p>
</td><td style="width: 116.667px;"><p dir="ltr"><span>LLONG_MAX</span></p>
</td></tr><tr><th style="width: 116.667px;"><p dir="ltr"><span>unsigned long long int</span></p>
</th><td style="width: 116.667px;"><p dir="ltr"><span>0 to 18446744073709551615 </span></p>
</td><td style="width: 116.667px;">
<p><span>—</span></p>
</td><td style="width: 116.667px;"><p dir="ltr"><span>ULLONG_MAX</span></p>
</td></tr><tr><th style="width: 116.667px;"><p dir="ltr"><span>float  </span></p>
</th><td style="width: 116.667px;"><p dir="ltr"><span>1.17549e-38 to 3.40282e+38 </span></p>
</td><td style="width: 116.667px;"><p dir="ltr"><span>FLT_MIN  </span></p>
</td><td style="width: 116.667px;"><p dir="ltr"><span>FLT_MAX </span></p>
</td></tr><tr><th style="width: 116.667px;"><p dir="ltr"><span>float (negative)</span></p>
</th><td style="width: 116.667px;"><p dir="ltr"><span>-1.17549e-38 to -3.40282e+38  </span></p>
</td><td style="width: 116.667px;"><p dir="ltr"><span>-FLT_MIN </span></p>
</td><td style="width: 116.667px;"><p dir="ltr"><span>-FLT_MAX</span></p>
</td></tr><tr><th style="width: 116.667px;"><p dir="ltr"><span>double</span></p>
</th><td style="width: 116.667px;"><p dir="ltr"><span>2.22507e-308 to 1.79769e+308  </span></p>
</td><td style="width: 116.667px;"><p dir="ltr"><span>DBL_MIN </span></p>
</td><td style="width: 116.667px;"><p dir="ltr"><span>DBL_MAX </span></p>
</td></tr><tr><th style="width: 116.667px;"><p dir="ltr"><span>double (negative) </span></p>
</th><td style="width: 116.667px;"><p dir="ltr"><span>-2.22507e-308 to -1.79769e+308 </span></p>
</td><td style="width: 116.667px;"><p dir="ltr"><span>-DBL_MIN </span></p>
</td><td style="width: 116.667px;"><p dir="ltr"><span>-DBL_MAX </span></p>
</td></tr></tbody></table>

**样例**

以下示例展示了数据类型的宏。

```
// 演示数据类型宏的 C++ 代码
#include <float.h> // 对于浮点数，双精度浮点数的宏
#include <iostream>
#include <limits.h> // 对于整型，字符型宏

using namespace std;

int main()
{
    //使用宏显示数据类型范围
    cout << "char ranges from: " << CHAR_MIN << " to "
         << CHAR_MAX << endl;
    cout << "\nshort char ranges from: " << SCHAR_MIN
         << " to " << SCHAR_MAX << endl;
    cout << "\nunsigned char ranges from: " << 0 << " to "
         << UCHAR_MAX << endl;

    cout << "\n\nshort int ranges from: " << SHRT_MIN
         << " to " << SHRT_MAX << endl;
    cout << "\nunsigned short int ranges from: " << 0
         << " to " << USHRT_MAX << endl;
    cout << "\nint ranges from: " << INT_MIN << " to "
         << INT_MAX << endl;
    cout << "\nunsigned int ranges from: " << 0 << " to "
         << UINT_MAX << endl;
    cout << "\nlong int ranges from: " << LONG_MIN << " to "
         << LONG_MAX << endl;
    cout << "\nunsigned long int ranges from: " << 0
         << " to " << ULONG_MAX << endl;
    cout << "\nlong long int ranges from: " << LLONG_MIN
         << " to " << LLONG_MAX << endl;
    cout << "\nunsigned long long int ranges from: " << 0
         << " to " << ULLONG_MAX << endl;

    cout << "\n\nfloat ranges from: " << FLT_MIN << " to "
         << FLT_MAX << endl;
    cout << "\nnegative float ranges from: " << -FLT_MIN
         << " to " << -FLT_MAX << endl;
    cout << "\ndouble ranges from: " << DBL_MIN << " to "
         << DBL_MAX << endl;
    cout << "\nnegative double ranges from: " << -DBL_MIN
         << " to " << -DBL_MAX << endl;

    return 0;
}
```

**输出**

```
char ranges from: -128 to 127

short char ranges from: -128 to 127

unsigned char ranges from: 0 to 255

short int ranges from: -32768 to 32767

unsigned short int ranges from: 0 to 65535

int ranges from: -2147483648 to 2147483647

unsigned int ranges from: 0 to 4294967295

long int ranges from: -9223372036854775808 to 9223372036854775807

unsigned long int ranges from: 0 to 18446744073709551615

long long int ranges from: -9223372036854775808 to 9223372036854775807

unsigned long long int ranges from: 0 to 18446744073709551615

float ranges from: 1.17549e-38 to 3.40282e+38

negative float ranges from: -1.17549e-38 to -3.40282e+38

double ranges from: 2.22507e-308 to 1.79769e+308

negative double ranges from: -2.22507e-308 to -1.79769e+308
```

