#Global Options
options(scipen = 999)

##packages
require(cluster)
require(dplyr)
require(data.table)
require(ggplot2)
require(plotly)

##Directory Setting
dir=paste(getwd(),'/GitHub/Car_Crawling_Danawa/data',sep="")
dir = gsub('문서','Documents',dir)
setwd(dir)

#Read Csv All_data
raw.data <- fread('all_data.csv',encoding = 'UTF-8') %>% as.data.frame()
raw.data <- raw.data[,-1]

#head
raw.data %>% head()

#For Cluster
#Data Handling
raw.data$전장 <- raw.data$전장 %>% as.numeric
raw.data$전고 <- raw.data$전고 %>% as.numeric
raw.data$전폭 <- raw.data$전폭 %>% as.numeric
#raw.data$축거 <- raw.data$축거 %>% as.numeric //this isn't needed to us.

#Processing for NA
data = na.omit(raw.data)

## if Car_name is Null, Car_name will be changed by Company_name
Null_car_name <- data$회사[data$차명==""]
data$차명[data$차명==""] <- Null_car_name


#Numeric Values change with Car_name ; Not Company Name. Using by Aggregate
df <- aggregate(전장~차명,data,mean)
df <- merge(df,aggregate(전고~차명,data,mean),by='차명')
df <- merge(df,aggregate(전폭~차명,data,mean),by='차명')

#Round mean Data
df$전장<-round(df$전장)
df$전고<-round(df$전고)
df$전폭<-round(df$전폭)

#가로 x 세로 Data
df$vh <- df$전장*df$전폭

#Plot 
plot(df)

#Kmeans Clustering
##소형/중형/대형/봉고/
df_kmeans = kmeans(df[,c("전고", "vh")], 4) 

#Counter Cluster
table(df_kmeans$cluster)

#add K-Means-Cluster to df$cluster
df$cluster <- df_kmeans$cluster %>% as.character

#ggplot
(car_graph<-ggplot(data=df, aes(x=vh, y=전고, colour=cluster,group = 차명)) + 
  geom_point(shape=19, size=4) + 
  ggtitle("Scatter Plot of CarData' K-means clusters")) %>% ggplotly

write.csv(df,'1.for_kmeans_df.csv')

