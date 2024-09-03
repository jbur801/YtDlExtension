let start = document.getElementById("start")
let ping = document.getElementById("ping")
let status = document.getElementById("status")


var port = null;
const spamPort = ()=>{
    setTimeout(()=>{
        if(port){
            port.postMessage({example: 'Hello from Chrome Extension!'})
            spamPort();
        }else{
            alert('no port')
        }

    },100)
}
start.addEventListener('click', () => {
    alert('trying to open vsCode')
    chrome.runtime.sendNativeMessage('com.ddddd.yt-dlp',{'hello':'world'},console.log('Message sent to native app'))
    port = chrome.runtime.connectNative('com.ddddd.ytdlp');
    onConnect();

    // // const callback =(res)=>alert(res);
    // spamPort();
    port.postMessage({example: 'Hello from Chrome Extension!'})
    onDisconnect();
})

ping.addEventListener('click', () => {
    port ?port.postMessage({example: 'Hello from Chrome Extension!'}):alert('no port')
})



function onDisconnect() {
    if(port){
        port.onDisconnect.addListener(function () {
            port = null;
            if (chrome.runtime.lastError) {
                alert(chrome.runtime.lastError.message);
            }
        });
    }

}

