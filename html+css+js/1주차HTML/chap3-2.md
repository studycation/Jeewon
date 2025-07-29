3-6>></br>
1.form태그: 폼 양식</br>

    <form action="서버 url" method="get 또는 post"></form>

2.input태그: 로그인 페이지의 아이디와 비밀번호처럼 입력받는 요소를 생성할 때 사용</br>
--> 한 줄짜리 입력 요소 생성/ type 속성: button(버튼), checkbox(체크박스), radio(라디오버튼) 넣을 수 있음

    <input type="종류" name="이름" value="초깃값">

3.label태그: form태그 안에서 사용하는 상호작용 요소에 이름을 붙일 때 사용</br>

    <label>
        아이디
        <input type="text">
    </label>
</br>

    //for 속성값과 id값이 같아야 함
    <label for="userpw">비밀번호</label>
    <input type="password" id="userpw">

    //for 속성값과 id값이 같아야 함
    <label for="username">
    이름
    <input type="text" id="username">
    </label>


4.fieldset과 legend 태그: fieldset를 이용하면 그룹별로 박스 모양의 테두리가 생김</br>
--> 이 그룹을 legend 태그로 이름을 붙일 수 있음

    <form action="#">
        <fieldset>
            <legend>그룹 이름</legend>
            <!--상호작용 요소 생략-->
        </fieldset>
    </form>


5.textarea태그: 여러 줄의 입력 요소  ->  input 대신 textarea로</br>
--> input은 </> 필요 X, textarea는 필요O</br>


6.select태그: 콤보박스 생성  +  항목 추가 시: option태그 사용</br>
--> 항목들을 그룹으로 묶고 싶으면: optgroup태그 사용 </br>
--> size속성: 콤보박스에서 화면에 노출되는 할목 개수 지정</br>
--> multiple 속성: 원래 1개만 선택 가능, BUT 이건 여러개 선택 가능(Ctrl로)</br>
--> selected 속성: 처음 기본 선택 항목 지정 가능


    <select name="city" id="city" size="3" multiple>
        <optgroup label="서울시">
            <option value="강북구">강북구</option>
            <option value="강북구" selected>서초구</option>
        </optgroup>
        <optgroup label="경기도 성남시">
            <option value="중원구">중원구</option>
            <option value="부당구">분당구</option>
        </optgroup>
    </select>

</br>
7.button 태그: input태그는 type,name,value 로 나타낼 수 있는데 .. --> button태그만 따로 만들 수도 있음!!</br>
--> 마찬가지로 type 속성값 가짐

    <button type="submit">
        <img src="facebook.png" alt="페이스북 버튼>
        페이스북에 등록하기
    </button>

</br>
***폼 관련 태그에서 공통으로 사용할 수 있는 것</br>
1.disabled 속성: 태그가 비활성화 됨</br>
    
    <input text="text" disabled>
    <button type="button" disabled>비활성</button>

2.readonly 속성: 읽기 전용으로 변경</br>

    <input type="password" readonly>
    <textarea readonly></textarea>

3.maxlength 속성: 글자 수 제한</br>

    <input type="url" maxlength="4">
    <textarea maxlength="4"></textarea>

4.checked 속성: 체크박스</br>

    <fieldset>
        <legend>좋아하는 과일</legend>
        <input type="checkbox" id="banana" name="banana" value="banana">
        <label for="banana">바나나</label>
        <input type="checkbox" id="apple" name="apple" value="apple">
        <label for="apple">사과</label>
        <input type="checkbox" id="orange" name="orange" value="orange">
        <label for="orange">오렌지</label>
    </fieldset>


5.placeholder 속성: 박스 안에 뭘 적도록 유도</br>

    <input type="tel" placeholder="전화번호를 입력해 주세요.">


</br></br>
3-7>></br>
1.table 태그: 그냥 전체적인 양식</br>
2.caption 태그: 표 제목</br>
--> 반드시 table 태그 안에서 첫 번째로 작성해야 함

    <table>
        <caption>표 제목</caption>
    </table>

3.tr 태그: 행(가로) 생성</br>
--> 태그 하나 == 행 하나

    <table>
        <tr></tr>
    </table>

4.th, td 태그:</br>
--> 제목을 나타내는 데이터: th태그</br>
--> 나머지 데이터를 나타내는 열: td태그</br>


5.rowspan, colspan 속성: 병합(행이나 열끼리 병합)</br>

6.thead, tfoot, tbody 태그: 행(가로)을 묶어서 그룹화</br>
--> thead 태그로 그룹화? -> th 태그로 열을 생성

    <table>
        <thead>
            <tr>
                <th>번호</th>        <!--th-->
                <!--생략-->
            </tr>
        </thead>
        <tfoot>
            <tr>
                <td>총 금액</td>      <!--td-->
                <!--생략-->
            </tr>
        </tfoot>
        <tbody>
            <tr>
                <td>1</td>            <!--td-->
                <td>콜라</td>
                <!--생략-->
            </tr>
        </tbody>
    </table>


7.col과 colgroup 태그: 열 전체를 그룹화 해서 통일된 스타일 적용

    <col>
    <colgroup span="그룹화 할 열의 개수">


8.scope 속성: 표 제목에만 th할 수 있었는데, 이를 통해서</br>
--> /th scope="row"> 로 써서 제목처럼 써줄 수 있음

    <table>
        <tr>
            <th scope="col">구분</th>
            <th>중간고사</th>
            <th>기말고사</th>
        </tr>
        <tr>
            <th scope="row">전공</th>
            <td>A+</td>
            <td>A</td>
        </tr>
        <tr>
            <th scope="row">교양</th>
            <td>B+</td>
            <td>A+</td>
        </tr>
    </table>


----->>> table태그만 있으면 표 완성X: 표의 틀만 완성O</br>
----->>> tr태그: 표의 행(가로) 생성</br>
----->>> th, td태그: 열 생성  +   th 태그: 표의 제목 생성 // td 태그: 표의 내용(?)</br>
----->>> thead, tfoot, tbody 태그: 표의 행(가로) 그룹 지을 때 사용</br>
