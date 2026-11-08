// Mobile navigation toggle, current year in the footer, and the Events gallery.
(function () {
  var btn = document.querySelector(".nav-toggle");
  var nav = document.getElementById("site-nav");
  if (btn && nav) {
    btn.addEventListener("click", function () {
      var open = nav.classList.toggle("open");
      btn.setAttribute("aria-expanded", open ? "true" : "false");
    });
  }
  var y = document.querySelectorAll("[data-year]");
  for (var i = 0; i < y.length; i++) y[i].textContent = new Date().getFullYear();

  var grid = document.querySelector("[data-masonry]");
  if (!grid) return;
  var items = Array.prototype.slice.call(grid.querySelectorAll(".gallery-item"));

  // Masonry: place each photo, in order, into the currently shortest column.
  var current = 0;
  function columnCount() {
    var w = grid.clientWidth;
    return w >= 900 ? 3 : w >= 300 ? 2 : 1;
  }
  function layout() {
    var n = columnCount();
    if (n === current) return;
    current = n;
    var cols = [], heights = [];
    for (var c = 0; c < n; c++) {
      var col = document.createElement("div");
      col.className = "masonry-col";
      cols.push(col);
      heights.push(0);
    }
    items.forEach(function (item) {
      var img = item.querySelector("img");
      var ratio = img.getAttribute("height") / img.getAttribute("width");
      var k = heights.indexOf(Math.min.apply(null, heights));
      cols[k].appendChild(item);
      heights[k] += ratio;
    });
    grid.innerHTML = "";
    cols.forEach(function (col) { grid.appendChild(col); });
    grid.classList.add("is-laid");
  }
  layout();
  var t;
  window.addEventListener("resize", function () { clearTimeout(t); t = setTimeout(layout, 120); });

  // Lightbox with previous/next, keyboard and swipe.
  var box = document.createElement("dialog");
  box.className = "lightbox";
  box.setAttribute("aria-label", "Photo viewer");
  box.innerHTML =
    '<figure><img alt=""><figcaption></figcaption><span class="lightbox-count"></span></figure>' +
    '<button type="button" class="lightbox-close" aria-label="Close">&times;</button>' +
    '<button type="button" class="lightbox-prev" aria-label="Previous photo">&lsaquo;</button>' +
    '<button type="button" class="lightbox-next" aria-label="Next photo">&rsaquo;</button>';
  document.body.appendChild(box);
  if (typeof box.showModal !== "function") return; // very old browsers: links open the photo
  var bigImg = box.querySelector("img"), cap = box.querySelector("figcaption"), count = box.querySelector(".lightbox-count");
  var index = 0;

  function show(i) {
    index = (i + items.length) % items.length;
    var item = items[index], alt = item.querySelector("img").alt;
    bigImg.src = item.getAttribute("href");
    bigImg.alt = alt;
    cap.textContent = alt;
    count.textContent = (index + 1) + " / " + items.length;
  }
  items.forEach(function (item, i) {
    item.addEventListener("click", function (e) {
      e.preventDefault();
      show(i);
      box.showModal();
    });
  });
  box.querySelector(".lightbox-close").addEventListener("click", function () { box.close(); });
  box.querySelector(".lightbox-prev").addEventListener("click", function () { show(index - 1); });
  box.querySelector(".lightbox-next").addEventListener("click", function () { show(index + 1); });
  box.addEventListener("click", function (e) { if (e.target === box) box.close(); });
  box.addEventListener("keydown", function (e) {
    if (e.key === "ArrowLeft") show(index - 1);
    if (e.key === "ArrowRight") show(index + 1);
  });
  var startX = null;
  box.addEventListener("touchstart", function (e) { startX = e.touches[0].clientX; }, { passive: true });
  box.addEventListener("touchend", function (e) {
    if (startX === null) return;
    var dx = e.changedTouches[0].clientX - startX;
    if (Math.abs(dx) > 50) show(index + (dx < 0 ? 1 : -1));
    startX = null;
  });
})();
