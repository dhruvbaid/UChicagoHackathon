$(document).ready(function() {
  $("btn").onClick(function() {
    $("bear-big").fadeOut();
    $("bear-bubble").fadeOut();
  });
});

/*jslint sub: true, maxerr: 50, indent: 4, browser: true */

(function (global) {
  document.getElementById("save").addEventListener("click", function () {
      global.localStorage.setItem("mySharedData", document.getElementById("output").value);
  }, false);
}(window));