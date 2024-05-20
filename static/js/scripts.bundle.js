"use strict";
var Base = (function () {
  var e = "active",
    t = $("body"),
    a = function (a, r) {
      var l = $("#line_loader");
      l.show().animate({ width: 20 + 80 * Math.random() + "%" }, 200),
        $.ajax({ url: a, type: "GET", dataType: "html" })
          .done(function (e, t, a) {
            "success" === t &&
              200 == a.status &&
              ((e = $("<div>" + e + "</div>")),
              $("head title").html(e.find("title").html()),
              $("#wrapper").html(e.find("#wrapper").html()),
              $("html, body").animate({ scrollTop: 0 }, 100),
              n(),
              i(),
              Dashboard.init());
          })
          .fail(function () {
            window.location.href = "404.html";
          })
          .always(function () {
            r &&
              r.length &&
              $(window).width() < 992 &&
              ($(".sidebar-toggler").toggleClass(e),
              t.removeAttr("data-sidebar-toggle")),
              l.animate({ width: "100%" }, 200).fadeOut(300, function () {
                $(this).width("0");
              });
          });
    },
    i = function () {
      var e = Utils.getLocalItem("skin"),
        t = document.getElementById("header"),
        a = document.getElementById("sidebar");
      e &&
        t &&
        a &&
        (t.setAttribute("data-header", e.header),
        a.setAttribute("data-sidebar", e.sidebar));
    },
    n = function () {
      var a, i, n, r, l;
      if (
        ($('[data-scroll="true"]').each(function () {
          new PerfectScrollbar(this, {
            wheelSpeed: 2,
            swipeEasing: !0,
            wheelPropagation: !1,
            minScrollbarLength: 40,
          });
        }),
        $(".swiper").each(function () {
          var e = parseInt(this.getAttribute("data-swiper-slides")),
            t = this.parentElement,
            a = this.getAttribute("data-swiper-loop"),
            i = this.getAttribute("data-swiper-autoplay"),
            n = t.querySelector(".swiper-button-next"),
            r = t.querySelector(".swiper-button-prev"),
            l = t.querySelector(".swiper-pagination"),
            o = this.getAttribute("data-swiper-pagination")
              ? this.getAttribute("data-swiper-pagination")
              : "bullets",
            s = t.querySelector(".swiper-scrollbar"),
            d = 1,
            p = 2;
          1 === e
            ? (d = p = 1)
            : e > 1 && e < 5
            ? ((d = 2), (p = 1))
            : e >= 5 && ((d = 3), (p = 2));
          var u = {
            speed: 500,
            slidesPerView: p,
            slidesPerGroup: p,
            spaceBetween: 16,
            a11y: !0,
            breakpoints: {
              576: { slidesPerView: d, slidesPerGroup: d },
              1200: { slidesPerView: e, slidesPerGroup: e, spaceBetween: 24 },
            },
          };
          a && (u.loop = a),
            i &&
              (u.autoplay = {
                delay: 5e3,
                disableOnInteraction: !1,
                pauseOnMouseEnter: !0,
              }),
            n && r && (u.navigation = { nextEl: n, prevEl: r }),
            l &&
              (u.pagination = {
                el: l,
                type: o,
                clickable: !0,
                dynamicBullets: !0,
              }),
            s && (u.scrollbar = { el: s, draggable: !0 }),
            new Swiper(this, u);
        }),
        document.querySelector(".dropzone") &&
          ((Dropzone.autoDiscover = !1),
          new Dropzone(".dropzone", { url: "/file/post" })),
        (a = "mat-tabs__line"),
        (i = $("<span>", { class: a })),
        (n = $(".mat-tabs")),
        (r = $(".nav-link")),
        n.each(function () {
          var e = $(this).find(".nav-link.active").outerWidth();
          i.stop().css({ width: e }), i.appendTo(this);
        }),
        r.on("click", function () {
          var e = $(this);
          e.closest(".mat-tabs")
            .find("." + a)
            .stop()
            .css({ left: e.position().left, width: e.outerWidth() });
        }),
        (l = !1),
        $(".sidebar-toggler").on("click", function () {
          (l = !l),
            $(this).toggleClass(e),
            t.attr("data-sidebar-toggle", l ? "true" : null);
        }),
        $("#search_input").on("click", function (e) {
          e.stopPropagation(), t.attr("data-search-results", "true");
        }),
        $(".search").on("click", function (e) {
          e.stopPropagation();
        }),
        t.on("click", function () {
          $(this).removeAttr("data-search-results");
        }),
        $(".amplitude-play-pause").hasClass("amplitude-playing"))
      ) {
        var o = Amplitude.getActiveSongMetadata();
        $("[data-play-id]").removeClass(e),
          $("[data-play-id=" + o.id + "]").addClass(e);
      }
    };
  return {
    init: function () {
      $("#loader").fadeOut(1e3),
        t.settings(),
        n(),
        $(window).on("popstate", function () {
          var e = window.location.href.split("#").pop();
          e && a(e);
        }),
        $(document).on(
          "click",
          'a:not([href^="#"])a:not([href^="mail"])a:not([href^="tel"]):not([href^="javascript"]):not(.external):not([target])',
          function (e) {
            e.preventDefault(), e.stopPropagation();
            var t = $(this).closest("#sidebar"),
              i =
                "undefined" !== $(this).attr("href")
                  ? $(this).attr("href")
                  : null;
            i && (window.history.pushState("", "", i), a(i, t));
          }
        );
    },
  };
})();
$(document).ready(function () {
  Base.init();
});
var ChartJs = {
  overrideDefaults() {
    var e = Chart.defaults,
      t = {
        color: Utils.isDarkMode()
          ? "#92929F"
          : Utils.getCSSVarValue("body-color"),
        borderColor: Utils.isDarkMode() ? "#34343e" : "#EFF2F5",
        font: { family: Utils.getCSSVarValue("body-font-family"), size: 13 },
        hover: { intersect: !1, mode: "index" },
      };
    Object.assign(e, t),
      Object.assign(e.plugins.tooltip, {
        titleMarginBottom: 6,
        caretSize: 6,
        caretPadding: 10,
        boxWidth: 10,
        boxHeight: 10,
        boxPadding: 4,
        intersect: !1,
        mode: "index",
        padding: { top: 8, right: 12, bottom: 8, left: 12 },
      });
  },
};
$(() => {
  ChartJs.overrideDefaults();
});
var Dashboard = (function () {
  var e, t, a, i;
  return {
    init: function () {
      !(function () {
        var t = document.getElementById("total_user");
        if ((e && e.destroy(), t)) {
          var a = {
            type: "line",
            data: {
              labels: ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul"],
              datasets: [
                {
                  label: "Users",
                  data: [65, 59, 42, 73, 56, 55, 40],
                  backgroundColor: Utils.getCSSVarValue("red"),
                  borderColor: Utils.getCSSVarValue("red"),
                  borderWidth: 2,
                  pointRadius: 0,
                  pointHoverRadius: 5,
                  pointHoverBorderWidth: 12,
                  pointBackgroundColor: Chart.helpers
                    .color(Utils.getCSSVarValue("red"))
                    .alpha(0)
                    .rgbString(),
                  pointBorderColor: Chart.helpers
                    .color(Utils.getCSSVarValue("red"))
                    .alpha(0)
                    .rgbString(),
                  pointHoverBackgroundColor: Utils.getCSSVarValue("red"),
                  pointHoverBorderColor: Chart.helpers
                    .color(Utils.getCSSVarValue("red"))
                    .alpha(0.1)
                    .rgbString(),
                },
              ],
            },
            options: {
              title: { display: !1 },
              responsive: !0,
              maintainAspectRatio: !1,
              elements: {
                borderJoinStyle: "bevel",
                borderCapStyle: "round",
                line: { tension: 0.4 },
              },
              scales: {
                x: { display: !1 },
                y: { display: !1, min: 0, max: 85 },
              },
              layout: { margin: 0, padding: 0 },
              plugins: { legend: { display: !1 } },
            },
          };
          e = new Chart(t, a);
        }
      })(),
        (function () {
          var e = document.getElementById("total_songs");
          if ((t && t.destroy(), e)) {
            var a = {
              type: "bar",
              data: {
                labels: ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul"],
                datasets: [
                  {
                    label: "Songs",
                    data: [65, 59, 42, 73, 56, 55, 40],
                    backgroundColor: Utils.getCSSVarValue("green"),
                    borderWidth: 0,
                    barThickness: 16,
                    pointRadius: 0,
                  },
                ],
              },
              options: {
                title: { display: !1 },
                responsive: !0,
                maintainAspectRatio: !1,
                elements: {
                  borderJoinStyle: "bevel",
                  borderCapStyle: "round",
                  line: { tension: 0.4 },
                },
                scales: {
                  x: { display: !1 },
                  y: { display: !1, min: 0, max: 85 },
                },
                layout: { margin: 0, padding: 0 },
                plugins: { legend: { display: !1 } },
              },
            };
            t = new Chart(e, a);
          }
        })(),
        (function () {
          var e = document.getElementById("purchases");
          if ((a && a.destroy(), e)) {
            var t = {
              type: "line",
              data: {
                labels: ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul"],
                datasets: [
                  {
                    label: "Purchases",
                    data: [65, 59, 42, 73, 56, 55, 40],
                    backgroundColor: "transparent",
                    borderColor: "#000000",
                    borderWidth: 2,
                    pointRadius: 0,
                    pointHoverRadius: 5,
                    pointHoverBorderWidth: 12,
                    pointBackgroundColor: Chart.helpers
                      .color("#000000")
                      .alpha(0)
                      .rgbString(),
                    pointBorderColor: Chart.helpers
                      .color("#000000")
                      .alpha(0)
                      .rgbString(),
                    pointHoverBackgroundColor: "#000000",
                    pointHoverBorderColor: Chart.helpers
                      .color("#000000")
                      .alpha(0.1)
                      .rgbString(),
                  },
                ],
              },
              options: {
                title: { display: !1 },
                responsive: !0,
                maintainAspectRatio: !1,
                elements: {
                  borderJoinStyle: "bevel",
                  borderCapStyle: "round",
                  line: { tension: 0.4 },
                },
                scales: {
                  x: { display: !1 },
                  y: { display: !1, min: 0, max: 85 },
                },
                layout: { margin: 0, padding: 0 },
                plugins: { legend: { display: !1 } },
              },
            };
            a = new Chart(e, t);
          }
        })(),
        (function () {
          var e = document.getElementById("user_statistics");
          if ((i && i.destroy(), e)) {
            var t = {
              type: "bar",
              data: {
                labels: ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul"],
                datasets: [
                  {
                    label: "Statistics",
                    data: [65, 59, 42, 73, 56, 55, 40],
                    backgroundColor: Utils.getCSSVarValue("purple"),
                    borderWidth: 0,
                    barThickness: 32,
                    pointRadius: 0,
                  },
                ],
              },
              options: {
                title: { display: !1 },
                responsive: !0,
                maintainAspectRatio: !1,
                elements: {
                  borderJoinStyle: "bevel",
                  borderCapStyle: "round",
                  line: { tension: 0.4 },
                },
                scales: {
                  y: {
                    min: 0,
                    max: 80,
                    grid: {
                      borderColor: Utils.isDarkMode() ? "#34343e" : "#EFF2F5",
                    },
                  },
                  x: {
                    grid: {
                      borderColor: Utils.isDarkMode() ? "#34343e" : "#EFF2F5",
                    },
                  },
                },
                layout: { margin: 0, padding: 0 },
                plugins: { legend: { display: !1 } },
              },
            };
            i = new Chart(e, t);
          }
        })();
    },
  };
})();
$(document).ready(function () {
  Dashboard.init();
});
var Player = (function () {
  var e = "active",
    t = $("body"),
    a = $("#playlist"),
    i = [],
    n = Amplitude.getConfig(),
    r = { playPause: !1, nextPrev: !1 },
    l = function (e) {
      setTimeout(e, Amplitude.getDelay());
    },
    o = function (t = !0) {
      $("#player").addClass("show"),
        Amplitude.getSongs() &&
          1 === Amplitude.getSongs().length &&
          (Amplitude.pause(),
          l(() => {
            Player.volumeBackground();
          })),
        Amplitude.init({
          songs: i,
          callbacks: {
            song_change: function () {
              l(() => {
                v(),
                  "playing" === Amplitude.getPlayerState()
                    ? g()
                    : $("[data-play-id]").removeClass(e),
                  d(n);
              });
            },
          },
        });
      var n = i[0];
      a.html(u(n)), p(!1), m(), t && (Amplitude.play(), g(), v()), d(n);
    },
    s = function (e) {
      var t = $(e).closest("[data-song-id]");
      return {
        id: parseInt(t.data("song-id")),
        name: t.data("song-name"),
        artist: t.data("song-artist"),
        album: t.data("song-album"),
        url: t.data("song-url"),
        cover_art_url: t.data("song-cover"),
      };
    },
    d = function (e) {
      var t = $("#player_options");
      t.find("[data-favorite-id]").attr("data-favorite-id", e.id),
        t.find("[data-playlist-id]").attr("data-playlist-id", e.id),
        t.find("[download]").attr("href", e.url);
    },
    p = function (e = !0) {
      $(
        ".amplitude-repeat, .amplitude-prev, .amplitude-next, .amplitude-shuffle"
      ).prop("disabled", e);
    },
    u = function (e) {
      var t = Amplitude.getActiveSongMetadata();
      return `<div class="list__item"\n        data-song-id="${
        e.id
      }"\n        data-song-name="${e.name}"\n        data-song-artist="${
        e.artist
      }"\n        data-song-album="${e.album}"\n        data-song-url="${
        e.url
      }"\n        data-song-cover="${
        e.cover_art_url
      }">\n            <div class="list__cover">\n                <img src="${
        e.cover_art_url
      }" alt="${
        e.name
      }">\n                <a href="javascript:void(0);" class="btn btn-play btn-sm btn-default btn-icon rounded-pill ${
        e.id === t.id ? "active" : ""
      }" data-play-id="${
        e.id
      }">\n                    <i class="ri-play-fill icon-play"></i>\n                    <i class="ri-pause-fill icon-pause"></i>\n                </a>\n            </div>\n            <div class="list__content">\n                <a href="song-details.html" class="list__title text-truncate">${
        e.name
      }</a>\n                <p class="list__subtitle text-truncate">\n                    <a href="artist-details.html">${
        e.artist
      }</a>\n                </p>\n            </div>\n            <ul class="list__option">\n                <li class="list__icon-hover">\n                    <a href="javascript:void(0);" role="button" class="d-inline-flex" data-remove-song-id="${
        e.id
      }">\n                        <i class="ri-close-line fs-6"></i>\n                    </a>\n                </li>\n                <li>\n                    <a href="javascript:void(0);" role="button" class="d-inline-flex" data-favorite-id="${
        e.id
      }">\n                        <i class="ri-heart-line heart-empty"></i>\n                        <i class="ri-heart-fill heart-fill"></i>\n                    </a>\n                </li>\n            </ul>\n        </div>`;
    },
    c = function () {
      (i = []),
        p(),
        Amplitude.pause(),
        (n.player_state = "paused"),
        Utils.removeLocalItem("songs"),
        a.html(
          '<div class="col-sm-8 col-10 mx-auto mt-5 text-center">\n            <i class="ri-music-2-line mb-3"></i>\n            <p>No songs, album or playlist are added on lineup.</p>\n        </div>'
        ),
        l(() => {
          h(), v();
        });
    },
    g = function () {
      var t = Amplitude.getActiveSongMetadata();
      $("[data-play-id]").removeClass(e),
        $("[data-play-id=" + t.id + "]").addClass(e);
    },
    m = function () {
      $(".amplitude-play-pause")
        .removeClass("amplitude-paused")
        .addClass("amplitude-playing");
    },
    h = function () {
      $(".amplitude-play-pause")
        .removeClass("amplitude-playing")
        .addClass("amplitude-paused"),
        $("[data-play-id]").removeClass(e);
    },
    v = function () {
      var e = Amplitude.getActiveSongMetadata(),
        t = Amplitude.getActivePlaylist() ? Amplitude.getActivePlaylist() : "";
      if ("mediaSession" in navigator) {
        var a = navigator.mediaSession;
        (a.metadata = new MediaMetadata({
          title: e.name,
          artist: e.artist,
          album: e.album,
          artwork: [
            { src: e.cover_art_url, sizes: "96x96", type: "image/jpg" },
            { src: e.cover_art_url, sizes: "128x128", type: "image/jpg" },
            { src: e.cover_art_url, sizes: "192x192", type: "image/jpg" },
            { src: e.cover_art_url, sizes: "256x256", type: "image/jpg" },
            { src: e.cover_art_url, sizes: "384x384", type: "image/jpg" },
            { src: e.cover_art_url, sizes: "512x512", type: "image/jpg" },
          ],
        })),
          i.length >= 1 &&
            !r.playPause &&
            ((r.playPause = !0),
            a.setActionHandler("play", () => (Amplitude.play(), m(), void g())),
            a.setActionHandler("pause", () => (Amplitude.pause(), void h()))),
          i.length >= 2 &&
            !r.nextPrev &&
            ((r.nextPrev = !0),
            a.setActionHandler("previoustrack", () => Amplitude.prev(t)),
            a.setActionHandler("nexttrack", () => Amplitude.next(t)));
      }
    };
  return {
    volumeBackground: function () {
      var e = $('.player-volume input[type="range"]'),
        t = parseInt(e.val(), 10),
        a = Utils.isDarkMode()
          ? "255, 255, 255"
          : Utils.getCSSVarValue("dark-rgb"),
        i =
          "linear-gradient(to right, rgb(" +
          a +
          ") 0%, rgb(" +
          a +
          ") " +
          t +
          "%, rgba(" +
          a +
          ", 0) " +
          t +
          "%, rgba(" +
          a +
          ", 0) 100%)";
      e.css("background", i);
    },
    init: function () {
      var r;
      !(function () {
        if (
          Utils.getLocalItem("songs") &&
          Utils.getLocalItem("songs").length &&
          ((i = Utils.getLocalItem("songs")), o(!1), h(), i.length > 1)
        )
          for (let t = 0; t < i.length; t++) {
            var e = i[t];
            0 === t ? a.html(u(e)) : a.append(u(e));
          }
      })(),
        t.on("click", "[data-play-id]", function () {
          var t = s(this),
            n = i.findIndex((e) => e.id === t.id);
          $(this).hasClass(e)
            ? (Amplitude.pause(), h())
            : -1 === n
            ? (i.push(t),
              1 === i.length
                ? o()
                : (a.append(u(t)), Amplitude.playSongAtIndex(i.length - 1)))
            : Amplitude.playSongAtIndex(n),
            Utils.setLocalItem("songs", i);
        }),
        t.on("click", "[data-queue-id]", function () {
          var e = s(this);
          -1 === i.findIndex((t) => t.id === e.id)
            ? (i.push(e), 1 === i.length ? o() : a.append(u(e)))
            : Utils.showMessage("Song already in Queue"),
            Utils.setLocalItem("songs", i);
        }),
        t.on("click", "[data-next-id]", function () {
          var e = s(this),
            t = Amplitude.getActiveIndex(),
            n = i.findIndex((t) => t.id === e.id);
          i && !i.length
            ? (i.push(e), o())
            : -1 === n
            ? (i.splice(t + 1, 0, e), a.find(".list__item").eq(t).after(u(e)))
            : Utils.showMessage("Song already in Queue"),
            Utils.setLocalItem("songs", i);
        }),
        t.on("click", "[data-collection-play-id]", function () {
          var e = $(this).attr("data-collection-play-id"),
            t = $("[data-collection-song-id=" + e + "]").find("[data-song-id]"),
            n = [],
            r = 0;
          t.each(function () {
            var e = s(this);
            n.push(e);
          }),
            i && !i.length ? ((i = n), o(), (r = 1)) : i.push(...n);
          for (let e = r; e < n.length; e++) a.append(u(n[e]));
          Utils.setLocalItem("songs", i);
        }),
        t.on("click", "[data-remove-song-id]", function (e) {
          e.stopPropagation();
          var t = parseInt($(this).data("remove-song-id")),
            a = $(this).closest("[data-song-id"),
            n = i.findIndex((e) => e.id === t);
          n > -1 &&
            (a.remove(), Amplitude.removeSong(n), 0 === i.length && c()),
            Utils.setLocalItem("songs", i);
        }),
        $("#clear_playlist").on("click", function () {
          if (i.length >= 1) {
            for (var e = 0; e < i.length; e++)
              a.find(".list__item").eq(e).remove();
            for (e = i.length - 1; e > -1; e--) {
              var t = i[e],
                n = Amplitude.getActiveSongMetadata();
              t.id !== n.id && Amplitude.removeSong(e);
            }
            c();
          }
        }),
        (r = $(".player-volume"))
          .find('input[type="range"]')
          .on("input", function () {
            var e = r.find(".ri-volume-mute-fill"),
              t = r.find(".ri-volume-down-fill"),
              a = r.find(".ri-volume-up-fill"),
              i = $(this),
              n = parseInt(i.val(), 10),
              l = "d-block",
              o = "d-none";
            Player.volumeBackground(),
              0 === n
                ? (e.removeClass(o).addClass(l), t.addClass(o), a.addClass(o))
                : n > 0 && n < 70
                ? (e.addClass(o), t.removeClass(o).addClass(l), a.addClass(o))
                : n > 70 &&
                  (e.addClass(o), t.addClass(o), a.removeClass(o).addClass(l));
          }),
        $(".amplitude-play-pause").on("click", function () {
          v(),
            l(() => {
              "playing" === Amplitude.getPlayerState()
                ? g()
                : $("[data-play-id]").removeClass(e);
            });
        }),
        $(".amplitude-prev").on("click", function () {
          n.player_state = "playing";
        }),
        $(".amplitude-next").on("click", function () {
          n.player_state = Amplitude.getActiveIndex() ? "playing" : "stopped";
        });
    },
  };
})();
$(document).ready(function () {
  Player.init();
}),
  (function (e, t, a, i) {
    e.fn.extend({
      settings: function (t) {
        (t = e.extend({}, e.settings.defaults, t)),
          this.each(function () {
            new e.settings(this, t);
          });
      },
    }),
      (e.settings = function (t, i) {
        var n,
          r,
          l,
          o = a.body,
          s = "skin",
          d = "setting",
          p = "Theme Settings",
          u = [
            "yellow",
            "orange",
            "red",
            "green",
            "blue",
            "purple",
            "indigo",
            "dark",
          ],
          c = ["light", "dark"],
          g = "data-theme",
          m = "data-header",
          h = "data-sidebar",
          v = "data-player",
          y = () => {
            var e = a.getElementById("header"),
              t = a.getElementById("sidebar"),
              n = a.getElementById("player"),
              r = {
                dark: i.dark,
                header: i.header,
                sidebar: i.sidebar,
                player: i.player,
              };
            Utils.setLocalItem(s, r),
              r.dark ? o.setAttribute(g, "dark") : o.removeAttribute(g),
              e && i.header && e.setAttribute(m, i.header),
              t && i.sidebar && t.setAttribute(h, i.sidebar),
              n && i.player && n.setAttribute(v, i.player);
          },
          f = (e, t, a) => {
            var i = `<div class="${d}__body__item"><span class="${d}__title">${t}</span>\n                <div class="${d}__options">`;
            for (let t = 0; t < e.length; t++) {
              var n = e[t];
              i += `<a href="javascript:void(0);" class="${d}__option ${d}__option--${n}" data-${a}-option="${n}"></a>`;
            }
            return (i += "</div></div>");
          },
          b = () => {
            var t = e(`#${d}`),
              a = e(`#${d}_toggler`),
              n = e(`.${d}__option`),
              r = "show",
              l = "active";
            e(o).on("click", () => {
              t.removeClass(r);
            }),
              a.on("click", () => {
                t.toggleClass(r);
              }),
              t.on("click", (e) => {
                e.stopPropagation();
              }),
              n.on("click", function () {
                var t = e(this),
                  a = t.data("theme-option"),
                  n = t.data("header-option"),
                  r = t.data("sidebar-option"),
                  o = t.data("player-option");
                a
                  ? (e("[data-theme-option]").removeClass(l),
                    (i.dark = "dark" === a),
                    Utils.changeSkin())
                  : n
                  ? (e("[data-header-option]").removeClass(l), (i.header = n))
                  : r
                  ? (e("[data-sidebar-option]").removeClass(l), (i.sidebar = r))
                  : o &&
                    (e("[data-player-option]").removeClass(l), (i.player = o)),
                  t.addClass(l),
                  y();
              });
          };
        (l = Utils.getLocalItem(s)) && (i = e.extend({}, i, l)),
          y(),
          (n = a.createElement("div")),
          (r = `<a href="javascript:void(0);" id="${d}_toggler">Settings</a>\n                    <div class="${d}__wrapper">\n                        <div class="${d}__head">${p}</div>\n                        <div class="${d}__body">`),
          (r += f(c, "Theme", "theme")),
          (r += f(u, "Header", "header")),
          (r += f(u, "Sidebar", "sidebar")),
          (r += f(u, "Player", "player")),
          (r +=
            '<p class="mt-4">Note: You can see the color change effect of the header, sidebar and player in the inner pages.</p></div></div>'),
          (n.id = d),
          (n.innerHTML = r),
          o.appendChild(n),
          b(),
          i.dark
            ? e('[data-theme-option="dark"]').addClass("active")
            : e('[data-theme-option="light"]').addClass("active"),
          e("[data-header-option=" + i.header + "]").addClass("active"),
          e("[data-sidebar-option=" + i.sidebar + "]").addClass("active"),
          e("[data-player-option=" + i.player + "]").addClass("active");
      }),
      (e.settings.defaults = {
        dark: !1,
        header: null,
        sidebar: null,
        player: null,
      });
  })(jQuery, window, document);
var Utils = {
  getCSSVarValue: function (e) {
    var t = getComputedStyle(document.documentElement).getPropertyValue(
      "--bs-" + e
    );
    return t && t.length > 0 && (t = t.trim()), t;
  },
  getLocalItem: function (e) {
    return JSON.parse(localStorage.getItem(e));
  },
  setLocalItem: function (e, t) {
    localStorage.setItem(e, JSON.stringify(t));
  },
  removeLocalItem: function (e) {
    localStorage.removeItem(e);
  },
  showMessage: function (e) {
    Snackbar.show({
      pos: this.isRTL() ? "bottom-left" : "bottom-right",
      text: e,
      showAction: !1,
    });
  },
  changeSkin: function () {
    setTimeout(() => {
      ChartJs.overrideDefaults(), Dashboard.init(), Player.volumeBackground();
    }, 10);
  },
  isDarkMode: function () {
    return "dark" === document.querySelector("body").getAttribute("data-theme");
  },
  isRTL: function () {
    return "rtl" === document.querySelector("html").getAttribute("direction");
  },
};
"undefined" != typeof module &&
  void 0 !== module.exports &&
  (module.exports = Utils);
//# sourceMappingURL=scripts.bundle.js.map
