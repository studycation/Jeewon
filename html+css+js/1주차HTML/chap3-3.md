3-8>></br>
1.audio 태그: 오디오 파일 삽입

    <audio src="오디오 파일 경로" controls></audio>
    ex.<audio src="Bourree - Joel Cummins.mp3" controls></audio>
</br>
--> controls: 사용자가 제어할 수 있는 패널</br>

2.video 태그

    <video src="비디오 파일 경로" controls></video>
    ex.<video src="sample.mp4" controls></video>
</br>
--> controls: 사용자가 제어할 수 있는 패널</br>

3.source 태그: audio, video 태그에서 리소스(파일)의 경로와 미디어 타입을 명시
</br>
--> 필수는 아니지만 되도록 같이 쓰는 것이 좋음(다양한 포맷에서 사용하기 위해)

    <audio controls>
        <source src="파일경로" type="미디어 타입">
    </audio>
    <video controls>
        <source src="파일경로" type="미디어 타입">
    </video>


3-9>> 시맨틱 태그</br>
1-1.header 태그: 웹 사이트의 최상단 or 좌측, 로고, 검색, 메뉴 같은 요소들 포함

    <header>
        header 구성요소
    </header>

1-2.nav 태그: 웹 페이지에서 내부의 다른 영역 or 외부를 연결하는 링크 영역을 구분

    <nav></nav>

2-1.section 태그: 논리적으로 관련 있는 내용 영역 구분할 때 사용</br>
--> 내용 영역을 구분할 때,,

    <section></section>

2-2.article 태그: 웹 페이지에서 독립적인 영역을 구분할 때</br>
--> ex. 로그인 영역</br>
--> article: 어떤 웹 페이지에서든 독립적으로 사용될 수 있는 영역</br>
--> section: 웹 페이지 안에서 ""관련 있는 내용""을 구분

    <article></article>

3.aside 태그: 주력 내용 or 독립적인 내용을 보기 어려울 때

    <aside></aside>

4.footer 태그: 푸터 영역을 구분할 때 사용 // 일반적으로 최하단에 있음</br>
--> 저작권 정보, 연락처, 사이트 맵 ..
</br>

----->>> p태그: 텍스트 작성할 때 사용하는 논시멘트 태그</br>
----->>> div, span 태그: 태표적인 HTML 논시멘트 태그