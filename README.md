# Car_Crawling_Danawa
- 다나와 차량 크롤링 데이터
- 해당 크롤링데이터는 MK.Corp 의 변무영 대표님의 오더로, 제작하였습니다.
- 해당 데이터의 목적은 OASIS Item의 전체 공간 소독시, 차량의 부피 측정을 위한 데이터 수집용 코드입니다.

### 제공되는 정보
- Context = 차량의 정보
- 제공되는 정보 : 전장,전폭,전고,축거 (mm)

### Python Files
- CarCrawler : 차량 정보 수집하는 JupyterNoteBook File (2021-02-21)
- carDataSet : 수집된 차량정보를 정리하고, (소,중,대,승합)순으로 정리하는 JupyterNoteBook File (2021-02-23)

### R Files
- cluster : R을 활용하여, 간단한 k-means cluster를 진행하였음.
#### R-세부 내용
- NA값 제거 및 기타 데이터 수집시 잘못된 차량데이터들 Delete.(해당 차량이 유용하지 않은 차량명이라 판단.)
- NA값 제거시, 확인결과 대부분 이미 같은 차량명이 존재 하였음. 그에따라, NA값을 갖고있는 Data를 Delete 하였음. 
- 차량의 세부분류 없이 차량명이 일치 할경우 해당 차량명끼리의 평균값(mean)으로 전폭,전고,전장을 다시 Remake.(Aggregate 부분)
- Clusterling 진행시, 부피에 따른 Cluster 진행. 따라서, 새로운 vh라는 변수를 생성하였음.
- vh는 (전장*전폭)으로 (가로*세로)

### Data File
- data Folder : 차량 정보를 수집한 data File 입니다. 
- 형식 : CSV File로 10000번 단위마다 Save 됩니다.

### Create At 2021-02-21
