# Car_Crawling_Danawa
- 다나와 차량 크롤링 데이터(http://auto.danawa.com/)
- 해당 크롤링데이터는 MK.Corp 의 변무영 대표님의 오더로, 제작하였습니다.
- 해당 데이터의 목적은 OASIS Item의 전체 공간 소독시, 차량의 부피 측정을 위한 데이터 수집용 코드입니다.   
   
***
## 1. 제공되는 정보
```
- Context = 차량의 정보
- 제공되는 정보 : 전장,전폭,전고,축거 (mm)
```   
***
## 2. Data File
- data Folder : 차량 정보를 수집한 data File 입니다. 
```
- CSV File로 10000번 단위마다 Save 됩니다.
```   
***

## 3. Graph File
- Graph Folder : 각종 시각화를 진행하였던 Graph Folder 
```
- 현재 Clustering 관련 png 및 html 파일만 존재.
```   
***
## 4. Python Files

- CarCrawler : 차량 정보 수집. (2021-02-21)
- carDataSet : 수집된 차량정보를 정리하고, (소,중,대,승합)순으로 정리. (2021-02-23)

***   
## 5. R Files
- cluster : R을 활용하여, 간단한 k-means cluster를 진행. (2021-02-23)
- Cluster-2 : 1차 Cluster 진행및 수정된 Data를 바탕으로 3차원 Cluster 진행. (2021-02-24)

### 5.1 1차 Clustering
#### 5.1.1 R-Data Processing
```
- NA값 제거 및 기타 데이터 수집시 잘못된 차량데이터들 Delete.(해당 차량이 유용하지 않은 차량명이라 판단.)
- NA값 제거시, 확인결과 대부분 이미 같은 차량명이 존재 하였음. 그에따라, NA값을 갖고있는 Data를 Delete. 
- 차량의 세부분류 없이 차량명이 일치 할경우 해당 차량명끼리의 평균값(mean)으로 전폭,전고,전장을 다시 Remake.(Aggregate 부분)
```
#### 5.1.2 R-Clustering
```
- Clustering 진행시, 부피에 따른 Cluster 진행. 따라서, 새로운 vh라는 변수를 생성하였음.
- vh는 (전장 * 전폭)으로 (가로 * 세로)로 만든 넓이 데이터임.
- vh와 전고(높이)로 부피 관련 K-means Clustering을 진행.
- 4개의 Cluster로 진행함(소형,중형,대형,기타를 생각하고 진행.)
- Cluster 결과 일부 잘 분류가 진행되었다고 판단되었으나, 트럭과 같은 변수들은 제거 하고 다시 Cluster 하기로 하였음.
```
   
   #### 5.1.3 R 결과
   - 1차(트럭과 같은 변수 제거전)   
       <img src="/graph/Before_delete.png" title="1차 K-Means Clusters" alt="First Cluster"></img><br/>   
   ```
   1. 총 4개의 Cluster.
   2. 1번 Cluster의 쏠라티,마운티,카운티,메가트럭 변수 제거 예정.
   3. 3번에 포함되어있는 마이티와 같은 트럭 변수는 제거 예정.
   4. 다시 2,3,4번의 Cluster로 재분류 할 예정.
   ```   
***
   
   ### 5.2 2차 Clustering
#### 5.2.1 R-Data Processing
```
- 트럭, 포터, 마이티와 같은 차량 제거
- Normalize(MinMaxScaling) 혹은 StandardScaling을 통해 정규화 진행
```
#### 5.2.2 R-Clustering
```
- 3차원 Clustering 진행.
- 두가지 정규화중 MinMaxScaling로 정규화 진행.
- 최적 군집수를 판별하여 Clustering.
```
   
   #### 5.2.3 R 결과   
   - 2차   
      
         
      <img src="/graph/After_delete_3DScatterPlot.png" href ="/graph/After_delete_3DScatterPlot.html" title="1차 K-Means Clusters" alt="First Cluster"></img><br/> 
      ```
      1. 해당 그래프의 3D Interactive Graph 위치 
        - /graph/After_delete_3DScatterPlot.html
      2. 기존 2차원으로 vh변수를 만들어 진행하였을때보다 잘 분류됨.
      3. 추후, 실제 데이터와 차량 군집의 Mapping하여 재분류 및 Cluster 들과의 관계성 파악필요.
      ```
***
 
### Create At 2021-02-21
- Update : 2021-02-23(1차 Cluster)
- Update : 2021-02-23(2차 Cluster 및 변수 제거) 
