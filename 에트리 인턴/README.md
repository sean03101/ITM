# 에트리 2021 하계 연수(21.07 ~ 08)


## 스마트 병영 프로젝트 
*    활동 시간 동안 GPS 활용해 이동 거리를 측정한 뒤, 이동에 따른 활동 대사량 측정 

![KakaoTalk_20240719_204443428](https://github.com/user-attachments/assets/fed228fb-df9c-4c20-aa5f-702161ace53e)


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

TDOA 측정을 위한 시간 감산 연산 및 복잡한 비선형 방정식 풀이로 인해 높은 위치 불확실성 발생
<br>
-> TDOA 측정값을 TDOA 이미지로 변환하여, CNN 모델을 통해 TDOA 오류가 추정 결과에 미치는 영향을 축소
![image](https://github.com/user-attachments/assets/755e052d-6750-4a9e-8ca9-8b9b44cbed1c)

### TITT 알고리즘 검증 실험

![image](https://github.com/user-attachments/assets/28bc6cf2-e587-489d-a6ad-19df827c2098)
<br>
실험 결과 장애물이 많은 환경에서 두 모델이 비슷한 기술적 통계를 보이지만, FCNNs 모델의 경우 이상치(Outlier)를 많이 포함
<br>
-> 제안하는 알고리즘을 통해 학습한 모델은 강건한(Robust)한 특성을 가지고 있음

### ICTC 2021 논문 투고
![image](https://github.com/user-attachments/assets/99fca618-45ee-4912-aa37-62ba56d09cd8)
<br>


## 군용 시나리오 제작 & 분석
*    요구사항 : VT-MAK 프로그램 분석을 통해 AI 부관 학습을 위한 다양한 군용 시나리오 제작, 메타 데이터 분석 및 데이터 구축 매뉴얼 작성
*    목표 : 정해진 병력으로 분대를 구성하고 적에 대항하는 시나리오 및 데이터 생성
*    계획
      *    시뮬레이터 환경 구축
      *    각 entity (객체, 환경) 속성 & 객체들 간상호작용 분석
      *    주어진 상황에서 시나리오 제작

### VT-MAK 프로그램 분석
![image](https://github.com/user-attachments/assets/2c17c70a-f599-46e9-b27d-b3d8a2f5ae84)
<br>
![image](https://github.com/user-attachments/assets/1ccdac11-0013-4a0a-b16c-b66119709722)
<br>
![image](https://github.com/user-attachments/assets/8116a21e-9e1c-4854-84aa-2bdd51c4bcc5)
<br>
![image](https://github.com/user-attachments/assets/d018a31a-1e97-4b16-8cc4-23ee88e58a47)


### 워게임 시나리오 구성 및 시나리오 로그 수집

![image](https://github.com/user-attachments/assets/496f2428-f7f7-4b22-8fc8-414dcbf8a368)
<br>
![image](https://github.com/user-attachments/assets/d850a42e-2b32-466d-b394-af268c1bb0ff)


### VT-MAK 사용 메뉴얼 제작
![image](https://github.com/user-attachments/assets/7bffc2a8-dbc9-4eac-84f3-f4c17a25e4b9)


## 그외 기타
![KakaoTalk_20240719_204443428_01](https://github.com/user-attachments/assets/f1d44b5f-3cce-4720-b025-92567e0683ec)
<br>
모션 캡처 시스템(Motion Capture System)을 사용해 무릎 관절 이상 판단 실험 보조


![KakaoTalk_20240719_204443428_02](https://github.com/user-attachments/assets/d85d04b0-0287-4836-ace4-27afa3b29c80)
<br>
카메라를 통해 사용자를 추적하여, 자동으로 운동량 측정하는 프로그램 제작 보조 
