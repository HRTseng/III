google.load("visualization", "1", {packages:["corechart"]});

google.load("visualization", "1", {packages:["timeline"]});
//google.setOnLoadCallback(drawVisualization);
google.setOnLoadCallback(drawTimeLineChart);

function clickKeywordAction(keyword){
	//drawVisualization(keyword);
	//addTimeLineNode(keyword);
	//getIssueLeader(keyword);
	
	$.ajax(
			{
			method: "get",
		           
	        url: "/dajax/data_with_keyword",
	        dataType:"json",
	        data :{'keyword' :keyword,}
			}
	).done(
			function (json){
				
				drawVisualization(json.heatIndexes);
				
				getIssueLeader(json.opinionLeaders);
				
				toggleTimeLineNode(keyword,json);
			}//done action
	
	);
	
}



function drawVisualization( json ) {
  // Some raw data (not necessarily accurate)

	 
	  
	
	
  var data = new google.visualization.arrayToDataTable(json.datas);

  var options = {
    title : json.title,
    
    titleTextStyle:{color: 'white',
		fontName: "微軟正黑體",
		fontSize: "20",
		bold: false,},
	vAxis: {title: "推噓文數",textStyle:{color: 'white',
			fontName: "微軟正黑體",
			fontSize: "14",
			bold: false,},
	titleTextStyle:{color: 'white',
			fontName: "微軟正黑體",
			fontSize: "16",
			bold: false,
			italic: false},},
	hAxis: {title: "時間(day)",textStyle:{color: 'white',
			fontName: "微軟正黑體",
			fontSize: "14",
			bold: false,},
	titleTextStyle:{color: 'white',
			fontName: "微軟正黑體",
			fontSize: "16",
			bold: false,
			italic: false},},
	tooltip: {textStyle:{color: 'black',
	fontName: "微軟正黑體",
	fontSize: "14",
	bold: false,}},
	legend:{textStyle:{color: 'white',
	fontName: "微軟正黑體",
	fontSize: "14",
	bold: false,},
	position: 'in'},
	lineWidth:3,
	seriesType: "bars",
	series: {2: {type: "line"}},
	backgroundColor:"black",
	fontSize:"20",
	fontName:"微軟正黑體",
	//pointSize:3,
	bar:{groupWidth:'70%'},
	chartArea:{left:30,top:40,width:'90%',height:'65%'},
	  };

	  var chart = new google.visualization.ComboChart(document.getElementById('lineChart'));
	  chart.draw(data, options);
}



var timeLineTable = null;
var timeLineChart = null;
var timeLineOptions = null;
function drawTimeLineChart() {
    var container = document.getElementById('timeline');
    timeLineChart = new google.visualization.Timeline(container);
    timeLineTable = new google.visualization.DataTable();

    timeLineTable.addColumn({ type: 'string', id: 'President' });
    timeLineTable.addColumn({ type: 'date', id: 'Start' });
    timeLineTable.addColumn({ type: 'date', id: 'End' });
    


    
	timeLineOptions = {
			avoidOverlappingGridLines:true,
			timeline: { colorByRowLabel: true ,
						rowLabelStyle: {fontName: '微軟正黑體', fontSize: 18, color: 'white' },
						barLabelStyle: {fontName: '微軟正黑體', fontSize: 12, color: 'white' },
			},
			tooltip:{isHtml:true},
			backgroundColor: 'black',
			width:565,
		};
			


    timeLineChart.draw(timeLineTable,timeLineOptions);
 }


function toggleTimeLineNode(name,json){
	
	var idx = nameIndexOf(name);
	if(idx != -1  ){
		if(timeLineTable.getNumberOfRows() ==1){
			return ;
		}
		timeLineTable.removeRow(idx);
		timeLineChart.draw(timeLineTable,timeLineOptions);
	}else{
		var tl = json.timeLine
		
	    timeLineTable.addRow(  [ name,  new Date(tl[0]),  new Date(tl[1]) ]);

	    timeLineChart.draw(timeLineTable,timeLineOptions);
	}
	

    
	

	
	
    function nameIndexOf(name){
    	for (var i = 0;i < timeLineTable.getNumberOfRows();i++){
    		 var n = timeLineTable.getValue(i, 0);
    		 if(name == n){
    		 	return i;
    		 }
    	}
    	return -1;
    }
}

function addTimeLineNode(name ,st_date ,end_date){
	
	$.ajax(
			{
	            method: "get",
	             
	            url: "/dajax/TimeLine",
	            data:{'keyword':name},
	           }//requests
			).done(function (json){
				var tl = json.timeLine
				
			    timeLineTable.addRow(  [ name,  new Date(tl[0]),  new Date(tl[1]) ]);

			    timeLineChart.draw(timeLineTable,timeLineOptions);
				
			})
	
	

}



function getIssueLeader(json ){
	

	var leader = $('div#OpinionLeader');
	
	leader.empty();
	
	var datas = json.authors;
	
	for (var i=0;i< datas.length ;i++){
		var cnt 	= datas[i][0];
		var author 	= datas[i][1];
		var title	= datas[i][2].substring(0,25);
		var art_id = datas[i][3];
		leader.append(
				'<div style="margin:2% 2%;height:37px; font-size:120%">'+
				//'<div class="push" >'+ cnt + '</div>'+
				'<div class="push" style="color:yellow;margin-right:2%;">' + author+'</div>' +
				'<div class="topic" style="margin-left:26%;"><a style="color:white;" href="art_'+art_id+'">' + title+'</a></div>'
				+'</div>'
		);
	}
						

}
