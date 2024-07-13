
p_xrayImage = document.getElementById('p_xrayImage');

imageChecker = document.getElementById("imageChecker")
output = document.getElementById('output')

p_xrayImage.addEventListener('change', function(event) {
    output.textContent ="";
  
    var file = event.target.files[0];
  
  
    var reader = new FileReader();
  
    reader.onload = function(e) {
      var image = new Image();
    
      image.src = e.target.result;
      displayImage.src = e.target.result;
      displayImage.classList.add("display", "display-block");
  
      image.onload = function() {
        var width = this.width;
        var height = this.height;
        if (width >400 && width <1000 && height >400 && height <1000){
            btn = document.getElementById("btn");
            btn.disabled = false;
            btn.style.display="block";
            imageChecker.textContent = "";
        }
        else{
            btn = document.getElementById("btn");
            btn.disabled = true;
            btn.style.display="none";
            imageChecker.textContent = "image is not eceptable..... ";
        }
  
      };
    };
  
    reader.readAsDataURL(file);
  });