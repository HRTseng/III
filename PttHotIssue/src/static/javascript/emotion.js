
function push_pie(data){
		
		var dataset=[data.upvote,data.normal,data.downvote];
		
		//(1)轉化資料為適合生成圓形圖的物件陣列
		var pie=d3.layout.pie(dataset);
		
		var h=180;
		var w=h;
		
		var outerRadius=w/2;//外半徑
		//(7)圓環內半徑
		var innerRadius=w/4;
		//(2)用svg的path繪製弧形的內置方法
		var arc=d3.svg.arc()//設置弧度的內外徑，等待傳入的資料生成弧度
		.outerRadius(outerRadius)
		.innerRadius(innerRadius)
		;
		
		var svg=d3.select("svg#push_cnt")
				.attr("width",w)
				.attr("height",h);
		//(3)顏色函數
		var color= ['red','blue','limegreen'];//d3.scale.category10();//創建序數比例尺和包括10中顏色的輸出範圍
		var pushtype = ['推','→','噓'];
		//(4)準備分組,把每個分組移到圖表中心
		var arcs=svg.selectAll("g.arc")
		.data(pie(dataset))
		.enter()
		.append("g")
		.attr("class","arc")
		//移到圖表中心
		.attr("transform","translate("+outerRadius+","+outerRadius+")")//translate(a,b)a表示橫坐標起點，b表示縱坐標起點
		
		.on("mouseenter", function(d) { d3.select(this).style("opacity", .7) ;})
		.on("mouseout", function(d) { d3.select(this).style("opacity", 1) ;})
		;
		
		//(5)為組中每個元素繪製弧形路路徑
		arcs.append("path")//每個g元素都追加一個path元素用綁定到這個g的資料d生成路徑資訊
		.attr("fill",function(d,i){//填充顏色
			return color[i];
		})
		.attr("d",arc);//將角度轉為弧度（d3使用弧度繪製）
		
		//(6)為組中每個元素添加文本
		arcs.append("text")//每個g元素都追加一個path元素用綁定到這個g的資料d生成路徑資訊
		.attr("transform",function(d){ 
			return "translate("+arc.centroid(d)+")";//計算每個弧形的中心點（幾何中心）
		})
		.attr("text-anchor","middle")
		.text(function(d,i){
			return pushtype[i]+" :" + d.value;//這裡已經轉為對象了
		})
		 .attr("fill", "white");;
}


