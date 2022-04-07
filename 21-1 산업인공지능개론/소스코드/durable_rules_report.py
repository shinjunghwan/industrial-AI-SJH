!pip install durable_rules
from durable.lang import *

with ruleset('코딩규칙'):
    @when_all(c.first << (m.rules == '일반규칙') & (m.method == '방법'))         
    def 일반규칙(c):
        number = 0
        number += 1
        print(str(number)+". 코딩시 탭(Tab)의 크기는 4컬럼(column)으로 한다.")
        number += 1
        print(str(number)+". 헤더 파일(Header file)에서 다른 헤더 파일을 include하는 것을 금한다.")
        number += 1
        print(str(number)+". Brace ({) 는 functionnn인 경우는 밑에, 그 이외의 경우는 옆에 붙인다.")
        number += 1
        print(str(number)+". 과도한 nesting을 피한다.(최대 5회를 넘지 않도록 한다.)")
        number += 1
        print(str(number)+". 지나친 기교를 부리지 않는다.")
        number += 1
        print(str(number)+". 5개 이상의 매개변수의 사용은 피한다.")
        print('{0} {1}에는'.format(c.first.rules, c.first.method))
        print("총 "+str(number)+"개의 방법이 있습니다.")

    @when_all(c.first << (m.rules == '소스파일') & (m.method == '방법'))         
    def 소스파일구성(c):
        number = 0
        number += 1
        print(str(number)+". 파일 이름은 2종류로 구분한다. 즉 헤더(hader)파일과 소스(source) 파일이다.")
        number += 1
        print(str(number)+". 파일의 내용을 쉽게  볼 수 있도록 하기 위하여 파일 head 설명부,개정 이력,Header File Inclusions,External Declarations,Global Declarations,Functions순서로 구성한다.")
        number += 1
        print(str(number)+". 파일 Headr 설명문은 파일 전체 내용을 개괄적으로 기술하는 부분으로서, 파일의 내용, 목적, 기능을 함축하여 파일에 관한 모든 정보를 기술한다.")
        number += 1
        print(str(number)+". function head에 function의 내용 , 목적, 기능을 함축하여 모든 정보를 기술한다.")
        print('{0} {1}에는'.format(c.first.rules, c.first.method))
        print("총 "+str(number)+"개의 방법이 있습니다.")
        
    @when_all(c.first << (m.rules == '설명문') & (m.method == '방법'))         
    def 설명문(c):
        number = 0
        number += 1
        print(str(number)+". 설명은 기본적으로 한글로 사용하는 것을 원칙으로 한다.")
        number += 1
        print(str(number)+". 소스 코드를 포함하고 있는 모든 파일은 파일 이름과 내용을 설명하는 설명문을 파일의 맨 앞에 포함하여야 한다")
        number += 1
        print(str(number)+". 모든 파일은 저작권 및 개정이력(revision history)에 대한 문구를 포함하여야한다.")
        number += 1
        print(str(number)+". 모든 function앞에는 해당 function에 대한 설명을 기록한다.")
        number += 1
        print(str(number)+". 모든 복잡한 코드 앞에는 설명을 붙혀야 한다.(block설명과 line설명)")
        number += 1
        print(str(number)+". 코드 설명문은 코드를 반복하느 것이 아니라 보완하는 것이어야 한다.")
        number += 1
        print(str(number)+". 설명문은 다른 설명문 안에 중첩(nested) 해서는 안된다.")
        number += 1
        print(str(number)+". Line설명은 그 시작점을 일치 시키도록 한다.")
        print('{0} {1}에는'.format(c.first.rules, c.first.method))
        print("총 "+str(number)+"개의 방법이 있습니다.")



    @when_all(c.first << (m.rules == '함수') & (m.method == '방법'))         
    def 함수(c):
        number = 0
        number += 1
        print(str(number)+". function 의 return을 명시적으로 선언 되어야 한다.")
        number += 1
        print(str(number)+". Function을 정의할 때, 매개 변수가 있으면, 시작 괄호와 첫번째 매개변수는같은 줄에 오도록 한다.")
        number += 1
        print(str(number)+". function 이름은 동사와 목적어를 표현하며, 약어보다는 전체 이름으로 표시한다")
        number += 1
        print(str(number)+". 단어와 단어는 연결자를 사용하여 연결 하지 않는다.")
        number += 1
        print(str(number)+". 의미 있는 단어의 첫 글자를 대문자로 기술 한다. 단, C 기본함수 와 같은 함수는 정의되어 있는 그대로 사용한다")
        number += 1
        print(str(number)+". 정의된 macro function은 대문자로만 기술 한다.")
        number += 1
        print(str(number)+". 포인터를 반환하는 함수는 오류가 발생한 경우에 NULL 포인터를 돌려주어야 한다")
        print('{0} {1}에는'.format(c.first.rules, c.first.method))
        print("총 "+str(number)+"개의 방법이 있습니다.")

    @when_all(c.first << (m.rules == '구조체') & (m.method == '방법'))         
    def 구조체(c):
        number = 0
        number += 1
        print(str(number)+". Structure 선언할 때는, 첫 단어만 대문자로 기술하고 _을 이용하여 의미 있는이름을 추가로 기술한다.")
        number += 1
        print(str(number)+". auto 변수로 사용할 때는, Define된 structure를 소문자로만 기술 한다.")   
        print('{0} {1}에는'.format(c.first.rules, c.first.method))
        print("총 "+str(number)+"개의 방법이 있습니다.")

    @when_all(c.first << (m.rules == '변수') & (m.method == '방법'))         
    def 변수(c):
        number = 0
        number += 1
        print(str(number)+". 변수는 가능한 최소한의 범위에서 선언되어야 한다.")
        number += 1
        print(str(number)+". 변수는 항상 초기화 되어야 한다.")
        number += 1
        print(str(number)+". 전역변수(global variable)는 의미 있는 단어의 첫 글자를 대문자로 기술한다.")
        number += 1
        print(str(number)+". 지역변수(local variable)는 소문자로만 기술 한다.")
        number += 1
        print(str(number)+". 정적변수(static variable)는 소문자 또는 _를 사용하여 기술한다.")
        number += 1
        print(str(number)+". 음수 값을 갖지 않는 변수는 항상 unsigned 로 선언하여 사용한다.")
        print('{0} {1}에는'.format(c.first.rules, c.first.method))
        print("총 "+str(number)+"개의 방법이 있습니다.")

    @when_all(c.first << (m.rules == '상수') & (m.method == '방법'))         
    def 상수(c):
        number = 0
        number += 1
        print(str(number)+". 모든 사용자 정의 상수(constant)는 모두 대문자로 기술 하는 것을 원칙으로한다")
        number += 1
        print(str(number)+". 상수의 이름을 주는 것이 코드를 명확하게 하는 데 도움이 되거나, 그 값이 기능적으로 중요할 때는 모든 경우에는 코드 내에 수치 값을 직접 사용하지말고,  심볼을 정의 하여 사용한다.")
        number += 1
        print(str(number)+". 상수를 정의 할 때는 #define을 사용하는 대신에, constant를 사용하는 것이 좋다")
        number += 1
        print(str(number)+". 열거형 리스트에서 리스트의 요소는 대문자로 써야 한다.")
        print('{0} {1}에는'.format(c.first.rules, c.first.method))
        print("총 "+str(number)+"개의 방법이 있습니다.")

    @when_all(c.first << (m.rules == '캐스팅') & (m.method == '방법'))         
    def 캐스팅(c):
        number = 0
        number += 1
        print(str(number)+". 타입 변환을 사용한 코드는 이해하기 어렵기 때문에, 가능하면 사용하지 않도록 한다.")
        print('{0} {1}에는'.format(c.first.rules, c.first.method))
        print("총 "+str(number)+"개의 방법이 있습니다.")

    @when_all(c.first << (m.rules == '띄어쓰기') & (m.method == '방법'))         
    def 띄어쓰기(c):
        number = 0
        number += 1
        print(str(number)+". 모듈 이름과 경계 표시자는 첫 column에 표시 한다.")
        number += 1
        print(str(number)+". 행에서 writing start point는 Tab key 의 배수로 한다.")
        number += 1
        print(str(number)+". 변수 선언부 다음의 한 줄 공백으로 띄운다.")
        number += 1
        print(str(number)+". subroutine call(library)앞 행, 뒤 행은 한 줄 공백으로 띄운다.")
        number += 1
        print(str(number)+". return문의 전행은 띄운다")
        number += 1
        print(str(number)+". 함수와 함수 사이의 구분 시에는 최소한 두개의 빈줄로 구분한다.")
        number += 1
        print(str(number)+". 파일 한에서 논리적인 부분을 분리하는 것은 파일의 가독성을 향상 시킨다.")
        number += 1
        print(str(number)+". 변수 선언부를 제외하고는 한 line 에서 ';'로 분리되는 여러 문장을 함께쓰지 않는다.")
        number += 1
        print(str(number)+". Assignment 전후는 한 칸 띄어 쓴다.")
        number += 1
        print(str(number)+". Arithmatic operator(+,-,*,/,%,--,++)는 operand와 붙여 쓴다.")
        number += 1
        print(str(number)+". Relational operator(>,>=.<.<=,==,!=), logical operator(&&,||,!),bitwise operator(&,|,^,~,>>,<<)는 operand와 한칸 띄어 쓴다.(단, ~는 경우에  따라 붙여 쓴다.)")
        number += 1
        print(str(number)+". if else, for, do while 문은 아래와 같이 ({) 는 if문장의 끝, (})는 if else 의 시작 column에 일치 시킨다.")
        number += 1
        print(str(number)+". 변수 선언시 변수의 type과 변수는 tab key 만큼 띄어 쓴다.")
        number += 1
        print(str(number)+". ',' 뒤에는 한 칸 띄어 쓴다.")
        number += 1
        print(str(number)+". #define - 띄어 쓰기는 tab으로 처리")
        print('{0} {1}에는'.format(c.first.rules, c.first.method))
        print("총 "+str(number)+"개의 방법이 있습니다.")

    @when_all(c.first << (m.rules == '매개변수') & (m.method == '방법'))         
    def 매개변수(c):
        number = 0
        number += 1
        print(str(number)+". 포인터 전달은 가능한 한 전달 하지 않는다.")
        number += 1
        print(str(number)+". 매개변수를 받는 모둘의 () 밖에서 type을 정의 한다.")
        number += 1
        print(str(number)+". Buffer에 대한 시작점(start point)을 받는 경우 그 의미를 나타낼수 있도록 한다.")
        number += 1
        print(str(number)+". Array의 시작점을 전달 할 때는 array의 시작임을 표시할 수 있도록 한다.")
        number += 1
        print(str(number)+". 여러 매개변수를 전달 할 경우 destination(write), source(read), contents(how much) 순으로 한다.")
        print('{0} {1}에는'.format(c.first.rules, c.first.method))
        print("총 "+str(number)+"개의 방법이 있습니다.")


    @when_all(c.first << (m.rules == '흐름제어') & (m.method == '방법'))         
    def 흐름제어(c):
        number = 0
        number += 1
        print(str(number)+". case문은 항상 break로 끝내야 한다. .(예외: returrn과 같은 문장을 이용해서 case문을 빠져 나올수 있다.)")
        number += 1
        print(str(number)+". switch문은 항상 예상하지 못한 결과에 대처하기 위해 default문을 포함해야 한다.")
        number += 1
        print(str(number)+". 만약 switch 문 안에 case 가정상적인 break를 가지고 있지 않다면, 이를 구별하기 쉽게 하고 의도적이라는 것을 표시하기 위해 주석을 달아야 한다.")
        number += 1
        print(str(number)+". goto 문을 사용하지 않는다.")
        number += 1
        print(str(number)+". 반복문은 반드시 목적에 맞는 것을 골라 써야 한다. 반복문은 각각 특성이 있다. for 반복문은 한번 수행할 때마다 반복 변수가 일정한 크기로 증가하고, 특정한 값에 이르면 중단한다. 이 이외의 경우는 While문이나 do while문이 사용 되어야 한다. 종료 조건이 반복문의 초기에 결정 될 수 있는 경우는 while문을 사용하고, 반면에 반복문의 종료시에 결정 될 경우는 do while 문을 사용 한다.   ")
        number += 1
        print(str(number)+". 항상 반복문의 아래(시작) 값은 포함하고, 윗(종료) 값은 포함하지 않는다.")
        number += 1
        print(str(number)+". continue 문은 비정상적인 루프 순환을 제외하고는 사용하지 않는다.")
        number += 1
        print(str(number)+". flag의 사용을 피할수 있다면, 반복문을 빠져 나오기 위해 break를 사용한다.")
        number += 1
        print(str(number)+". test가 포인터인 경우 , if(test) 나 if(!test)는 이 이해가 어려우므로, 사용하지 않는다.")
        print('{0} {1}에는'.format(c.first.rules, c.first.method))
        print("총 "+str(number)+"개의 방법이 있습니다.")
        
    @when_all(c.first << (m.rules == '들여쓰기') & (m.method == '방법'))         
    def 들여쓰기(c):
        number = 0
        number += 1
        print(str(number)+". 중괄호의 위치를 통일 시킨다.")
        number += 1
        print(str(number)+". 내부 블록은 들여 쓴다.")
        number += 1
        print(str(number)+". 피 제어부는 들여 쓴다.")
        number += 1
        print(str(number)+". 쓸데 없는 들여 쓰기를 하지 말것")
        print('{0} {1}에는'.format(c.first.rules, c.first.method))
        print("총 "+str(number)+"개의 방법이 있습니다.")
        
    @when_all(c.first << (m.rules == '주석') & (m.method == '방법'))         
    def 주석(c):
        number = 0
        number += 1
        print(str(number)+". 한 줄 주석과 주석 상자를 구분하라 변수 사전 작성용 주석을 달아라. 의사코드를 프로그램에 기입하라.")
        number += 1
        print(str(number)+". 프로그램의 목적을 주석으로 달아라")
        number += 1
        print(str(number)+". 프로그램 앞부분에 머리주석을 반드시 달아라")
        print('{0} {1}에는'.format(c.first.rules, c.first.method))
        print("총 "+str(number)+"개의 방법이 있습니다.")
        
    @when_all(c.first << (m.rules == '식별자') & (m.method == '방법'))         
    def 식별자(c):
        number = 0
        number += 1
        print(str(number)+". 변수 이름을 체계적으로 지어라. ")
        number += 1
        print(str(number)+". 헝가리안 표기법으로 변수 이름을 지어라.(Option)")
        number += 1
        print(str(number)+". 변수의 자료형을 변수 이름에 접두사로 표기하라.(Option) ")
        number += 1
        print(str(number)+". 기억 영역 계층을 접두사로 활용하라. (Option)")
        number += 1
        print(str(number)+". 함수의 역할을 접두사로 활용하라.")
        number += 1
        print(str(number)+". 이름을 의미 있게 지어라.")
        number += 1
        print(str(number)+". 비슷한 변수 이름을 사용하지 말것.")
        number += 1
        print(str(number)+". 의미를 잃지 않는 범위에서 짧게 지어라 이름이 길면 밑줄 또는 대소문자로 구분하라")
        number += 1
        print(str(number)+". 변수 이름을 밑줄로 시작하지 말것.")
        number += 1
        print(str(number)+". 밑줄을 과도하게 사용하지 말것")
        number += 1
        print(str(number)+". 대소문자를 적절히 배합해서 만들어라.")
        number += 1
        print(str(number)+". 변수나 객체의 이름은 소문자로 시작한다")
        number += 1
        print(str(number)+". 함수,클래스,구조형,공용형 등의 이름을 대문자로 시작한다.(메소드 포함)")
        number += 1
        print(str(number)+". 기호 상수나 매크로 함수는 모든 글자를 대문자로만 짓는다")
        print('{0} {1}에는'.format(c.first.rules, c.first.method))
        print("총 "+str(number)+"개의 방법이 있습니다.")

    @when_all(c.first << (m.rules == '연산자') & (m.method == '방법'))         
    def 연산자(c):
        number = 0
        number += 1
        print(str(number)+". 조건 연산자는 경우에 따라서 효율성을 발휘 한다.")
        number += 1
        print(str(number)+". 연산자의 우선순위에 의존하는 식을 만들지 말것.")
        number += 1
        print(str(number)+". 포인터 연산자를 변수 이름쪽에 붙여서 써라.")
        number += 1
        print(str(number)+". 시프트 연산 대신 산술 연산을 사용하라.(Option)")
        number += 1
        print(str(number)+". 극단적으로 효율성을 추구하지 말것.") 
        print('{0} {1}에는'.format(c.first.rules, c.first.method))
        print("총 "+str(number)+"개의 방법이 있습니다.")

    @when_all(c.first << (m.rules == '명료하게하는') & (m.method == '방법'))         
    def 명료(c):
        number = 0
        number += 1
        print(str(number)+". 약삭빠른 코드 대신에 명료하고 이해하기 쉬운 프로그램을 작성하라.")
        number += 1
        print(str(number)+". While 문에서 관계/대입 연산자의 우선순위를 혼동하지 말것.")
        number += 1
        print(str(number)+". 묵시적인 ‘non zero test‘를 하지 말것.")
        number += 1
        print(str(number)+". 조건식에 대입문을 사용하지 말것.")
        number += 1
        print(str(number)+". 부작용이 나타나지 않도록 주의 하라.")
        number += 1
        print(str(number)+". 함수의 원형에도 인수의 자료형을 표기 하라.")
        number += 1
        print(str(number)+". 인수에도 이름을 기입하라.")
        number += 1
        print(str(number)+". 반환 자료형을 반드시 표기 하라.")
        number += 1
        print(str(number)+". 결과 값에 주의 하라.")
        print('{0} {1}에는'.format(c.first.rules, c.first.method))
        print("총 "+str(number)+"개의 방법이 있습니다.")

    @when_all(c.first << (m.rules == '이식하기쉬운') & (m.method == '방법'))         
    def 이식성(c):
        number = 0
        number += 1
        print(str(number)+". 파일 이름의 길이를 20자로 제한하라.")
        number += 1
        print(str(number)+". 파일 이름에 특수 문자를 사용 하지 말것.")
        number += 1
        print(str(number)+". 조건부 컴파일을 활용하여, 이식성을 높혀라.")
        number += 1
        print(str(number)+". 컴파일러의 한계를 인식하라.")
        number += 1
        print(str(number)+". 자료형의 크기가 달라질 수 있다는 점을 고려하라.")
        number += 1
        print(str(number)+". 절대 경로를 지정하지 말것.")
        print('{0} {1}에는'.format(c.first.rules, c.first.method))
        print("총 "+str(number)+"개의 방법이 있습니다.")

    @when_all(c.first << (m.rules == '정밀하게하는') & (m.method == '방법'))         
    def 정밀한(c):
        number = 0
        number += 1
        print(str(number)+". 컴퓨터는 생각 보다 정밀하지 않다.")
        number += 1
        print(str(number)+". 정밀한 계산이 필요하다면, 부동 소수점 연산을 피하라.")
        number += 1
        print(str(number)+". 정밀한 계산에는 float형보다 double형을 사용하라.")
        number += 1
        print(str(number)+". 정수형의 크기를 확인 하라.")
        number += 1
        print(str(number)+". 계산 단위를 반드시 명시 하라.")
        number += 1
        print(str(number)+". 나눗셈 연산에는 주의를 기울여라.")
        number += 1
        print(str(number)+". 자료형의 변환이 이루어지지 않도록 하라.")
        print('{0} {1}에는'.format(c.first.rules, c.first.method))
        print("총 "+str(number)+"개의 방법이 있습니다.")

    @when_all(c.first << (m.rules == '성능향상') & (m.method == '방법'))         
    def 성능(c):
        number = 0
        number += 1
        print(str(number)+". 성능이 중요하다면, 될수 있는한 출력하지 말것.")
        number += 1
        print(str(number)+". 연산을 단순한 형태로 바꿔라.")
        number += 1
        print(str(number)+". 효율성이 요구되는 큰 파일을 다룰 때는 바이너리 파일을 사용하라.")
        number += 1
        print(str(number)+". 패키드 구조체와 언팩키드 구조체의 장단점을 인식하고 사용하라.")
        number += 1
        print(str(number)+". 실행 환경을 고려하여, 언어를 선택 하라.")
        print('{0} {1}에는'.format(c.first.rules, c.first.method))
        print("총 "+str(number)+"개의 방법이 있습니다.")

    @when_all(c.first << (m.rules == '이해하기쉽게하는') & (m.method == '방법'))         
    def 이해(c):
        number = 0
        number += 1
        print(str(number)+". goto 문을 사용하지 말것.")
        number += 1
        print(str(number)+". C의 구성 요소를 선행처리기로 치환하지 말것.")
        number += 1
        print(str(number)+". 긴 자료형은 짧은  이름으로 바꿔 사용하라.")
        number += 1
        print(str(number)+". 조건식 보다는 if문을 사용하라.")
        number += 1
        print(str(number)+". 배열의 차원을 3차원으로 한정하라.")
        print('{0} {1}에는'.format(c.first.rules, c.first.method))
        print("총 "+str(number)+"개의 방법이 있습니다.")

    @when_all(c.first << (m.rules == 'UI') & (m.method == '방법'))         
    def 인터페이스(c):
        number = 0
        number += 1
        print(str(number)+". 입력 값을 저장할 변수의 크기를 충분히 확보하라.")
        number += 1
        print(str(number)+". 변환 지정자와 매개변수의 개수를 일치 시켜라.")
        number += 1
        print(str(number)+". 5개 이상 매개변수의 사용은 피한다.")
        number += 1
        print(str(number)+". Scanf() 함수보다는 fget()와 sscanf() 함수를 사용하라.")
        number += 1
        print(str(number)+". Fflush()함수를 사용해 표준 입출력 장치이 버퍼를 비울것.")
        print('{0} {1}에는'.format(c.first.rules, c.first.method))
        print("총 "+str(number)+"개의 방법이 있습니다.")


    @when_all(c.first << (m.rules == '오류없게하는') & (m.method == '방법'))         
    def 오류제거(c):
        number = 0
        number += 1
        print(str(number)+". 배열의 첨자는 0부터 시작한다는 것을 잊지 말것.")
        number += 1
        print(str(number)+". 치환 문자열은 반드시 괄호로 씌울것.")
        number += 1
        print(str(number)+". 파일을 열었다면, 반드시 닫아라.")
        number += 1
        print(str(number)+". 컴파일러의 경고(warning error)를 무시하지 말것.")
        number += 1
        print(str(number)+". 런타임 오류를 인식하고, 그것이 발생하지 않도록 코드를 작성하라.")
        number += 1
        print(str(number)+". 배열이 큰 경우에는 정적 변수로 선언 하라.")
        number += 1
        print(str(number)+". 헤더 파일(header file)에서 다른 헤더 파일을 include하는 것은 금한다.")
        number += 1
        print(str(number)+". 과도한 nesting을 피한다.(최대 5회를 넘지 않도록 한다,)")   
        print('{0} {1}에는'.format(c.first.rules, c.first.method))
        print("총 "+str(number)+"개의 방법이 있습니다.")
    
    #@when_all(+m.rules)
    #def output(c):
    #    print('-----{0} {1} {2}'.format(c.m.rules, c.m.method, c.m.count))


assert_fact('코딩규칙', { 'rules': '일반규칙','method': '방법'})
assert_fact('코딩규칙', { 'rules': '소스파일','method': '방법'})
assert_fact('코딩규칙', { 'rules': '설명문','method': '방법'})
assert_fact('코딩규칙', { 'rules': '함수','method': '방법'})
assert_fact('코딩규칙', { 'rules': '구조체','method': '방법'})
assert_fact('코딩규칙', { 'rules': '변수','method': '방법'})
assert_fact('코딩규칙', { 'rules': '상수','method': '방법'})
assert_fact('코딩규칙', { 'rules': '캐스팅','method': '방법'})
assert_fact('코딩규칙', { 'rules': '띄어쓰기','method': '방법'})
assert_fact('코딩규칙', { 'rules': '매개변수','method': '방법'})
assert_fact('코딩규칙', { 'rules': '흐름제어','method': '방법'})
assert_fact('코딩규칙', { 'rules': '들여쓰기','method': '방법'})
assert_fact('코딩규칙', { 'rules': '주석','method': '방법'})
assert_fact('코딩규칙', { 'rules': '식별자','method': '방법'})
assert_fact('코딩규칙', { 'rules': '연산자','method': '방법'})
assert_fact('코딩규칙', { 'rules': '명료하게하는','method': '방법'})
assert_fact('코딩규칙', { 'rules': '이식하기쉬운','method': '방법'})
assert_fact('코딩규칙', { 'rules': '정밀하게하는','method': '방법'})
assert_fact('코딩규칙', { 'rules': '성능향상','method': '방법'})
assert_fact('코딩규칙', { 'rules': '이해하기쉽게하는','method': '방법'})
assert_fact('코딩규칙', { 'rules': 'UI','method': '방법'})
assert_fact('코딩규칙', { 'rules': '오류없게하는','method': '방법'})
