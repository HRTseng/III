
var width = 960,    height = 500

var color = d3.scale.category10();    //顏色區分IFELSE

function colorByGroup(d) { 
	//圓的顏色	
	var num = d.nub/10
	return color(num > 10 ? 10 :num);
}//function colorByGroup
	
function value(d) { 
	return d.value*50; //VALUE長度
}   



function draw_relatived_group (data) {
	alert();
	var svg = d3.select("svg#relatived_group")   //SVG的大小
    .attr("width", width)
    .attr("height", height)
    ;

	var force = d3.layout.force()
	    .gravity(.05)
	    .distance(value)    //調整線的長度
	    .charge(-100)
	    .size([width, height]);
				
				
	force.nodes(data.nodes)
	  	 .links(data.links)
	  	 .start();
	  
	 var raw_data_range = [
							d3.min(data.nodes,function(d) {	return d.nub ;})
							,d3.max(data.nodes,function(d) { return d.nub ;})
							];
					  
	//線的SCALE尺度設定 [min,max] -> [1,6]
	var lScale = d3.scale.linear()    
			.domain(raw_data_range)						
			.range([1,6])	  

	//線的粗細
	var link = svg.selectAll(".link")    
					.data(data.links)
					.enter().append("line")
					.attr("stroke-width", 
					 //粗細是VALUE
					function(d){   return lScale(d.value*5);	}//func
			)
		  .attr("class", "link");
		  

	 var node = svg.selectAll(".node")
		  .data(data.nodes)
		.enter().append("g")
		  .attr("class", "node")
		  .call(force.drag);

	//圓的SCALE尺度設定 [min,max] -> [5,10]
	 var rScale = d3.scale.linear()    
				.domain(raw_data_range)
				.range([5,10])
			
	//圓的SCALE尺度設定		
	var ropScale = d3.scale.linear()    
				.domain(raw_data_range)
				.range([0,1])
		 
	node.append('circle')    //大圓
		//半徑 * 5
		.attr('r',  function(d){  return rScale(d.nub*5);})
			.attr('fill', colorByGroup)    //顏色
			//透明度
			.attr('fill-opacity',  function(d){   return ropScale(d.nub);} )
			.attr('stroke',"black")

	var tScale = d3.scale.linear()    //字體大小的SCALE尺度設定
			.domain(raw_data_range)
			.range([8,13])
			
			
		node.append("text")
			  .attr("dx",  function(d){    //半徑
				
				return -rScale(d.nub*5);
				
			} )
			  .attr("dy", ".35em")
			  .attr("fill", function(d, i) {
						return color(i);
					})    //字體顏色
			  .text(function(d) { return d.name })
			.style("font-size", function(d) { 
			return tScale(d.nub*4) + "px"; });

	  force.on("tick", function() {
		link.attr("x1", function(d) { return d.source.x; })
			.attr("y1", function(d) { return d.source.y; })
			.attr("x2", function(d) { return d.target.x; })
			.attr("y2", function(d) { return d.target.y; });

		node.attr("transform", function(d) {
			return "translate(" + d.x + "," + d.y + ")";     //回傳座標點
		
		});
	  });
}


