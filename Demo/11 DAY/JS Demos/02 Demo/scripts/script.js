const refDiv = document.getElementById('output')

function showAlert()
{
  window.alert("You clicked on a button!")
}

function openWindow()
{
  // window.open('home.html')
  window.open('https://www.google.com','_blank','width=400,height:300')

}

function reloadPage()
{
   location.reload()
}

function logNavigator()
{
  refDiv.innerHTML = `<pre>
  App Name: ${navigator.appName}
  User Agent: ${navigator.userAgent}
  Online: ${navigator.onLine}
  Platform: ${navigator.platform}
  Language: ${navigator.language}
  </pre>
  `;
}

function logLocation()
{
  refDiv.innerHTML = `<pre>
  URL: ${location.href}
  Host: ${location.host}
  Pathname: ${location.pathname}
  </pre>`;
}

function goBack(){
  history.back()
}

function logScreen()
{
 refDiv.innerHTML = `<pre>
    Screen Width: ${screen.width}
    Available Height: ${screen.availHeight}
    Color Depth: ${screen.colorDepth}
    Pixel Depth: ${screen.pixelDepth}
  </pre>`;
}