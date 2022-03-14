

$(document).ready(function (){
    setInterval(function(){
        orderNotification()
        orderListView()
        orderCount()
    });
})

function orderNotification(){
    var url = 'http://127.0.0.1:8000/api/orderNotify/'

    var request = new XMLHttpRequest();
    request.onreadystatechange = function(){
        if (this.readyState == 4 && this.status == 200){
            var data = JSON.parse(request.responseText)
            var div = document.getElementById('orderNotify')
            div.innerHTML = "";
            for (var i=0; i< data.length; i++){
                
                div.innerHTML = '<div class="toast align-items-center" role="alert" aria-live="assertive" aria-atomic="true"><div class="d-flex"><div class="toast-body">' + data[i].message + '</div><button type="button" class="btn-close me-2 m-auto" data-bs-dismiss="toast" aria-label="Close"></button></div></div>')
                console.log(data[i].message)
            }
            
        }
    };
    request.open("GET", url, true);
    request.send()
}




function orderCount(){
    var url = 'http://127.0.0.1:8000/api/showorders/'

    var request = new XMLHttpRequest();
    request.onreadystatechange = function(){
        if (this.readyState == 4 && this.status == 200){
            var data = JSON.parse(request.responseText)
            
            document.getElementById('orderCount').innerHTML = data.length
            
            console.log(data.length)
        }
    };
    request.open("GET", url, true);
    request.send()
}





function orderListView(){
    var url = 'http://127.0.0.1:8000/api/showorders/';
    var data_body = document.getElementById('data_body')
    data_body.innerHTML = "";

    var request = new XMLHttpRequest();
    request.onreadystatechange = function(){
        if (this.readyState == 4 && this.status == 200){
            var data = JSON.parse(request.responseText)

          
            for (var i=0; i< data.length; i++){
                var row = data_body.insertRow(i);
                var count = 
                id = row.insertCell(0)
                user = row.insertCell(1)
                ordered = row.insertCell(2)
                payment_method = row.insertCell(3)
                cartitems = row.insertCell(4)
                orderStatus = row.insertCell(5)
                created = row.insertCell(6)

                id.innerHTML = data[i].id
                user.innerHTML = data[i].user['username']
                ordered.innerHTML = data[i].ordered
                payment_method.innerHTML = data[i].payment_method
                
                x_item = "";
                for (j in data[i].cartitems){
                    x_item += data[i].cartitems[j].item.name + "<br>"
                    console.log(x_item)
                }
                cartitems.innerHTML = x_item
                orderStatus.innerHTML = data[i].status
                created.innerHTML = data[i].created

        }
         

        data_body.className = 'table table-striped'
        data_body.appendChild(table);
        

        }
    };

    request.open("GET", url, true);
    request.send()
    
}











