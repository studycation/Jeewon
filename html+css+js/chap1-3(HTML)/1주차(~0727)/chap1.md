1-1장>

//HTML 기본 구조

//1.DTD: 문서형 정의
<!DOCTYPE html>
//2.html 시작
<html lang="ko">

    //3.문서 정보 정의
    <head>                                                         
        <meta charset="UTF-8">     <!--meta 태그는 메타데이터 정의하는데 사용-->
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>My first Web Page!</title>     <!--HTML 문서제목-->
    </head>

    //4.웹 브라우저에 표시할 내용
    <body>
        <!--웹 페이지에 표시할 내용 적기-->
        <p>나의 첫 번째 웹 페이지</p>
    </body> 

//2.html 끝                                                       
</html>



1-2장>
태그: '<태그명>'
속성: 태그에 의미를 보충하는 역할 '<태그명 속성명="속성값">' ex)<html lang="ko">
문법:
- 콘텐츠가 있는 문법: <title>My first Web Page!</title> 시작테크/콘텐츠/종료테그
- 콘텐츠가 없는 문법: <br> 빈 테그

--> HTML 문법을 이루는 가장 작은 단위: 태그

- 줄 바꿈 & 들여쓰기 제대로 하는 것이 가독성에 좋음 
<!--
<html lang="ko">
    <head>
        <!--head 내용 생략-->
    </head>
    <body>
        <!--body 내용 생략-->
    </body>
<!--
</html>
-->