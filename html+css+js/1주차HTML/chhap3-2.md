3-6>>
1.form태그: 폼 양식
<body>

    <form action="서버 url" method="get 또는 post"></form>

2.input태그: 로그인 페이지의 아이디와 비밀번호처럼 입력받는 요소를 생성할 때 사용
-> type,name,value 속성 존재/ type 필수 & 나머지는 선택
<body>

    <input type="종류" name="이름" value="초깃값">

3.label태그: form태그 안에서 사용하는 상호작용 요소에 이름을 붙일 때 사용
<body>

    <label>
        아이디
        <input type="text">
    </label>

    //for 속성값과 id값이 같아야 함
    <label for="userpw">비밀번호</label>
    <input type="password" id="userpw">

    //for 속성값과 id값이 같아야 함
    <label for="username">
    이름
    <input type="text" id="username">
    </label>


