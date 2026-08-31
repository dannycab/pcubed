(function () {
  var root = document.documentElement;

  function sync() {
    var theme = root.getAttribute("data-theme") || "light";
    var fontSize = root.getAttribute("data-font-size") || "md";
    document.querySelectorAll("[data-theme-choice]").forEach(function (btn) {
      btn.setAttribute("aria-pressed", String(btn.dataset.themeChoice === theme));
    });
    document.querySelectorAll("[data-fontsize-choice]").forEach(function (btn) {
      btn.setAttribute("aria-pressed", String(btn.dataset.fontsizeChoice === fontSize));
    });
  }

  document.addEventListener("DOMContentLoaded", function () {
    sync();

    var toggle = document.getElementById("a11y-toolbar-toggle");
    var panel = document.getElementById("a11y-toolbar-panel");

    toggle.addEventListener("click", function () {
      var expanded = toggle.getAttribute("aria-expanded") === "true";
      toggle.setAttribute("aria-expanded", String(!expanded));
      panel.hidden = expanded;
    });

    document.querySelectorAll("[data-theme-choice]").forEach(function (btn) {
      btn.addEventListener("click", function () {
        var theme = btn.dataset.themeChoice;
        root.setAttribute("data-theme", theme);
        localStorage.setItem("pcubed-theme", theme);
        sync();
      });
    });

    document.querySelectorAll("[data-fontsize-choice]").forEach(function (btn) {
      btn.addEventListener("click", function () {
        var fontSize = btn.dataset.fontsizeChoice;
        root.setAttribute("data-font-size", fontSize);
        localStorage.setItem("pcubed-font-size", fontSize);
        sync();
      });
    });
  });
})();
