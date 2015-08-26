
// json format
//	words = {
//			{text: '八仙', size: 120},
//	}

function draw_word_cloud(json) { 
	
	var width = 450 ;
	var height = 250;
	
	var datas = json.datas
	var fill = d3.scale.category20();
	
	var lScale = d3.scale.linear()    //SCALE尺度設定
	.domain([
	         d3.min(datas,function(d) { 	return d.size;	})
	         ,d3.max(datas,function(d) { 	return d.size;	})
	         ])
	.range([30,75])	  
	
	 d3.layout.cloud().size([width*0.8, height])
	      .words(datas  )
	      .rotate(function() { return ~~(Math.random() * 2) * 90; })
	      .font("Impact")
	      .fontSize(function(d) { return lScale( d.size) ; })//note!!
	      .on("end", draw)
	      .start();

	drawVisualization(datas[0].text);
	
  function draw(words) {
    d3.select("#hotwordcloud").append("svg")
        
    	.attr("width", width*1.1)
        .attr("height", height)
        .style("border", "solid white 1px")
        //.style("margin-left", "60px")
        .append("g")
        .attr("transform", "translate(150,150)")
        
	   .selectAll("a")
	    .data(words)
	    .enter().append("a")
	    .attr({"xlink:href": "#"})
//    .on("click", function(d, i){ 
////        d3.select(this) 
////            .attr({"xlink:href": "http://example.com/" + d});
//    	alert(d.text);
//    	drawVisualization(d.text);
//    })
        
      .selectAll("text")
        .data(words)
      .enter().append("text")
        .style("font-size", function(d) { return d.size + "px"; })
        .style("font-family", "Impact")
        
        .style("margin", "10px")
        
        .style("fill", function(d, i) { return fill(i); })
        .attr("text-anchor", "middle")
        .attr("transform", function(d) {
          return "translate(" + [d.x, d.y] + ")rotate(" + d.rotate + ")";
        })
        .text(function(d) { return d.text; })
            .on("click", function(d, i){ 
//        d3.select(this) 
//            .attr({"xlink:href": "http://example.com/" + d});
	    	
	    	drawVisualization(d.text);
    })
        ;
  }
 }