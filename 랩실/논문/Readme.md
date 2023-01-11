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
![논문 구성도](/img/논문 구성도.png)
<br>
 1. 기존 데이터를 통해 1명의 감염자가 몇 명을 감염시켰는지에 대한 계보 데이터로 변환   
 2. 과거의 전파 사례를 통해 한 명의 보균자가 얼마나 많은 사람에게 바이러스를 전파할 수 있는지에 대해서 극한 수치 이론을 적용하여 통계적으로 추정
 3. 대중교통을 통해서 이동하는 승객에 대한 데이터를 바탕으로 몇 명의 피감염자가 타 지역에 새롭게 생길 수 있는지에 대한 시뮬레이션 연구를 수행
