4장></br>
4-1>></br>
1.문법 형식</br>
--> a.선택자: CSS 스타일을 적용할 HTML 태그(요소)를 선택하는 영역</br>
--> b.선언부: 선택자에서 선택한 태그에 적용할 스타일을 작성하는 영역; "{}"</br>
--> c.선택자{속성:값;}</br>

    h1{
        font-size:24px;
        color:red;
    }

2.주석: /* 주석 내용 */

</br></br>

4-2>></br>
1.내부 스타일 시트: HTML 파일 내부에 CSS 토드를 작성하는 방법</br>
--> HTML에 style 태그 작성</br>

    <head>
        <title>내부 스타일 시트</title>
        <style>
            h1{
                color:blue;
            }
        </style>
    </head>
    <body>
        <h1>내부 스타일 시트</h1>
    </body>

</br>
2.외부 스타일 시트: style.css파일을 별도로 만들어서 HTML문서와 CSS파일을 연결
</br>
    HTML파일

    <head>
        <title>내부 스타일 시트(External Style Sheet)</title>
        <link rel="stylesheet" href="style.css">
    </head>
    <body>
        <h1>내부 스타일 시트</h1>
    </body>

    CSS 파일

    h1{
        color:red;
    }

</br>

----->>> 실무에서는 대부분 ""외부 스타일 시트 방법""을 사용함</br>
: 유지 보수가 편하고 성능적으로도 가장 좋기 때문