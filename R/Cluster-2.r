#Global Options
options(scipen = 999)

##packages
require(cluster)
require(dplyr)
require(data.table)
require(ggplot2)
require(plotly)

#Working Directory Set
dir=paste(getwd(),'/GitHub/Car_Crawling_Danawa/data',sep="")

#Read Csv for DATA
data = fread('1.for_kmeans_df.csv')[,-1] %>% as.data.frame()

data %>% head()


#Delete 1-Cluster(4EA) likes del_car
del_car <- c('포터','마이티','트럭')

delete_function <- function(data,del_car){
  for(num in 1:length(del_car)){
    if(grep(del_car[num],data$차명))
    data <- data[-grep(del_car[num],data$차명),]
  }
  return(data)
}

update_data <- delete_function(data,del_car)


##MinMax Scaling(Normalize) or StandardScale
normalize <- function(x) {
  return((x-min(x))/(max(x)-min(x)))
}

update_data$scale_전장 <- normalize(update_data$전장)
update_data$scale_전폭 <- normalize(update_data$전폭)
update_data$scale_전고 <- normalize(update_data$전고)
# update_data$Scale_전장 <- scale(update_data$전장)
# update_data$Scale_전폭 <- scale(update_data$전폭)
# update_data$Scale_전고 <- scale(update_data$전고)


##Table
table(update_data$cluster)


#plot
plot(update_data)


#Kmeans Clustering
data_kmeans = kmeans(update_data[,c("scale_전고", "scale_전폭",'scale_전장')], 5) 


#Counter Cluster
table(data_kmeans$cluster)


#add K-Means-Cluster to df$cluster
update_data$cluster <- data_kmeans$cluster %>% as.character


#ggplot
plot_ly(data=update_data, x=~전장, y=~전폭, z=~전고, type="scatter3d", mode="markers", color=~cluster,text=~차명)

