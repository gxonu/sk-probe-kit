# NAND 셀·전하 저장·문턱전압

ID: `M06` · 단계 3 · 출처 확인: 2026-10-30

NAND는 저장 전하가 바꾼 문턱전압 상태로 정보를 구분하고 전원 없이도 보존한다.

## 원리·동작

floating gate는 절연된 도전층, charge trap은 절연막의 포획 상태를 이용한다. 셀들을 직렬로 연결한 string에서 선택 셀의 전도를 판별한다. 설명용 SLC에서는 프로그램된 높은 문턱 상태와 소거된 낮은 문턱 상태를 구분한다.

## 지표·공식과 적용 조건

문턱전압(Vth)과 판독 기준 전압(Vref)은 다르다. 상태는 이상적인 점이 아니라 분포를 갖는다. bit 값과 상태의 대응은 인코딩·제품별로 확인한다.

## 직접 만든 적용 예제

가상 두 상태의 Vth가 0.5 V와 2 V, Vref=1.2 V라면 단순 판별 모델에서 낮은 Vth 셀은 켜지고 높은 Vth 셀은 꺼진다. 실제 읽기 바이어스나 프로그램 전압으로 사용하지 않는다.

## 혼동·적용 한계

비휘발성이 무기한 무오류를 뜻하지 않는다. 모든 3D NAND가 같은 저장막·소거 방법을 사용한다고 가정하지 않는다. 구체적 적층·제조 방식은 4단계 범위다.

## 과제에서 확인할 질문

- 측정값이 Vth 분포인가 읽기 기준 전압인가?
- floating gate/charge trap과 상태 부호화가 명시돼 있는가?

## 출처

- [S41: KIOXIA — What is NAND Flash Memory?](https://www.kioxia.com/en-jp/rd/technology/nand-flash.html)
- [S49: KIOXIA — Analyzing Managed Flash Device Lifetime Reliability Part 1: The Fundamentals of TBW, WAF and NAND Flash Memory Endurance](https://americas.kioxia.com/content/dam/kioxia/en-us/business/memory/mlc-nand/asset/KIOXIA_TBW_WAF_NAND_Endurance_Technical_Brief.pdf)

원리는 공개 출처를 자체 요약했다. 예제·질문은 교육용 작성이며 실제 출제 문제·제품 보증값·권장 설정이 아니다.
