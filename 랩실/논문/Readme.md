# 국내 코로나 확진자 데이터 분석을 통한 지역 간 감염 전파 시뮬레이션 연구 (A simulation study on the COVID-19 infection spread in Korea using infection database)

## Abstract
COVID-19과 같은 바이러스 전염병의 확산은 보균자의 지역 간 이동을 통해서 일어나곤 한다. 본 연구는 시뮬레이션 연구를 통해 2019년에 비해서 큰 폭으로 감소한 2020년의 대중교통을 이용한 지역간의 이동이 전염병의 확산에 어떤 영향을 미쳤는지 살펴본다. 예비 연구의 단계에서는 질병관리청에서 발표한 감염자-피감염자의 쌍에 대한 정보를 바탕으로 트리구조의 감염 계보를 생성하고, 한 명의 보균자가 확률적으로 몇 명의 피감염자를 발생시키는가에 대한 확률 분포가 두 개의 확률 분포의 중첩의 형태로 되어있음을 확인한다. 주 연구인 시뮬레이션 연구에서는 한국철도공사에서 제공하는 여객 승하차 데이터를 이용해 서울-부산간 대중 교통 이용량을 추정하고, 포아송 과정을 이용한 시뮬레이션 연구를 수행하였다. 이를 통해 2019년에 비해서 약 3배가 줄어든 2020년의 대중교통 이동량이 전염 수치에 대해 큰 차이를 가져오는 것을 확인할 수 있다. 이는 당국의 이동 자제 권고와 국민들의 수준높은 협조가 전염병의 확산을 저지하는데 큰 역할을 하고 있음을 의미한다. 


### Dataset

> KCDC에서 발표한 감염 사례 데이터셋

|    **Variable**    |                                                            **Description**                                                           |
|:------------------:|:------------------------------------------------------------------------------------------------------------------------------------:|
|   **patient_id**   | ex) 1000000001, 1000000002                                                                                                           |
|       **sex**      | male or female                                                                                                                       |
|       **age**      | ex) 20s, 30s, 40s,...                                                                                                                |
|    **province**    | ex) Seoul, Kyunggi-do, Pusan,...                                                                                                     |
|      **city**      | ex) Nowon-gu, Suwon-si, Saha-gu,...                                                                                                  |
| **infection_case** | group infection event (NaN if individual infection) ex) overseas inflow, Milal Shelter,                                              |
|  **infsected_by**  | patient_id of individual infection source (NaN if group infection event or infection source unknown)  ex) 2002000001, 1000000002,... |
| **confirmed_date** | the date when infection is confirmed by authority (YYYY-MM-DD)                                                                       |

<br>

> 국내 기차 탑승 데이터

|  **Variable** |             **Description**             |       **Example**      |
|:-------------:|:---------------------------------------:|:----------------------:|
|   **RUN_DT**  | Date                                    | 20200101               |
|   **STN_CD**  | Station code                            | 924, 39023             |
| **STN_CD_NM** | Station name                            | Seoul, Yongsan, Anyang |
| **ABRD_PRNB** | Number of people on board               | 387, 19702             |
| **COFF_PRNB** | Number of people getting off the train  |                        |


<br>


### 논문 구성도

<p align="center">
 <img src = "./img/논문 구성도.png">
</p>

<br>

 1. 기존 데이터를 통해 1명의 감염자가 몇 명을 감염시켰는지에 대한 계보 데이터로 변환   
 2. 과거의 전파 사례를 통해 한 명의 보균자가 얼마나 많은 사람에게 바이러스를 전파할 수 있는지에 대해서 극한 수치 이론을 적용하여 통계적으로 추정
 3. 대중교통을 통해서 이동하는 승객에 대한 데이터를 바탕으로 몇 명의 피감염자가 타 지역에 새롭게 생길 수 있는지에 대한 시뮬레이션 연구를 수행



### 감염경로 계보 생성

<p align="center">
 <img src = "./img/계보 생성.png">
</p>

<br>
KCDC 데이터셋은 감염자(infected_by)-피감염자(patient_id)의 형태의 쌍대 데이터로 정리되어 있기에 본질적인 전파 메커니즘에 해당하는 네트워크 구조를 쉽게 판단할 수 없음 
&rarr;
네트워크 구조를 복원

- infected_by 변수의 값이 비어있는 확진자의 경우는 최초 감염자로 분류
- 최초 감염자가 마지막으로 감염시킨 확진자가 나오는 기간 동안 총 몇 명을 감염시켰는지 계산



### 감염 계보 분석

<p align="center">
 <img src = "./img/데이터 분석.png">
</p>
<br>

> 10대 이하 감염자의 비율은 계보 트리에서 낮아질수록 높은 감염 확률을 보임

생산 인구 연령대의 이동량은 감소X   &nbsp; &nbsp; &nbsp; why)산업지구(가산디지털단지, 종로) 이동량 그대로
<br>
&rarr; 10대 이하 감염자들은 가정에서 부모들로부터 감염되는 경우가 많다
<br>
&rarr; 20-50대의 인구의 사회활동을 제한하는 것은 힘든 일이기에 이들에 대한 적극적인 방역 지원 조치가 바이러스의 확산을 막는데에 결정적
<br>


> 타지역으로의 감염 184건 중 140건의 경우가 서울, 인천 경기도의 수도권 지역내에 일어난 감염

수도권은 인구가 밀집된 구역일 뿐만 아니라 수도권에 거주하는 인구들은 생활 반경이 넓고, 일상적으로 이동하기 때문에 이와 같은 결과가 일어난 것으로 추정
<br>
&rarr; 수도권에서의 방역 실패는 전국적 대유행을 야기시킬 수 있다는 것을 의미


### 감염 확률 분포 함수 추정

> 최초 감염자가 1주일간 감염시킨 사람들의 수
<p align="center">
 <img src = "./img/기존 분포.png">
</p>
<br>

- 평균 4.7명의 확진자, 중간값은 3.5명, Q3 7명, 최대값은 49명
- 오른쪽으로 극단적으로 꼬리가 긴 분포
- X축 주간 감염강도가 낮은 경우 분포가 종형의 모습, 일정 주간 감염강도 이상에서는 분포가 완만히 감소 

&rarr;  **극한 수치 이론 (Extreme Value Theory, EVT) 적용** : 주간감염강도 7명을 기준으로 하여 2개의 독립적인 분포함수를 추정하고 이를 중첩하는 형태로 모형화

- 이유
    1. 관찰할 수 있듯이 7명을 기준으로 두 개의 다른 패턴이 관찰
    2. 7명은 평균적으로 매일 1명에 해당하므로 직관적
    3. 결과적으로 모델링된 분포가 위의 실험 관찰값을 잘 설명

<br>

> 추정한 주간 전파율 분포들
<p align="center">
 <img src = "./img/추정한 주간 전파율 분포.png">
</p>
<br>

- 1주일간 7명 이하 “normal case”(87.21%) vs 이상 "Extreme case"(12.79%)

- normal case
    * 평균 3.24명, 중간값 3.50명, 표준편차 2.13명
    * 좌우로 대칭이며 종형의 모습을 보이기에 **정규분포**로 근사

- Extreme case
    * 평균 14.76명, 중간값 11.26명, 표준편차 8.32명
    * 극단적이게 오른쪽으로 skewed
    * 형상 매개변수(shape parameter)의 수치는 1.046이며 척도 매개변수(scale parameter)는 7.915인 **와이블 분포**로 추정

> 추정한 분포와 실제 분포 비교
<p align="center">
 <img src = "./img/분포 비교.png">
</p>
<br>

|  **범위**  | **[0, 1]** | **(1,3]** | **(3,5)** | **(5,7]** | **(7, inf]** |
|:----------:|:----------:|:---------:|:---------:|:---------:|:------------:|
| **Actual** |     63     |     94    |    107    |     70    |      49      |
|  **Model** |     41     |    110    |    118    |     56    |      58      |


통계 검정의 결과로서 자유도 16, 유의확률 0.220 &rarr; 반적인 신뢰수준에서 유의하지 않음



### 감염 확률 분포 함수 추정

> 코로나 발발 전 vs 후 서울발 부산행 이동 승객 수 
<style type="text/css">
.tg  {border-collapse:collapse;border-spacing:0;}
.tg td{border-color:black;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;
  overflow:hidden;padding:10px 5px;word-break:normal;}
.tg th{border-color:black;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;
  font-weight:normal;overflow:hidden;padding:10px 5px;word-break:normal;}
.tg .tg-0pky{border-color:inherit;text-align:left;vertical-align:top}
</style>
<table class="tg">
<thead>
  <tr>
    <th class="tg-0pky"></th>
    <th class="tg-0pky"></th>
    <th class="tg-0pky"></th>
    <th class="tg-0pky"></th>
    <th class="tg-0pky"></th>
    <th class="tg-0pky"></th>
    <th class="tg-0pky"></th>
    <th class="tg-0pky"></th>
  </tr>
</thead>
<tbody>
  <tr>
    <td class="tg-0pky"></td>
    <td class="tg-0pky"></td>
    <td class="tg-0pky"></td>
    <td class="tg-0pky"></td>
    <td class="tg-0pky"></td>
    <td class="tg-0pky"></td>
    <td class="tg-0pky"></td>
    <td class="tg-0pky"></td>
  </tr>
  <tr>
    <td class="tg-0pky"></td>
    <td class="tg-0pky"></td>
    <td class="tg-0pky"></td>
    <td class="tg-0pky"></td>
    <td class="tg-0pky"></td>
    <td class="tg-0pky"></td>
    <td class="tg-0pky"></td>
    <td class="tg-0pky"></td>
  </tr>
  <tr>
    <td class="tg-0pky"></td>
    <td class="tg-0pky"></td>
    <td class="tg-0pky"></td>
    <td class="tg-0pky"></td>
    <td class="tg-0pky"></td>
    <td class="tg-0pky"></td>
    <td class="tg-0pky"></td>
    <td class="tg-0pky"></td>
  </tr>
  <tr>
    <td class="tg-0pky"></td>
    <td class="tg-0pky"></td>
    <td class="tg-0pky"></td>
    <td class="tg-0pky"></td>
    <td class="tg-0pky"></td>
    <td class="tg-0pky"></td>
    <td class="tg-0pky"></td>
    <td class="tg-0pky"></td>
  </tr>
  <tr>
    <td class="tg-0pky"></td>
    <td class="tg-0pky"></td>
    <td class="tg-0pky"></td>
    <td class="tg-0pky"></td>
    <td class="tg-0pky"></td>
    <td class="tg-0pky"></td>
    <td class="tg-0pky"></td>
    <td class="tg-0pky"></td>
  </tr>
  <tr>
    <td class="tg-0pky"></td>
    <td class="tg-0pky"></td>
    <td class="tg-0pky"></td>
    <td class="tg-0pky"></td>
    <td class="tg-0pky"></td>
    <td class="tg-0pky"></td>
    <td class="tg-0pky"></td>
    <td class="tg-0pky"></td>
  </tr>
  <tr>
    <td class="tg-0pky"></td>
    <td class="tg-0pky"></td>
    <td class="tg-0pky"></td>
    <td class="tg-0pky"></td>
    <td class="tg-0pky"></td>
    <td class="tg-0pky"></td>
    <td class="tg-0pky"></td>
    <td class="tg-0pky"></td>
  </tr>
  <tr>
    <td class="tg-0pky"></td>
    <td class="tg-0pky"></td>
    <td class="tg-0pky"></td>
    <td class="tg-0pky"></td>
    <td class="tg-0pky"></td>
    <td class="tg-0pky"></td>
    <td class="tg-0pky"></td>
    <td class="tg-0pky"></td>
  </tr>
  <tr>
    <td class="tg-0pky"></td>
    <td class="tg-0pky"></td>
    <td class="tg-0pky"></td>
    <td class="tg-0pky"></td>
    <td class="tg-0pky"></td>
    <td class="tg-0pky"></td>
    <td class="tg-0pky"></td>
    <td class="tg-0pky"></td>
  </tr>
  <tr>
    <td class="tg-0pky"></td>
    <td class="tg-0pky"></td>
    <td class="tg-0pky"></td>
    <td class="tg-0pky"></td>
    <td class="tg-0pky"></td>
    <td class="tg-0pky"></td>
    <td class="tg-0pky"></td>
    <td class="tg-0pky"></td>
  </tr>
  <tr>
    <td class="tg-0pky"></td>
    <td class="tg-0pky"></td>
    <td class="tg-0pky"></td>
    <td class="tg-0pky"></td>
    <td class="tg-0pky"></td>
    <td class="tg-0pky"></td>
    <td class="tg-0pky"></td>
    <td class="tg-0pky"></td>
  </tr>
</tbody>
</table>