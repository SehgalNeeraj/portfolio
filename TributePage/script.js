let body = document.querySelector("#main");
let toggle_btn = document.querySelector(".custom-control-input");
toggle_btn.addEventListener("click", toggleBtn);

function toggleBtn() {
  if (body.classList.contains("light-mode")) {
    body.classList.replace("light-mode", "dark-mode");
    document.getElementById("title-div-light-mode").id = "title-div-dark-mode";
    document.getElementById("tribute-info-light-mode").id =
      "tribute-info-dark-mode";
  } else {
    body.classList.replace("dark-mode", "light-mode");
    document.getElementById("title-div-dark-mode").id = "title-div-light-mode";
    document.getElementById("tribute-info-dark-mode").id =
      "tribute-info-light-mode";
  }
}
