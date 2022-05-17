let id = Math.floor((Math.random() * 19) + 1);
function jsonImage() {
   fetch('item.json')
      .then(response => response.json())
      .then(data => {
         //document.querySelector("#debug").innerText = data.logos[0].logo_link
         var image = data.logos[id].logo_link;
         document.getElementById("picture").src= image;
      })
}