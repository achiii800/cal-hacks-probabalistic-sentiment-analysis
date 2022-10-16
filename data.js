const button = document.getElementById("submit");
button.onclick= function() {
    let ticker = document.getElementById("filterword").value;
    
    console.log(ticker)
    const request = new XMLHttpRequest()
    request.open('POST',`/ProcessUserInfo/${JSON.stringify(ticker)}`)
    request.send(); 
        
    }
