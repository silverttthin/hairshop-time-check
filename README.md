### 만들게 된 배경
- 매번 머리 자르려하면 2-3주간 미용실 예약이 꽉 찼는데 수시로 예약취소 시간대가 생겼나 들락나락하다 화가 나서 만들었습니다

- uv, 셀레니움도 배우고 싶어 LLM 러다이트 운동의 일환으로 초심으로 돌아가 스택 오버플로우, 공식문서만을 참고


### todo
- [x] **월 기준 무지성 완탐**: 현재 월의 모든 날짜에 대한 예약 가능 시간대 조회 (휴일, 이미 지난 날짜, 마감 및 예약가능 일 대응)
- [ ] **날짜 범위 지정**: 특정 기간(start, end) 입력받아 거기만 처리
    - [ ] **월 전환 대응**: 다음 달로 넘어갈 때의 calendar DOM 변화 처리
- [ ] **알림 시스템**: 예약 가능 시간 발견 시 알람(아마 카톡 api 사용 예정, 이럼 서버로 만들어야 할듯?)
- [ ] **스케줄러**: 스케줄링 적용(너무 빈번히는 절대 안됨)


## 기타

- 개인적 용도 + 요청횟수 최소로만 (because of robots.txt)

## 도움됐던 글들
1. https://devocean.sk.com/blog/techBoardDetail.do?ID=167420&boardType=techBlog
2. https://wikidocs.net/73539
3. https://www.selenium.dev/documentation/webdriver/waits/
4. https://stackoverflow.com/questions/21713280/find-div-element-by-multiple-class-names
5. https://stackoverflow.com/questions/32713009/how-to-check-if-element-contains-specific-class-attribute
6. https://stackoverflow.com/questions/64887947/how-to-use-nested-selenium-selectors
 
