# RDD 생성 → 변환 누적 → 액션 실행 흐름

---

## RDD 생성 단계

parallelize, textFile, binaryFiles로 RDD를 만들면 초기 RDD와 파티션 구조만 결정되고 계산은 실행되지 않는다.

---

## 변환(map, filter 등) 누적 단계

map, filter, flatMap은 파티션에서 어떤 계산을 할지 계획만 등록하며 실제 계산은 하지 않는다.
이 시점까지는 lazy 상태다.

```
rdd2 = rdd.map(...)
rdd3 = rdd2.filter(...)
```

---

## 액션(reduce, collect, count, take 등) 실행 단계

reduce는 RDD 전체를 하나의 값으로 축소하는 집계 연산이며, 동시에 전체 DAG를 실행하는 트리거 역할을 한다.

reduce를 호출하면 다음이 수행된다.

* 원본 데이터 읽기
* 누적된 map/filter/flatMap 계산 수행
* 각 파티션 결과를 reduce 함수로 병합하여 최종 값 생성

---

## 정확한 요약

1. parallelize/textFile/binaryFiles → RDD 생성 및 파티션 결정
2. map/filter → 계산 계획 누적
3. reduce/collect/count/take → 전체 파이프라인 실행
4. reduce → 실행을 트리거하고 집계 결과 반환

---

## 최종 정리

map은 “계획을 쌓는 단계”,
reduce는 “전체 계산을 실행하여 최종 값을 만드는 액션”이다.
