# 에트리 2021 하계 연수(21.07 ~ 08)


## 스마트 병영 프로젝트 
*    활동 시간 동안 GPS 활용해 이동 거리를 측정한 뒤, 이동에 따른 활동 대사량 측정 

### GPS 데이터 수집
*    휴대용 GPS 디바이스를 군복에 넣어두고 하루동안 이동량 측정
*    디바이스를 중앙 컴퓨터에 연결해, 측정한 데이터(.gp) csv 파일로 변형
*    csv 파일 컬럼 : ['ID', 'Date-Time', 'Latitude', 'Longitude']   

### 이동거리 및 활동 대사량 계산
*    파이썬 내 'haversine' 라이브러리를 이용해 하루 동안 이동한 총 거리 계산
*    이때 1초 동안 0.3m 내로 움직일 경우, GPS 오차로 설정하고 계산X
  
*    총 이동 거리를 Harris - Benedict 공식에 의거해 활동 대사량 계산
*    이때 속력이 4m/s 이상이라면 달리는 것이라 판단해 다르게 칼로리 계산


## 딥러닝을 활용한 UWB 실험
*    요구 사항 : 신호 오류가 많이 발생할 수 있는 장애물이 많은 공간에서도 정확하게 신호를 수신 받아 타겟의 정확한 위치를 알고 싶다.
*    목표 : 타겟이 일반적이지 않는 상황(동일한 공간 반복 이동, 결측치 생성)에서 가장 효과적인 알고리즘은 무엇인지 탐구

### 실험 환경 구축
![image](https://github.com/user-attachments/assets/353eb2ec-4876-49af-887d-7fc54a5d6d18)

*    앵커 4개를 이용하여 좌표 공간 생성
*    태그를 이용하여 타겟의 좌표 값 생성 준비
*    CCU (Central Computing Unit)로 사용할 컴퓨터와 앵커와 태그 동기화
*    요구 사항에 맞게 앵커 4개 사이에 통신을 방해할 각종 장애물 설치  

### 측정 좌표 보정 알고리즘 실험 진행
![image](https://github.com/user-attachments/assets/86eaa471-9b33-477c-8901-852d8a80e3d8)

*    타겟의 위치 좌표를 보정해주는 다양한 알고리즘(Naïve Bayes, Clustering 등) 활용
*    알고리즘들을 활용하여 보정된 타겟의 위치 좌표 로그 데이터들을 생성

### 이론 기반 측정 좌표 보정 알고리즘 실험 결과
![image](https://github.com/user-attachments/assets/4417e4a5-64de-4ea1-8d1a-6a432703e3ae)
※ 귀무 : 해당 좌표 값들의 평균은 타겟이 원운동을 했던 중심 좌표이다

*    오차 원인 : TDOA 보정 알고리즘에 상관없이 기기의 오차에 대해 민감하게 반응!
*    극복 방안 : 넓은 공간에서 수행 or 기계의 태생적 오류 극복

### TITT(TDOA image based target tracking)

![image](https://github.com/user-attachments/assets/755e052d-6750-4a9e-8ca9-8b9b44cbed1c)





## 군용 시나리오 제작 & 분석
