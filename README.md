# 🐾 공냥 프롬프트 킷 VOL.2

**막연한 한마디를 gpt-image-2 완성 프롬프트로 컴파일하는 Claude Code 스킬.**

![공냥 프롬프트 킷 VOL.2 키비주얼](docs/main.png)

"포스터 하나 만들어줘" 수준의 요청을 받아, 바로 생성에 넣을 수 있는 완성 한국어 프로덕션 프롬프트를 만든다. 1,000장 규모의 라이브러리·화보·포스터·만화를 뽑으며 검증한 규칙을 스킬 하나로 정리했다. 위 키비주얼도 이 킷으로 컴파일한 프롬프트(C11 시네마틱 키아트)로 생성한 것이다.

> 인터랙티브 데모: **[kimsh-1.github.io/gongnyang-prompt-kit](https://kimsh-1.github.io/gongnyang-prompt-kit)**

## 빠른 시작

```bash
git clone https://github.com/kimsh-1/gongnyang-prompt-kit
ln -s "$PWD/gongnyang-prompt-kit/skills/image-prompt" ~/.claude/skills/image-prompt
```

Claude Code에서 "이미지 프롬프트 써줘", "화보 프롬프트", "키아트" 같은 트리거나 `/image-prompt`로 실행한다.

- 심볼릭 링크로 설치하면 레포 업데이트가 자동 반영된다. 복사로 설치했다면 업데이트마다 다시 복사해야 한다.
- 검증기 실행에는 Node.js가 필요하다.

## 무엇을 하나

![컴파일 데모 — 거친 요청 → 완성 프롬프트 → 검증기 통과](docs/hero.gif)

거친 요청 → 완성 프롬프트 → 검증기 통과. 이 세 단계가 스킬 안에서 끝난다.

| 입력 | 출력 |
|---|---|
| "봄밤 야시장 포스터 하나 만들어줘" | 장면·카메라·조명·팔레트(HEX)·텍스트 배치까지 지정된 완성 프롬프트 + `AR 4:5` |

이미지 생성 자체는 이 스킬의 범위 밖이다. 대량 생성·병렬 스폰은 [codex-fleet](https://github.com/kimsh-1/codex-fleet)의 `codex-imagegen` 스킬을 쓰고, 한 장이면 `codex`에 직접 넣는다. (생성까지 하려면 [Codex CLI](https://github.com/openai/codex) 로그인 + ChatGPT Plus/Pro가 필요하다.)

## 생성 예시 — 한마디가 이렇게 된다

아래 24컷 전부, 각 이미지 좌하단 칩에 적힌 한마디가 사람이 입력한 전부고, **이미지 줄 바로 아래 행이 킷이 실제로 모델에 넣은 인입 프롬프트 전문**이다 — 한마디가 스킬을 거치면 어떻게 달라지는지 그대로 보면 된다. 마지막 두 줄은 v2.2 변수 축 시연이다. 특히 "빗자루" 세 컷은 **입력이 완전히 같고 사조 축(M1/M3/M10)만 다르다**. 컴파일 레코드 원본은 [`examples/showcase.jsonl`](examples/showcase.jsonl).

| | | | |
|---|---|---|---|
| ![화보 한 장](docs/showcase/SC01.webp) | ![립밤 광고컷](docs/showcase/SC02.webp) | ![재즈바 포스터](docs/showcase/SC03.webp) | ![이어폰 도감](docs/showcase/SC04.webp) |
| <sub>**“화보 한 장”** → 한국 여성 모델의 룩북 전신 컷, 상업 패션 카탈로그 완성도. Scene: 미색 스튜디오 배경 앞에 선 20대 한국 여성 모델, 오버사이즈 울 코트에 니트 셋업, 자연스러운 워킹 포즈, 프레임 안엔 인물 한 명 단독. Camera: 전신 세로 구도, 눈높이, shallow DoF, background falls off softly. Lighting: 큰 소프트박스 정면광과 옅은 림, long soft-edged shadows. Color grading: 웜 아이보리 #F7F4EC, 카멜 #C19A6B, 잉크 #1C1A17. Texture/Medium: natural skin texture, visible pores, subtle film grain, 울 원단의 결. AR 2:3</sub> | <sub>**“립밤 광고컷”** → 립밤 제품 히어로 매크로, 상업 뷰티 광고 완성도. Scene: 젖은 유리 표면 위에 세워진 민트색 립밤 스틱 하나, 주위로 튀어오른 물방울과 얇은 물결, 제품 표면에 맺힌 이슬. Camera: 매크로 근접, 제품 정중앙, 배경은 부드럽게 흐려진다. Lighting: 클린 스튜디오광, 하이라이트는 하얗게 날아가지 않게, 투명한 젖은 반사. Color grading: 민트 #BFE8DE, 화이트 #FAFAFA, 딥그린 #1E4D40. Texture/Medium: 물방울 매크로 물리, 유리 반사, 미세 그레인. AR 1:1</sub> | <sub>**“재즈바 포스터”** → 한국어 재즈바 포스터, 상업 인쇄 완성도. Scene: 상단 1/3 타이틀 밴드, 중앙에 콘트라베이스 연주자의 딥블루 실루엣 일러스트와 담배연기 같은 얇은 곡선, 하단 캡션 밴드. 정돈된 매거진 여백. Camera: 정면 평면 구성, 중앙 정렬, 풀블리드. Lighting: 무대 스포트라이트 하나가 실루엣 뒤에서 번지는 글로우. Color grading: 미드나잇 #101A2E, 크림 #F3EEE2, 브라스 골드 #C9A24B. Texture/Medium: 매트 아트지, 미세 그레인, 인쇄 톤. Text-in-image: headline "밤과 재즈" 상단 중앙(굵은 세리프, 크림), caption "매주 금·토" 하단 중앙(콘덴스드 산세리프, 골드). All text appears once, perfectly legible — no duplicate text, no extra words, no invented glyphs, no watermark. AR 4:5</sub> | <sub>**“이어폰 도감”** → 무선 이어폰 분해 도감 컷, 산업 디자인 도록 완성도. Scene: 딥네이비 무대 중앙에 이어폰 한 쪽이 수직으로 분해되어 떠 있는 exploded view — 하우징, 드라이버 유닛, 기판, 배터리가 층층이 정렬. 각 부품에서 헤어라인 리더선이 뻗어 작은 플로팅 라벨 박스로 이어진다. Camera: 정면 아이소메트릭 느낌의 평면 구성, 중앙 정렬. Lighting: 부드러운 톱라이트, 부품 금속면에 절제된 스펙큘러. Color grading: 딥네이비 #0F1D30, 실버 #C9CDD4, 민트 라인 #5EEAD4. Texture/Medium: 양극산화 금속·수지 재질 매크로, 클린 벡터 라벨. Text-in-image: callout "드라이버" 좌중 라벨 박스, callout "배터리" 우중 라벨 박스. All text appears once, perfectly legible — no duplicate text, no extra words, no invented glyphs, no watermark. AR 3:4</sub> |
| ![향수 캠페인](docs/showcase/SC05.webp) | ![커피 인포그래픽](docs/showcase/SC06.webp) | ![절약 카드뉴스](docs/showcase/SC07.webp) | ![그래놀라 패키지](docs/showcase/SC08.webp) |
| <sub>**“향수 캠페인”** → 향수 런칭 캠페인 포스터, 하이엔드 코스메틱 광고 완성도. Scene: 아침 안개 낀 은방울꽃 수풀 사이에 반쯤 잠긴 유리 향수 보틀 하나, 보틀 위로 맺힌 이슬, 상단은 타이틀용 여백. Camera: 로우앵글 근접, 보틀 중앙, 배경 수풀은 부드럽게 흐려진다. Lighting: 새벽 백라이트가 보틀 유리를 투과하는 글로우, 옅은 안개 산란. Color grading: 포그 그린 #DCE8DC, 크리스탈 #F6F8F6, 딥 포레스트 #24402E. Texture/Medium: 유리 굴절, 이슬 매크로, 미세 필름 그레인. Text-in-image: headline "MUGUET" 상단 중앙(elegant thin serif, wide letter-spacing, 딥 포레스트). All text appears once, perfectly legible — no duplicate text, no extra words, no invented glyphs, no watermark. AR 4:5</sub> | <sub>**“커피 인포그래픽”** → 핸드드립 커피 4단계 인포그래픽, 에디토리얼 다이어그램 완성도. Scene: 크림 캔버스에 세로 플로우 — 라운드 카드 4개가 위에서 아래로 이어지고 카드 사이는 가는 화살표. 각 카드 안에 플랫 일러스트(원두, 그라인더, 드리퍼, 잔). 상단 타이틀 밴드. Camera: 정면 평면, 중앙 정렬, 풀블리드. Lighting: 균등광, 옅은 카드 그림자. Color grading: 크림 #F5EFE6, 로스트 브라운 #6B4A32, 테라코타 #C2714F. Texture/Medium: 매트 벡터 평면, 종이 질감. Text-in-image: headline "한 잔의 순서" 상단 밴드 중앙(굵은 산세리프), 카드 라벨 위에서 아래로 "원두", "분쇄", "추출", "한 잔" 각 카드 하단(중간 굵기 산세리프). All text appears once, perfectly legible — no duplicate text, no extra words, no invented glyphs, no watermark. AR 2:3</sub> | <sub>**“절약 카드뉴스”** → SNS 카드뉴스 커버, 핀테크 에디토리얼 완성도. Scene: 소프트 옐로 평면 위에 커다란 동전 저금통 플랫 일러스트, 동전 하나가 떨어지는 순간, 좌상단에 타이틀 블록, 우하단에 페이지 인디케이터 점 3개. 읽기 여백이 넉넉한 매거진 레이아웃. Camera: 정면 평면, 풀블리드. Lighting: 균등광, 일러스트에 옅은 오프셋 그림자. Color grading: 소프트 옐로 #FFE9A8, 잉크 #1F2430, 코럴 #F2695C. Texture/Medium: 매트 벡터 평면, 종이 톤. Text-in-image: headline "하루 만 원 룰" 좌상단(굵은 산세리프, 잉크), subhead "한 달 30만 원" 그 아래 절반 크기(코럴). All text appears once, perfectly legible — no duplicate text, no extra words, no invented glyphs, no watermark. AR 1:1</sub> | <sub>**“그래놀라 패키지”** → 그래놀라 브랜드 패키지 목업, 상업 제품 사진 완성도. Scene: 밝은 오크 테이블 위 크라프트 파우치 패키지 하나, 주위에 흩어진 귀리와 견과 약간, 뒤로 아침 창가 흐림. 파우치 전면엔 심플한 산 모양 라인 로고와 라벨 영역. Camera: 정면 45도, 제품 중앙, shallow DoF. Lighting: 아침 창가 자연광, 부드러운 사이드 섀도. Color grading: 크라프트 #C8A878, 크림 #F5EFE2, 딥그린 #2E4636. Texture/Medium: 크라프트지 재질, 무광 인쇄 마감, 곡물 매크로. Text-in-image: headline "산아침" 파우치 라벨 중앙(붓 느낌 한글 로고타입, 딥그린). All text appears once, perfectly legible — no duplicate text, no extra words, no invented glyphs, no watermark. AR 1:1</sub> |
| ![로켓 3D 아이콘](docs/showcase/SC09.webp) | ![고양이 4컷 만화](docs/showcase/SC10.webp) | ![SF 키아트](docs/showcase/SC11.webp) | ![럭셔리 시계](docs/showcase/SC13.webp) |
| <sub>**“로켓 3D 아이콘”** → 로켓 3D 앱 아이콘, 클레이 렌더 완성도. Scene: 파스텔 그라데이션 배경 중앙에 통통한 클레이 질감 로켓 하나, 둥근 창과 미니 화염, 살짝 기울어 떠 있는 포즈. 글자 없는 단일 오브젝트 클린 구성. Camera: 정면 3/4, 오브젝트 중앙. Lighting: 소프트 스튜디오 3점광, 부드러운 접지 그림자. Color grading: 파스텔 스카이 #CDE4F5, 코럴 #F58A7A, 크림 #FFF5EA. Texture/Medium: 매트 클레이 표면, 부드러운 베벨, 미세 SSS 느낌. AR 1:1</sub> | <sub>**“고양이 4컷 만화”** → 고양이 일상 4컷 만화 한 페이지, 출판 퀄리티. Scene: 2x2 grid of four panels, equal gutters, 읽기 방향 좌상→우상→좌하→우하. Panel 1: establishing shot, 식탁 밑에서 눈만 내민 검은 고양이. Panel 2: close-up, 간식 봉지를 바라보는 반짝이는 눈, 말풍선 "간식?". Panel 3: 집사의 단호한 손가락, 말풍선 "안돼". Panel 4: reaction shot, 바닥에 녹아내린 고양이, 과장된 절망 이펙트 선. Camera: 컷마다 앵글 변화, 클린 칸 구성. Lighting: 플랫 셀 셰이딩, 옅은 스크린톤 그림자. Color grading: 웜 화이트 #FFF8EE, 잉크 #26221E, 머스터드 #E8B54D. Texture/Medium: 깔끔한 잉킹 선화, soft cel shading, 스크린톤. All text appears once, perfectly legible — no duplicate text, no extra words, no invented glyphs, no watermark. AR 1:1</sub> | <sub>**“SF 키아트”** → Cinematic science-fiction key art. Scene: a lone explorer in a weathered vac-suit stands on a ridge of black glass dunes, facing a colossal ringed gas giant rising over the horizon; twin moons hang in the upper sky band left empty for a future title; the bottom eighth stays a clean dark band. Camera: ultra-wide vista, tiny human figure against vast scale, deep aerial perspective. Lighting: cold planet-light rim on the dunes, warm suit visor glow as the only warm note, long soft shadows. Color grading: void indigo #101528, glacial teal #6FB5AE, ember amber #D98A4B. Texture/Medium: cinematic grain, faint dust haze drifting across the ridge. AR 16:9</sub> | <sub>**“럭셔리 시계”** → 수동 크로노그래프 손목시계 에디토리얼 컷, 하이엔드 매거진 완성도. Scene: 회색 석회암 판 위에 놓인 시계 하나, generous negative space dominating the frame, subject occupying under one third, 곁에 마른 유칼립투스 가지 하나. Camera: 탑다운에서 살짝 기운 앵글, shallow DoF. Lighting: soft directional daylight with long gentle shadows, 케이스 금속에 절제된 하이라이트. Color grading: muted ivory field #F5F1E8, ink #1C1A17, taupe accent #8C7B6B. Texture/Medium: matte uncoated paper grain, 석재 결, 사파이어 글라스 반사. AR 4:5</sub> |
| ![비 오는 골목](docs/showcase/SC14.webp) | ![미니멀 텀블러](docs/showcase/SC15.webp) | ![타이포 전시 포스터](docs/showcase/SC16.webp) | ![대시보드 히어로](docs/showcase/SC17.webp) |
| <sub>**“비 오는 골목”** → Single frame from a film, a rainy Seoul back alley at night. Scene: a lone figure with a translucent umbrella walks away from camera down a narrow alley, storefront light spilling across wet pavement, steam rising from a vent. Camera: shallow DoF with background falling off softly, low over-the-shoulder tracking distance. Lighting: warm key from a doorway against cool shadow pools, faint drifting haze catching the light. Color grading: deep shadow #0E1420, warm highlight #D9A566, steel-blue midtone #4A6670. Texture/Medium: fine photographic grain, subtle anamorphic-style horizontal flare, rain streaks catching light. AR 16:9</sub> | <sub>**“미니멀 텀블러”** → 스테인리스 텀블러 제품 히어로. Scene: product hero on a seamless white stage #FAFAFA, perfectly clean single-subject composition, 세이지 그린 무광 텀블러 하나가 정중앙에 수직으로. Camera: 정면 눈높이, 제품이 프레임 하단 2/3를 차지. Lighting: soft top-light with one crisp contact shadow anchoring the object, polished surface reflections kept subtle. Color grading: 화이트 #FAFAFA, 세이지 #9DB4A0, 잉크 #111111. Texture/Medium: true-to-material 무광 파우더코팅 질감, 매끈한 금속 림. AR 1:1</sub> | <sub>**“타이포 전시 포스터”** → 타이포그래피 전시 포스터, 모더니스트 인쇄 완성도. Scene: strict modernist grid layout, oversized grotesque sans-serif type as the dominant visual element, flat off-white field #F2F2EF, 대형 타이틀이 좌상단에서 시작해 그리드를 가로지르고, 우하단에 작은 정보 블록, one signal-red accent #E63329 원형 도형 하나가 타이틀과 겹친다. asymmetric composition with disciplined alignment. Camera: 정면 평면, 풀블리드. Lighting: 균등한 인쇄 평면광. Color grading: 오프화이트 #F2F2EF, 블랙 #111111, 시그널 레드 #E63329. Texture/Medium: flat matte print finish, 옅은 종이 결. Text-in-image: headline "형태와 여백" 대형(black weight 산세리프, 블랙), caption "3.14 — 4.20" 우하단 소형(모노스페이스). All text appears once, perfectly legible — no duplicate text, no extra words, no invented glyphs, no watermark. AR 2:3</sub> | <sub>**“대시보드 히어로”** → SaaS 대시보드 히어로 그래픽. Scene: near-black canvas #0B0D12, hairline borders instead of shadows, 중앙에 살짝 기울어 떠 있는 대시보드 UI 카드 3장 — 추상 막대·블록·스파크라인 도형으로만 구성, one restrained mint glow accent #5EEAD4 이 메인 차트 라인을 따라 흐른다. dark technical premium mood, crisp UI-card surfaces floating with subtle depth. Camera: 정면에서 살짝 부감, 카드 중앙 정렬. Lighting: 민트 글로우 발광과 카드 에지의 헤어라인 하이라이트. Color grading: 니어블랙 #0B0D12, 민트 #5EEAD4, 딤 그레이 #8B93A7. Texture/Medium: 매트 다크 평면, 유리 느낌 카드 표면, 미세 그레인. AR 16:9</sub> |
| ![다방 성냥갑](docs/showcase/SC18.webp) | ![워크숍 배너](docs/showcase/SC19.webp) | ![연말 초대장](docs/showcase/SC20.webp) | ![사르르 의성어 타이포](docs/showcase/SC21.webp) |
| <sub>**“다방 성냥갑”** → vintage Korean offset-print poster 스타일의 성냥갑 디자인 컷. Scene: 바랜 크림 배경 위에 놓인 레트로 성냥갑 하나, 갑면에는 김이 오르는 커피잔 일러스트와 태양 방사선 무늬, visible halftone dots and slight ink misregistration. Camera: 정면 탑다운, 성냥갑 중앙, 주위에 성냥개비 두어 개. Lighting: 균등한 스캔 느낌 평면광, 옅은 드롭 섀도. Color grading: aged cream paper #E8DCC4, vermilion #B33A2B, indigo-blue #274A78 spot inks. Texture/Medium: worn paper texture at the edges, 오프셋 망점, 접힘 자국. Text-in-image: headline "청자다방" 갑면 상단 아치형(bold brush-stroke Korean headline, 주홍). All text appears once, perfectly legible — no duplicate text, no extra words, no invented glyphs, no watermark. AR 1:1</sub> | <sub>**“워크숍 배너”** → 어린이 메이커 워크숍 웹 배너, 에디토리얼 일러스트 완성도. Scene: warm white canvas #FFF9F2, rounded card shapes tinted in soft peach #FFD9C7, mint #CDE8DE and lavender #D9D2F0, 중앙에 flat friendly illustration style with simple geometric characters — 아이 캐릭터 셋이 블록·로봇·물감으로 무언가를 만드는 장면, 좌측 1/3은 빈 여백. Camera: 정면 평면, 풀블리드. Lighting: even soft lighting. Color grading: 웜 화이트 #FFF9F2, 피치 #FFD9C7, 민트 #CDE8DE, 라벤더 #D9D2F0. Texture/Medium: paper-smooth matte finish, 플랫 벡터 셰이프. AR 16:9</sub> | <sub>**“연말 초대장”** → 연말 갈라 초대장, 레터프레스 인쇄 완성도. Scene: deep navy field #101A2E, embossed gold-foil motifs #C9A24B catching a soft raking light — 중앙 상단에 월계수 리스와 별 모티프, 중앙에 타이틀 영역, 하단에 가는 골드 라인 오너먼트, letterpress paper texture with debossed line ornaments. Camera: 정면 탑다운 평면, 중앙 대칭. Lighting: 사선 raking light가 금박 엠보스를 따라 반짝임. Color grading: 딥 네이비 #101A2E, 골드 포일 #C9A24B, 크림 #F3EEE2. Texture/Medium: 코튼지 레터프레스 눌림, 금박 스펙큘러, ceremonial premium finish. Text-in-image: headline "초대합니다" 중앙(elegant thin serif 느낌의 한글 명조, 크림), caption "12.31 7PM" 하단 중앙 소형(골드). All text appears once, perfectly legible — no duplicate text, no extra words, no invented glyphs, no watermark. AR 2:3</sub> | <sub>**“사르르 포스터”** → 디저트 카페 포스터 — 녹아내리는 한글 타이포그래피가 주인공. Scene: 크림색 필드 상단 2/3를 커다란 한글 레터링 '사르르'가 차지하고, 하단에 따뜻한 팬 위 버터 한 조각이 작게 놓인 구성. letterforms melting like butter on a warm pan: edges softening and gently drooping, the last syllable dissolving into a thin glossy pool beneath the baseline, weight thinning from first glyph to last. Camera: 정면 평면 그래픽 구성, 중앙 정렬, 포스터 풀블리드. Lighting: soft even studio glow, 균일하고 부드러운 인쇄 광. Color grading: warm butter yellow #F2B705, cream field #FFF9F2, toasted brown accent #B8722C. Texture/Medium: matte print finish with subtle paper grain, glossy highlights kept to the melted pool. Text-in-image: headline "사르르" 상단 중앙(두툼한 라운드 한글 레터링, 버터 옐로). All text appears once, perfectly legible — no duplicate text, no extra words, no invented glyphs, no watermark. AR 4:5</sub> |
| ![빗자루 — M1 바우하우스](docs/showcase/SC22.webp) | ![빗자루 — M3 멤피스](docs/showcase/SC23.webp) | ![빗자루 — M10 와비사비](docs/showcase/SC24.webp) | ![소풍 로고 — T4 네거티브 스페이스](docs/showcase/SC25.webp) |
| <sub>**“빗자루”** → 생활용품 브랜드 컨셉 포스터 — 빗자루 한 자루의 바우하우스 재해석. Scene: 기하 프리미티브로 재구성된 빗자루 — 자루는 완전한 원기둥, 솔은 정삼각형 블록, 오프화이트 필드 위 그래픽 포스터 구성, 프레임 안엔 빗자루 하나 단독. Bauhaus-inspired composition of geometric primitives — circle, triangle, square — functionalist grid, form strictly following function. Camera: 정면 그래픽 뷰, 비대칭 중앙 배치, 여백 40%. Lighting: flat even poster light, 한 방향의 긴 플랫 섀도 하나. Color grading: primary red #E63329, yellow #F2B705, blue #1D4E89 on off-white field #F2F2EF. Texture/Medium: flat matte screen-print finish, 미세한 인쇄 그레인. AR 1:1</sub> | <sub>**“빗자루”** → 생활용품 브랜드 컨셉 포스터 — 빗자루 한 자루의 멤피스 재해석. Scene: 삐딱하게 기운 빗자루가 화면 중앙, 주변에 스퀴글·지그재그·점 패턴이 흩어진 팝 구성, 프레임 안엔 빗자루 하나 단독. Memphis design language — tilted playful geometry, squiggles and zigzag patterns, deliberate mismatch that still reads as one system. Camera: 정면 그래픽 뷰, 기울어진 대각 배치. Lighting: flat even pop light, 그림자는 오프셋된 플랫 컬러 블록. Color grading: clashing pink #F25C9B, teal #20B2AA, yellow #F2B705 with bold black outlines #111111 on warm white #FFF9F2. Texture/Medium: flat pop finish, 매트 벡터 일러스트 질감. AR 1:1</sub> | <sub>**“빗자루”** → 생활용품 브랜드 컨셉 사진 — 수제 나무 빗자루의 와비사비 재해석. Scene: 손으로 엮은 수수 빗자루 한 자루가 화면 오른쪽 아래에 조용히 기대어 있고, 비대칭 여백이 프레임을 지배하는 구성, 프레임 안엔 빗자루 하나 단독. wabi-sabi restraint — asymmetric emptiness dominating the frame, natural imperfection kept visible: uneven bristles, raw wood grain, hand-tied cord. Camera: 정면에서 살짝 비낀 앵글, 피사체는 프레임 하단 1/3, shallow DoF로 배경이 부드럽게 물러남. Lighting: 창가의 낮은 사선 자연광, long quiet shadows. Color grading: earthen neutrals #B8AD9E #6E6558 on undyed field #F0EBE2. Texture/Medium: quiet handmade finish, 자연 섬유와 나무 결의 질감, 미세 필름 그레인. AR 1:1</sub> | <sub>**“소풍 로고”** → 피크닉 브랜드 워드마크 컨셉 보드. Scene: 따뜻한 종이 필드 중앙에 한글 워드마크 '소풍' 단독 — a tiny kite silhouette subtly hidden inside the round counterspace of the final "ㅇ", discovered on the second look; every other stroke kept clean and geometric. Camera: 정면 평면 로고 프레젠테이션 구도, 워드마크가 프레임 중앙 1/3 폭, 넉넉한 여백. Lighting: soft even paper light, 균일한 문서 촬영 광. Color grading: single ink #111111 on warm paper field #F5F1E8, 연에만 민트 포인트 #5EEAD4. Texture/Medium: letterpress paper texture, 잉크의 미세한 눌림과 번짐. Text-in-image: wordmark "소풍" 중앙(클린 지오메트릭 한글 산세리프, 잉크 블랙). All text appears once, perfectly legible — no duplicate text, no extra words, no invented glyphs, no watermark. AR 1:1</sub> |

### 스킬 전후 — 같은 요청, 같은 모델

똑같은 gpt-image-2에 요청만 다르게 넣었다. **왼쪽은 사람이 친 한 줄 그대로, 오른쪽은 그 한 줄을 킷이 컴파일한 프롬프트**다. 각 이미지 하단 칩에 실제 들어간 입력이 그대로 적혀 있다.

| 스킬 없이 — `파도 타이포그래피 포스터` | 킷 컴파일 — T1 움직임 번역 |
|---|---|
| ![스킬 없이 — 파도 타이포그래피 포스터](docs/showcase/SC26B.webp) | ![킷 컴파일 — 파도, T1 움직임 번역](docs/showcase/SC26.webp) |

<details>
<summary>SC26 컴파일 프롬프트 전문</summary>

```
타이포그래피 아트 포스터 — 파도의 에너지를 실은 한글 레터링이 유일한 피사체. Scene: 옅은
포말빛 필드 전면을 거대한 한글 레터링 '파도'가 채우는 구성. letterforms carrying the surge
of a breaking wave: thick brush strokes swelling and curling upward with momentum, stroke tips
bursting into fine white spray droplets, the baseline rolling like a swell, deep-sea ink
gradating to foam white inside each stroke — the lettering is the only subject in the frame,
all of the wave's energy living inside the strokes. Camera: 정면 평면 포스터 구성, 레터링이
프레임의 80%를 차지하는 과감한 스케일. Lighting: 균일한 인쇄 광, 획 안쪽에만 깊이감 있는 톤
변화. Color grading: deep sea ink #1D4E89, midnight undertone #101A2E, foam white #F5F8FA,
시안 스프레이 포인트 #5EEAD4. Texture/Medium: 두꺼운 스크린프린트 잉크 질감, 획 가장자리의
미세한 물보라 입자. Text-in-image: headline "파도" 화면 중앙(초대형 브러시 한글 레터링,
딥블루). All text appears once, perfectly legible — no duplicate text, no extra words,
no invented glyphs, no watermark. AR 4:5
```

</details>

| 스킬 없이 — `야시장 타이포그래피 포스터, 힙하고 키치하게` | 킷 컴파일 — T3 의도 왜곡 |
|---|---|
| ![스킬 없이 — 야시장 타이포그래피 포스터](docs/showcase/SC27B.webp) | ![킷 컴파일 — 야시장, T3 의도 왜곡](docs/showcase/SC27.webp) |

<details>
<summary>SC27 컴파일 프롬프트 전문</summary>

```
키치 네온 타이포그래피 포스터 — 의도적으로 왜곡된 한글 레터링이 주인공. Scene: 순흑에 가까운
밤 필드 중앙에 대형 한글 레터링 '야시장' — deliberately distorted lettering: each glyph
sliced horizontally at its waist, the upper half shifted sideways like a mis-registered screen
print, strokes stretched tall and slightly wobbling as if seen through hot night air,
distortion stopping just before legibility breaks. 글자 주변에 네온 사인의 옅은 글로우와 작은
전구 점들이 흩어진 야시장 무드. Camera: 정면 평면 포스터 구성, 레터링이 프레임 70%를 차지.
Lighting: 네온 글로우가 글자 획에서 배어나오는 self-lit lettering, 배경은 딥 섀도. Color
grading: hot pink neon #F25C9B, electric mint offset layer #5EEAD4, warm bulb amber #F2B705,
near-black night field #0B0D12. Texture/Medium: 네온 튜브의 유리 광택과 미세한 헤이즈,
스크린프린트 오프셋의 어긋난 잉크 레이어. Text-in-image: headline "야시장" 중앙(초대형
절단·오프셋 한글 레터링, 핑크+민트 이중 레이어). All text appears once, perfectly legible —
no duplicate text, no extra words, no invented glyphs, no watermark. AR 4:5
```

</details>

다른 컷들의 전체 프롬프트도 전부 [`examples/showcase.jsonl`](examples/showcase.jsonl)에 있다.

## 핵심 규칙

잘 나오게 하는 규칙이 아니라, **안 나오게 만드는 습관을 막는** 규칙이다.

| 규칙 | 이유 |
|---|---|
| **네거티브 기본 금지** | gpt-image-2는 "no crowd" 같은 장면 네거티브를 오히려 그 단어로 렌더한다. 장면 배제는 전부 긍정형 — "프레임 안엔 인물 한 명, 단독". |
| **예외는 화이트리스트 2종뿐** | Tier-1 텍스트 렌더 가드(`no duplicate text` 등 7종, 렌더 텍스트가 있을 때만) · Tier-2 화보 컴플라이언스 페어(명시 선언 시만). 나머지 부정문은 전부 검증기가 잡는다. |
| **앞 브래킷 금지** | size는 API 파라미터다. 프롬프트에는 끝에 `AR x:y` 토큰 하나만 둔다. |
| **글자 배치는 영역 문법** | "상단 1/3 타이틀 밴드", 롤 라벨(headline/subhead/callout), 따옴표 카피 고정. 밀집 텍스트는 quality high와 페어링. |
| **장비 스펙 → 결과 서술** | 모델은 `Canon R5 f/1.4`를 모른다. "shallow DoF, background falls off softly"처럼 결과로 쓴다. |
| **SD 품질태그·죽은 단어 금지** | `masterpiece, 8k`도, "예쁘게·고급스럽게·어워드 수준으로"도 노이즈다. 기준이 프롬프트 밖에 있으면 평균값만 나온다 — 수치·몸 반응·구체 예시로 환원한다. |
| **수치를 박는다** | HEX 팔레트, 켈빈, `key:fill 1:2` — 수치가 품질을 올린다. |
| **1행 = 1컷 = 1 호출** | 한 캔버스에 여러 컷을 그리드로 그리지 않는다. (카드뉴스처럼 그리드 자체가 산출물인 경우만 예외.) |

## 두 가지 포맷

| | Format A — 라벨 6섹션 | Format B — 화보 플랫 콤마형 |
|---|---|---|
| **구조** | Scene / Camera / Lighting / Color grading / Texture / Text-in-image | 피사체→얼굴→헤어→장르앵커→장면→의상→구도→조명→팔레트 `#HEX`→질감을 콤마로 잇는 한 문장 |
| **용도** | 포스터·키아트·인포그래픽·도감 등 구조물 전반 | 단독 인물 화보·에디토리얼 전용 |

## 카테고리 C1~C12

패션/화보 · 뷰티 · 한국어 포스터 · 제품 도감 · 캠페인 · 인포그래픽 · 카드뉴스 · 브랜딩 목업 · 3D 아이콘 · 만화/웹툰 · 시네마틱 키아트 · **프레젠테이션 덱(신규)**. 컷타입과 기본 AR은 `references/category-patterns.md`에 있다.

"있어보이게"는 감으로 조립하지 않는다 — `references/look-presets.md`의 **룩 프리셋 8종**(럭셔리 에디토리얼·시네마틱 그레이드·미니멀 프로덕트·스위스 타이포·다크 테크·레트로 인쇄·파스텔·골드 포일)에서 골라 드롭인한다.

시안을 여러 개 벌리거나 컨셉부터 잡을 땐 `references/concept-axes.md`의 **변수 축**을 쓴다 — 미학 사조 10종(바우하우스~와비사비, 조형언어 분해 드롭인), 몸 반응 번역("고급스럽게" 대신 "목소리를 낮추고 조용히 보게 되는"), 모순쌍 레이어 분리, 음악·장면→컬러 번역, 타이포 아트 4기법(위 [스킬 전후](#스킬-전후--같은-요청-같은-모델) 비교가 T1·T3 실물이다). 같은 피사체를 축 하나로 스윕하면 양산 컨셉 시안이 나온다.

## 검증기

작성한 프롬프트가 규칙을 지켰는지 자동으로 검사한다. 티어를 인지해서 화이트리스트 밖 네거티브만 잡는다.

```bash
node skills/image-prompt/scripts/check_prompt.mjs examples/poster.txt      # 텍스트 모드
node skills/image-prompt/scripts/check_prompt.mjs --tier 2 examples/hwabo_formatB.txt
node skills/image-prompt/scripts/check_prompt.mjs --jsonl examples/prompts.sample.jsonl
node skills/image-prompt/scripts/check_prompt.mjs --test                   # 회귀 셀프테스트
```

`{ok, format, tier, errors, warnings}` JSON을 반환한다. 화이트리스트 밖 네거티브·앞 브래킷·SD 폐기어휘·사이즈락 위반·슬롯 토큰 잔존은 `error`(긍정형 rewrite 힌트 포함), 빈 형용사·HEX 누락 등은 `warning`. 통과·실패 샘플은 `examples/`에 있다.

## 구조

![공냥 프롬프트 킷 구조 — 거친 요청 → 스킬 코어 → 레퍼런스 → 완성 프롬프트 → 검증기 → 이미지 생성](docs/architecture.png)

거친 요청이 스킬 코어와 레퍼런스를 거쳐 완성 프롬프트가 되고, 검증기를 통과해야 생성으로 넘어간다. (이 구조도 역시 이 킷으로 컴파일한 C6 인포그래픽 프롬프트로 생성했다.)

```
skills/image-prompt/
├─ SKILL.md                      # 코어 — 워크플로우·철칙·티어 네거티브·포맷 A/B·사이즈락·라우팅
├─ references/                   # 필요할 때만 읽는 깊은 내용
│  ├─ category-patterns.md       #   C1~C12 컷타입·기본 AR·만화 A/B·키아트·덱
│  ├─ look-presets.md            #   프리미엄 룩 프리셋 8종 드롭인
│  ├─ concept-axes.md            #   변수 축 — 사조 10종·몸 반응 번역·모순쌍·컬러 번역·타이포 아트
│  ├─ typography-layout.md       #   영역 문법·롤 라벨·폰트 어휘·정확 문자열·그리드
│  ├─ editorial-hwabo.md         #   화보 Format B·슬롯 12종·컴플라이언스 레인
│  ├─ jsonl-and-examples.md      #   jsonl 스키마·모델 팩트·codex 호출 골격
│  ├─ photo-vocab.md             #   카메라·조명·필름·구도·색 어휘 + 국문/영문 혼용
│  └─ style-taxonomy.md          #   패션 21종 + persona DNA + 마스터 템플릿
└─ scripts/
   ├─ check_prompt.mjs           # 티어 인식 검증기 (--jsonl/--tier/--api/--test)
   └─ fixtures/                  # 회귀 테스트 픽스처
```

SKILL.md에는 항상 로드되는 코어만 두고, 깊은 디테일은 `references/`로 분리했다(progressive disclosure).

## 라이선스

MIT
