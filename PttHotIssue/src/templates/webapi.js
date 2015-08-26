
function getArticleUpDownVote(art_id ,sussce_callback) {
   $.ajax({
       method: "GET",  
       crossDomain: true,  
       contentType: "application/json",
       url: "http://10.120.30.5:8000/dajax/emotion",
       dataType: 'json',
       data:{'art_id':art_id }
      
     })
       .done(sussce_callback);
	
}

function getHotIssueLineGraph(issue_id ,sussce_callback){
   $.ajax({
       method: "GET",          
       url: "http://10.120.30.5:8000/dajax/hotIssueLine",
       data:{'issue_id':issue_id }
      
     })
       .done(sussce_callback);
}
