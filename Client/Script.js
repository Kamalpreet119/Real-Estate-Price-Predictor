function onPageLoad(){
    //A Function to call some routines when the HTML Page is loaded
    console.log("Document loading");
    var url="http://127.0.0.1:5000/get_location_names";//HTTP Call
    $.get(url,function(data,status){//Making get call to the same URL
        console.log("Got response for get_location_names request");
        if(data){
            var locations=data.locations;
            var uiLocations=document.getElementById("uiLocations");
            $('#uiLocations').empty();
            for(var i in locations){//Iterating through the locations one by one and Adding in the drop-down
                var opt=new Option(locations[i]);
                $('#uiLocations').append(opt);
            }
        }
    });
}

window.onload=onPageLoad;

function getBathValue(){//Iterating through Button Bar and give back the value of Bath
    var uiBathrooms=document.getElementsByName("uiBathrooms");
    for(var i in uiBathrooms){
        if(uiBathrooms[i].checked){
            return parseInt(i)+1;
        }
    }
    return -1;//Invalid Value
}
  
function getBHKValue(){//Iterating through Button Bar and give back the value of BHK
    var uiBHK=document.getElementsByName("uiBHK");
    for(var i in uiBHK){
        if(uiBHK[i].checked){
            return parseInt(i)+1;
        }
    }
    return -1;// Invalid Value
}

function onClickedEstimatePrice(){
    console.log("Estimate Price Button Clicked");
    //Fetching values
    var sqft=document.getElementById("uiSqft");
    var bhk=getBHKValue();
    var bathrooms=getBathValue();
    var location=document.getElementById("uiLocations");
    var estPrice=document.getElementById("uiEstimatedPrice");
  
    var url="http://127.0.0.1:5000/predict_house_price";
    
    //Jquery Post Call
    $.post(url,{
        total_sqft:parseFloat(sqft.value),
        bhk:bhk,
        bath:bathrooms,
        location:location.value
    },function(data,status) {
        console.log(data.estimated_price);
        estPrice.innerHTML="<h2>"+data.estimated_price.toString()+" Lakh</h2>";
        console.log(status);
    });
}
  